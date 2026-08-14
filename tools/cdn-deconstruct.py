#!/usr/bin/env python3
"""Decode and sort EVERY blob in the CDN mirror, across all cores.

The earlier pass (`cdn-extract-text.py`) was single-threaded and only kept text, so 196,455 of the
197,333 blobs were classified and thrown away. This one decodes all of them and sorts the results by
what they actually are.

## Why this is CPU and RAM work, not GPU work

The machine has a 9950X3D (16C/32T), 61.7 GB of RAM and an RTX 5090. Only two of those three help:

- **32 threads** — decompression is the whole cost and every blob is independent, so this is a clean
  parallel map. Expect close to linear scaling.
- **61.7 GB RAM** — the entire 17 GB mirror fits in memory. Workers read whole files rather than
  streaming, and the OS page cache keeps the hot set resident after the first pass.
- **The 5090 does nothing here.** LZMA is sequential and branch-heavy: each symbol depends on the
  decoder state left by the previous one, which is the opposite of what a GPU is for. There is no
  CUDA LZMA that beats 32 CPU threads on this, and writing one would cost more than the run saves.
  Said plainly rather than quietly leaving the GPU idle and letting it look considered.

Multiprocessing, not threads: CPython's GIL is released inside `lzma` but re-acquired for every
Python-level operation around it, and the classification work between decompressions is Python.

## What it produces

`docs/client-extract/` sorted by content, plus `CENSUS.tsv` with one row per blob — its hash, what
it turned out to be, the compressed and decompressed sizes. **Every blob gets a row, including the
ones that fail**, because a blob missing from the census is indistinguishable from one that was
never looked at.

Usage:  python Tools/cdn-deconstruct.py [--workers N] [--limit N] [--write-binaries]
"""
import io
import lzma
import multiprocessing as mp
import os
import re
import sys
import time

MIRROR = r"D:/CDN/Mirror/16042"
OUT = "docs/client-extract"

LZMA_MAGIC = bytes.fromhex("5d000010")
FILTERS = [{"id": lzma.FILTER_LZMA1, "dict_size": 0x100000, "lc": 3, "lp": 0, "pb": 2}]

# Four-character codes seen in the census. Several are stored little-endian and so read backwards.
FOURCC = {
    b"LDOM": ("model", "m3"),
    b"XFG\x00": ("graphics", "xfg"),
    b"RIFF": ("audio", "riff"),
    b"aera": ("area", "area"),
    b"AERA": ("area", "area"),
    b"YKSX": ("sky", "sky"),
    b"FEDS": ("shader-def", "sdef"),
    b"LBTD": ("table", "tbl"),
    b"NGND": ("engine", "engn"),
    b"FEDI": ("idef", "idef"),
    b"STGT": ("tgts", "tgts"),
    b"SHDR": ("shader", "shdr"),
    b"KCAP": ("archive", "archive"),
    b"\x89PNG": ("png", "png"),
    b"DDS ": ("dds", "dds"),
}

TEXT_STARTS = (b"<?xm", b"<For", b"<Add", b"<Xml", b"<Doc", b"--", b"local ", b"function ",
               b"<Sprite", b"<Ui", b"#", b"//")


def decompress(raw, limit=None):
    if raw[:4] == LZMA_MAGIC:
        d = lzma.LZMADecompressor(format=lzma.FORMAT_RAW, filters=FILTERS)
        return d.decompress(raw[5:], limit) if limit else d.decompress(raw[5:])
    return raw[:limit] if limit else raw


def classify(head):
    for magic, (kind, ext) in FOURCC.items():
        if head.startswith(magic):
            return kind, ext
    if head.startswith(TEXT_STARTS) or head[:2] in (b"\xff\xfe", b"\xfe\xff"):
        return "text", "txt"
    printable = sum(1 for b in head[:256] if 9 <= b < 127)
    if len(head) > 16 and printable / min(len(head), 256) > 0.95:
        return "text", "txt"
    return "unknown", "bin"


def hint_for(text):
    m = re.search(r"<([A-Za-z][A-Za-z0-9_]{2,40})", text[:4000])
    if m:
        return m.group(1)[:40]
    m = re.search(r"--+\s*([A-Za-z][A-Za-z0-9_ .-]{3,40})", text[:400])
    if m:
        return re.sub(r"[^A-Za-z0-9_.-]+", "-", m.group(1).strip())[:40]
    return ""


def work(name):
    """Runs in a worker process. Returns a census row; writes text assets to disk."""
    path = os.path.join(MIRROR, name)
    sha = name[:-4]
    try:
        with open(path, "rb") as f:
            raw = f.read()
    except Exception as e:
        return (sha, "unreadable", 0, 0, "", str(e)[:60])

    comp = len(raw)
    container = "lzma" if raw[:4] == LZMA_MAGIC else "raw"

    try:
        full = decompress(raw)
    except Exception as e:
        return (sha, "decompress-failed", comp, 0, container, str(e)[:60])

    kind, ext = classify(full[:512])

    # Text is the seam worth keeping as files; everything else is censused, not written, because
    # 16 GB of decoded audio and textures on disk answers no question this project has.
    hint = ""
    if kind == "text":
        try:
            text = full.decode("utf-8")
        except UnicodeDecodeError:
            try:
                text = full.decode("utf-16")
            except UnicodeDecodeError:
                return (sha, "text-undecodable", comp, len(full), container, "")
        stripped = text.lstrip()
        sub = "xml" if stripped.startswith("<") else ("lua" if re.match(r"^(--|local |function )", stripped) else "text")
        hint = hint_for(text)
        fname = "%s-%s.%s" % (sha[:12], hint, "xml" if sub == "xml" else ("lua" if sub == "lua" else "txt")) if hint \
            else "%s.%s" % (sha[:12], "xml" if sub == "xml" else ("lua" if sub == "lua" else "txt"))
        d = os.path.join(OUT, sub)
        os.makedirs(d, exist_ok=True)
        with io.open(os.path.join(d, fname), "w", encoding="utf-8", newline="") as f:
            f.write(text)
        kind = sub

    return (sha, kind, comp, len(full), container, hint)


def main():
    workers = os.cpu_count() or 8
    if "--workers" in sys.argv:
        workers = int(sys.argv[sys.argv.index("--workers") + 1])
    limit = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else 0

    files = sorted(f for f in os.listdir(MIRROR) if f.endswith(".bin"))
    if limit:
        files = files[:limit]

    os.makedirs(OUT, exist_ok=True)
    print("%d blobs, %d worker processes" % (len(files), workers))

    started = time.time()
    rows = []
    # chunksize matters: at 197k tiny tasks the IPC round-trip dominates otherwise
    with mp.Pool(workers) as pool:
        for i, row in enumerate(pool.imap_unordered(work, files, chunksize=64), 1):
            rows.append(row)
            if i % 20000 == 0:
                rate = i / (time.time() - started)
                print("  %6d / %d   %.0f blobs/sec" % (i, len(files), rate))

    elapsed = time.time() - started
    with io.open(os.path.join(OUT, "CENSUS.tsv"), "w", encoding="utf-8", newline="") as f:
        f.write("# Every blob in the CDN mirror, decoded and classified.\n")
        f.write("# EVERY blob has a row, including failures - a blob missing from this file would be\n")
        f.write("# indistinguishable from one that was never examined.\n")
        f.write("sha1\tkind\tcompressed\tdecompressed\tcontainer\thint\n")
        for r in sorted(rows):
            f.write("\t".join(str(x) for x in r) + "\n")

    import collections
    counts = collections.Counter(r[1] for r in rows)
    total_in = sum(r[2] for r in rows)
    total_out = sum(r[3] for r in rows)
    print("\n%d blobs in %.1fs (%.0f/sec, %d workers)" % (len(rows), elapsed, len(rows) / elapsed, workers))
    print("%.1f GB compressed -> %.1f GB decoded (%.2fx)"
          % (total_in / 2**30, total_out / 2**30, (total_out / total_in) if total_in else 0))
    print()
    for k, n in counts.most_common():
        print("  %-20s %7d  %5.1f%%" % (k, n, 100.0 * n / len(rows)))


if __name__ == "__main__":
    main()
