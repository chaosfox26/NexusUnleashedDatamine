#!/usr/bin/env python3
"""Determine the PROp record layout in .area files, or prove it is not fixed-size.

`.area` files carry a `PROp` chunk holding world object placement - real coordinates and rotations
from the shipped client, for scenery, doodads and interactables. Nobody has extracted these because
the container format was undocumented until now.

## The method

Guessing a struct from one file is how a wrong layout becomes permanent. Instead, solve for it:

If records are fixed-size, then for EVERY file:

    payloadLength = headerBytes + recordCount x recordStride

and `recordCount` must appear as a u32 somewhere in those header bytes - a format does not store a
count it never writes down.

So: search every (headerBytes, recordStride) pair, and keep only those where the arithmetic holds on
*all* files AND the implied count is actually present in the header. A candidate that works on 90% of
files is not the answer; a real layout has no exceptions.

If nothing survives, that is a result too - it means records are variable-length, and it is reported
as such rather than by relaxing the test until something passes.

## Validation, if a candidate survives

Arithmetic alone can be coincidence at small strides. Any surviving candidate is checked against
physics: the float triple at the position offset must fall inside the plausible world range, and must
do so for essentially every record in every file. Numbers that decode as sane coordinates in 99% of
cases are a layout; numbers that decode as 1e38 are three bytes of something else.

Usage:  python Tools/crack-prop.py [--sample N] [--workers N]
"""
import collections
import io
import lzma
import multiprocessing as mp
import os
import struct
import sys

MIRROR = r"D:/CDN/Mirror/16042"
TREE = "docs/client-extract/FILETREE.tsv"

LZ = bytes.fromhex("5d000010")
FILTERS = [{"id": lzma.FILTER_LZMA1, "dict_size": 0x100000, "lc": 3, "lp": 0, "pb": 2}]

MAX_HEADER = 96
MIN_STRIDE, MAX_STRIDE = 12, 320
WORLD_LIMIT = 100000.0        # generous; real WildStar coords are well inside this


def decompress(raw):
    if raw[:4] == LZ:
        return lzma.LZMADecompressor(format=lzma.FORMAT_RAW, filters=FILTERS).decompress(raw[5:])
    return raw


def prop_payload(data):
    off, b = 0, data[8:]
    while off + 8 <= len(b):
        tag = b[off:off + 4]
        if not (len(tag) == 4 and all(32 <= c < 127 for c in tag)):
            return None
        size, = struct.unpack_from("<I", b, off + 4)
        if size > len(b) - off - 8:
            return None
        if tag[::-1] == b"PROp":
            return b[off + 8: off + 8 + size]
        off += 8 + size
    return None


def load(args):
    sha, path = args
    try:
        p = prop_payload(decompress(open(os.path.join(MIRROR, sha + ".bin"), "rb").read()))
    except Exception:
        return None
    if not p or len(p) < 64:
        return None
    return (path, p)


def candidates(payloads):
    """Every (header, stride) that divides cleanly on all files with the count present in the header."""
    ok = []
    for header in range(0, MAX_HEADER + 1, 4):
        # counts the header could be declaring, per file
        headwords = []
        for _, p in payloads:
            if len(p) < header + 4:
                headwords.append(set())
            else:
                headwords.append({struct.unpack_from("<I", p, i)[0] for i in range(0, header, 4)})

        for stride in range(MIN_STRIDE, MAX_STRIDE + 1, 4):
            good = True
            for (path, p), hw in zip(payloads, headwords):
                rem = len(p) - header
                if rem <= 0 or rem % stride:
                    good = False
                    break
                if (rem // stride) not in hw:
                    good = False
                    break
            if good:
                ok.append((header, stride))
    return ok


def score_positions(payloads, header, stride):
    """Fraction of records whose best float-triple decodes as a plausible coordinate, per offset."""
    best = (0.0, None)
    for pos in range(0, stride - 12 + 1, 4):
        sane = total = 0
        for _, p in payloads:
            n = (len(p) - header) // stride
            for i in range(min(n, 200)):
                o = header + i * stride + pos
                try:
                    x, y, z = struct.unpack_from("<fff", p, o)
                except struct.error:
                    continue
                total += 1
                if all(abs(v) < WORLD_LIMIT and v == v for v in (x, y, z)) and any(v != 0 for v in (x, y, z)):
                    sane += 1
        if total:
            frac = sane / total
            if frac > best[0]:
                best = (frac, pos)
    return best


def main():
    sample = int(sys.argv[sys.argv.index("--sample") + 1]) if "--sample" in sys.argv else 400
    workers = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else (os.cpu_count() or 8)

    files, seen = [], set()
    with io.open(TREE, encoding="utf-8") as f:
        for ln in f:
            if ln.startswith(("#", "path")):
                continue
            p = ln.rstrip("\n").split("\t")
            if len(p) >= 5 and p[0].lower().endswith(".area") and p[1] not in seen:
                seen.add(p[1])
                files.append((p[1], p[0]))

    print("scanning %d .area files on %d workers for PROp chunks" % (len(files), workers))
    with mp.Pool(workers) as pool:
        payloads = [r for r in pool.imap_unordered(load, files, chunksize=8) if r]
    print("found %d PROp chunks" % len(payloads))
    if not payloads:
        return

    payloads.sort(key=lambda r: len(r[1]))
    work = payloads[:sample] if sample else payloads
    print("solving over %d of them\n" % len(work))

    cands = candidates(work)
    if not cands:
        print("NO fixed-size layout satisfies all %d files." % len(work))
        print("Records are variable-length, or the count is not stored in the first %d bytes."
              % MAX_HEADER)
        print("Reported as a negative rather than relaxing the test until something passes.")
        return

    print("%d candidate layout(s) survive on all %d files:\n" % (len(cands), len(work)))
    scored = []
    for header, stride in cands:
        frac, pos = score_positions(work, header, stride)
        scored.append((frac, header, stride, pos))
        print("  header %3d  stride %3d  -> best float-triple at +%s decodes as sane coords in %.1f%% of records"
              % (header, stride, pos, 100.0 * frac))

    scored.sort(reverse=True)
    frac, header, stride, pos = scored[0]
    print("\nBEST: header %d bytes, %d-byte records, position at record+%d (%.1f%% plausible)"
          % (header, stride, pos, 100.0 * frac))

    if frac < 0.95:
        print("\nBelow 95% - NOT accepted as the layout. Arithmetic alone can be coincidence.")
        return

    total = sum((len(p) - header) // stride for _, p in payloads)
    print("\nAcross all %d PROp chunks that is %s placed objects." % (len(payloads), format(total, ",")))

    print("\nsample records:")
    path, p = work[len(work) // 2]
    n = (len(p) - header) // stride
    print("  %s  (%d records)" % (path, n))
    for i in range(min(n, 6)):
        o = header + i * stride
        x, y, z = struct.unpack_from("<fff", p, o + pos)
        head = p[o:o + 12].hex()
        print("    %2d  pos (%10.2f, %9.2f, %10.2f)   first12 %s" % (i, x, y, z, head))


if __name__ == "__main__":
    main()
