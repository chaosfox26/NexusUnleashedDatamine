# Spell

*Object, documented by the client itself.*

**49 calls.** 4 carry `Deprecated="true"` — reported, not filtered, because that flag is set on entries known to be alive in 16042.

### `GetAOETargetInfo()`

Does a lua_newtable of eSelectionType if not aoe, otherwise many (10+) fields relating to the aoe data.

**Returns** — `Table` 

### `GetAbilityCharges()`

*no description in the client's documentation*

### `GetBaseSpellId()`

*no description in the client's documentation*

### `GetCastInfoString()`

*no description in the client's documentation*

### `GetCastMethod()`

Does a lua_pushinteger of pSpell's castMethod.

### `GetCastTime()`

Does a lua_pushnumber of pSpell's castTime * 0.001f, else 0.0f if null.

### `GetCastTimeOverride()`

*no description in the client's documentation*

### `GetCasterInnateCosts()`

Does a lua_newtable with an index, eType, and nValue.

### `GetCasterInnateRequirements()`

Does a lua_newtable with an index, eVital, nValue, and eEval.

### `GetChannelData()`

Does a lua_newtable with fMaxTime, fInitialDelay, and fPulseTime.

### `GetClass()`

Does a lua_pushinteger of pSpell's SpellClass.

### `GetClassPower()`

`deprecated flag set` Does a lua_pushinteger of pSpell's power, 0 if pSpell's spellClass <= 0.

### `GetCombatMode()`

`deprecated flag set` Does a lua_pushinteger of pSpell's combatModeId.

### `GetCooldownRemaining()`

*no description in the client's documentation*

### `GetCooldownTime()`

Does a lua_pushnumber of pSpell's spellCoolDown * 0.001f.

### `GetCostInfoString()`

*no description in the client's documentation*

### `GetFlavor()`

Does a lua_pushstring of pSpell's localized ActionBarTooltip, or nil if null.

### `GetGCDTime()`

*no description in the client's documentation*

### `GetIcon()`

Does a lua_pushstring of pSpell's iconPath, or nil if null.

### `GetId()`

*no description in the client's documentation*

### `GetLasBonusEachTierDesc()`

*no description in the client's documentation*

### `GetLasTierDesc()`

*no description in the client's documentation*

### `GetMaximumRange()`

Does a lua_pushinteger of pSpell's targetMaximumRange, or 0.0f if null.

### `GetMinimumRange()`

Does a lua_pushinteger of pSpell's targetMinimumRange, or 0.0f if null.

### `GetName()`

Does a lua_pushwstring of pSpell's localized IdName, or nil if null.

### `GetPrerequisites()`

Does a lua_newtable of many (10+) fields relating to pSpell's preqrequisites.

**Returns** — `Table` 

### `GetPrice()`

Does a LuaGameTypes_Money::New of pSpell's price.

### `GetProxyChannelData()`

*no description in the client's documentation*

### `GetReagents()`

Does a lua_newtable with an index, nRequired, eType, and item relating to pSpell's reagents.

### `GetRequiredLevel()`

*no description in the client's documentation*

### `GetRequiredWorldZone()`

Does a lua_pushwstring of a localized pWorldZone's nameId if pSpell requires a specific world zone.

### `GetSchool()`

Does a lua_pushinteger of pSpell's school.

### `GetSpellServiceTokenCost()`

*no description in the client's documentation*

### `GetTargetAngle()`

Does a lua_pushnumber of pSpell's targetAngle.

### `GetTargetInnateRequirements()`

Does a lua_newtable with an index, eVital, nValue, and eEval of target inate requirements.

### `GetThresholdTime()`

*no description in the client's documentation*

### `GetTier()`

Does a lua_pushinteger of pSpell's tierIndex.

### `GetTradeskillRequirements()`

*no description in the client's documentation*

### `IsBeneficial()`

*no description in the client's documentation*

### `IsFreeformTarget()`

*no description in the client's documentation*

### `IsMovingInterrupted()`

*no description in the client's documentation*

### `IsNew()`

Does a lua_pushboolean of pSpell's IsNewItem.

### `IsSelfSpell()`

*no description in the client's documentation*

### `SetNewFlag(bNew)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `bNew` | Boolean |  |

### `ShouldHideCooldownInTooltip()`

*no description in the client's documentation*

### `ShowFloater()`

*no description in the client's documentation*

### `__eq()`

`deprecated flag set` *no description in the client's documentation*

### `__gc()`

`deprecated flag set` *no description in the client's documentation*

### `is()`

*no description in the client's documentation*

