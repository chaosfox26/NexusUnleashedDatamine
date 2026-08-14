#!/usr/bin/env python3
"""Crude Lua block-balance check for the NexusIntrospect addon.

There is no Lua interpreter on this machine, and a syntax error in the addon does not produce a
useful failure - it produces an addon that does not load, which reports nothing at all and looks
exactly like an addon with nothing to say. This is not a parser and cannot replace one; it catches
the one class of mistake that hand-editing a 1,700 line file actually produces, which is an
unbalanced block.

Counts block openers against `end`, ignoring keywords inside strings and comments.
"""
import re
import sys

path = sys.argv[1] if len(sys.argv) > 1 else (
    r"C:/Users/nexus/AppData/Roaming/NCSOFT/WildStar/Addons/NexusIntrospect/NexusIntrospect.lua")

src = open(path, encoding="utf-8", errors="replace").read().splitlines()

KW = re.compile(r"\b(function|elseif|if|for|while|do|end|repeat|until|then)\b")

depth = 0
opens = []          # stack of (line_no, keyword) so an imbalance names a place, not just a count
problems = []

for lineno, raw in enumerate(src, 1):
    # strip comments and string literals - a `--` inside a string would break this, and the addon
    # has none, but strings containing the word "function" are everywhere in the Print calls
    line = re.sub(r'"[^"]*"', '""', raw)
    line = re.sub(r"'[^']*'", "''", line)
    line = re.sub(r"--.*$", "", line)

    toks = KW.findall(line)
    # `for`/`while` are followed by their own `do`; count the pair once
    i = 0
    while i < len(toks):
        t = toks[i]
        if t in ("for", "while"):
            opens.append((lineno, t))
            # swallow the matching `do`
            if "do" in toks[i + 1:]:
                toks.pop(i + 1 + toks[i + 1:].index("do"))
        elif t == "function":
            opens.append((lineno, t))
        elif t == "if":
            opens.append((lineno, t))
        elif t == "do":
            opens.append((lineno, "do"))
        elif t == "repeat":
            opens.append((lineno, "repeat"))
        elif t == "until":
            if opens and opens[-1][1] == "repeat":
                opens.pop()
            else:
                problems.append("line %d: `until` with no `repeat`" % lineno)
        elif t == "end":
            if opens:
                opens.pop()
            else:
                problems.append("line %d: `end` with nothing open" % lineno)
        i += 1

for lineno, kw in opens:
    problems.append("line %d: `%s` never closed" % (lineno, kw))

if problems:
    print("UNBALANCED (%d)" % len(problems))
    for p in problems[:20]:
        print("  " + p)
    sys.exit(1)

print("balanced: %d lines, all blocks closed" % len(src))
