#!/usr/bin/env python3
"""Pull every text asset - Lua, XML, config - out of the WildStar CDN mirror.

The census showed the store is overwhelmingly audio, textures and models, but a thin seam of it is
TEXT: blobs opening with `<?xm`, `<For`, `<Add` and `-- ` (a Lua comment). Those are the client's own
UI forms and scripts, and they are worth more to this project than the other 99%, because they show
the Apollo API *being used* rather than merely named.

Nothing here is guessed from a filename - there are no filenames. The store is content-addressed:
every file is called after its SHA1 and no manifest exists. So each blob is opened, sniffed, and
classified by what it actually contains.

Files are named `<detected-kind>/<sha1-prefix>-<hint>.<ext>`, where the hint comes from inside the
content (an XML root element, a Lua header comment). A blob whose content suggests no name keeps its
hash alone - inventing a plausible name for it would be the same mistake as inventing an API method.

Usage:  python Tools/cdn-extract-text.py [--limit N]
"""
import io
import lzma
import os
import re
import sys

MIRROR = r"D:/CDN/Mirror/16042"
OUTDIR = "docs/client-extract"

LZMA_MAGIC = bytes.fromhex("5d000010")
FILTERS = [{"id": lzma.FILTER_LZMA1, "dict_size": 0x100000, "lc": 3, "lp": 0, "pb": 2}]

# openings that mark a text asset. Checked against the decompressed head, not the blob.
TEXT_STARTS = (b"<?xm", b"<For", b"<Add", b"<Xml", b"<Doc", b"--", b"local ", b"function ",
               b"<Sprite", b"<Ui", b"#", b"//")


def decompress(raw, limit=None):
    if raw[:4] == LZMA_MAGIC:
        d = lzma.LZMADecompressor(format=lzma.FORMAT_RAW, filters=FILTERS)
        return d.decompress(raw[5:], limit) if limit else d.decompress(raw[5:])
    return raw[:limit] if limit else raw


def looks_text(head):
    if head.startswith(TEXT_STARTS):
        return True
    # UTF-16 XML, which the client uses for some forms
    if head[:2] in (b"\xff\xfe", b"\xfe\xff"):
        return True
    printable = sum(1 for b in head if 9 <= b < 127)
    return len(head) > 16 and printable / len(head) > 0.95


def hint_for(text):
    m = re.search(r"<([A-Za-z][A-Za-z0-9_]{2,40})", text[:4000])
    if m:
        return m.group(1)[:40]
    m = re.search(r"--+\s*([A-Za-z][A-Za-z0-9_ .-]{3,40})", text[:400])
    if m:
        return re.sub(r"[^A-Za-z0-9_.-]+", "-", m.group(1).strip())[:40]
    m = re.search(r"function\s+([A-Za-z_][A-Za-z0-9_.:]{2,40})", text[:2000])
    if m:
        return m.group(1).replace(":", "-")[:40]
    return ""


def main():
    limit = 0
    if "--limit" in sys.argv:
        limit = int(sys.argv[sys.argv.index("--limit") + 1])

    files = sorted(f for f in os.listdir(MIRROR) if f.endswith(".bin"))
    if limit:
        files = files[:limit]

    os.makedirs(OUTDIR, exist_ok=True)
    found = {"lua": 0, "xml": 0, "text": 0}
    manifest = []
    scanned = 0

    for f in files:
        scanned += 1
        path = os.path.join(MIRROR, f)
        try:
            with open(path, "rb") as fh:
                raw = fh.read(1 << 20)
            head = decompress(raw, 256)
        except Exception:
            continue

        if not head or not looks_text(head):
            continue

        try:
            with open(path, "rb") as fh:
                full = decompress(fh.read())
        except Exception:
            continue

        try:
            text = full.decode("utf-8")
        except UnicodeDecodeError:
            try:
                text = full.decode("utf-16")
            except UnicodeDecodeError:
                continue

        stripped = text.lstrip()
        if stripped.startswith("<"):
            kind, ext = "xml", "xml"
        elif re.match(r"^(--|local |function )", stripped):
            kind, ext = "lua", "lua"
        else:
            kind, ext = "text", "txt"

        hint = hint_for(text)
        sha = f[:-4]
        name = "%s-%s.%s" % (sha[:12], hint, ext) if hint else "%s.%s" % (sha[:12], ext)
        sub = os.path.join(OUTDIR, kind)
        os.makedirs(sub, exist_ok=True)
        with io.open(os.path.join(sub, name), "w", encoding="utf-8", newline="") as out:
            out.write(text)

        found[kind] += 1
        manifest.append((kind, sha, len(text), hint))

        if scanned % 20000 == 0:
            sys.stderr.write("  %d scanned, %d text assets\n" % (scanned, sum(found.values())))
            sys.stderr.flush()

    with io.open(os.path.join(OUTDIR, "MANIFEST.tsv"), "w", encoding="utf-8", newline="") as out:
        out.write("# Text assets recovered from the content-addressed CDN mirror.\n")
        out.write("# The store has no filenames - every blob is named for its SHA1 - so `hint` is\n")
        out.write("# taken from INSIDE the content and is a description, not the original filename.\n")
        out.write("kind\tsha1\tchars\thint\n")
        for kind, sha, n, hint in sorted(manifest):
            out.write("%s\t%s\t%d\t%s\n" % (kind, sha, n, hint))

    print("scanned %d blobs" % scanned)
    print("recovered: %d lua, %d xml, %d other text" % (found["lua"], found["xml"], found["text"]))
    print("wrote %s/" % OUTDIR)


if __name__ == "__main__":
    main()
