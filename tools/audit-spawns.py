#!/usr/bin/env python3
"""Find misplaced creature spawns by internal consistency, without Carbine's original spawn table.

## The idea, which came from the operator

Carbine's spawn list is not in the client and never will be. But their **designer names are
constraints**: a creature called "Bloodbloom Vale Defense" belongs in Bloodbloom Vale, a "Q7539 Quest
Flavor Object" belongs near Q7539's objectives, and a creature with eleven spawns in one zone and one
in another has an outlier. Correct placement can be *inferred from constraints* rather than copied.

## Why distance matters more than zone

A creature standing just across a zone boundary is legitimately in a different area - zones have
edges and things sit near them. Ranking outliers by **distance from their own species' cluster** is
what separates a real error from a border case.

That distinction changed the answer on the first creature it was applied to. The Elderoot Tendril
(52367) has 11 spawns in area 1415 and 1 in 1417, which looked like the misplacement the operator
suspected. It is **172 units** from the cluster - a border case, probably fine. Meanwhile creature
36354, an "Elderoot Refuge Defender", sits **1,113 units** from its own group, which no boundary
explains.

## What this does NOT do

It cannot say where a creature *should* be, only that a spawn disagrees with its own kind. A creature
legitimately placed alone - a unique NPC, a quest giver at a remote location - will look like an
outlier and is not one. Every row is a candidate for a human to judge, which is why the output is
ranked rather than filtered.

Usage:  python Tools/audit-spawns.py <zone.sql> [--min-group 4] [--far 200]
"""
import collections
import io
import math
import re
import sys

CREATURES = "docs/client-data/tables/creature2.tsv"

ROW = re.compile(r"\(@GUID\+\d+,\s*(\d+),\s*(\d+),\s*@WORLD,\s*(\d+),"
                 r"\s*(-?[\d.]+),\s*(-?[\d.]+),\s*(-?[\d.]+)")


def designer_names():
    """creature id -> Carbine's internal Description. The single most useful column in creature2.

    Nothing else resolves a creature name: localizedText.tsv holds only sound and version metadata,
    and the display strings live in the en-US.bin language file, not in any dumped table.
    """
    out = {}
    with io.open(CREATURES, encoding="utf-8", errors="replace") as f:
        for ln in f:
            q = ln.rstrip("\n").split("\t")
            if len(q) > 4 and q[0].isdigit():
                out[q[0]] = q[2]
    return out


def main():
    if len(sys.argv) < 2:
        print(__doc__.strip().splitlines()[-1])
        return
    path = sys.argv[1]
    min_group = int(sys.argv[sys.argv.index("--min-group") + 1]) if "--min-group" in sys.argv else 4
    far = float(sys.argv[sys.argv.index("--far") + 1]) if "--far" in sys.argv else 200.0

    names = designer_names()
    text = io.open(path, encoding="utf-8", errors="replace").read()
    ents = [(m.group(2), m.group(3), float(m.group(4)), float(m.group(5)), float(m.group(6)))
            for m in ROW.finditer(text)]
    if not ents:
        print("no entity rows parsed from %s" % path)
        return

    by = collections.defaultdict(list)
    for cid, area, x, y, z in ents:
        by[cid].append((area, x, y, z))

    print("%s: %s spawns, %s distinct creatures\n" % (path, format(len(ents), ","), format(len(by), ",")))

    found = []
    for cid, rows in by.items():
        if len(rows) < min_group:
            continue
        areas = collections.Counter(r[0] for r in rows)
        if len(areas) < 2:
            continue
        maj, majn = areas.most_common(1)[0]
        # a creature split evenly across zones has no "home" to be an outlier from
        if majn / len(rows) < 0.75:
            continue
        core = [(x, y, z) for a, x, y, z in rows if a == maj]
        for a, x, y, z in rows:
            if a == maj:
                continue
            d = min(math.dist((x, y, z), c) for c in core)
            found.append((d, cid, len(rows), a, maj, x, y, z))

    found.sort(reverse=True)
    hard = [f for f in found if f[0] > far]

    print("SPAWNS THAT DISAGREE WITH THEIR OWN SPECIES, ranked by distance from its cluster")
    print("(beyond %.0f units a zone boundary no longer explains it)\n" % far)
    for d, cid, n, a, maj, x, y, z in found[:25]:
        mark = "**" if d > far else "  "
        print(" %s %8.1f  creature %-7s x%-3d  area %s vs %s" % (mark, d, cid, n, a, maj))
        print("              %s" % names.get(cid, "?")[:70])
        print("              at (%9.2f, %8.2f, %9.2f)" % (x, y, z))

    print("\n%d outlier spawns; %d beyond %.0f units (marked **) are the ones worth looking at."
          % (len(found), len(hard), far))
    print("A uniquely-placed creature - a lone quest giver - will appear here and is NOT an error.")


if __name__ == "__main__":
    main()
