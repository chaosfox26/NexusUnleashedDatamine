# Class resources — which index each class actually reads

Source: `docs/client-extract/lua/e4399f90286b-Client-Lua-Script-for-ClassResources.lua`, Carbine's own
class resource UI, build 16042.

This is the bar under the action set — Psi Points, Volatility, Suit Power, Actuators, Spell Power.
Every class reads a **different resource index**, and the client states them as bare integers.

## The indices, read from the client's own branches

| class | resource index | secondary |
|---|---|---|
| Warrior | `GetResource(1)` / `GetMaxResource(1)` | — |
| Engineer | `GetResource(1)` / `GetMaxResource(1)` | — |
| Medic | `GetResource(1)` / `GetMaxResource(1)` | Focus |
| Esper | `GetResource(1)` — combo/Psi Points | Focus |
| Stalker | `GetResource(3)` / `GetMaxResource(3)` | — |
| Spellslinger | `GetResource(4)` / `GetMaxResource(4)` | Focus |

Dispatched on `unitPlayer:GetClassId()` against `GameLib.CodeEnumClass`, one `OnCreate<Class>` per
branch — `OnCreateEngineer`, `OnCreateEsper`, `OnCreateSpellslinger`, `OnCreateMedic`,
`OnCreateWarrior`, `OnCreateStalker`. Six branches, no default.

**Four of six classes share index 1.** The resource index alone does not identify a class, and
anything keying behaviour off "which resource moved" cannot distinguish Warrior from Engineer from
Medic from Esper.

## Focus is not a resource index

```lua
local nFocusMax     = math.floor(unitPlayer:GetMaxFocus())
local nFocusCurrent = math.floor(unitPlayer:GetFocus())
```

Focus — the mana-like pool the three casting classes use — has **dedicated accessors**, not a
`GetResource(n)` index. It is a separate system from the class resource, and a server treating them
as the same numbered vital would be wrong about both.

Note the `math.floor`: the client floors focus for display, so a fractional server value is expected
and is not a rounding bug.

## The `GetResource` signature

`GetResource` accepts a **bare integer**, and elsewhere the same call is made with an enum member:

```lua
unitPlayer:GetResource(1)                                        -- ClassResources
unitPlayer:GetResource(Unit.CodeEnumEUnitStatType.Resources0)    -- SprintMeter
```

Same function, both forms — so the enum members are plain integers and the index space is shared
between class resources and the sprint/dash energies. What is **not** established is the numeric
value of any `CodeEnumEUnitStatType` member; see `sprint-and-dash.md` for why string order in the
binary cannot supply it.

That gap matters here: it means the class indices above (1, 3, 4) **cannot yet be mapped onto our
`Vital` enum** with confidence. They are the client's numbers, recorded exactly as the client states
them.

## Class ids

`GameLib.CodeEnumClass` members appear in the binary near offset 11808536 — `Engineer`, `Warrior`,
`Spellslinger`, `Stalker` are visible in the surrounding strings, in hash order rather than
declaration order, so again **no numeric values from adjacency**.

Our own mapping, established earlier from signature abilities and holding across all six captures, is
in `docs/NOTE.md`: `1 Warrior · 2 Engineer · 3 Esper · 4 Medic · 5 Stalker · 7 Spellslinger`. That
came from measurement, not from this file, and this file does not contradict it.
