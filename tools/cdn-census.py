#!/usr/bin/env python3
"""Census the WildStar CDN mirror: what is actually in the 197,333 content blobs.

D:\\CDN\\Mirror\\16042 is a flat, content-addressed store - every file is named for its SHA1 and
there is no manifest, so nothing says what any blob holds until you open it.

Container formats, measured over a 4,000-blob sample:

    5d 00 00 10   54.6%   LZMA
    RIFF          41.3%   audio
    XFG\\0          4.1%   WildStar's own graphics container

The LZMA is NOT the lzma_alone container Python expects. The header is five bytes - one properties
byte (0x5D = lc3 lp0 pb2) and a four-byte dictionary size (1 MB) - with no uncompressed-size field,
so it needs FORMAT_RAW with an explicit LZMA1 filter starting at offset 5. FORMAT_ALONE fails on
every blob with "Corrupt input data", which reads like a corrupt mirror rather than a wrong reader.

Only the first chunk of each blob is decompressed. The point is to identify the content, and pulling
17 GB through the decompressor to read four magic bytes would take hours.

Usage:  python Tools/cdn-census.py [sample-size]     (0 = every blob)
"""
import collections
import io
import lzma
import os
import sys

MIRROR = r"D:/CDN/Mirror/16042"
OUT = "docs/reference-data/cdn-blob-census.tsv"

LZMA_MAGIC = bytes.fromhex("5d000010")
FILTERS = [{"id": lzma.FILTER_LZMA1, "dict_size": 0x100000, "lc": 3, "lp": 0, "pb": 2}]

# inner magic -> what it is. Names are from the bytes themselves; several are little-endian
# four-character codes, so they read backwards (LDOM = MODL).
KNOWN = {
    b"LDOM": "model (MODL)",
    b"XFG\x00": "graphics (XFG)",
    b"RIFF": "audio/video (RIFF)",
    b"\x89PNG": "PNG image",
    b"DDS ": "DDS texture",
    b"AREA": "area/map data",
    b"TEXT": "text",
    b"\x00\x00\x00\x00": "zero-prefixed (unidentified)",
}


def sniff(raw):
    """Return (container, inner_head) - inner_head is None when nothing could be read."""
    if raw[:4] == LZMA_MAGIC:
        try:
            d = lzma.LZMADecompressor(format=lzma.FORMAT_RAW, filters=FILTERS)
            return "lzma", d.decompress(raw[5:], 64)
        except Exception:
            return "lzma", None
    if raw[:4] == b"RIFF":
        return "riff", raw[:64]
    if raw[:4] == b"XFG\x00":
        return "xfg", raw[:64]
    return "other", raw[:64]


def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
    files = [f for f in os.listdir(MIRROR) if f.endswith(".bin")]
    files.sort()
    if limit:
        step = max(1, len(files) // limit)
        files = files[::step][:limit]

    containers = collections.Counter()
    inners = collections.Counter()
    examples = {}
    failures = 0

    for i, f in enumerate(files):
        path = os.path.join(MIRROR, f)
        try:
            with open(path, "rb") as fh:
                raw = fh.read(1 << 16)
        except Exception:
            failures += 1
            continue

        container, head = sniff(raw)
        containers[container] += 1
        if head is None:
            inners["<decompress failed>"] += 1
            continue

        key = head[:4]
        label = KNOWN.get(key)
        if label is None:
            # printable four-character code, or hex when it is not text
            label = (key.decode("ascii") if all(32 <= b < 127 for b in key)
                     else key.hex())
        inners[label] += 1
        if label not in examples:
            examples[label] = (f, head[:48])

    print("blobs examined: %d   read failures: %d" % (len(files), failures))
    print("\ncontainers:")
    for c, n in containers.most_common():
        print("   %-8s %6d  %5.1f%%" % (c, n, 100.0 * n / len(files)))

    print("\ninner content:")
    with io.open(OUT, "w", encoding="utf-8", newline="") as out:
        out.write("# What the CDN mirror blobs contain, by inner magic after decompression.\n")
        out.write("# source: %s  (sample of %d of the full store)\n" % (MIRROR, len(files)))
        out.write("kind\tcount\tpercent\texampleBlob\n")
        for label, n in inners.most_common(40):
            pct = 100.0 * n / len(files)
            blob = examples.get(label, ("", b""))[0]
            print("   %-28s %6d  %5.1f%%  %s" % (label, n, pct, blob[:16]))
            out.write("%s\t%d\t%.2f\t%s\n" % (label, n, pct, blob))

    print("\nwrote %s" % OUT)


if __name__ == "__main__":
    main()
