#!/usr/bin/env python3
"""Mine real Apollo call signatures out of the client's own Lua.

The binary gives 2,152 method NAMES and nothing else - no argument count, no order, no types. The
community reference gives signatures for some, and has already been shown wrong by omission. The
client's own UI source gives neither of those problems: it is the API being used, by the people who
wrote it, against the build we run.

For each `Namespace.Method(args)` call site this records the argument count and one real example.
Where a method is called with different counts, all are kept - that is optional arguments, and
collapsing them to one number would invent a signature.

Deliberately NOT done: inferring types from argument names. `nSomething` suggests a number by the
client's own Hungarian convention, but a convention is not a declaration, and this project has been
burned twice by plausible-looking API facts that nothing verified.

Usage:  python Tools/mine-api-usage.py
"""
import collections
import glob
import io
import os
import re

SRC = "docs/client-extract/lua"
OUT = "docs/reference-data/apollo-call-sites.tsv"
BINARY_LIST = "docs/reference-data/apollo-api-client.tsv"

CALL = re.compile(r"\b([A-Z][A-Za-z0-9_]*)\.([A-Za-z_][A-Za-z0-9_]*)\s*\(")


def split_args(text, start):
    """Return the argument substring for a call whose '(' is at `start`, or None if unbalanced."""
    depth, i, n = 0, start, len(text)
    while i < n:
        c = text[i]
        if c in "([{":
            depth += 1
        elif c in ")]}":
            depth -= 1
            if depth == 0:
                return text[start + 1:i]
        elif c in "\"'":
            q, i = c, i + 1
            while i < n and text[i] != q:
                i += 2 if text[i] == "\\" else 1
        i += 1
    return None


def count_args(arg_text):
    if arg_text is None:
        return None
    s = arg_text.strip()
    if not s:
        return 0
    depth, count = 0, 1
    for c in s:
        if c in "([{":
            depth += 1
        elif c in ")]}":
            depth -= 1
        elif c == "," and depth == 0:
            count += 1
    return count


def main():
    files = sorted(glob.glob(os.path.join(SRC, "*.lua")))
    if not files:
        print("no extracted Lua at %s - run Tools/cdn-extract-text.py first" % SRC)
        return

    # arities[(ns, method)] = {argcount: (example, sourcefile)}
    arities = collections.defaultdict(dict)
    for path in files:
        text = io.open(path, encoding="utf-8", errors="replace").read()
        base = os.path.basename(path)
        for m in CALL.finditer(text):
            ns, method = m.group(1), m.group(2)
            args = split_args(text, m.end() - 1)
            n = count_args(args)
            if n is None:
                continue
            key = (ns, method)
            if n not in arities[key]:
                example = re.sub(r"\s+", " ", "%s.%s(%s)" % (ns, method, (args or "").strip()))[:160]
                arities[key][n] = (example, base)

    # which of these the binary confirms - a call site for a name absent from the binary would be
    # either a different build or a reader bug, and either way is worth seeing
    inbin = set()
    if os.path.exists(BINARY_LIST):
        with io.open(BINARY_LIST, encoding="utf-8") as f:
            for ln in f:
                if not ln.startswith("#") and "\t" in ln:
                    inbin.add(ln.split("\t")[0])

    with io.open(OUT, "w", encoding="utf-8", newline="") as f:
        f.write("# Apollo call sites mined from the CLIENT'S OWN Lua (docs/client-extract/lua).\n")
        f.write("# argCounts lists every distinct arity seen - several means optional arguments,\n")
        f.write("# and collapsing them to one number would invent a signature.\n")
        f.write("# inBinary: whether the method name is also in WildStar64.exe.\n")
        f.write("namespace\tmethod\targCounts\tinBinary\texample\texampleFrom\n")
        for (ns, method), by_n in sorted(arities.items()):
            counts = sorted(by_n)
            example, src = by_n[counts[0]]
            f.write("%s\t%s\t%s\t%s\t%s\t%s\n"
                    % (ns, method, ",".join(str(c) for c in counts),
                       "yes" if method in inbin else "no", example, src))

    total = len(arities)
    confirmed = sum(1 for (_, m) in arities if m in inbin)
    optional = sum(1 for v in arities.values() if len(v) > 1)
    print("%d Lua files scanned" % len(files))
    print("%d distinct Namespace.Method call sites" % total)
    print("   confirmed in the binary: %d" % confirmed)
    print("   NOT in the binary:       %d" % (total - confirmed))
    print("   with more than one arity (optional args): %d" % optional)

    per_ns = collections.Counter(ns for ns, _ in arities)
    print("\nmost-used namespaces in the client's own UI:")
    for ns, n in per_ns.most_common(12):
        print("   %-20s %d methods" % (ns, n))
    print("\nwrote %s" % OUT)


if __name__ == "__main__":
    main()
