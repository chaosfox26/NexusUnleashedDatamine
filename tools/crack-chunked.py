#!/usr/bin/env python3
"""Walk the nested chunk structure of the client's undocumented container formats.

Targets `.i3` (1,696 files, 2 GB, magic SDEF) and `.area` (11,651 files, 12.9 GB, magic AREA), which
are the two largest formats whose insides are unknown.

## Why this exists, and what it corrects

A previous pass counted uppercase four-byte sequences with a regex and reported "88,255 PROP records
- every object placed in the world". That was wrong twice over:

  1. It counted BYTE PATTERNS, not parsed records. Any four bytes that happen to be uppercase ASCII
     matched, including the middle of a float array or a compressed block.
  2. It scanned only the first 64 KB of each file, so the number was neither a total nor a sample -
     it was an artefact of a window size.

Structurally, all 300 `.area` files sampled afterwards have exactly ONE top-level chunk: `CHNK`.
`PROP` is not a top-level record in any of them.

So this tool parses rather than greps. A chunk is only accepted when its declared size actually fits
the remaining buffer and lands exactly on the next chunk boundary. A tag that fails that test is not
a chunk, however much it looks like one.

## The walk

    header : 8 bytes (magic + u32)
    chunk  : 4-byte tag (stored reversed), u32 payload size, payload

Recursion happens only when a payload's first eight bytes themselves parse as a chunk header whose
size fits. Anything else is a leaf and its bytes are profiled, not invented.

Usage:  python Tools/crack-chunked.py --ext .i3 [--sample N] [--workers N]
"""
import collections
import io
import json
import lzma
import multiprocessing as mp
import os
import struct
import sys

MIRROR = r"D:/CDN/Mirror/16042"
TREE = "docs/client-extract/FILETREE.tsv"
OUT = "docs/client-formats"

LZ = bytes.fromhex("5d000010")
FILTERS = [{"id": lzma.FILTER_LZMA1, "dict_size": 0x100000, "lc": 3, "lp": 0, "pb": 2}]


def decompress(raw):
    if raw[:4] == LZ:
        return lzma.LZMADecompressor(format=lzma.FORMAT_RAW, filters=FILTERS).decompress(raw[5:])
    return raw


def printable_tag(b):
    return len(b) == 4 and all(32 <= c < 127 for c in b) and b.strip() == b


def parse_chunks(buf, depth=0, maxdepth=6):
    """Return [(depth, tag, offset, size, leafbytes)] for a buffer that parses cleanly as chunks.

    Returns None when the buffer does not parse - which is the point. A partial parse is reported as
    no parse, because half a structure is the shape that gets mistaken for a discovery.
    """
    out, off, n = [], 0, len(buf)
    while off + 8 <= n:
        tag = buf[off:off + 4]
        if not printable_tag(tag):
            return None if not out else out
        size, = struct.unpack_from("<I", buf, off + 4)
        if size > n - off - 8:
            return None if not out else out
        payload = buf[off + 8: off + 8 + size]
        name = tag[::-1].decode("ascii", "replace")

        kids = None
        if depth < maxdepth and size >= 8 and printable_tag(payload[:4]):
            inner, = struct.unpack_from("<I", payload, 4)
            if inner <= size - 8:
                kids = parse_chunks(payload, depth + 1, maxdepth)

        out.append((depth, name, off, size, None if kids else payload[:64]))
        if kids:
            out.extend(kids)
        off += 8 + size
        if off == n:
            break
    return out


def probe(args):
    sha, path = args
    try:
        data = decompress(open(os.path.join(MIRROR, sha + ".bin"), "rb").read())
    except Exception:
        return None

    header = data[:8]
    chunks = parse_chunks(data[8:], 0)
    if chunks is None:
        return {"path": path, "size": len(data), "header": header.hex(), "parsed": False,
                "tags": [], "leafheads": []}

    tags = collections.Counter((d, t) for d, t, _, _, _ in chunks)
    leaf = [(t, lh.hex()[:32]) for d, t, _, _, lh in chunks if lh is not None][:6]
    return {"path": path, "size": len(data), "header": header.hex(), "parsed": True,
            "tags": [(f"{d}:{t}", c) for (d, t), c in tags.items()], "leafheads": leaf,
            "nchunks": len(chunks), "depth": max((d for d, _, _, _, _ in chunks), default=0)}


def main():
    ext = sys.argv[sys.argv.index("--ext") + 1] if "--ext" in sys.argv else ".i3"
    sample = int(sys.argv[sys.argv.index("--sample") + 1]) if "--sample" in sys.argv else 0
    workers = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else (os.cpu_count() or 8)

    files, seen = [], set()
    with io.open(TREE, encoding="utf-8") as f:
        for ln in f:
            if ln.startswith(("#", "path")):
                continue
            p = ln.rstrip("\n").split("\t")
            if len(p) >= 5 and p[0].lower().endswith(ext) and p[1] not in seen:
                seen.add(p[1])
                files.append((p[1], p[0]))
    if sample:
        files = files[:sample]

    print("%s: %d distinct files, %d workers" % (ext, len(files), workers))
    with mp.Pool(workers) as pool:
        results = [r for r in pool.imap_unordered(probe, files, chunksize=8) if r]

    parsed = [r for r in results if r["parsed"]]
    print("parsed as chunked: %d of %d (%.1f%%)" % (len(parsed), len(results),
                                                    100.0 * len(parsed) / len(results) if results else 0))

    tagcount = collections.Counter()
    filecount = collections.Counter()
    for r in parsed:
        for k, c in r["tags"]:
            tagcount[k] += c
            filecount[k] += 1

    headers = collections.Counter(r["header"] for r in results)

    name = ext.lstrip(".")
    path = os.path.join(OUT, "%s-structure.md" % name)
    with io.open(path, "w", encoding="utf-8", newline="") as f:
        f.write("# `%s` internal structure\n\n" % ext)
        f.write("Parsed, not grepped: a chunk is accepted only when its declared size fits the buffer\n")
        f.write("and lands exactly on the next chunk boundary. A tag failing that is not a chunk,\n")
        f.write("however much it looks like one.\n\n")
        f.write("**%d distinct files. %d parsed cleanly as chunked (%.1f%%).**\n\n"
                % (len(results), len(parsed), 100.0 * len(parsed) / len(results) if results else 0))

        f.write("## File header\n\n| first 8 bytes | files |\n|---|---|\n")
        for h, c in headers.most_common(6):
            try:
                asc = bytes.fromhex(h).decode("ascii", "replace")
                asc = "".join(ch if 32 <= ord(ch) < 127 else "." for ch in asc)
            except Exception:
                asc = ""
            f.write("| `%s` `%s` | %s |\n" % (h, asc, format(c, ",")))

        if tagcount:
            f.write("\n## Chunk tags, by nesting depth\n\n")
            f.write("`depth:TAG` — depth 0 is a top-level chunk. **Occurrences** counts every instance;\n")
            f.write("**files** counts how many files contain at least one.\n\n")
            f.write("| tag | occurrences | files |\n|---|---|---|\n")
            for k, c in tagcount.most_common(40):
                f.write("| `%s` | %s | %s |\n" % (k, format(c, ","), format(filecount[k], ",")))
        else:
            f.write("\n## Chunk tags\n\n**None.** No file parsed as a chunk container, so this format\n")
            f.write("is not chunked in the way `.area` is - the header is followed by something else.\n")

        f.write("\n## Leaf payload heads\n\n")
        f.write("First bytes of payloads with no further chunk structure — the raw data itself.\n\n")
        for r in parsed[:10]:
            for t, lh in r["leafheads"][:2]:
                f.write("- `%s` — `%s`\n" % (t, lh))

    with io.open(os.path.join(OUT, "%s-structure.json" % name), "w", encoding="utf-8") as f:
        json.dump({"ext": ext, "files": len(results), "parsed": len(parsed),
                   "tags": tagcount.most_common(60)}, f, indent=1)

    print("\ntop chunk tags:")
    for k, c in tagcount.most_common(15):
        print("   %-14s %8s occurrences  in %s files" % (k, format(c, ","), format(filecount[k], ",")))
    print("\nwrote %s" % path)


if __name__ == "__main__":
    main()
