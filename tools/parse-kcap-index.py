#!/usr/bin/env python3
"""Walk a KCAP archive index and recover the client's real filenames.

The CDN mirror is content-addressed: 197,333 blobs each named for its own SHA1, with no manifest and
no filenames. `ClientData.index` is the missing half - 12.4 MB naming what all of it is.

## The format, worked out from the bytes

    offset 0    "KCAP", u32 version = 1
    offset 520  u64 fileSize, u64, u64 blockTableOffset, u64 blockCount
    offset 576  "AIDX", u32 version, u32 build (16042), u32
    blockTable  blockCount x (u64 offset, u64 size)

Every block is one directory:

    u32 dirCount
    u32 fileCount
    dirCount  x (u32 nameOffset, u32 blockIndex)                       8 bytes
    fileCount x (u32 nameOffset, u32 flags, u64 writeTime,            56 bytes
                 u64 uncompressedSize, u64 compressedSize, u8 sha1[20], u32)
    string table, NUL-separated, shared by both arrays

**The SHA1 in a file entry is the CDN blob name.** Confirmed on the first row read: hash
e7a6a2ab03148c87f7f3d36b61f1b5f230094f38 exists in the mirror AND is 1,543 bytes, matching that
row's compressedSize exactly - two independent checks out of one entry.

Three things established by arithmetic rather than assumption, each of which I first read wrong:

- `blockCount` is a COUNT, not a byte size. 8680 x 16 = 138,880, which fills the file from the block
  table to EOF. Read as a size it gave 542 blocks and nothing parsed.
- The `16042` at offset 584 is the BUILD NUMBER, not a block index. Using it as an index threw an
  out-of-range error - the useful kind of failure, one that cannot be mistaken for success.
- The second u32 of a block is a FILE COUNT, not padding. Reading it as padding parsed only the
  directory half and recovered 2,067 names out of 45,004, with seven of the nine top-level folders
  showing exactly one child each. A tree that lopsided is the shape of a parser giving up, not of a
  real filesystem.

Usage:  python Tools/parse-kcap-index.py [index-path ...]
"""
import collections
import io
import os
import struct
import sys

OUT = "docs/client-extract/FILETREE.tsv"
DEFAULT = [r"D:/CDN/Install/Patch/ClientData.index"]


def load_blocks(d):
    _size, _pad, bt, count = struct.unpack_from("<QQQQ", d, 520)
    return [struct.unpack_from("<QQ", d, bt + i * 16) for i in range(count)]


def read_block(d, offset, size):
    """Return (dirs, files) for one block, or None if it does not parse as one."""
    if size < 8:
        return None
    ndir, nfile = struct.unpack_from("<II", d, offset)
    if ndir > 60000 or nfile > 60000:
        return None

    entries_end = 8 + ndir * 8 + nfile * 56
    if entries_end > size:
        return None

    strings = d[offset + entries_end: offset + size]

    def name_at(off):
        if off >= len(strings):
            return None
        end = strings.find(b"\x00", off)
        if end < 0:
            return None
        try:
            return strings[off:end].decode("ascii")
        except UnicodeDecodeError:
            return None

    dirs = []
    for i in range(ndir):
        no, blk = struct.unpack_from("<II", d, offset + 8 + i * 8)
        n = name_at(no)
        if n is None:
            return None
        dirs.append((n, blk))

    files = []
    base = offset + 8 + ndir * 8
    for i in range(nfile):
        no, flags, _wtime, usize, csize = struct.unpack_from("<IIQQQ", d, base + i * 56)
        sha = d[base + i * 56 + 32: base + i * 56 + 52].hex()
        n = name_at(no)
        if n is None:
            return None
        files.append((n, sha, usize, csize, flags))

    return dirs, files


def walk(path, rows, mirror_names):
    d = open(path, "rb").read()
    if d[:4] != b"KCAP":
        print("  %s: not a KCAP file" % os.path.basename(path))
        return 0, 0

    blocks = load_blocks(d)

    root = None
    for i, (o, s) in enumerate(blocks):
        if s == 0:
            continue
        b = read_block(d, o, s)
        if b and any(n in ("Art", "UI", "Audio", "Map", "DB") for n, _ in b[0]):
            root = i
            break
    if root is None:
        print("  %s: no root block found" % os.path.basename(path))
        return 0, 0

    ndirs = nfiles = 0
    seen = set()
    stack = [(root, "")]
    while stack:
        block, path_so_far = stack.pop()
        if block in seen or block >= len(blocks):
            continue
        seen.add(block)
        o, s = blocks[block]
        if s == 0:
            continue

        parsed = read_block(d, o, s)
        if parsed is None:
            rows.append((path_so_far or "?", "", 0, 0, "unparsed"))
            continue

        dirs, files = parsed
        ndirs += 1
        for name, sha, usize, csize, flags in files:
            full = "%s/%s" % (path_so_far, name) if path_so_far else name
            present = "yes" if sha in mirror_names else "no"
            rows.append((full, sha, usize, csize, present))
            nfiles += 1
        for name, child in dirs:
            stack.append((child, "%s/%s" % (path_so_far, name) if path_so_far else name))

    return ndirs, nfiles


def main():
    paths = sys.argv[1:] or DEFAULT

    mirror = r"D:/CDN/Mirror/16042"
    mirror_names = set()
    if os.path.isdir(mirror):
        mirror_names = {f[:-4] for f in os.listdir(mirror) if f.endswith(".bin")}
    print("mirror holds %d blobs" % len(mirror_names))

    rows = []
    for p in paths:
        if not os.path.exists(p):
            print("  missing: %s" % p)
            continue
        nd, nf = walk(p, rows, mirror_names)
        print("  %-24s %5d directories, %6d files" % (os.path.basename(p), nd, nf))

    with io.open(OUT, "w", encoding="utf-8", newline="") as f:
        f.write("# The client's real filenames, recovered from the KCAP archive index.\n")
        f.write("# The CDN mirror is content-addressed and nameless; the sha1 column is what names it -\n")
        f.write("# each one is a blob filename in D:\\CDN\\Mirror\\16042.\n")
        f.write("# inMirror=no means the index lists a file the mirror does not hold.\n")
        f.write("path\tsha1\tuncompressed\tcompressed\tinMirror\n")
        for r in sorted(rows):
            f.write("%s\t%s\t%d\t%d\t%s\n" % r)

    present = sum(1 for r in rows if r[4] == "yes")
    print("\n%d files named, %d present in the mirror (%.1f%%)"
          % (len(rows), present, 100.0 * present / len(rows) if rows else 0))
    print("wrote %s" % OUT)

    tops = collections.Counter(r[0].split("/")[0] for r in rows)
    print("\nby top-level folder:")
    for t, n in tops.most_common(12):
        print("   %-14s %7d" % (t, n))

    exts = collections.Counter(os.path.splitext(r[0])[1].lower() for r in rows)
    print("\nby extension:")
    for e, n in exts.most_common(16):
        print("   %-14s %7d" % (e or "(none)", n))


if __name__ == "__main__":
    main()
