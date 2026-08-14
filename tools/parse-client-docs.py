#!/usr/bin/env python3
"""Turn the client's OWN API documentation into one document per library and object.

`Documentation.xml` was shipped inside the game and recovered from the CDN mirror. It is 1.3 MB of
Carbine's own reference: 47 libraries, 65 objects, 37 window controls, 2,138 methods, 1,430
functions, 1,726 named-and-typed parameters, 548 return values, 915 events, and 234 enum sets
holding 3,575 constants.

It supersedes every other API source we have:

  the community reference   incomplete - omits GetTenacity, GetToughness, GetHope, and ~30% more
  the binary strings        names only, no arguments, no types, no descriptions
  the client's own Lua      real call sites, but only for what the UI happens to use
  THIS                      names, argument names, TYPES, descriptions, and deprecation flags

One caveat carried into every generated file: a great many entries are marked `Deprecated="true"`,
including things demonstrably alive in 16042. The flag appears to have been applied wholesale rather
than per entry, so it is REPORTED, never used to filter. Dropping an entry because a possibly-stale
attribute says so is how a real method gets deleted from a reference.

Usage:  python Tools/parse-client-docs.py
"""
import collections
import io
import os
import re
import xml.etree.ElementTree as ET

SRC = "docs/client-extract/xml"
OUT = "docs/client-api"


def find_source():
    for name in sorted(os.listdir(SRC)):
        if name.endswith("-Documentation.xml"):
            return os.path.join(SRC, name)
    return None


def esc(s):
    return (s or "").replace("|", "\\|").replace("\n", " ").strip()


def signature(node):
    params = node.findall("Param")
    if not params:
        return "%s()" % node.get("Name")
    return "%s(%s)" % (node.get("Name"), ", ".join(p.get("Name", "?") for p in params))


def write_container(kind, node, outdir):
    name = node.get("Name")
    if not name:
        return None

    calls = node.findall("Method") + node.findall("Function")
    if not calls:
        return None

    path = os.path.join(outdir, "%s.md" % re.sub(r"[^A-Za-z0-9_.-]", "_", name))
    dep = sum(1 for c in calls if c.get("Deprecated") == "true")

    with io.open(path, "w", encoding="utf-8", newline="") as f:
        f.write("# %s\n\n" % name)
        f.write("*%s, documented by the client itself.*\n\n" % kind)
        if node.get("Desc"):
            f.write("%s\n\n" % node.get("Desc"))
        f.write("**%d calls.**" % len(calls))
        if dep:
            f.write(" %d carry `Deprecated=\"true\"` — reported, not filtered, "
                    "because that flag is set on entries known to be alive in 16042." % dep)
        f.write("\n\n")

        for c in sorted(calls, key=lambda x: (x.get("Name") or "")):
            f.write("### `%s`\n\n" % signature(c))
            if c.get("Deprecated") == "true":
                f.write("`deprecated flag set` ")
            if c.get("Desc"):
                f.write("%s\n\n" % esc(c.get("Desc")))
            else:
                f.write("*no description in the client's documentation*\n\n")

            params = c.findall("Param")
            if params:
                f.write("| parameter | type | meaning |\n|---|---|---|\n")
                for p in params:
                    f.write("| `%s` | %s | %s |\n"
                            % (p.get("Name", "?"), p.get("Type", "—"), esc(p.get("Desc"))))
                f.write("\n")

            rets = c.findall("ReturnValue")
            if rets:
                f.write("**Returns** — ")
                f.write("; ".join("`%s` %s" % (r.get("Type", "?"), esc(r.get("Desc"))) for r in rets))
                f.write("\n\n")

            notes = c.get("InternalNotes")
            if notes:
                f.write("> Carbine's own note: %s\n\n" % esc(notes))

    return (name, len(calls), dep)


def main():
    src = find_source()
    if not src:
        print("Documentation.xml not found under %s" % SRC)
        return

    root = ET.parse(src).getroot()
    os.makedirs(OUT, exist_ok=True)

    written = []
    for kind, tag, sub in (("Library", "Library", "libraries"),
                           ("Object", "Object", "objects"),
                           ("Window control", "WindowControl", "window-controls")):
        d = os.path.join(OUT, sub)
        os.makedirs(d, exist_ok=True)
        for node in root.iter(tag):
            r = write_container(kind, node, d)
            if r:
                written.append((sub,) + r)

    # ---- enums: one file, because they are looked up not browsed ----
    sets = list(root.iter("EnumSet"))
    with io.open(os.path.join(OUT, "ENUMS.md"), "w", encoding="utf-8", newline="") as f:
        f.write("# Enums, from the client's own documentation\n\n")
        f.write("**%d sets.** These are the values every API argument expects. Where a set has\n" % len(sets))
        f.write("explicit numbers they are given; where the client documents only names, the order is\n")
        f.write("shown but **no numeric value is invented** — declaration order is not a guarantee of\n")
        f.write("value, and guessing one produces an off-by-one that reads like data.\n\n")
        for s in sorted(sets, key=lambda x: (x.get("Name") or "")):
            f.write("## %s\n\n" % s.get("Name"))
            if s.get("Desc"):
                f.write("%s\n\n" % esc(s.get("Desc")))
            vals = s.findall("Enum")
            if not vals:
                f.write("*no values listed*\n\n")
                continue
            has_value = any(v.get("Value") is not None for v in vals)
            f.write("| name | %s | meaning |\n|---|---|---|\n" % ("value" if has_value else "order"))
            for i, v in enumerate(vals):
                num = v.get("Value") if has_value else str(i)
                f.write("| `%s` | %s | %s |\n" % (v.get("Name", "?"), num, esc(v.get("Desc"))))
            f.write("\n")

    # ---- events ----
    events = list(root.iter("Event"))
    with io.open(os.path.join(OUT, "EVENTS.md"), "w", encoding="utf-8", newline="") as f:
        f.write("# Events, from the client's own documentation\n\n")
        f.write("**%d events**, with the arguments each one delivers.\n\n" % len(events))
        f.write("Compare with `docs/client-systems/EVENTS.md`, which lists the 1,067 events the client's\n")
        f.write("own UI actually *registers handlers for*. An event documented here but never handled\n")
        f.write("there may still fire; an event handled there is definitely real.\n\n")
        for e in sorted(events, key=lambda x: (x.get("Name") or "")):
            f.write("### `%s`\n\n" % (e.get("Name") or "?"))
            if e.get("Desc"):
                f.write("%s\n\n" % esc(e.get("Desc")))
            params = e.findall("Param")
            if params:
                f.write("| argument | type | meaning |\n|---|---|---|\n")
                for p in params:
                    f.write("| `%s` | %s | %s |\n"
                            % (p.get("Name", "?"), p.get("Type", "—"), esc(p.get("Desc"))))
                f.write("\n")
            if e.get("InternalNotes"):
                f.write("> Carbine's own note: %s\n\n" % esc(e.get("InternalNotes")))

    # ---- index ----
    with io.open(os.path.join(OUT, "README.md"), "w", encoding="utf-8", newline="") as f:
        f.write("# The client's own API documentation\n\n")
        f.write("Recovered from `Documentation.xml`, shipped inside the game and pulled out of the CDN\n")
        f.write("mirror. This is Carbine's reference, not a community reconstruction.\n\n")
        f.write("| source | names | arguments | types | descriptions |\n|---|---|---|---|---|\n")
        f.write("| community reference | partial | some | some | some |\n")
        f.write("| binary strings | **all** | no | no | no |\n")
        f.write("| the client's own Lua | used-only | **yes** | inferred | no |\n")
        f.write("| **this** | **all** | **yes** | **yes** | **yes** |\n\n")
        f.write("`Deprecated=\"true\"` appears on entries that are demonstrably alive in 16042, so it\n")
        f.write("looks wholesale rather than per-entry. It is **reported and never used to filter**.\n\n")
        by = collections.Counter(w[0] for w in written)
        f.write("- `libraries/` — %d files\n" % by.get("libraries", 0))
        f.write("- `objects/` — %d files\n" % by.get("objects", 0))
        f.write("- `window-controls/` — %d files\n" % by.get("window-controls", 0))
        f.write("- `ENUMS.md` — %d sets\n" % len(sets))
        f.write("- `EVENTS.md` — %d events\n\n" % len(events))
        f.write("| document | calls | flagged deprecated |\n|---|---|---|\n")
        for sub, name, n, dep in sorted(written, key=lambda w: -w[2]):
            f.write("| [%s](%s/%s.md) | %d | %s |\n"
                    % (name, sub, re.sub(r"[^A-Za-z0-9_.-]", "_", name), n, dep or "—"))

    print("wrote %d documents" % len(written))
    print("  %d enum sets, %d events" % (len(sets), len(events)))
    for sub, n in collections.Counter(w[0] for w in written).items():
        print("  %-16s %d" % (sub, n))


if __name__ == "__main__":
    main()
