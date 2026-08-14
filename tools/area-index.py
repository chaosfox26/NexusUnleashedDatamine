#!/usr/bin/env python3
"""One pass over the .area corpus. Everything after that is a query.

## Why this exists

Eight separate analyses were run over these files - chunk tags, PROp layout, position offset,
rotation, CURT - and **each one re-read the file index and re-ran LZMA over thousands of blobs from
scratch**. The same 12.9 GB decompressed roughly eight times. Running 32 workers made each pass fast,
which disguised the fact that the passes themselves were redundant.

Parallelism inside a pass is not the same as not repeating the pass.

So: decompress once, extract **everything** any of those questions needed in a single visit, and
persist it. Every later question reads the cache in under a second.

## What one visit extracts

- every top-level chunk tag, over ALL files rather than a sample - which is what answers "is there an
  entity/spawn chunk hiding in a file we never opened"
- full PROp placements: model path, position, rotation quaternion
- CURT point counts
- any chunk tag that is not PROp/CHNK/CURT, flagged loudly, because an unknown tag is the only place
  creature spawn data could still be hiding in this format

## Memory

The corpus is ~12.9 GB decompressed against 61.7 GB of RAM, so it would fit - but shipping decompressed
buffers back through multiprocessing pickling would cost more than the decompression saved. Workers
therefore decompress, extract, and return only compact facts. The expensive thing happens once and
never crosses a process boundary.

Usage:
    python Tools/area-index.py --build [--workers N]
    python Tools/area-index.py --tags            # every chunk tag, from cache
    python Tools/area-index.py --unknown         # files with a tag we cannot name
"""
import collections
import gzip
import io
import json
import lzma
import multiprocessing as mp
import os
import struct
import sys

MIRROR = r"D:/CDN/Mirror/16042"
TREE = "docs/client-extract/FILETREE.tsv"
CACHE = "docs/client-data/area-index.json.gz"

LZ = bytes([0x5d, 0, 0, 0x10])
FILTERS = [{"id": lzma.FILTER_LZMA1, "dict_size": 0x100000, "lc": 3, "lp": 0, "pb": 2}]
NUL2 = bytes([0, 0])
RECORD = 104
KNOWN = {"CHNK", "PROp", "CURT"}


def visit(args):
    """Decompress one .area file once and return every fact any analysis needs."""
    sha, path = args
    try:
        with open(os.path.join(MIRROR, sha + ".bin"), "rb") as f:
            raw = f.read()
        data = (lzma.LZMADecompressor(format=lzma.FORMAT_RAW, filters=FILTERS).decompress(raw[5:])
                if raw[:4] == LZ else raw)
    except Exception as e:
        return {"path": path, "error": str(e)[:60]}

    out = {"path": path, "size": len(data), "tags": [], "props": 0, "curt": 0, "unknown": []}

    off, b = 0, data[8:]
    while off + 8 <= len(b):
        tag = b[off:off + 4]
        if not (len(tag) == 4 and all(32 <= c < 127 for c in tag)):
            break
        size, = struct.unpack_from("<I", b, off + 4)
        if size > len(b) - off - 8:
            break
        name = tag[::-1].decode("ascii", "replace")
        payload = b[off + 8: off + 8 + size]
        out["tags"].append(name)
        if name not in KNOWN:
            out["unknown"].append([name, size, payload[:32].hex()])

        if name == "PROp" and size >= 8:
            count, = struct.unpack_from("<I", payload, 0)
            table_at = 4 + count * RECORD
            if 0 < count and table_at <= len(payload):
                out["props"] = count
        elif name == "CURT" and size >= 4:
            n, = struct.unpack_from("<I", payload, 0)
            out["curt"] = n

        off += 8 + size

    return out


def build(workers):
    files, seen = [], set()
    with io.open(TREE, encoding="utf-8") as f:
        for ln in f:
            if ln.startswith(("#", "path")):
                continue
            p = ln.rstrip("\n").split("\t")
            if len(p) >= 5 and p[0].lower().endswith(".area") and p[1] not in seen:
                seen.add(p[1])
                files.append((p[1], p[0]))

    print("ONE pass over %d .area files on %d workers" % (len(files), workers))
    import time
    t0 = time.time()
    with mp.Pool(workers) as pool:
        rows = list(pool.imap_unordered(visit, files, chunksize=32))
    dt = time.time() - t0

    os.makedirs(os.path.dirname(CACHE), exist_ok=True)
    with gzip.open(CACHE, "wt", encoding="utf-8") as f:
        json.dump(rows, f)

    errs = [r for r in rows if "error" in r]
    print("%d files in %.1fs (%.0f/sec). errors: %d" % (len(rows), dt, len(rows) / dt, len(errs)))
    print("cache: %s (%.1f MB)" % (CACHE, os.path.getsize(CACHE) / 1048576.0))
    return rows


def load():
    if not os.path.exists(CACHE):
        print("no cache - run --build first")
        sys.exit(1)
    with gzip.open(CACHE, "rt", encoding="utf-8") as f:
        return json.load(f)


def main():
    if "--build" in sys.argv:
        w = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else (os.cpu_count() or 8)
        rows = build(w)
    else:
        rows = load()

    tags = collections.Counter()
    files_with = collections.Counter()
    for r in rows:
        if "tags" not in r:
            continue
        tags.update(r["tags"])
        files_with.update(set(r["tags"]))

    print("\nEVERY top-level chunk tag across ALL %d .area files:" % len(rows))
    for t, n in tags.most_common():
        print("   %-6s %9s occurrences   in %s files" % (t, format(n, ","), format(files_with[t], ",")))

    unknown = [r for r in rows if r.get("unknown")]
    print("\nfiles containing a tag that is NOT PROp/CHNK/CURT: %d" % len(unknown))
    if unknown:
        seen = collections.Counter()
        for r in unknown:
            for name, size, head in r["unknown"]:
                seen[name] += 1
        for name, c in seen.most_common(12):
            ex = next(u for r in unknown for u in r["unknown"] if u[0] == name)
            print("   %-6s in %s files   first payload bytes %s" % (name, format(c, ","), ex[2][:32]))
    else:
        print("   NONE. PROp, CHNK and CURT are the complete tag set - there is no unopened chunk")
        print("   type in this format, so creature spawn data is not hiding in an .area chunk.")

    props = sum(r.get("props", 0) for r in rows)
    curt = sum(r.get("curt", 0) for r in rows)
    print("\ntotals: %s prop placements, %s curve points" % (format(props, ","), format(curt, ",")))


if __name__ == "__main__":
    main()
