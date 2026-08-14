# Abilities and tiers — what the client actually does

Source: `docs/client-extract/lua/950b06eedd13-Client-Lua-Script-for-ToolTips.lua` and
`...-AbilityAMPs.lua`, build 16042.

## The client computes no damage in Lua

The entire tier-bonus display is:

```lua
wndNextTierString:SetText(tTierSpells.tTiers[1].splObject:GetLasBonusEachTierDesc())
wndTier4String:SetText(   tTierSpells.tTiers[5].splObject:GetLasTierDesc())
wndTier8String:SetText(   tTierSpells.tTiers[9].splObject:GetLasTierDesc())
```

Three calls, three pre-rendered strings from the engine. **There is no arithmetic.** The numbers a
player sees are formatted C++-side and handed to Lua as text.

This is the third independent confirmation that scaling cannot be read off the client: the `Spell`
class exposes no effect parameters, no Lua code computes damage, and the only numeric output is a
sentence. Measuring the rendered text against a moving stat vector — what `/nuscale` does — is the
only client-side route there is.

## The tier array is offset by one from what the player sees

This is a labelling trap, and our own data files walk into it.

| array index | window it fills | what the player calls it |
|---|---|---|
| `tTiers[1]` | *"next tier"* bonus text | **base spell** (Tier 0) |
| `tTiers[5]` | `wndTier4String` | **Tier 4** |
| `tTiers[9]` | `wndTier8String` | **Tier 8** |

`nCurrentTier` is the **array index**, not the player-facing tier — the colour check is
`nCurrentTier >= 5` for the window labelled Tier 4.

`AbilityBook.GetSpellTierLevelRequirements()` says the same thing in its own words: *"Index 1 is the
base spell, while 2 is Tier 1, etc."*

**So our `tier` column of 1–9 is the player's Tier 0–8.** The coefficients in
`docs/client-data/ability-coefficients.tsv` are attached to the right spell ids — the join was on
`spellId`, not on the label — but anyone reading "tier 9" as the ninth upgrade is off by one, and the
maximum a player can reach reads as **Tier 8**.

## Two bugs in Carbine's shipped code

**One.** The guard and the dereference disagree:

```lua
if tTierSpells and tTierSpells.tTiers and tTierSpells.tTiers[1]
   and tTierSpells.tTiers[5] and tTierSpells.tTiers[8] then
        ...
        wndTier8String:SetText(tTierSpells.tTiers[9].splObject:GetLasTierDesc())
```

It checks `[8]` and then reads `[9]`. An ability with exactly eight entries passes the guard and then
indexes nil.

**Two** is in `SprintMeter.lua` — dash read from `Resources6` on one path and `Resources7` on another,
in the same file. See `sprint-and-dash.md`.

Both matter for the same reason: **the client is not self-consistent**, so "match the client" is not
a sufficient rule when our server and the client disagree. You have to ask which of the client's own
answers is the live one.

## Signatures confirmed by real use

```lua
AbilityBook.GetAbilityInfo(splSource:GetId(), 0, 0)     -- three arguments
AbilityBook.GetAbilitiesList(Spell.CodeEnumSpellTag.Misc) -- one, a spell tag
AbilityBook.GetTotalPower()                              -- none
```

`GetAbilityInfo` is called with both two and three arguments across the corpus, so the third is
optional. `docs/reference-data/apollo-call-sites.tsv` carries every arity seen rather than one
number, because collapsing them would invent a signature.

## AMP points (#70)

`AbilityAMPs.lua` only ever *displays* the numbers:

```lua
local nTotalPower     = AbilityBook.GetTotalPower()
local nAvailablePower = AbilityBook.GetAvailablePower()
local bLockedInPoints = AbilityBook.GetAvailableLockedInPower() < AbilityBook.GetTotalPower()
```

No progression formula, no per-level table lookup — the total arrives from the engine. Combined with
the separate finding that the AMP total is **not** in `LevelUpUnlock` (that column holds localised
text ids), the client-side route to #70 is one call to `GetTotalPower()` in game, and the
server-side route is wherever the engine sources it — still unknown.
