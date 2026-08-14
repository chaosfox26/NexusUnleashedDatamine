# SpellEffectType — the decoder ring for the 116 unimplemented effects

`docs/client-data/tables/spellEffectType.tsv` — **150 rows**, one per effect type, exactly matching
the `SpellEffectType` enum our server declares and the 34/150 coverage figure `check.ps1` reports.

This table was unreachable until now. It is the single most useful thing in the 2 million rows.

## What it contains

```
Id  Flags  DataType00 DataType01 DataType02 ... DataType09
1   31     2          1          1              2
2   21     0          2          0              2
```

Every `Spell4Effects` row carries `DataBits00` through `DataBits09` — ten raw 32-bit fields whose
meaning depends entirely on the effect type. **`spellEffectType` says how to read them.**

`DataType00..09` gives the type of each corresponding `DataBits` slot for that effect. Without it,
`DataBits03 = 1084227584` is an opaque integer. With it, you know whether that is a float
(`1084227584` as bits is `5.0f`), a spell id, a property index, or unused.

## Why this is the blocker, not the data

The state of play before this:

- we can calculate any ability's **damage** — verified, `AP × c₁ + Level × c₂`
- we know all **202 class abilities** and their coefficients per tier
- the server implements **34 of 150** effect types

Damage is one effect type. The other 149 are everything else combat does — `CCStateSet`,
`Absorption`, `SapVital`, `Proc`, `ModifyInterruptArmor`, `DistributedDamage`, `Transference`,
`SpellDispel`, `ThreatModification`. Each needs its `DataBits` decoded before it can be implemented,
and that decoding is per effect type.

**This table is what turns "116 unimplemented effects" from a research problem into a coding
problem.**

## Reading a DataType value

The `DataType` values are small integers (0, 1, 2 observed). What each means is **not yet
established** — three candidate readings exist and none has been confirmed:

- a type tag (0 unused, 1 integer, 2 float)
- an index into a type table elsewhere
- a flag set rather than an enum

**Do not implement against a guess here.** The cheapest confirmation is the one that has worked every
time on this project: take an effect whose behaviour is already known — `Damage`, which we have
verified against the client to the decimal — read its `DataType` row, and check the interpretation
reproduces the coefficients we already measured. If `Damage`'s row does not decode to what we know
`Damage` does, the reading is wrong.

## Companion tables, now also available

| table | rows | what it carries |
|---|---|---|
| `spell4Effects` | 131,010 | the effect rows themselves — `EffectType`, `DamageType`, `ParameterType[]`, `ParameterValue[]`, `DataBits00..09` |
| `spell4EffectModification` | — | modifications applied to effects |
| `spell4EffectGroupList` | 21 | effect grouping, 33 columns |
| `spell4HitResults` | 12 | hit outcome flags |
| `spell4Conditions` | 48 | `ConditionMask` / `ConditionValue` |
| `spell4CCConditions` | 12 | crowd-control conditions |
| `cCStates` | 28 | the CC state list |
| `cCStateDiminishingReturns` | 16 | DR curve |
| `cCStateAdditionalData` | — | per-state extra data |
| `distanceDamageModifier` | 7 | falloff for `DistanceDependentDamage` |

`distanceDamageModifier` having exactly **7 rows** is worth noting: `DistanceDependentDamage` is one
of the unimplemented effect types, and its entire modifier table is seven rows. That is a small,
self-contained effect to implement first and prove the method on.

## Adjacent find: `classSecondaryStatBonus`

36 rows, and it is per-class stat scaling:

```
Id  SecondaryStat00  SecondaryStat01  SecondaryStat02  Modifier00  Modifier01  Modifier02
5   32               47               0                0.5         0.5         0
7   35               0                0                0.61        0           0
```

Two or three `UnitProperty2Id` references with a modifier each. This is how a class converts its
primary attributes into secondary stats — the layer sitting between the character sheet and the
damage formula, and another thing we had no visibility into.
