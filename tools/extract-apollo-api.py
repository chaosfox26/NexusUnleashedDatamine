#!/usr/bin/env python3
"""Extract the Apollo Lua API from the WildStar client binary itself.

The community API reference is secondary and demonstrably incomplete - it is missing Tenacity,
Toughness, Hope, Cooldown Reduction and Focus Pool, all of which the live character sheet shows. The
client is the authority (CLAUDE.md rule 7a: the client is definitive, the web ranks below it).

Method. The Lua bindings register each method by NAME, so every name exists in the binary as a
null-terminated string, and the registration tables put them next to each other. So:

  1. pull every null-terminated identifier-shaped string with its file offset
  2. find where the names we already know from the reference land
  3. take EVERY identifier in those same regions - that is the real surface, including the entries
     the reference never had

Step 3 is the point. Filtering to names already known would only ever reproduce the list we started
with, which is the mistake this whole exercise exists to correct.

Usage:  python Tools/extract-apollo-api.py [path-to-WildStar64.exe]
"""
import collections
import io
import os
import re
import sys

EXE = sys.argv[1] if len(sys.argv) > 1 else r"D:/CDN/Install/Client64/WildStar64.exe"
REF = "docs/reference-data/apollo-api-surface.tsv"
OUT = "docs/reference-data/apollo-api-client.tsv"

# identifier-shaped, long enough not to be noise
IDENT = re.compile(rb"[A-Za-z_][A-Za-z0-9_]{3,63}\x00")


def main():
    data = open(EXE, "rb").read()
    print("%s: %.1f MB" % (os.path.basename(EXE), len(data) / 1048576.0))

    strings = []          # (offset, name)
    for m in IDENT.finditer(data):
        strings.append((m.start(), m.group()[:-1].decode("ascii")))
    print("identifier-shaped strings: %d" % len(strings))

    # names we already know, purely to locate the regions
    known = set()
    if os.path.exists(REF):
        with io.open(REF, encoding="utf-8") as f:
            for ln in f:
                if ln.startswith("#"):
                    continue
                p = ln.rstrip("\n").split("\t")
                if len(p) == 3:
                    known.add(p[2].split("(")[0].strip())
                    known.add(p[0])
    print("reference names used as anchors: %d" % len(known))

    hits = [(off, n) for off, n in strings if n in known]
    if not hits:
        print("no anchors found - the binary may be packed; nothing to report honestly")
        return
    print("anchors located in the binary: %d" % len(hits))

    # Cluster the anchors, then keep every identifier inside a cluster's span. A gap larger than
    # GAP means we have left the registration data and wandered into unrelated strings.
    GAP = 4096
    offs = sorted(o for o, _ in hits)
    regions, start, prev = [], offs[0], offs[0]
    for o in offs[1:]:
        if o - prev > GAP:
            regions.append((start, prev))
            start = o
        prev = o
    regions.append((start, prev))
    span = sum(b - a for a, b in regions)
    print("regions: %d covering %.1f KB" % (len(regions), span / 1024.0))

    inside = []
    ri = 0
    for off, n in strings:
        while ri < len(regions) and off > regions[ri][1]:
            ri += 1
        if ri < len(regions) and regions[ri][0] <= off <= regions[ri][1]:
            inside.append((off, n))

    # method-shaped names are the ones worth asserting on
    verbs = ("Get", "Set", "Is", "Can", "Has", "Add", "Remove", "Show", "Hide", "Create",
             "Destroy", "Request", "Send", "Find", "Register", "Unregister", "Load", "Save",
             "Enable", "Disable", "Toggle", "Reset", "Clear", "Start", "Stop", "Update")
    methods = sorted({n for _, n in inside if n.startswith(verbs)})
    novel = sorted(m for m in methods if m not in known)

    with io.open(OUT, "w", encoding="utf-8", newline="") as f:
        f.write("# Apollo API names read from the CLIENT BINARY, not from any external reference.\n")
        f.write("# source: %s\n" % EXE)
        f.write("# inReference=no means the community docs never had it.\n")
        f.write("name\tinReference\n")
        for m in methods:
            f.write("%s\t%s\n" % (m, "yes" if m in known else "no"))

    print("\nmethod-shaped names in the API regions: %d" % len(methods))
    print("   already in the reference: %d" % (len(methods) - len(novel)))
    print("   NOT in the reference:     %d" % len(novel))

    # the specific question the character sheet raised
    print("\nstats the reference lacked but the character sheet shows:")
    for stat in ("Tenacity", "Toughness", "Hope", "CooldownReduction", "FocusPool",
                 "GlanceMitigation", "MultiHitSeverity", "PvPPower"):
        found = sorted(n for _, n in strings if stat.lower() in n.lower())[:4]
        print("   %-18s %s" % (stat, ", ".join(found) if found else "NOT FOUND IN BINARY"))

    print("\nwrote %s" % OUT)


if __name__ == "__main__":
    main()
