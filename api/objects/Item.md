# Item

*Object, documented by the client itself.*

**181 calls.** 96 carry `Deprecated="true"` — reported, not filtered, because that flag is set on entries known to be alive in 16042.

### `CanAutoSalvage()`

*no description in the client's documentation*

### `CanAutoSalvage()`

`deprecated flag set` *no description in the client's documentation*

### `CanCombineInEldanForge()`

*no description in the client's documentation*

### `CanDelete()`

*no description in the client's documentation*

### `CanDelete()`

`deprecated flag set` *no description in the client's documentation*

### `CanEquip(itemId)`

Does a lua_pushboolean if itemId can be equipped. uses as library

| parameter | type | meaning |
|---|---|---|
| `itemId` | TItem2Id |  |

### `CanEquip()`

`deprecated flag set` *no description in the client's documentation*

### `CanMoveToSupplySatchel()`

*no description in the client's documentation*

### `CanMoveToSupplySatchel()`

`deprecated flag set` *no description in the client's documentation*

### `CanSalvage()`

*no description in the client's documentation*

### `CanSalvage()`

`deprecated flag set` *no description in the client's documentation*

### `CanTakeFromSupplySatchel()`

*no description in the client's documentation*

### `CanTakeFromSupplySatchel()`

`deprecated flag set` *no description in the client's documentation*

### `CodeEnumItem2Family()`

`deprecated flag set` *no description in the client's documentation*

### `GetActivateSpell()`

`deprecated flag set` Currently has no implementation

### `GetActivateSpell()`

`deprecated flag set` *no description in the client's documentation*

### `GetAdditiveInfo()`

*no description in the client's documentation*

### `GetAdditiveInfo()`

`deprecated flag set` *no description in the client's documentation*

### `GetArmor()`

`deprecated flag set` *no description in the client's documentation*

### `GetArmor()`

`deprecated flag set` *no description in the client's documentation*

### `GetAvailableDyeChannel()`

*no description in the client's documentation*

### `GetAvailableDyeChannel()`

`deprecated flag set` *no description in the client's documentation*

### `GetBackpackCount()`

*no description in the client's documentation*

### `GetBackpackCount()`

`deprecated flag set` *no description in the client's documentation*

### `GetBagSlots()`

*no description in the client's documentation*

### `GetBagSlots()`

`deprecated flag set` *no description in the client's documentation*

### `GetBankCount()`

*no description in the client's documentation*

### `GetBankCount()`

`deprecated flag set` *no description in the client's documentation*

### `GetBuyPrice()`

Returns the success of a new LuaGameTypes_Money with BuyFromVendorPrice specified by itemData, or nil if null.

### `GetBuyPrice()`

`deprecated flag set` *no description in the client's documentation*

### `GetCharges()`

Does a lua_pushinteger of GetBatteryCharge specified by itemData, or nil if null.

### `GetCharges()`

`deprecated flag set` *no description in the client's documentation*

### `GetChatLinkString()`

*no description in the client's documentation*

### `GetChatLinkString()`

`deprecated flag set` *no description in the client's documentation*

### `GetCostumeUnlockInfo()`

*no description in the client's documentation*

### `GetDataFromId()`

*no description in the client's documentation*

### `GetDetailedInfo(itemCompare, arFlags)`

Returns a table of data for the given item.  This information is generally used for building item tooltips.

| parameter | type | meaning |
|---|---|---|
| `itemCompare` | Item | The item to compare with the primary item. |
| `arFlags` | Item.CodeEnumItemDetailedTooltip | If provided then the results are restricted to the identified groups of data. |

**Returns** — `Table` Detailed information of the provided items.  If the information is not relevant for the item or does not match the flags that were passed in, it will not be part of the table that is returned.

### `GetDetailedInfo()`

`deprecated flag set` *no description in the client's documentation*

### `GetDurability()`

*no description in the client's documentation*

### `GetDurability()`

`deprecated flag set` *no description in the client's documentation*

### `GetDurationRemaining()`

*no description in the client's documentation*

### `GetDurationRemaining()`

`deprecated flag set` *no description in the client's documentation*

### `GetDurationTotal()`

*no description in the client's documentation*

### `GetDurationTotal()`

`deprecated flag set` *no description in the client's documentation*

### `GetEffectiveLevel()`

*no description in the client's documentation*

### `GetEmptySockets()`

`deprecated flag set` *no description in the client's documentation*

### `GetEmptySockets()`

`deprecated flag set` *no description in the client's documentation*

### `GetEquipSpell()`

`deprecated flag set` Currently has no implementation

### `GetEquipSpell()`

`deprecated flag set` *no description in the client's documentation*

### `GetEquippedCount()`

*no description in the client's documentation*

### `GetEquippedCount()`

`deprecated flag set` *no description in the client's documentation*

### `GetEquippedItemForItemType()`

Returns a new item that is a copy of the equipped item at a type specified by itemData, or nil if null.

### `GetEquippedItemForItemType()`

`deprecated flag set` *no description in the client's documentation*

### `GetGivenQuest()`

Does a LuaGameTypes_Quest::New of the quest specified by itemData, or nil if null.

### `GetGivenQuest()`

`deprecated flag set` *no description in the client's documentation*

### `GetGlobalCatalystInfo()`

*no description in the client's documentation*

### `GetGlobalCatalystInfo()`

`deprecated flag set` *no description in the client's documentation*

### `GetGlyphBonus()`

`deprecated flag set` *no description in the client's documentation*

### `GetGlyphBonus()`

`deprecated flag set` *no description in the client's documentation*

### `GetGlyphInfo()`

`deprecated flag set` *no description in the client's documentation*

### `GetGlyphInfo()`

`deprecated flag set` *no description in the client's documentation*

### `GetHousingDecorInfoId()`

*no description in the client's documentation*

### `GetHousingDecorInfoId()`

`deprecated flag set` *no description in the client's documentation*

### `GetIcon()`

Does a lua_pushwstring of buttonIcon specified by itemData, or empty string if null.

### `GetIcon()`

`deprecated flag set` *no description in the client's documentation*

### `GetInventoryId()`

*no description in the client's documentation*

### `GetInventoryId()`

`deprecated flag set` *no description in the client's documentation*

### `GetItemCategory()`

*no description in the client's documentation*

### `GetItemCategory()`

`deprecated flag set` *no description in the client's documentation*

### `GetItemCategoryName()`

*no description in the client's documentation*

### `GetItemCategoryName()`

`deprecated flag set` *no description in the client's documentation*

### `GetItemFamily()`

*no description in the client's documentation*

### `GetItemFamily()`

`deprecated flag set` *no description in the client's documentation*

### `GetItemFamilyName()`

*no description in the client's documentation*

### `GetItemFamilyName()`

`deprecated flag set` *no description in the client's documentation*

### `GetItemFlavor()`

Does a lua_pushwstring of the localized tooltip specified by itemData, or nil if null.

### `GetItemFlavor()`

`deprecated flag set` *no description in the client's documentation*

### `GetItemFromInventoryLoc()`

*no description in the client's documentation*

### `GetItemId()`

*no description in the client's documentation*

### `GetItemId()`

`deprecated flag set` *no description in the client's documentation*

### `GetItemPower()`

*no description in the client's documentation*

### `GetItemPower()`

`deprecated flag set` *no description in the client's documentation*

### `GetItemQuality()`

Does a lua_pushinteger of the item quality specified by itemData, or nil if null.

### `GetItemQuality()`

`deprecated flag set` *no description in the client's documentation*

### `GetItemType()`

Does a lua_pushinteger of item2Type specified by itemData, or nil if null.

### `GetItemType()`

`deprecated flag set` *no description in the client's documentation*

### `GetItemTypeName()`

*no description in the client's documentation*

### `GetItemTypeName()`

`deprecated flag set` *no description in the client's documentation*

### `GetMaxCharges()`

Does a lua_pushinteger of batteryChargeMax specified by itemData, or nil if null.

### `GetMaxCharges()`

`deprecated flag set` *no description in the client's documentation*

### `GetMaxDurability()`

*no description in the client's documentation*

### `GetMaxDurability()`

`deprecated flag set` *no description in the client's documentation*

### `GetMaxStackCount()`

Does a lua_pushinteger of maxStackCount specified by itemData, or nil if null.

### `GetMaxStackCount()`

`deprecated flag set` *no description in the client's documentation*

### `GetMicrochipInfo()`

`deprecated flag set` *no description in the client's documentation*

### `GetMicrochipInfo()`

`deprecated flag set` *no description in the client's documentation*

### `GetName()`

Does a lua_pushwstring of the localized string id name specified by itemData, or empty string if null.

### `GetName()`

`deprecated flag set` *no description in the client's documentation*

### `GetPowerLevel()`

Does a lua_pushinteger of the item power level specified by itemData, or nil if null.

### `GetPowerLevel()`

`deprecated flag set` *no description in the client's documentation*

### `GetProcSpell()`

`deprecated flag set` *no description in the client's documentation*

### `GetProcSpell()`

`deprecated flag set` *no description in the client's documentation*

### `GetProficiencyInfo()`

Does a lua_newtable with id, has, and name specified by itemData, or nil if null.

### `GetProficiencyInfo()`

`deprecated flag set` *no description in the client's documentation*

### `GetPropertyName()`

*no description in the client's documentation*

### `GetRepairCost()`

*no description in the client's documentation*

### `GetRepairCost()`

`deprecated flag set` *no description in the client's documentation*

### `GetRequiredClass()`

Does a lua_newtable of the required classes specified by itemData, or nil if null.

### `GetRequiredClass()`

`deprecated flag set` *no description in the client's documentation*

### `GetRequiredFaction()`

*no description in the client's documentation*

### `GetRequiredFaction()`

`deprecated flag set` *no description in the client's documentation*

### `GetRequiredLevel()`

Does a lua_pushinteger of the item level specified by itemData, or nil if null.

### `GetRequiredLevel()`

`deprecated flag set` *no description in the client's documentation*

### `GetRequiredRace()`

Does a lua_newtable of the required races specified by itemData, or nil if null.

### `GetRequiredRace()`

`deprecated flag set` *no description in the client's documentation*

### `GetReturnTimeRemaining()`

*no description in the client's documentation*

### `GetReturnTimeRemaining()`

`deprecated flag set` *no description in the client's documentation*

### `GetRuneInfo()`

`deprecated flag set` *no description in the client's documentation*

### `GetRuneInfo()`

`deprecated flag set` *no description in the client's documentation*

### `GetRuneSlots()`

*no description in the client's documentation*

### `GetSellPrice()`

Returns the success of a new LuaGameTypes_Money with SellToVendorPrice specified by itemData, or nil if null.

### `GetSellPrice()`

`deprecated flag set` *no description in the client's documentation*

### `GetSetBonuses()`

*no description in the client's documentation*

### `GetSetBonuses()`

`deprecated flag set` *no description in the client's documentation*

### `GetSigils()`

`deprecated flag set` *no description in the client's documentation*

### `GetSlot()`

Does a lua_pushinteger of slotId specified by itemData, or nil if null.

### `GetSlot()`

`deprecated flag set` *no description in the client's documentation*

### `GetSlotName()`

Does a lua_pushwstring of the slot name specified by itemData, or nil if null.

### `GetSlotName()`

`deprecated flag set` *no description in the client's documentation*

### `GetStackCount(itemInstance)`

Does a lua_pushinteger of GetStackCount specified by itemData, or nil if null.

| parameter | type | meaning |
|---|---|---|
| `itemInstance` | LuaItemInstance |  |

### `GetStackCount()`

`deprecated flag set` *no description in the client's documentation*

### `GetTradeskillSchematicId()`

*no description in the client's documentation*

### `GetTradeskillSchematicId()`

`deprecated flag set` *no description in the client's documentation*

### `GetVirtualItems()`

*no description in the client's documentation*

### `GetWeaponDamageMax()`

`deprecated flag set` *no description in the client's documentation*

### `GetWeaponDamageMax()`

`deprecated flag set` *no description in the client's documentation*

### `GetWeaponDamageMin()`

`deprecated flag set` *no description in the client's documentation*

### `GetWeaponDamageMin()`

`deprecated flag set` *no description in the client's documentation*

### `GetWeaponPower()`

`deprecated flag set` Does a lua_pushnumber of weapon power specified by itemData, or 0.0f if null.

### `GetWeaponPower()`

`deprecated flag set` *no description in the client's documentation*

### `GetWeaponSpeed()`

`deprecated flag set` Does a lua_pushnumber of weapon speed specified by itemData, or 0.0f if null.

### `GetWeaponSpeed()`

`deprecated flag set` *no description in the client's documentation*

### `HasRestockingFee()`

*no description in the client's documentation*

### `HasRestockingFee()`

`deprecated flag set` *no description in the client's documentation*

### `IsAlwaysTradeable()`

*no description in the client's documentation*

### `IsAtEldanForge()`

*no description in the client's documentation*

### `IsAuctionable()`

*no description in the client's documentation*

### `IsAuctionable()`

`deprecated flag set` *no description in the client's documentation*

### `IsCommodity()`

*no description in the client's documentation*

### `IsCommodity()`

`deprecated flag set` *no description in the client's documentation*

### `IsDeprecated()`

*no description in the client's documentation*

### `IsDestroyOnLogout()`

*no description in the client's documentation*

### `IsDestroyOnLogout()`

`deprecated flag set` *no description in the client's documentation*

### `IsDestroyOnZone()`

*no description in the client's documentation*

### `IsDestroyOnZone()`

`deprecated flag set` *no description in the client's documentation*

### `IsEquippable()`

*no description in the client's documentation*

### `IsEquippable()`

`deprecated flag set` *no description in the client's documentation*

### `IsSalvagedLootSoulbound()`

*no description in the client's documentation*

### `IsSoulbound()`

*no description in the client's documentation*

### `IsSoulbound()`

`deprecated flag set` *no description in the client's documentation*

### `IsTradeableTo()`

*no description in the client's documentation*

### `IsUnique()`

Does a lua_pushboolean of the item bind flag specified by itemData, or nil if null.

### `IsUnique()`

`deprecated flag set` *no description in the client's documentation*

### `MoveToSupplySatchel()`

*no description in the client's documentation*

### `MoveToSupplySatchel()`

`deprecated flag set` *no description in the client's documentation*

### `PlayEquipSound()`

*no description in the client's documentation*

### `PlayEquipSound()`

`deprecated flag set` *no description in the client's documentation*

### `TakeFromSupplySatchel()`

*no description in the client's documentation*

### `TakeFromSupplySatchel()`

`deprecated flag set` *no description in the client's documentation*

### `__eq()`

`deprecated flag set` *no description in the client's documentation*

### `__gc()`

`deprecated flag set` *no description in the client's documentation*

### `isData()`

*no description in the client's documentation*

### `isData()`

*no description in the client's documentation*

### `isGlyphData()`

`deprecated flag set` *no description in the client's documentation*

### `isGlyphData()`

`deprecated flag set` *no description in the client's documentation*

### `isInstance()`

*no description in the client's documentation*

### `isInstance()`

*no description in the client's documentation*

### `isModdableData()`

*no description in the client's documentation*

### `isModdableData()`

*no description in the client's documentation*

### `isRuneData()`

*no description in the client's documentation*

### `isRuneData()`

*no description in the client's documentation*

