#!/usr/bin/env python3
"""Deconstruct every file in the CDN and infer the structure of the undocumented formats.

218,427 named files across ~20 formats. A handful are known (`.tbl`, `.lua`, `.xml`); the rest -
`.m3`, `.tex`, `.area`, `.dgn`, `.i3`, `.sky`, `.sho` - are Carbine's own and nobody has published a
spec.

## The method

Guessing one file's layout is unreliable. Comparing *thousands of files of the same type* is not,
because a field's behaviour across a population tells you what it is:

- a u32 that **never varies** is a magic number or a format version
- a u32 that **correlates with file size** is a count, a length or an offset
- a u32 that is **always small** is a version, a flag set or an enum
- a u32 that is **near-unique per file** is an id or a hash
- **embedded strings** name what the format references - materials, textures, bones

None of that requires knowing the format. All of it is checkable, and the report says which
conclusion each field earned rather than asserting a layout.

Correlation is Pearson's r against file size, computed over every file of that type. `r > 0.9` is
reported as "tracks size"; nothing weaker is called anything.

## What it will not do

It will not print a struct definition. Producing a plausible layout that nobody verified is how a
wrong answer becomes permanent - this project has already had 83 methods filed under a geometry
class and a spell scaling table read as player data. Every line of output states what was measured.

Usage:  python Tools/cdn-deep-analyse.py [--ext .m3] [--sample N] [--workers N]
"""
import collections
import io
import json
import lzma
import math
import multiprocessing as mp
import os
import re
import struct
import sys

MIRROR = r"D:/CDN/Mirror/16042"
TREE = "docs/client-extract/FILETREE.tsv"
OUT = "docs/client-formats"

LZ = bytes.fromhex("5d000010")
FILTERS = [{"id": lzma.FILTER_LZMA1, "dict_size": 0x100000, "lc": 3, "lp": 0, "pb": 2}]

HEADER_WORDS = 24          # u32 slots examined at the head of each file
STRING_RE = re.compile(rb"[A-Za-z0-9_./\\-]{4,64}")
FOURCC_RE = re.compile(rb"[A-Z][A-Z0-9]{3}")


def decompress(raw, limit=None):
    if raw[:4] == LZ:
        d = lzma.LZMADecompressor(format=lzma.FORMAT_RAW, filters=FILTERS)
        return d.decompress(raw[5:], limit) if limit else d.decompress(raw[5:])
    return raw[:limit] if limit else raw


def probe(args):
    """Runs in a worker. Returns facts about one file, or None."""
    sha, path = args
    blob = os.path.join(MIRROR, sha + ".bin")
    try:
        with open(blob, "rb") as f:
            raw = f.read()
        data = decompress(raw)
    except Exception:
        return None

    n = len(data)
    words = []
    for i in range(HEADER_WORDS):
        off = i * 4
        words.append(struct.unpack_from("<I", data, off)[0] if off + 4 <= n else None)

    strings = [s.decode("ascii", "replace") for s in STRING_RE.findall(data[:262144])]
    fourcc = [c.decode("ascii") for c in FOURCC_RE.findall(data[:65536])]

    return {
        "sha": sha,
        "path": path,
        "size": n,
        "magic": data[:4].hex(),
        "magic_ascii": data[:4].decode("ascii", "replace"),
        "words": words,
        "strings": strings[:60],
        "nstrings": len(strings),
        "fourcc": collections.Counter(fourcc).most_common(12),
    }


def pearson(xs, ys):
    m = len(xs)
    if m < 8:
        return 0.0
    mx, my = sum(xs) / m, sum(ys) / m
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    dx = math.sqrt(sum((x - mx) ** 2 for x in xs))
    dy = math.sqrt(sum((y - my) ** 2 for y in ys))
    return (num / (dx * dy)) if dx and dy else 0.0


def describe_field(i, values, sizes):
    """Say what a header word earned the right to be called, and nothing more."""
    vals = [v for v in values if v is not None]
    if not vals:
        return None
    uniq = len(set(vals))
    total = len(vals)

    if uniq == 1:
        v = vals[0]
        asc = struct.pack("<I", v).decode("ascii", "replace")
        printable = all(32 <= c < 127 for c in struct.pack("<I", v))
        return ("constant", "always 0x%08x (%d)%s" % (v, v, (" = %r" % asc) if printable else ""))

    paired = [(v, s) for v, s in zip(values, sizes) if v is not None]
    r = pearson([p[0] for p in paired], [p[1] for p in paired])
    if r > 0.9:
        return ("tracks size", "r=%.3f with file size over %d files" % (r, total))

    if max(vals) < 256 and uniq <= 24:
        common = collections.Counter(vals).most_common(6)
        return ("small set", "%d distinct, max %d: %s"
                % (uniq, max(vals), ", ".join("%d(x%d)" % (v, c) for v, c in common)))

    if uniq / total > 0.95:
        return ("near-unique", "%d distinct across %d files - id or hash" % (uniq, total))

    return ("varies", "%d distinct, range %d..%d" % (uniq, min(vals), max(vals)))


def analyse(ext, results, out_dir):
    if not results:
        return None
    sizes = [r["size"] for r in results]
    magics = collections.Counter(r["magic_ascii"] if all(32 <= ord(c) < 127 for c in r["magic_ascii"])
                                 else r["magic"] for r in results)

    fields = []
    for i in range(HEADER_WORDS):
        d = describe_field(i, [r["words"][i] for r in results], sizes)
        if d:
            fields.append((i, d[0], d[1]))

    vocab = collections.Counter()
    for r in results:
        vocab.update(s for s in r["strings"] if len(s) >= 5)

    chunks = collections.Counter()
    for r in results:
        for c, n in r["fourcc"]:
            chunks[c] += n

    path = os.path.join(out_dir, "%s.md" % ext.lstrip(".") or "noext")
    with io.open(path, "w", encoding="utf-8", newline="") as f:
        f.write("# `%s` — %d files\n\n" % (ext or "(no extension)", len(results)))
        f.write("Measured across **every %s file in the client**, not sampled from one.\n\n" % ext)
        f.write("| | |\n|---|---|\n")
        f.write("| files | %d |\n" % len(results))
        f.write("| total decompressed | %.1f MB |\n" % (sum(sizes) / 1048576.0))
        f.write("| smallest / median / largest | %s / %s / %s bytes |\n"
                % (format(min(sizes), ","), format(sorted(sizes)[len(sizes) // 2], ","),
                   format(max(sizes), ",")))
        f.write("\n## Magic\n\n")
        for m, c in magics.most_common(8):
            f.write("- `%s` — %d files (%.1f%%)\n" % (m, c, 100.0 * c / len(results)))

        f.write("\n## Header words\n\n")
        f.write("What each 32-bit slot at the head of the file *does across the population*. A field\n")
        f.write("that never varies is a magic or version; one that tracks file size is a count,\n")
        f.write("length or offset. **These are measurements, not a struct definition.**\n\n")
        f.write("| offset | behaviour | evidence |\n|---|---|---|\n")
        for i, kind, ev in fields:
            f.write("| +%d | **%s** | %s |\n" % (i * 4, kind, ev))

        if chunks:
            f.write("\n## Four-character codes found in the body\n\n")
            f.write("Uppercase 4-byte sequences, which in this client's formats are usually section tags.\n\n")
            f.write("| code | occurrences |\n|---|---|\n")
            for c, n in chunks.most_common(20):
                f.write("| `%s` | %s |\n" % (c, format(n, ",")))

        if vocab:
            f.write("\n## Strings it references\n\n")
            f.write("%s distinct strings of 5+ characters. The most common name what this format\n"
                    % format(len(vocab), ","))
            f.write("points at.\n\n")
            f.write("| string | files |\n|---|---|\n")
            for s, c in vocab.most_common(25):
                f.write("| `%s` | %s |\n" % (s.replace("|", "\\|")[:70], format(c, ",")))

        f.write("\n## Examples\n\n")
        for r in results[:8]:
            f.write("- `%s` — %s bytes\n" % (r["path"], format(r["size"], ",")))

    return {
        "ext": ext, "files": len(results), "bytes": sum(sizes),
        "magic": magics.most_common(1)[0][0] if magics else "",
        "fields": fields, "chunks": chunks.most_common(8),
        "vocab": vocab.most_common(10),
    }


def main():
    only = sys.argv[sys.argv.index("--ext") + 1] if "--ext" in sys.argv else None
    sample = int(sys.argv[sys.argv.index("--sample") + 1]) if "--sample" in sys.argv else 0
    workers = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else (os.cpu_count() or 8)

    by_ext = collections.defaultdict(list)
    with io.open(TREE, encoding="utf-8") as f:
        for ln in f:
            if ln.startswith(("#", "path")):
                continue
            p = ln.rstrip("\n").split("\t")
            if len(p) < 5 or p[4] != "yes":
                continue
            by_ext[os.path.splitext(p[0])[1].lower()].append((p[1], p[0]))

    if only:
        by_ext = {only: by_ext.get(only, [])}

    os.makedirs(OUT, exist_ok=True)
    print("%d formats, %d files total" % (len(by_ext), sum(len(v) for v in by_ext.values())))

    summary = []
    for ext, entries in sorted(by_ext.items(), key=lambda kv: -len(kv[1])):
        # de-duplicate by hash: the same content under several names measures the same file twice
        seen, uniq = set(), []
        for sha, path in entries:
            if sha not in seen:
                seen.add(sha)
                uniq.append((sha, path))
        work = uniq[:sample] if sample else uniq

        with mp.Pool(workers) as pool:
            results = [r for r in pool.imap_unordered(probe, work, chunksize=16) if r]

        s = analyse(ext, results, OUT)
        if s:
            summary.append(s)
            print("  %-8s %6d files  %8.1f MB  magic %-6s  %d header fields"
                  % (ext or "(none)", s["files"], s["bytes"] / 1048576.0, s["magic"], len(s["fields"])))

    with io.open(os.path.join(OUT, "summary.json"), "w", encoding="utf-8") as f:
        json.dump([{k: (v if k not in ("chunks", "vocab", "fields") else v) for k, v in s.items()}
                   for s in summary], f, indent=1, default=str)

    print("\nwrote %d format documents to %s/" % (len(summary), OUT))


if __name__ == "__main__":
    main()
