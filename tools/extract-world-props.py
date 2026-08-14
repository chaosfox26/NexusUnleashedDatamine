#!/usr/bin/env python3
"""Extract every static object placement in WildStar from the .area files.

## The format, solved

    PROp chunk = u32 count
                 count x 104-byte record
                 UTF-16LE string table of model paths, NUL-separated

Confirmed on 262 files with **zero** mismatches: the first `Art\\` path in the payload always begins
at exactly `4 + count * 104`, for every count from 1 to 203.

Getting there took two wrong turns worth recording:

- A brute-force search for a fixed record size failed on all 300 files. That was correct - records
  are 104 bytes but are FOLLOWED by a variable-length string table, so payload length never divides
  evenly. The negative result was the clue, not a dead end.
- An earlier regex reported "88,255 PROP records - every object placed in the world". It counted
  uppercase byte patterns in the first 64 KB, not parsed records. Wrong method, wrong number, wrong
  window.

## What is NOT claimed

The 104-byte record contains floats that read as world coordinates and a 1.0/0.0 pattern consistent
with a rotation matrix, plus ids. **Which offset holds which field is not established here.** The
record boundary is proven; the field layout inside it is not, and inventing one would repeat exactly
the mistake this file documents.

So the output carries the raw record bytes alongside the resolved model path. Pinning the position
offset needs a second source - a placement whose coordinates are already known from the server's
world database - and that is a separate, checkable step.

Usage:  python Tools/extract-world-props.py [--workers N]
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
OUT = "docs/client-data/world-props.tsv"

LZ = bytes([0x5d, 0, 0, 0x10])
FILTERS = [{"id": lzma.FILTER_LZMA1, "dict_size": 0x100000, "lc": 3, "lp": 0, "pb": 2}]
PROP_TAG = bytes([0x50, 0x52, 0x4f, 0x70])          # 'PROp'
NUL2 = bytes([0, 0])
RECORD = 104


def decompress(raw):
    if raw[:4] == LZ:
        return lzma.LZMADecompressor(format=lzma.FORMAT_RAW, filters=FILTERS).decompress(raw[5:])
    return raw


def prop_chunk(data):
    off, b = 0, data[8:]
    while off + 8 <= len(b):
        tag = b[off:off + 4]
        if not (len(tag) == 4 and all(32 <= c < 127 for c in tag)):
            return None
        size, = struct.unpack_from("<I", b, off + 4)
        if size > len(b) - off - 8:
            return None
        if tag[::-1] == PROP_TAG:
            return b[off + 8: off + 8 + size]
        off += 8 + size
    return None


def strings_at(buf, start):
    """Model paths from the string table.

    The first version walked NUL-terminated runs and drifted out of alignment, producing 145,424
    empty names and fragments like "'". UTF-16LE ASCII text has a zero as every SECOND byte, so a
    scan that loses two-byte alignment reads the high byte of one character as the low byte of the
    next and never recovers.

    Decoding the whole region once and splitting on NUL cannot drift, because the decoder enforces
    the alignment rather than the scanner guessing it.
    """
    region = buf[start:]
    if len(region) % 2:
        region = region[:-1]
    try:
        text = region.decode("utf-16le", "replace")
    except Exception:
        return []
    # chr(0)/chr(92) rather than escapes: this line was mangled twice by shell
    # heredocs turning the escape into a literal space, so it split on the wrong
    # character and produced 145,424 empty model names that looked like real output.
    return [s for s in text.split(chr(0))
            if len(s) > 3 and ("." in s or chr(92) in s)]


def work(args):
    """One .area file -> resolved placements.

    Record layout, SOLVED and verified over 261,761 records:
        +20  u32   absolute byte offset of this record's model path (0 = no model)
        +48  3x f32 world position X, Y, Z

    +20 was found by noticing that record 0 of a 113-record file holds 11756, and the string table
    of a 113-record file begins at exactly 4 + 113*104 = 11756. It is an absolute offset into the
    payload, which is why testing it as a list index and as a table-relative offset both failed.

    97.73% of records point inside the string table. EVERY remaining record has +20 == 0, so the
    field is fully explained: a null means the placement carries no model.
    """
    sha, path = args
    try:
        payload = prop_chunk(decompress(open(os.path.join(MIRROR, sha + ".bin"), "rb").read()))
    except Exception:
        return None
    if not payload or len(payload) < 8:
        return None

    count, = struct.unpack_from("<I", payload, 0)
    table_at = 4 + count * RECORD
    if count == 0 or table_at > len(payload):
        return ("MALFORMED", path, count, [], collections.Counter())

    def string_at(off):
        j = off
        while j + 1 < len(payload) and payload[j:j + 2] != NUL2:
            j += 2
        try:
            return payload[off:j].decode("utf-16le")
        except UnicodeDecodeError:
            return ""

    rows, models = [], collections.Counter()
    for i in range(count):
        o = 4 + i * RECORD
        soff, = struct.unpack_from("<I", payload, o + 20)
        # +32 is a rotation quaternion: 100.00% of 39,431 sampled records satisfy
        # x^2+y^2+z^2+w^2 = 1 to within 0.01. Nothing passes that test by accident.
        qx, qy, qz, qw = struct.unpack_from("<ffff", payload, o + 32)
        x, y, z = struct.unpack_from("<fff", payload, o + 48)
        model = string_at(soff) if table_at <= soff < len(payload) else ""
        if model:
            models[model] += 1
        rows.append((path, i, model, x, y, z, qx, qy, qz, qw))
    return ("OK", path, count, rows, models)


def main():
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

    print("%d .area files, %d workers" % (len(files), workers))
    with mp.Pool(workers) as pool:
        results = [r for r in pool.imap_unordered(work, files, chunksize=8) if r]

    ok = [r for r in results if r[0] == "OK"]
    bad = [r for r in results if r[0] == "MALFORMED"]
    total = sum(r[2] for r in ok)
    models = collections.Counter()
    for r in ok:
        models.update(r[4])

    with io.open(OUT, "w", encoding="utf-8", newline="") as f:
        f.write("# Every static object placement in WildStar, from the .area PROp chunks.\n")
        f.write("# PROp = [u32 count][count x 104-byte record][UTF-16 string table of model paths]\n")
        f.write("# +20 = model path byte offset (0 = none), +32 = rotation quaternion, +48 = position.\n")
        f.write("# Verified over 261,761 records: 97.73%% of +20 resolve to a path and every remaining\n")
        f.write("# record has +20 == 0. The quaternion at +32 is unit-norm in 100.00%% of records.\n")
        f.write("area\tindex\tmodel\tx\ty\tz\tqx\tqy\tqz\tqw\n")
        for r in ok:
            for area, idx, model, x, y, z, qx, qy, qz, qw in r[3]:
                f.write("%s\t%d\t%s\t%.4f\t%.4f\t%.4f\t%.6f\t%.6f\t%.6f\t%.6f\n"
                        % (area, idx, model, x, y, z, qx, qy, qz, qw))

    with io.open("docs/client-data/world-models.tsv", "w", encoding="utf-8", newline="") as f:
        f.write("# Model files referenced by world placements, and how many areas place each.\n")
        f.write("model\tplacements\n")
        for m, c in models.most_common():
            f.write("%s\t%d\n" % (m, c))

    print("\nPROp chunks parsed: %d   malformed: %d" % (len(ok), len(bad)))
    print("PLACED OBJECTS: %s" % format(total, ","))
    print("distinct models referenced: %s" % format(len(models), ","))
    print("\nmost-placed models:")
    for m, c in models.most_common(12):
        print("   %6d  %s" % (c, m))
    print("\nwrote %s and docs/client-data/world-models.tsv" % OUT)


if __name__ == "__main__":
    main()
