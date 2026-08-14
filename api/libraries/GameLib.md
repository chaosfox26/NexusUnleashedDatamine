# GameLib

*Library, documented by the client itself.*

**247 calls.** 20 carry `Deprecated="true"` — reported, not filtered, because that flag is set on entries known to be alive in 16042.

### `AcceptDuel()`

*no description in the client's documentation*

### `AreAnyItemsNew()`

*no description in the client's documentation*

### `AreQuestUnitCalloutsVisible()`

*no description in the client's documentation*

### `AreSettlerStructureCalloutsVisible()`

*no description in the client's documentation*

### `AssignMasterLoot()`

*no description in the client's documentation*

### `BuyBankBagSlot()`

`deprecated flag set` *no description in the client's documentation*

### `CanDisembarkVehicle()`

*no description in the client's documentation*

### `CanDye()`

*no description in the client's documentation*

### `CanEditKeySet(nKeySet)`

Does a lua_pushboolean if nKeySet is NOT any of the default 3 input key sets.

| parameter | type | meaning |
|---|---|---|
| `nKeySet` | Integer |  |

### `CanEquipBagItem()`

*no description in the client's documentation*

### `CanRepairAll()`

*no description in the client's documentation*

### `CanSetNavPoint()`

*no description in the client's documentation*

### `CanVacuum()`

Does a lua_pushboolean of GetCanVacuum.

### `Cheat_MakeMeLevel50()`

`deprecated flag set` *no description in the client's documentation*

### `ClearAllTargetMarkers()`

*no description in the client's documentation*

### `ClearCityDirection()`

*no description in the client's documentation*

### `ClearNavPoint()`

*no description in the client's documentation*

### `CodeEnumSetNavPointFailed()`

`deprecated flag set` *no description in the client's documentation*

### `CurrencyCap()`

*no description in the client's documentation*

### `DeclineDuel()`

*no description in the client's documentation*

### `DisableTutorialType()`

*no description in the client's documentation*

### `Disembark()`

*no description in the client's documentation*

### `DoAnyItemsBeginQuest()`

*no description in the client's documentation*

### `DragDropDataToItemLocation(nData)`

Does a lua_newtable with eType, nBagIndex, and nBagSlot.

| parameter | type | meaning |
|---|---|---|
| `nData` | Integer |  |

### `DyeItems()`

`deprecated flag set` *no description in the client's documentation*

### `EquipBagItem()`

*no description in the client's documentation*

### `ForfeitDuel()`

*no description in the client's documentation*

### `GetAbilityPoints()`

*no description in the client's documentation*

### `GetAccountRealmCharacter()`

*no description in the client's documentation*

### `GetAllTutorials()`

*no description in the client's documentation*

### `GetAllZoneCompletionMapZones()`

*no description in the client's documentation*

### `GetAttributePoints()`

*no description in the client's documentation*

### `GetAvailableTargetMarkers()`

*no description in the client's documentation*

### `GetBagItem()`

*no description in the client's documentation*

### `GetBindPoint()`

*no description in the client's documentation*

### `GetCCStateStunTimeRemaining()`

*no description in the client's documentation*

### `GetCharInputKeySet(nCharIndex)`

`deprecated flag set` Runs the GetKeyBindingsFromTable specified by nCharIndex. Also does a lua_pushnil if a wait is needed for the server to reply for the key binding list.

| parameter | type | meaning |
|---|---|---|
| `nCharIndex` | Integer |  |

### `GetCharacterList()`

`deprecated flag set` Does a lua_newtable of a counter as an integer and a character name list entry as a string.

### `GetClassInnateAbilitySpells()`

*no description in the client's documentation*

### `GetClassName()`

Does a localized lua_pushwstring corresponding to nId from DbFileTable_Class_GetByID, or nil if null.

**Returns** — `String` 

### `GetControlledUnit()`

Returns a new unit that is a copy of the controlled unit, or nil if null.

**Returns** — `Unit` 

### `GetCostumeCount()`

`deprecated flag set` *no description in the client's documentation*

### `GetCostumeIndex()`

`deprecated flag set` *no description in the client's documentation*

### `GetCostumeItem()`

`deprecated flag set` *no description in the client's documentation*

### `GetCostumeItemIcon()`

`deprecated flag set` *no description in the client's documentation*

### `GetCostumeUnlockLevel()`

`deprecated flag set` *no description in the client's documentation*

### `GetCredits()`

*no description in the client's documentation*

### `GetCurrInputKeySet()`

Does a lua_pushinteger of CurrInputSet.

### `GetCurrentClassInnateAbilityIndex()`

*no description in the client's documentation*

### `GetCurrentClassInnateAbilitySpell()`

*no description in the client's documentation*

### `GetCurrentWorldId()`

*no description in the client's documentation*

### `GetCurrentZoneId()`

*no description in the client's documentation*

### `GetCurrentZoneMap()`

*no description in the client's documentation*

### `GetCurrentZonePvpRules()`

*no description in the client's documentation*

### `GetDefaultRecallCommand()`

*no description in the client's documentation*

### `GetDisabledGameplaySystems()`

*no description in the client's documentation*

### `GetDuelOpponent()`

*no description in the client's documentation*

### `GetDuelState()`

*no description in the client's documentation*

### `GetDyeCost()`

*no description in the client's documentation*

### `GetDyeUnlockLevel()`

*no description in the client's documentation*

### `GetEmptyInventorySlots()`

*no description in the client's documentation*

### `GetErrorCategories()`

*no description in the client's documentation*

### `GetFrameRate()`

*no description in the client's documentation*

### `GetGadgetAbility()`

*no description in the client's documentation*

### `GetGameCommand()`

*no description in the client's documentation*

### `GetGameExitInfo()`

*no description in the client's documentation*

### `GetGameMode()`

*no description in the client's documentation*

### `GetGameTime()`

Does a lua_pushdouble of GetGameTime / 1000.0 as a double.

### `GetGearScore()`

*no description in the client's documentation*

### `GetGuildHolomarkDistance()`

*no description in the client's documentation*

### `GetGuildHolomarkVisible()`

*no description in the client's documentation*

### `GetHealthyGamingStatus()`

*no description in the client's documentation*

### `GetInputActionCategories()`

Does a lua_newtable with id, strName of action categories.

### `GetInputActionNameByEnum()`

*no description in the client's documentation*

### `GetInputKeyNameText(inputKey)`

Does a lua_pushwstring of the input key's name.

| parameter | type | meaning |
|---|---|---|
| `inputKey` | SInputKey |  |

### `GetInputKeySet(nInputSet)`

Runs the GetKeyBindingsFromTable specified by nInputSet. Also does a lua_pushnil if a wait is needed for the server to reply for the key binding list.

| parameter | type | meaning |
|---|---|---|
| `nInputSet` | EInputKeySet |  |

### `GetInstanceSettings()`

*no description in the client's documentation*

### `GetInteractHintArrowObject()`

*no description in the client's documentation*

### `GetInteractiveUnit()`

Does a lua_pushinteger of g_game's ClosestInteractiveUnit.

### `GetKeyBinding()`

*no description in the client's documentation*

### `GetKeyBindingByEnum()`

*no description in the client's documentation*

### `GetKeyBindings()`

Does a lua_newtable that describes the current key bindings.

### `GetKnownDyes()`

*no description in the client's documentation*

### `GetLastTargetedPlayerName()`

*no description in the client's documentation*

### `GetLatency()`

*no description in the client's documentation*

### `GetLevelCap()`

*no description in the client's documentation*

### `GetLevelUpFanfareDuration()`

*no description in the client's documentation*

### `GetLevelUpUnlock()`

*no description in the client's documentation*

### `GetLevelUpUnlockTypes()`

*no description in the client's documentation*

### `GetLocalTime()`

Does a lua_newtable with year, month, day, dayOfWeek, hour, minute, second.

### `GetLootRolls()`

*no description in the client's documentation*

### `GetMasterLoot()`

*no description in the client's documentation*

### `GetMountList()`

`deprecated flag set` *no description in the client's documentation*

### `GetNavPoint()`

*no description in the client's documentation*

### `GetNavPointChatLinkString()`

*no description in the client's documentation*

### `GetNextBankBagCost()`

`deprecated flag set` *no description in the client's documentation*

### `GetNumBankBagSlots()`

*no description in the client's documentation*

### `GetNumClassInnateAbilitySpells()`

*no description in the client's documentation*

### `GetOmnibitsBonusInfo()`

*no description in the client's documentation*

### `GetPendingLevelUpUnlocks()`

*no description in the client's documentation*

### `GetPendingRemovalWarningRemaining()`

*no description in the client's documentation*

### `GetPendingTutorials()`

*no description in the client's documentation*

### `GetPetDismissCommand()`

*no description in the client's documentation*

### `GetPingTime()`

*no description in the client's documentation*

### `GetPlayerBuffWindowProperties()`

*no description in the client's documentation*

### `GetPlayerCurrency(nType)`

Returns a new LuaGameTypes_Money that is a copy of nType's money value.

| parameter | type | meaning |
|---|---|---|
| `nType` | ECurrencyType |  |

### `GetPlayerDeathState()`

*no description in the client's documentation*

### `GetPlayerGenericVehicleUnit()`

*no description in the client's documentation*

### `GetPlayerLevel()`

*no description in the client's documentation*

### `GetPlayerMountUnit()`

Returns a new unit that is a copy of the mount unit, else 1 and nil if null.

**Returns** — `Unit` 

### `GetPlayerPets()`

*no description in the client's documentation*

### `GetPlayerRewardProperties()`

*no description in the client's documentation*

### `GetPlayerRewardProperty()`

*no description in the client's documentation*

### `GetPlayerTaxiUnit()`

Returna the taxi that the player is currently on.

**Returns** — `Unit` The taxi that the player is riding

### `GetPlayerUnit()`

Returns a new unit that is a copy of the character unit, or nil if null.

**Returns** — `Unit` 

### `GetPlayerUnitByName()`

*no description in the client's documentation*

### `GetPlayerVehicleUnit()`

Returns a new unit that is a copy of the vehicle unit, else 1 and nil if null.

**Returns** — `Unit` 

### `GetPvpFlagInfo()`

*no description in the client's documentation*

### `GetRapidTransportCooldown()`

*no description in the client's documentation*

### `GetRapidTransportDestinationsForWorld()`

*no description in the client's documentation*

### `GetRealmName()`

Does a lua_pushwstring of GetRealmName.

### `GetRepairAllCost()`

*no description in the client's documentation*

### `GetReputationInfo()`

*no description in the client's documentation*

### `GetReputationLevels()`

*no description in the client's documentation*

### `GetRewardPropertyName()`

*no description in the client's documentation*

### `GetServerTime()`

*no description in the client's documentation*

### `GetShortcutMount()`

*no description in the client's documentation*

### `GetShortcutPotion()`

*no description in the client's documentation*

### `GetSpell()`

*no description in the client's documentation*

### `GetSpellThresholdTimePrcntDone()`

*no description in the client's documentation*

### `GetStuckCooldowns()`

*no description in the client's documentation*

### `GetTargetMarkerIcon()`

*no description in the client's documentation*

### `GetTargetUnit()`

Returns a new unit that is a copy of the target unit, else 0 if null.

**Returns** — `Unit` 

### `GetTaxisForWorld()`

*no description in the client's documentation*

### `GetTeleportIlliumSpell()`

*no description in the client's documentation*

### `GetTeleportThaydSpell()`

*no description in the client's documentation*

### `GetTextTypeMaxLength()`

*no description in the client's documentation*

### `GetTickCount()`

Does a lua_pushint of GetTickCount casted as an integer.

### `GetTotalAbilityPoints()`

*no description in the client's documentation*

### `GetTotalInventorySlots()`

*no description in the client's documentation*

### `GetTutorial()`

*no description in the client's documentation*

### `GetTutorialAnchorInfo()`

*no description in the client's documentation*

### `GetTutorialLayouts()`

*no description in the client's documentation*

### `GetTutorialPopupContext()`

*no description in the client's documentation*

### `GetTutorialVisibilityFlags()`

*no description in the client's documentation*

### `GetTutorialsForCategory()`

*no description in the client's documentation*

### `GetUnitById()`

*no description in the client's documentation*

### `GetUnitScreenPosition()`

*no description in the client's documentation*

### `GetUnknownDyes()`

*no description in the client's documentation*

### `GetUnlockedLevelCap()`

*no description in the client's documentation*

### `GetUnlocksForLevel()`

*no description in the client's documentation*

### `GetVanityPetList()`

`deprecated flag set` *no description in the client's documentation*

### `GetVersionInfo()`

*no description in the client's documentation*

### `GetWorldCompletionPercent()`

*no description in the client's documentation*

### `GetWorldDifficulty()`

*no description in the client's documentation*

### `GetWorldTimeOfDay()`

Does a lua_pushdouble of GetWorldTimeOfDay as a double. (This is not divided by 1000.0)

### `GetWorldTooltipContainer()`

*no description in the client's documentation*

### `GetXpBonusData(nWho)`

Does a lua_newtable that describes an xp bonus.

| parameter | type | meaning |
|---|---|---|
| `nWho` | Integer |  |

### `GetZoneCompletion()`

*no description in the client's documentation*

### `GetZoneCompletionTypes()`

*no description in the client's documentation*

### `GetZoneExplorationPercent()`

*no description in the client's documentation*

### `GetZoneMap()`

*no description in the client's documentation*

### `HasBindPoint()`

*no description in the client's documentation*

### `HasTutorialSound()`

*no description in the client's documentation*

### `HasXPBonus()`

*no description in the client's documentation*

### `InRatedPvpMatch()`

*no description in the client's documentation*

### `InitiateDuel()`

*no description in the client's documentation*

### `InitiatePTRCharacterCopy()`

*no description in the client's documentation*

### `InvokePreOrder()`

`deprecated flag set` *no description in the client's documentation*

### `IsCharacterLoaded()`

Does a lua_pushboolean of g_game's IsLoaded as a boolean.

### `IsControlledUnit()`

Does a lua_pushboolean whether pUnit is equal to GetControlledUnit. Parameter: unitToCheck: CUnit

### `IsCostumeSlotVisible()`

`deprecated flag set` *no description in the client's documentation*

### `IsCurrentInnateAbilityActive()`

*no description in the client's documentation*

### `IsIgnoringDuelRequests()`

*no description in the client's documentation*

### `IsInLocation()`

*no description in the client's documentation*

### `IsInWorldZone()`

*no description in the client's documentation*

### `IsKeyBindable()`

*no description in the client's documentation*

### `IsLevelUpUnlockViewed()`

*no description in the client's documentation*

### `IsMouseLockOn()`

*no description in the client's documentation*

### `IsNavPointSet()`

*no description in the client's documentation*

### `IsNeedRollAllowed()`

*no description in the client's documentation*

### `IsOverdriveActive()`

*no description in the client's documentation*

### `IsPrivilegeRestricted()`

*no description in the client's documentation*

### `IsPvpFlagged()`

*no description in the client's documentation*

### `IsPvpServer()`

*no description in the client's documentation*

### `IsSpellSurgeActive()`

*no description in the client's documentation*

### `IsTextValid()`

*no description in the client's documentation*

### `IsTutorialCategoryVisible()`

*no description in the client's documentation*

### `IsTutorialNoPageAlert()`

*no description in the client's documentation*

### `IsTutorialViewed()`

*no description in the client's documentation*

### `IsTutorialZone()`

*no description in the client's documentation*

### `IsZoneInZone()`

*no description in the client's documentation*

### `ItemLocationToDragDropData(nLocationType, nBagIndex, nBagSlot)`

Does a lua_pushinteger of GetDragDropData specified by nLocationType, nBagIndex, and nBagSlot.

| parameter | type | meaning |
|---|---|---|
| `nLocationType` | Integer for enum EInventoryLocation |  |
| `nBagIndex` | Integer |  |
| `nBagSlot` | EBagSlot |  |

### `LeavePendingRemovalInstance()`

*no description in the client's documentation*

### `MarkCityDirection()`

*no description in the client's documentation*

### `MarkLevelUpUnlockViewed()`

*no description in the client's documentation*

### `MarkTutorialViewed()`

*no description in the client's documentation*

### `OnClosedInstanceSettings()`

*no description in the client's documentation*

### `OpenFortunes()`

*no description in the client's documentation*

### `OpenStore()`

*no description in the client's documentation*

### `PassOnLoot()`

*no description in the client's documentation*

### `PauseGameActionInput(bPaused)`

Runs the PauseGameAction with bPaused.

| parameter | type | meaning |
|---|---|---|
| `bPaused` | Boolean |  |

### `PlayTutorialSound()`

*no description in the client's documentation*

### `PrepareInfractionReport()`

*no description in the client's documentation*

### `RefreshCustomTelegraphColors()`

*no description in the client's documentation*

### `ReplayLevelUp()`

*no description in the client's documentation*

### `ReportBug()`

*no description in the client's documentation*

### `ResetAttributePoints()`

*no description in the client's documentation*

### `ResetLevelUpUnlocks()`

*no description in the client's documentation*

### `ResetSingleInstance()`

*no description in the client's documentation*

### `ResetTutorials()`

*no description in the client's documentation*

### `RollOnLoot()`

*no description in the client's documentation*

### `SearchRelationshipStatusByCharacterName()`

*no description in the client's documentation*

### `SetCostumeIndex()`

`deprecated flag set` *no description in the client's documentation*

### `SetCostumeItem()`

`deprecated flag set` *no description in the client's documentation*

### `SetCostumeSlotVisible()`

`deprecated flag set` *no description in the client's documentation*

### `SetCurrInputKeySet(nInputSet)`

Does an update of InputSet specified by nInputSet. Also does a lua_pushboolean of false if a wait is needed for the server to reply for the key binding list.

| parameter | type | meaning |
|---|---|---|
| `nInputSet` | EInputKeySet |  |

### `SetCurrentClassInnateAbilityIndex()`

*no description in the client's documentation*

### `SetDefaultRecallCommand()`

*no description in the client's documentation*

### `SetIgnoreDuelRequests()`

*no description in the client's documentation*

### `SetInstanceSettings()`

*no description in the client's documentation*

### `SetInteractHintArrowObject()`

*no description in the client's documentation*

### `SetKeyBindings(tInputTable)`

Runs the SaveInputKeySet after updating the key bindings table.

| parameter | type | meaning |
|---|---|---|
| `tInputTable` | LuaTable |  |

### `SetMouseLock()`

`deprecated flag set` *no description in the client's documentation*

### `SetNavPoint()`

*no description in the client's documentation*

### `SetSharedChallengePreference()`

*no description in the client's documentation*

### `SetShortcutMount()`

*no description in the client's documentation*

### `SetShortcutPotion()`

*no description in the client's documentation*

### `SetTargetUnit(pUnitToSelect)`

Runs the set target id method on pUnitToSelect's unit id.

| parameter | type | meaning |
|---|---|---|
| `pUnitToSelect` | CUnit |  |

### `SetWorldTooltipContainer()`

*no description in the client's documentation*

### `ShowGuildHolomark()`

*no description in the client's documentation*

### `ShowNavPointHintArrow()`

*no description in the client's documentation*

### `ShowUI()`

*no description in the client's documentation*

### `SpendAttributePoints()`

*no description in the client's documentation*

### `StopTutorialSound()`

*no description in the client's documentation*

### `SummonVanityPet()`

*no description in the client's documentation*

### `SupportStuck()`

*no description in the client's documentation*

### `SwapBagItems()`

*no description in the client's documentation*

### `TogglePvpFlags()`

*no description in the client's documentation*

### `ToggleQuestUnitCallouts()`

*no description in the client's documentation*

### `ToggleSettlerStructureCallouts()`

*no description in the client's documentation*

### `ToggleTutorialVisibilityFlags()`

*no description in the client's documentation*

### `UIExitCinematics()`

Runs g_game's UIExitCinematicsMode method with 100 as the parameter.

### `UIStartCinematics()`

Runs g_game's UIEnterCinematicsMode method.

### `WhiteOutFadeIn()`

Runs g_game's WhiteOutFadeIn method.

### `WhiteOutFadeOut()`

Runs g_game's WhiteOutFadeOut method with 3000 as the parameter.

### `WorldLocToScreenPoint()`

*no description in the client's documentation*

