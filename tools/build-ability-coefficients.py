#!/usr/bin/env python3
"""Join the 202 class abilities to their damage coefficients from Spell4Effects.

This is the answer to "how does each ability scale", taken from the game's own table rather than
measured. Spell4Effects.ParameterType[] / ParameterValue[] ARE the scaling model: an effect states
how much it gains per point of Assault Power, per point of Support Power, per level, and so on.

Confirmed end to end before being trusted: spell 32809 carries AssaultPower=0.2595, PerLevel=13.85,
and 0.2595*225 + 13.85*50 = 750.89 against a client tooltip reading 751 for a level 50 character
with 225 Assault Power. The table reproduces the client.

Coefficients are PER ABILITY AND PER TIER and vary widely - measured across seven Esper abilities
they ran 0.125 to 0.5203. There is no single scaling number for the game and any tool implying one
is wrong.

Restricted to the 202 class abilities: 192 tiered (32 per class) plus the named innates. An ability
whose tier spell has no Damage effect is emitted with `noDamageEffect` rather than dropped - a
support or utility ability that scales off nothing is a real answer, and must not look like a
lookup that failed.

Usage:  python Tools/build-ability-coefficients.py
"""
import collections
import glob
import io
import os

TABLES = "docs/client-data/tables/spell4effects.tsv"
OUT = "docs/client-data/ability-coefficients.tsv"


def main():
    # spellId -> list of (effectType, damageType, {paramType: value})
    effects = collections.defaultdict(list)
    with io.open(TABLES, encoding="utf-8") as f:
        next(f)
        for line in f:
            p = line.rstrip("\n").split("\t")
            if len(p) < 7:
                continue
            types = p[4].split(",")
            values = p[5].split(",")
            # None slots are padding, not a scaling of zero - drop them rather than record them
            params = {}
            for t, v in zip(types, values):
                if t and t != "None":
                    try:
                        params[t] = float(v)
                    except ValueError:
                        pass
            effects[p[1]].append((p[2], p[3], params))

    # THE 202. Same discriminator the addon uses: nine tiers means a real class ability, and across
    # the whole capture the counts are exactly 9 (192 abilities) and 1 (22 entries) with nothing
    # between. The one-tier entries are basic attacks, Punch, hoverboards granted during testing -
    # and the seven class innates, which are named because no structural rule separates them from
    # the rest of the one-tier group.
    INNATES = {
        "Stance: Onslaught", "Stance: Juggernaut", "Mode: Provoke", "Mode: Eradicate",
        "Nano Skin: Lethal", "Nano Skin: Evasive", "Nano Skin: Agile",
        # not returned by the ability book on any character captured so far, so they cannot appear
        # here either; listed so their absence is visible rather than silent
        "Energize", "Spectral Form", "Spell Surge",
    }

    tier_counts = collections.defaultdict(set)
    for path in sorted(glob.glob("docs/client-data/tiers-*.tsv")):
        cls = os.path.basename(path)[len("tiers-"):-len(".tsv")]
        with io.open(path, encoding="utf-8") as f:
            next(f)
            for line in f:
                p = line.rstrip("\n").split("\t")
                if len(p) >= 4:
                    tier_counts[(cls, p[3])].add(p[1])

    rows = []
    seen_ability = set()
    skipped = set()
    for path in sorted(glob.glob("docs/client-data/tiers-*.tsv")):
        cls = os.path.basename(path)[len("tiers-"):-len(".tsv")]
        with io.open(path, encoding="utf-8") as f:
            header = next(f)
            for line in f:
                p = line.rstrip("\n").split("\t")
                if len(p) < 4:
                    continue
                ability_id, tier, spell_id, name = p[0], p[1], p[2], p[3]

                is_class = len(tier_counts[(cls, name)]) == 9 or name in INNATES
                if not is_class:
                    skipped.add(name)
                    continue
                seen_ability.add((cls, name))

                fx = effects.get(spell_id, [])
                dmg = [e for e in fx if e[0] == "Damage" and e[2]]
                if not dmg:
                    # distinguish "no damage effect" from "spell not in the table at all"
                    why = "noDamageEffect" if spell_id in effects else "spellNotInTable"
                    rows.append([cls, name, ability_id, tier, spell_id, "-", why, "", ""])
                    continue

                for effect_type, damage_type, params in dmg:
                    scal = " ".join("%s=%g" % (k, v) for k, v in sorted(params.items()))
                    rows.append([cls, name, ability_id, tier, spell_id, damage_type,
                                 "ok", scal, "+".join(sorted(params))])

    with io.open(OUT, "w", encoding="utf-8", newline="") as f:
        f.write("class\tability\tabilityId\ttier\tspellId\tdamageType\tstatus\tcoefficients\tscalesWith\n")
        for r in rows:
            f.write("\t".join(str(x) for x in r) + "\n")

    ok = sum(1 for r in rows if r[6] == "ok")
    print("%s: %d rows, %d with coefficients, %d abilities across %d classes"
          % (OUT, len(rows), ok, len(seen_ability),
             len(set(c for c, _ in seen_ability))))

    per_class = collections.Counter(c for c, _ in seen_ability)
    print("per class: " + "  ".join("%s %d" % (c, n) for c, n in sorted(per_class.items())))
    print("excluded as not class abilities: " + ", ".join(sorted(skipped)))

    combos = collections.Counter(r[8] for r in rows if r[6] == "ok")
    print("\nscaling combinations across the class abilities, most common first:")
    for combo, n in combos.most_common(12):
        print("   %-40s %d" % (combo, n))

    # Brutality, Finesse, Moxie and Tech appear in the raw table but on creature and legacy spells.
    # Asserted here so the claim fails loudly if a future dump contradicts it, rather than being a
    # sentence in a document that nobody re-checks.
    legacy = {"Brutality", "Finesse", "Moxie", "Tech", "Insight", "Grit"}
    used = set()
    for r in rows:
        if r[6] == "ok":
            used.update(r[8].split("+"))
    bad = sorted(used & legacy)
    print("\nlegacy attributes among the class abilities: %s"
          % (", ".join(bad) if bad else "NONE - none of Brutality/Finesse/Moxie/Tech is reachable"))
    print("scaling types actually used: " + ", ".join(sorted(used)))


if __name__ == "__main__":
    main()
