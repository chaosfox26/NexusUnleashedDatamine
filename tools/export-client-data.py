#!/usr/bin/env python3
"""Export NexusIntrospect captures to docs/client-data/ TSVs, one set per class.

Reads the addon's per-character SavedVariables and writes amps-<class>.tsv,
abilities-<class>.tsv and tiers-<class>.tsv in the format the two existing hand-made files
already use, so old and new sit side by side without a consumer needing to care which is which.

Class is identified by signature ability name rather than by anything the capture states, because
the capture does not state it - the client tells an addon what the character HAS, not what it IS.
Signature abilities are exclusive to one class, and the six AMP sets being fully disjoint is an
independent check on the mapping.

The tier `name` column is filled from the capture's own TIER rows. The previous hand-made files
have it EMPTY - a regex over the flattened spell object did not match and a blank column was
written rather than the name.

Usage:  python Tools/export-client-data.py [--dry-run]
"""
import glob
import os
import re
import sys

SAVE_GLOB = (r"C:/Users/nexus/AppData/Roaming/NCSOFT/WildStar/AddonSaveData"
             r"/*/*/*/NexusIntrospect_0_Char.xml")
OUT_DIR = "docs/client-data"

# one exclusive ability per class - none of these exists on any other class
SIGNATURES = {
    "Psyblade Strike":   "esper",
    "Spatial Shift":     "spellslinger",
    "Unstoppable Force": "warrior",
    "Gamma Rays":        "medic",
    "Energy Auger":      "engineer",
    "Shred":             "stalker",
}


def unescape(s):
    return (s.replace("&lt;", "<").replace("&gt;", ">")
             .replace("&quot;", '"').replace("&amp;", "&"))


def field(blob, key, default=""):
    m = re.search(re.escape(key) + r"=([^ ]+)", blob)
    return m.group(1) if m else default


def parse(path):
    t = open(path, encoding="utf-8", errors="replace").read()

    tiers = re.findall(r'V="TIER\|(\d+)\|(\d+)\|spell=(\d+)\|([^|]*)\|([^"]*)"', t)
    abilities = re.findall(r'V="ABILITY\|(\d+)\|([^|]*)\|tier=[^/]*/(\d+)\|[^|]*\|([^"]*)"', t)

    # one row per augment per spec; the same augment repeats across specs, so keep the first
    augs = {}
    for m in re.finditer(r'V="AUGMENT\|spec=(\d+)\|key=\d+\|cost=(\d+)\|name=([^|]*)\|([^"]*)"', t):
        blob = unescape(m.group(4))
        nid = field(blob, "nId")
        if nid and nid not in augs:
            augs[nid] = {
                "id": nid,
                "name": unescape(m.group(3)),
                "cost": field(blob, "nPowerCost", m.group(2)),
                "categoryId": field(blob, "nCategoryId"),
                "categoryTier": field(blob, "nCategoryTier"),
                "row": field(blob, "nDisplayRow"),
                "col": field(blob, "nDisplayColumn"),
                "requiresAmpId": field(blob, "nEldanAugmentationIdRequired"),
                "spellId": field(blob, "nSpellIdAugment"),
                "description": re.sub(r"\s+", " ", (re.split(r"strDescription=", blob) + [""])[1]
                                      .split("strTitle=")[0]).strip(),
            }

    names = {n.strip() for _, _, _, n, _ in tiers if n.strip()}
    cls = next((c for sig, c in SIGNATURES.items() if sig in names), None)
    return cls, augs, abilities, tiers


def write(path, header, rows, dry):
    if dry:
        print("   would write %-42s %d rows" % (path, len(rows)))
        return
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write("\t".join(header) + "\n")
        for r in rows:
            f.write("\t".join(str(x).replace("\t", " ").replace("\n", " ") for x in r) + "\n")
    print("   %-46s %d rows" % (path, len(rows)))


def main():
    dry = "--dry-run" in sys.argv
    if not dry:
        os.makedirs(OUT_DIR, exist_ok=True)

    seen = {}
    for p in glob.glob(SAVE_GLOB):
        cls, augs, abilities, tiers = parse(p)
        if not cls:
            print("SKIP (class not identified): %s" % os.path.basename(os.path.dirname(p)))
            continue
        if cls in seen:
            continue
        seen[cls] = True
        print("%s  <- %s" % (cls, os.path.basename(os.path.dirname(p))))

        write("%s/amps-%s.tsv" % (OUT_DIR, cls),
              ["id", "name", "cost", "categoryId", "categoryTier", "row", "col",
               "requiresAmpId", "spellId", "description"],
              [[a["id"], a["name"], a["cost"], a["categoryId"], a["categoryTier"], a["row"],
                a["col"], a["requiresAmpId"], a["spellId"], a["description"]]
               for a in sorted(augs.values(), key=lambda x: int(x["id"]))], dry)

        write("%s/abilities-%s.tsv" % (OUT_DIR, cls),
              ["id", "name", "maxTiers", "description"],
              sorted(((i, n, mt, re.sub(r"\s+", " ", d)[:400]) for i, n, mt, d in abilities),
                     key=lambda x: int(x[0])), dry)

        # bonusDescription is the point of this file for combat work: it is the damage the CLIENT
        # itself computes for this ability at this tier, for a character with these stats. That makes
        # it an oracle for our own damage maths - if the server disagrees with it for the same
        # character, the server is wrong. It was omitted from the first export, which is why the
        # tier files looked like pure metadata.
        write("%s/tiers-%s.tsv" % (OUT_DIR, cls),
              ["abilityId", "tier", "spellId", "name", "levelReq", "tierPointCost",
               "trainingCost", "canPurchase", "prereqLocked", "bonusDescription"],
              sorted(([b, ti, sp, nm.strip(),
                       field(rest, "nLevelReq"), field(rest, "nTierPointCost"),
                       field(rest, "nTrainingCost"), field(rest, "bCanPurchase"),
                       field(rest, "bPrereqLocked"),
                       re.sub(r"\s+", " ", unescape(
                           (re.split(r"strTierBonusDescription=", rest) + [""])[1]
                           .split("strName=")[0])).strip()]
                      for b, ti, sp, nm, rest in tiers), key=lambda x: (int(x[0]), int(x[1]))), dry)

    print("\n%d class(es) exported" % len(seen))


if __name__ == "__main__":
    main()
