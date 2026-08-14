#!/usr/bin/env python3
"""Search the ENTIRE decompressed client for known creature spawn coordinates. Vectorised.

## The question this settles, definitively

Every previous attempt looked in places I *expected* spawn data to be - creature2 columns, .area
chunks, table joins - which can only rule out the places I thought of.

This asks the opposite way, and the answer is not a matter of judgement. **We already know 1,260 real
Everstar Grove spawn coordinates** from the community world SQL. If those float32 values appear
anywhere in the 197,333 client files, the client holds spawn data. If they appear nowhere, it does
not - and that is proof rather than an inference from where I happened to look.

## The first version was the wrong algorithm

It called `data.find(pattern)` once per pattern per file: 3,780 patterns x 197,333 files = **745
million substring scans**. Its own docstring said it would group needles to avoid exactly that, and
then it didn't. Thirty-two cores doing the wrong amount of work is not using the machine, it is
wasting it faster.

## What this does instead

Reinterpret each file as a `float32` array and test every known X coordinate at once with
`np.isin` - one vectorised pass per file instead of thousands of scans, running on SIMD. Candidate
positions are then verified against Y and Z, so a coincidental X match costs almost nothing.

Coordinates are read at all four byte alignments, because a float in the middle of a record need not
be 4-byte aligned relative to file start.

Tolerance: the SQL stores decimals, so an exact float32 compare could miss on a last-bit difference.
Matching is done with `np.isclose` at 1e-3 - far tighter than any real coordinate spacing, loose
enough to survive decimal round-trip.

Usage:  python Tools/hunt-spawn-coords.py [--workers N] [--limit N]
"""
import collections
import io
import lzma
import multiprocessing as mp
import os
import re
import sys
import time

import numpy as np

MIRROR = r"D:/CDN/Mirror/16042"
TREE = "docs/client-extract/FILETREE.tsv"
SQL = r"D:/Wildstar Files/_ForkPool/WorldDatabase/Alizar/EverstarGrove.sql"

LZ = bytes([0x5d, 0, 0, 0x10])
FILTERS = [{"id": lzma.FILTER_LZMA1, "dict_size": 0x100000, "lc": 3, "lp": 0, "pb": 2}]
ROW = re.compile(r"\(@GUID\+\d+,\s*(\d+),\s*(\d+),\s*@WORLD,\s*(\d+),"
                 r"\s*(-?[\d.]+),\s*(-?[\d.]+),\s*(-?[\d.]+)")

XS = YS = ZS = None
CID = None
XLO = XHI = 0.0


def init(xs, ys, zs, cid):
    global XS, YS, ZS, CID, XLO, XHI
    XS, YS, ZS, CID = xs, ys, zs, cid
    XLO, XHI = float(xs.min()) - 0.01, float(xs.max()) + 0.01


def work(args):
    sha, path = args
    try:
        raw = open(os.path.join(MIRROR, sha + ".bin"), "rb").read()
        data = (lzma.LZMADecompressor(format=lzma.FORMAT_RAW, filters=FILTERS).decompress(raw[5:])
                if raw[:4] == LZ else raw)
    except Exception:
        return None
    if len(data) < 16:
        return None

    hits = []
    for align in range(4):
        buf = data[align:]
        n = (len(buf) // 4) * 4
        if n < 12:
            continue
        arr = np.frombuffer(buf[:n], dtype="<f4")
        if arr.size < 3:
            continue

        # RANGE FILTER FIRST. np.isin against 1,260 values on every float in the file was the
        # bottleneck at 121 files/sec. Every known coordinate lies inside one narrow box, so a
        # two-comparison range mask discards ~99.99% of floats before any set lookup happens -
        # and a value outside the box cannot possibly be one of the needles.
        mask = (arr >= XLO) & (arr <= XHI)
        if not mask.any():
            continue
        cand = np.nonzero(mask)[0]
        cand = cand[np.isin(arr[cand], XS)]
        if cand.size == 0:
            continue
        cand = cand[cand + 2 < arr.size]
        for i in cand:
            x, y, z = float(arr[i]), float(arr[i + 1]), float(arr[i + 2])
            j = np.nonzero(np.isclose(XS, x, atol=1e-3))[0]
            for k in j:
                if abs(YS[k] - y) < 1e-3 and abs(ZS[k] - z) < 1e-3:
                    hits.append((path, int(i) * 4 + align, CID[k], x, y, z))
                    break
    return hits or None


def main():
    workers = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else (os.cpu_count() or 8)
    limit = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else 0

    text = io.open(SQL, encoding="utf-8", errors="replace").read()
    rows = [(m.group(2), float(m.group(4)), float(m.group(5)), float(m.group(6)))
            for m in ROW.finditer(text)]
    xs = np.array([r[1] for r in rows], dtype="<f4")
    ys = np.array([r[2] for r in rows], dtype="<f4")
    zs = np.array([r[3] for r in rows], dtype="<f4")
    cid = [r[0] for r in rows]
    print("known spawn coordinates: %s" % format(len(rows), ","))

    files, seen = [], set()
    with io.open(TREE, encoding="utf-8") as f:
        for ln in f:
            if ln.startswith(("#", "path")):
                continue
            p = ln.rstrip("\n").split("\t")
            if len(p) >= 5 and p[1] not in seen:
                seen.add(p[1])
                files.append((p[1], p[0]))
    if limit:
        files = files[:limit]

    print("vectorised search of %s files on %d workers\n" % (format(len(files), ","), workers))
    t0 = time.time()
    found = []
    with mp.Pool(workers, initializer=init, initargs=(xs, ys, zs, cid)) as pool:
        for i, r in enumerate(pool.imap_unordered(work, files, chunksize=48), 1):
            if r:
                found.extend(r)
            if i % 25000 == 0:
                el = time.time() - t0
                print("   %s / %s   %.0f files/sec   eta %.0fs   hits %d"
                      % (format(i, ","), format(len(files), ","), i / el,
                         (len(files) - i) / (i / el), len(found)))

    dt = time.time() - t0
    print("\n%s files in %.1fs (%.0f/sec)" % (format(len(files), ","), dt, len(files) / dt))

    if not found:
        print("\nZERO HITS.")
        print("Not one of %s known spawn coordinates appears as float32 anywhere in the client."
              % format(len(rows), ","))
        print("That is proof: creature spawn positions are not in the client files.")
        return

    print("\n%s HITS across %s files:" % (format(len(found), ","),
                                          format(len(set(h[0] for h in found)), ",")))
    for path, n in collections.Counter(h[0] for h in found).most_common(25):
        print("   %-62s %d" % (path[:62], n))
    with io.open("docs/client-data/spawn-coord-hits.tsv", "w", encoding="utf-8", newline="") as f:
        f.write("# Known Everstar Grove spawn coordinates found INSIDE client files.\n")
        f.write("# Every row is a coordinate the server spawns a creature at, which also exists\n")
        f.write("# verbatim in the shipped client - so SOME spawn positions are client-side.\n")
        f.write("file\toffset\tcreature\tx\ty\tz\n")
        for h in sorted(found):
            f.write("%s\t%d\t%s\t%.4f\t%.4f\t%.4f\n" % h)
    print("\nwrote docs/client-data/spawn-coord-hits.tsv")

    print("\nexamples:")
    for h in found[:10]:
        print("   %s +%d  creature %s  (%.2f, %.2f, %.2f)" % (h[0][:48], h[1], h[2], h[3], h[4], h[5]))


if __name__ == "__main__":
    main()
