# Nexus Unleashed — Datamine

A complete teardown of the WildStar client, build **16042** (the final patch, 2018).

Every file in the game has been decompressed, named, classified and profiled. Several container
formats that had no public specification are decoded here for the first time.

```
197,333  content blobs in the CDN mirror        →  all opened
218,427  files recovered by their real name     →  100% present
     21  formats profiled across the population
     38  GB decompressed and read
  2.1 M  rows extracted from 376 game tables
  1.27 M static world object placements, with position and rotation
```

---

## Why this took cracking

The game shipped as a **content-addressed store**: 197,333 files, each named after a SHA-1 of its own
contents, with no manifest and no filenames. Two locks sat in front of it.

**The compression is not what it claims.** Every blob opens with a 5-byte LZMA header that omits the
uncompressed-size field the standard container requires. Every standard tool therefore rejects all
197,333 files as **corrupt** — which reads like a broken download rather than a wrong key, and is why
the store looked like a dead end. It needs `FORMAT_RAW` with an explicit LZMA1 filter (`lc=3 lp=0
pb=2`, 1 MB dict) starting at **offset 5**.

**The names live somewhere else.** `ClientData.index` is a `KCAP` archive holding the real directory
tree. Decoding it pairs every path to the SHA-1 its contents are stored under — which is what turns a
pile of hashes into a filesystem.

Both are documented in [`docs/FILENAMES.md`](docs/FILENAMES.md) and
[`docs/CDN-CONTENTS.md`](docs/CDN-CONTENTS.md).

---

## What the client is made of

| folder | files | | format | files | what it is |
|---|---:|---|---|---:|---|
| `Audio/` | 88,419 | | `.wem` | 88,267 | Wwise audio |
| `Art/` | 83,561 | | `.tex` | 74,673 | textures |
| `Map/` | 27,949 | | `.m3` | 34,748 | models |
| `UI/` | 16,311 | | `.area` | 15,051 | world chunks |
| `Sky/` | 1,291 | | `.dgn` | 986 | dungeon geometry |
| `DB/` | 384 | | `.tbl` | 384 | **the game database** |
| `Shaders/` | 311 | | `.lua` | 203 | **the game's own UI code** |
| `EnvMap/` | 191 | | `.bnk` | 152 | Wwise sound banks |

**384 blobs classify as game tables; 384 `.tbl` files exist on disk.** Exact match, from two
directions sharing no code — the strongest available evidence that the mirror is complete.

---

## Formats decoded here

### `PROp` — world object placement · **fully solved**

Inside every `.area` file. This is where Carbine put every tree, crate, light and structure.

```
PROp = u32 count
       count × 104-byte record
       UTF-16LE string table of model paths

record  +20  u32     absolute byte offset of this record's model path  (0 = none)
        +32  4×f32   rotation quaternion
        +48  3×f32   world position X, Y, Z
```

Verified: the string table always begins at exactly `4 + count × 104` (262 files, zero mismatches).
`+20` resolves for 97.73% of 261,761 records and **every remaining record is exactly 0** — a null, not
a parse failure. `+32` is unit-norm in **100.00%** of 39,431 sampled records.

→ **[`data/world-props/`](data/world-props/)** — 1,266,484 placements, model + position + rotation,
split into 114 per-map files (the combined file exceeds GitHub's 100 MB limit).

### `.area` container · solved

`aera` header, then `(4-byte tag reversed, u32 size, payload)`. Across **all 11,651 files** there are
exactly three top-level tags and no others:

| tag | files | contents |
|---|---:|---|
| `CHNK` | 11,651 | terrain grid — 225 cells of 24 bytes (15×15) |
| `PROp` | 5,651 | object placement, above |
| `CURT` | 964 | path/spline points, `(X, 155.00, Z)` at constant height |

### `KCAP` archive index · solved

```
+0    "KCAP", u32 version
+520  u64 fileSize, u64, u64 blockTableOffset, u64 blockCount
+576  "AIDX", u32 version, u32 build (16042)
block u32 dirCount, u32 fileCount,
      dirCount  × (u32 nameOffset, u32 blockIndex)          8 bytes
      fileCount × (u32 nameOffset, u32 flags, u64 writeTime,
                   u64 uncompressedSize, u64 compressedSize,
                   u8 sha1[20], u32)                        56 bytes
      NUL-separated UTF-16LE string table
```

**The SHA-1 in a file entry is the CDN blob name.**

### `.tex` · partially decoded

Magic `XFG`, version `3` constant across all 61,857 files. **`+8` and `+12` are width and height** —
tested against 3,000 files: 512×512, 1024×1024, 64×64, 704×384, 57.9% power-of-two pairs. Pixel
format enum at `+24` (11 values). Pixel data not decoded.

### `.m3` · header only

Magic `MODL`, version field is **100 in all 34,568 files** — one model revision game-wide. A flag at
`+8` is set in every file but 20. Mesh and vertex layout not decoded.

### `.i3` · **not** chunked

1,696 files, 2 GB, magic `SDEF`. **Zero of 1,696 parse as a chunk container** — a clean negative that
rules out the obvious hypothesis. Still the largest unidentified format in the game.

---

## The game database

All **376 tables, 2,096,496 rows** as TSV in [`data/game-tables/`](data/game-tables/).

Notable for server work:

| table | rows | why it matters |
|---|---:|---|
| `spell4Effects` | 131,010 | `ParameterType[]`/`ParameterValue[]` **are** the damage scaling model |
| `spellEffectType` | 150 | `DataType00..09` says how to read each effect's `DataBits00..09` |
| `creature2` | 53,137 | **column 3 is Carbine's own designer name** — the only human-readable creature identity |
| `worldLocation2` | 33,396 | position + facing quaternion + radius, keyed by world/zone |
| `spline2Node` | 380,577 | **patrol paths** |
| `localizedText` | 539,252 | every string id in the game |

**The verified damage formula:**

```
AssaultPower = AssaultRating × 0.25          (GameFormula 1266)
damage       = AP × c₁ + Level × c₂          (per effect, from Spell4Effects)
```

Confirmed against the live client: spell 32809 carries `AP=0.2595, PerLevel=13.85`, and
`0.2595 × 225 + 13.85 × 50 = 750.89` against a tooltip reading **751**.

Only **four** scaling types are reachable by any player ability: `AssaultPower`, `SupportPower`,
`PerLevel`, `CasterShieldCapacity`. Brutality, Finesse, Moxie and Tech appear thousands of times in
the raw table but **every occurrence is on a creature or legacy spell**.

---

## The class system

Derived from the CDN game tables, and the reason the damage formula above is checkable rather than
theoretical.

| file | what it holds |
|---|---|
| [`data/class-system/ability-coefficients.tsv`](data/class-system/ability-coefficients.tsv) | **the 202 class abilities with per-tier damage scaling** — 1,812 rows, 518 carrying coefficients |
| [`data/class-system/spell-id-map.tsv`](data/class-system/spell-id-map.tsv) | 44,082 spell name → id rows. **23.2% of spell names are shared**, so names are not identity |
| [`data/class-system/ability-id-map.tsv`](data/class-system/ability-id-map.tsv) | ability name → base id and the spell id of each of its 9 tiers |
| [`data/class-system/ability-counts.tsv`](data/class-system/ability-counts.tsv) | how 202 breaks down, and why three different counts are each correct about something |
| [`data/class-system/class-innate-abilities.tsv`](data/class-system/class-innate-abilities.tsv) | the 10 innates, three of which the ability-book API does not return at all |
| [`data/class-system/character-stats.tsv`](data/class-system/character-stats.tsv) | the character sheet at the **naked baseline** — 40 stats, from the live client |
| [`data/class-system/everstar-suspect-entities.tsv`](data/class-system/everstar-suspect-entities.tsv) | 79 AI-bearing entities standing on client scenery — a worked example of using this data as an auditor |

**202 = 192 tiered abilities (32 per class, identical across all six) + 10 innates.** The
discriminator is tier count: across 220 captured rows the values are exactly 9 and 1, nothing
between.

`character-stats.tsv` is the one file here not derived from the CDN — it is the client's own
character sheet, read off-screen. It is included because it is what proves the four-scaling-type
finding: Brutality, Finesse, Moxie and Tech are absent from the sheet, which independently agrees
with no ability referencing them.

Two traps recorded in the tier data, both of which cost real time:

- **The tier array is offset by one.** `tTiers[5]` fills the window labelled Tier 4; `tTiers[9]`
  fills Tier 8. The `tier` column runs 1–9, which is the player's Tier 0–8.
- **`AssaultPower` and `SupportPower` are both 225 on an ungeared level-50 character**, so no single
  capture can separate an AP coefficient from an SP one.

Further analysis in [`docs/tables/`](docs/tables/) and [`docs/systems/`](docs/systems/) — including
`spellEffectType`, whose `DataType00..09` is the decoder ring for `Spell4Effects.DataBits00..09` and
turns 116 unimplemented spell effects from a research problem into a coding problem.

---

## The API

Three independent sources, in increasing authority:

| source | names | args | types | descriptions |
|---|---|---|---|---|
| community reference | partial | some | some | some |
| `WildStar64.exe` strings | **all** | no | no | no |
| the client's own `Documentation.xml` | **all** | **yes** | **yes** | **yes** |

- [`api/`](api/) — **147 documents** from the client's shipped `Documentation.xml`: 46 libraries,
  65 objects, 36 window controls, 234 enum sets (3,575 constants), 915 events
- [`docs/binary-api/`](docs/binary-api/) — 50 namespace files read from the executable;
  **652 methods appear in no public documentation**
- [`data/apollo-call-sites.tsv`](data/apollo-call-sites.tsv) — 834 real call signatures mined from
  Carbine's own UI code, 584 binary-confirmed

[`source/lua/`](source/lua/) holds **191 original client UI scripts** (`Copyright (c) NCsoft`) and
[`source/xml/`](source/xml/) 631 UI forms.

---

## Tools

Everything here is reproducible from the client. Nothing is hand-transcribed.

| tool | what it does |
|---|---|
| `cdn-deconstruct.py` | decodes all 197,333 blobs and classifies them — **15.5s on 32 cores** |
| `parse-kcap-index.py` | walks the archive index; recovers 218,427 real filenames |
| `extract-world-props.py` | every world object with model, position, rotation |
| `crack-prop.py` | solves record layout by constraint, or proves it is not fixed-size |
| `cdn-deep-analyse.py` | profiles a format across its whole population |
| `area-index.py` | one pass over `.area`, cached; every later question is instant |
| `hunt-spawn-coords.py` | vectorised search of the entire client for known coordinates |
| `parse-client-docs.py` | the client's own API docs → 147 documents |
| `extract-apollo-api.py` | reads the API surface out of the executable |
| `TableDump-Program.cs` | `--all` dumps every game table via reflection |

---

## Method

Formats with no specification were mapped **statistically across their whole population**, never by
reading one file and proposing a layout:

| behaviour across every file of a type | conclusion |
|---|---|
| never varies | magic or version |
| correlates with file size (`r > 0.9`) | count, length, or offset |
| always small, few distinct values | version, flag, or enum |
| near-unique per file | id or hash |
| printable run | a name the format references |

**No tool here prints a struct definition it has not verified.** Where a field's role is unknown the
documentation says so and gives the range. That rule exists because guessing produced two confident
wrong answers during this work, and neither announced itself.

---

## What is still unknown

Listed rather than glossed, because a gap written down stays a gap and a guess becomes a fact nobody
re-checks.

- **`.i3`** — 1,696 files, 2 GB, magic `SDEF`, not chunked, purpose unknown. Largest unidentified format.
- **96 blobs** appear in no index. They exist and nothing names them.
- **`.m3` mesh/vertex layout** — headers profiled, geometry not parsed.
- **`.tex` pixel data** — dimensions and format enum read, pixels not decoded.
- **`PROp` scale** — no 3-float window behaves like one; may be absent or stored as a single value.
- **`spellEffectType.DataType` values** — small ints (0/1/2), meaning not established. Confirm by
  decoding `Damage`, whose behaviour is verified, before implementing anything against them.
- **Creature spawn positions** — *most* are not client-side, but **43 known spawn coordinates were
  found** in `WorldLocation2.tbl`, `Spline2Node.tbl` and `Map/Eastern/*.area`. The pattern: hazards,
  path-followers, quest objects and interactables carry client-side positions because the client must
  render or predict them. Ordinary mobs do not. See [`data/spawn-coord-hits.tsv`](data/spawn-coord-hits.tsv).

---

## Provenance

**These files had no names.** The store is content-addressed; every name here is either recovered from
the archive index or built as `<sha1-prefix>-<hint>` where the hint comes from *inside* the content.
`MANIFEST.tsv` and `FILETREE.tsv` carry the full SHA-1 for everything, so any file traces back to the
exact blob it came from.

This is NCsoft's copyrighted material, recovered from a client the operator owns, published as
reference for WildStar preservation. **NCsoft retains all rights to the original assets and code.**
The extraction tools, format specifications and analysis in this repository are original work; the
game data and UI source they operate on are not.

Nothing here is intended to be pasted into a server implementation — these are Lua UI scripts and
binary assets, and a server is a different language on the other side of the wire. What transfers is
the **facts**: which resource index a class reads, what a record layout is, how damage scales.
