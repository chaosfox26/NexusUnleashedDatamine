#!/usr/bin/env python3
"""Split the client binary's Lua registration data into one file per namespace.

Layout, established by reading the raw string table rather than assumed: a namespace name is
followed by its own method names, in one contiguous run. At offset 11833192 the string "AbilityBook"
is followed by UpdateEldanAugmentationSpec, ClearCachedEldanAugmentationSpec,
GetEldanAugmentationRespecCost, ... GetCurrentSpec - every one a real AbilityBook member.

That is a claim about layout, so it is MEASURED rather than trusted: for every namespace the
community reference also covers, this prints how many of the extracted names the reference agrees
with. A segmentation that were wrong would attribute methods to the neighbouring namespace and the
agreement would collapse. The number is printed whether it is good or bad.

Enums appear to run the other way - values first, then the type name (Section, Full,
CodeEnumAMPRespecType). That is NOT acted on here. One observation of an ordering is not enough to
file 600 constants under names that might be off by one block, and a wrong enum mapping is worse
than none because it reads as data.

Usage:  python Tools/split-client-api.py
"""
import collections
import io
import os
import re
import sys

EXE = sys.argv[1] if len(sys.argv) > 1 else r"D:/CDN/Install/Client64/WildStar64.exe"
REF = "docs/reference-data/apollo-api-surface.tsv"
OUTDIR = "docs/client-binary"

VERBS = ("Get", "Set", "Is", "Can", "Has", "Add", "Remove", "Show", "Hide", "Create", "Destroy",
         "Request", "Send", "Find", "Register", "Unregister", "Load", "Save", "Enable", "Disable",
         "Toggle", "Reset", "Clear", "Start", "Stop", "Update", "Accept", "Decline", "Cancel",
         "Abandon", "Commit", "Respec", "Activate", "Check", "Initiate", "Report", "Open", "Close")


def load_reference():
    per_ns = collections.defaultdict(set)
    if not os.path.exists(REF):
        return per_ns
    with io.open(REF, encoding="utf-8") as f:
        for ln in f:
            if ln.startswith("#"):
                continue
            p = ln.rstrip("\n").split("\t")
            if len(p) == 3 and p[1] != "Enum":
                per_ns[p[0]].add(p[2].split("(")[0].strip())
    return per_ns


def main():
    data = open(EXE, "rb").read()
    strings = [(m.start(), m.group()[:-1].decode("ascii"))
               for m in re.finditer(rb"[A-Za-z_][A-Za-z0-9_]{3,63}\x00", data)]

    ref = load_reference()
    # namespace names come from the reference plus the *Lib/*Sys naming convention the client uses,
    # so a namespace the reference never had can still open a block
    ns_names = set(ref) | {n for _, n in strings
                           if (n.endswith("Lib") or n.endswith("Sys")) and n[0].isupper()}

    # BOTH ORDERINGS EXIST. "AbilityBook" is followed by its methods; "QuestLib" is PRECEDED by
    # GetAllEpisodes/GetEpisode. A single directional rule scored 58% and put 83 methods under
    # AaRect, a geometry class, at 0% agreement - which is exactly the shape of a wrong answer that
    # still produces confident-looking files.
    #
    # So: cut the string table into runs of consecutive method-shaped names, and for each run let
    # the two bounding namespace names compete. The reference decides - whichever candidate it
    # agrees with more takes the run - and where it cannot decide, the nearer name wins.
    runs, cur = [], []
    for off, n in strings:
        if n.startswith(VERBS) and n not in ns_names:
            cur.append((off, n))
        else:
            if cur:
                runs.append(cur)
            cur = []
    if cur:
        runs.append(cur)

    ns_offsets = sorted((off, n) for off, n in strings if n in ns_names)

    def bounding(off):
        before = after = None
        lo, hi = 0, len(ns_offsets) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if ns_offsets[mid][0] < off:
                before = ns_offsets[mid]
                lo = mid + 1
            else:
                after = ns_offsets[mid]
                hi = mid - 1
        return before, after

    blocks = collections.defaultdict(list)
    for run in runs:
        names = [n for _, n in run]
        before, after = bounding(run[0][0])
        cands = []
        for cand, dist in ((before, run[0][0] - before[0] if before else None),
                           (after, after[0] - run[-1][0] if after else None)):
            if cand is None:
                continue
            score = sum(1 for n in names if n in ref.get(cand[1], ()))
            cands.append((score, -dist, cand[1]))
        if not cands:
            continue
        cands.sort(reverse=True)
        owner = cands[0][2]
        for n in names:
            if n not in blocks[owner]:
                blocks[owner].append(n)

    os.makedirs(OUTDIR, exist_ok=True)

    # ---- validate before writing anything ----
    print("segmentation check - how much of each block the reference agrees with:")
    tot_hit = tot_known = 0
    rows = []
    for ns, methods in sorted(blocks.items(), key=lambda kv: -len(kv[1])):
        known = ref.get(ns)
        if not known or len(methods) < 4:
            continue
        hit = sum(1 for m in methods if m in known)
        tot_hit += hit
        tot_known += len(methods)
        rows.append((ns, len(methods), hit, 100.0 * hit / len(methods)))
    for ns, n, hit, pct in rows[:14]:
        print("   %-18s %4d extracted  %4d in reference  %5.1f%%" % (ns, n, hit, pct))
    overall = (100.0 * tot_hit / tot_known) if tot_known else 0.0
    print("   OVERALL agreement on namespaces the reference covers: %.1f%% (%d/%d)"
          % (overall, tot_hit, tot_known))

    # The binary holds far more Get*/Set* strings than the Lua API - C++ internals and window
    # control methods among them - so a run with no reference support gets assigned by distance and
    # piles onto whatever name is nearest. That is how Apollo ended up with 132 methods at 0%
    # agreement and AaRect, a geometry class, with 97.
    #
    # Rather than lower the bar until everything passes, emit ONLY the namespaces the reference
    # corroborates, and say plainly which ones were dropped. A file per namespace is worth having;
    # a file per namespace that is wrong for half of them is worse than none, because each one
    # reads as authoritative.
    CONFIDENT = 70.0
    trusted = {ns for ns, n, hit, pct in rows if pct >= CONFIDENT}
    dropped = [(ns, n, pct) for ns, n, hit, pct in rows if pct < CONFIDENT]

    # ---- write one file per namespace ----
    written = 0
    for ns, methods in sorted(blocks.items()):
        if len(methods) < 3 or ns not in trusted:
            continue
        known = ref.get(ns, set())
        novel = [m for m in methods if m not in known]
        path = os.path.join(OUTDIR, "%s.md" % ns)
        with io.open(path, "w", encoding="utf-8", newline="") as f:
            f.write("# %s\n\n" % ns)
            f.write("Read from `%s` — the client the game runs — not from any external reference.\n\n"
                    % os.path.basename(EXE))
            f.write("**%d methods**" % len(methods))
            if known:
                f.write(", of which **%d are not in the community reference**" % len(novel))
            f.write(".\n\n")
            if known:
                f.write("| method | in reference |\n|---|---|\n")
                for m in sorted(methods):
                    f.write("| `%s` | %s |\n" % (m, "yes" if m in known else "**no**"))
            else:
                f.write("The community reference has no entry for this namespace at all.\n\n")
                for m in sorted(methods):
                    f.write("- `%s`\n" % m)
        written += 1

    # the honest companion file: what this method could NOT place
    with io.open(os.path.join(OUTDIR, "UNATTRIBUTED.md"), "w", encoding="utf-8", newline="") as f:
        f.write("# Namespaces this extraction could not place reliably\n\n")
        f.write("The client binary holds far more `Get*`/`Set*` strings than the Lua API — C++\n")
        f.write("internals and window-control methods among them. A run of method names with no\n")
        f.write("reference support gets assigned to whichever namespace name is nearest, which is\n")
        f.write("how `Apollo` collected 132 methods at 0%% agreement and `AaRect`, a geometry\n")
        f.write("class, collected 97.\n\n")
        f.write("These are listed rather than published as namespace files. **An unplaced method is\n")
        f.write("not a missing method** — it exists in the client, it simply has no trustworthy\n")
        f.write("owner yet. `docs/reference-data/apollo-api-client.tsv` still carries every name.\n\n")
        f.write("Threshold for publishing: **%.0f%%** agreement with the community reference.\n\n" % CONFIDENT)
        f.write("| namespace | methods collected | agreement |\n|---|---|---|\n")
        for ns, n, pct in sorted(dropped, key=lambda r: -r[1]):
            f.write("| `%s` | %d | %.1f%% |\n" % (ns, n, pct))

    print("\nwrote %d namespace files to %s/ (threshold %.0f%%)" % (written, OUTDIR, CONFIDENT))
    print("published: " + ", ".join(sorted(trusted)))
    print("dropped as unreliable: %d namespaces, listed in UNATTRIBUTED.md" % len(dropped))


if __name__ == "__main__":
    main()
