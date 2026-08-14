# Sprint and dash — what the client's own UI does

Source: `docs/client-extract/lua/a552798a2169-Client-Lua-Script-for-SprintMeter.lua`, recovered from
the CDN mirror. Carbine's own sprint meter, build 16042.

This is the standing unsolved bug: **`mps` never rises and resource 0 never depletes across 334
samples — the client refuses to *start* the sprint.** Dash (resource 7) depletes and regenerates
normally, which already ruled out a general resource-plumbing fault.

## Sprint has its own events. It is not read from a generic resource update.

```lua
Apollo.RegisterEventHandler("SprintStateUpdated",       "OnSprintStateUpdated", self)
Apollo.RegisterEventHandler("DashEnergyUpdated",        "OnDashEnergyUpdated", self)
Apollo.RegisterEventHandler("SprintEnergyUpdated",      "OnSprintEnergyUpdated", self)
Apollo.RegisterEventHandler("PlayerMovementSpeedUpdate","OnPlayerMovementSpeedUpdate", self)
```

Four dedicated events. The meter is driven by these, **not** by a generic vital/stat update, so a
server that updates the underlying vital without producing the event the client listens for would
show exactly what we see: a bar that never moves.

## The resource indices, from the client itself

```lua
-- OnDocumentReady, lines 82-83
self:OnSprintEnergyUpdated(unitPlayer:GetResource(Unit.CodeEnumEUnitStatType.Resources0),
                           unitPlayer:GetMaxResource(Unit.CodeEnumEUnitStatType.Resources0))
self:OnDashEnergyUpdated(  unitPlayer:GetResource(Unit.CodeEnumEUnitStatType.Resources6), ...)

-- OnCharacterCreated, lines 113-114
self:OnSprintEnergyUpdated(... Resources0 ...)
self:OnDashEnergyUpdated(  ... Resources7 ...)
```

**Sprint is `Resources0` in both paths.** That independently confirms `ForgeUI_SprintDash.lua`'s
`sprintResource = 0`, which CLAUDE.md already cites — two sources, agreeing, neither derived from the
other.

**Dash is `Resources6` in one path and `Resources7` in the other.** That is a real inconsistency in
Carbine's shipped code, not a transcription error here — both lines are in the same file. `ForgeUI`
says 7, and our own measurement showed resource 7 depleting, so 7 is the live one and line 83 is a
client-side bug that only fires on the `OnDocumentReady` path.

Worth knowing before anyone "fixes" a disagreement between our server and the client by matching the
client: **the client is not self-consistent here.**

## Where our server does not line up

`Source/NexusUnleashed.Game.Static/Entity/Vital.cs`:

```csharp
Health         = 0x0001,   Breath   = 0x0002,   ShieldCapacity = 0x0003,
KineticEnergy  = 0x0004,   Endurance = 0x0005,
Resource1      = 0x0006,   ...   Resource6 = 0x000B,
Dash           = 0x0010,
```

**There is no `Resource0`.** Our enum starts at `Resource1 = 6`, and the index the client reads sprint
from has no named counterpart on our side. `Endurance = 5` is the suspicious neighbour — sprint
energy is what WildStar's UI calls endurance — but that is a *hypothesis about a naming*, not a
verified mapping, and it is written here as one.

## What is NOT established

The numeric values of `Unit.CodeEnumEUnitStatType`. `Resources0` through `Resources10` all exist as
strings in `WildStar64.exe` (offsets 11709088–11709272) but sit in **hash-table order**, not
declaration order: `Resources8, Resources9, Resources6, Resources7, Resources4, Resources5,
Resources2, Resources3, Resources0, Resources1`. The integers are in the data section behind
pointers.

So string order gives no mapping, and inferring one from adjacency would be exactly the mistake that
put 83 methods under `AaRect`. **The mapping is open.**

## The lead, stated as a lead

The client drives its sprint bar from `SprintEnergyUpdated` and reads `Resources0`. Our server has no
vital at that index. The next thing to check is whether the server ever sends a vital the client maps
to `Resources0` at all — because if it does not, the bar can never move and the client has no reason
to believe sprint is available.

That is consistent with every symptom so far, and it is **not yet proven**. Three confident theories
about sprint have already been wrong (CLAUDE.md rule 7a records them), so this one gets tested before
anything is changed.

Cheapest test: `/nustat` in game and read what `GetResource(Resources0)` and
`GetMaxResource(Resources0)` return. If max is 0, the server never established the resource.
