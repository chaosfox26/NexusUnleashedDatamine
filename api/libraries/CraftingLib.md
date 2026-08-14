# CraftingLib

*Library, documented by the client itself.*

This library is the primary way that the UI interacts with various tradeskills and schematics.  This includes tradeskills that the player has chosen, as well as ones that they are automatically granted such as cooking and runecrafting.

**54 calls.** 15 carry `Deprecated="true"` — reported, not filtered, because that flag is set on entries known to be alive in 16042.

### `AddAdditive(itemAdditive)`

Attempts to add an additive to the current crafting attempt.

| parameter | type | meaning |
|---|---|---|
| `itemAdditive` | Item | The additive that should be used for the current crafting session. |

### `AddRuneSlot(nNewSlotCount)`

`deprecated flag set` Attempts to add a rune slot to an item.

| parameter | type | meaning |
|---|---|---|
| `nNewSlotCount` | Integer | The number of rune slots on the item after adding a new one. |

> Carbine's own note: Need to figure out what event is fired if this is successful.

### `ClearRuneSlot(nSlotIdx)`

`deprecated flag set` Attempts to remove the rune in the specified rune slot.

| parameter | type | meaning |
|---|---|---|
| `nSlotIdx` | Integer | The index of the rune slot that the function will attempt to clear. |

> Carbine's own note: Need to figure out what event is fired as a response.

### `CompleteCraft(tCrafting)`

Tells the client to complete the current schematic.  If this is called on a non-equipment based crafting schematic, no parameters are needed.

| parameter | type | meaning |
|---|---|---|
| `tCrafting` | Table | The parameters representing the player's chooses while crafting. |

**Returns** — `Bool` Returns true if the request was sent to the server.

> Carbine's own note: Thresholds should be allowed to be 1 based in Lua.

### `CompleteRerollRuneType()`

`deprecated flag set` *no description in the client's documentation*

### `CraftItem(idSchematic)`

Begins a crafting attempt for the specified schematic.

| parameter | type | meaning |
|---|---|---|
| `idSchematic` | Integer | The schematic that the player is trying to craft. |

### `ForgetTradeskill()`

`deprecated flag set` This function has no code and does nothing.

### `GetAchievementCategoryForTier(eTradeskill, eTier)`

Gets the achievement category id for the tradeskill tier's associated achievement.

| parameter | type | meaning |
|---|---|---|
| `eTradeskill` | CraftingLib.CodeEnumTradeskill | The tradeskill that the function will use to find the achievement category. |
| `eTier` | CraftingLib.CodeEnumTradeskillTier | The tier that the function will return the achievement category id for. |

**Returns** — `Integer` The id number for the achievement category that the tradeskill tier belongs to.

### `GetAvailableAdditives(eTradeskill, idSchematic)`

Gets a list of the additives that are available for the specified schematic.

| parameter | type | meaning |
|---|---|---|
| `eTradeskill` | CraftingLib.CodeEnumTradeskill | The tradeskill that the schematic belongs to. |
| `idSchematic` | Integer | The function will get the additives that can be used with the schematic with this id. |

**Returns** — `Item` An array of the different additives that can be used with the schematic.

### `GetAvailableCatalysts(eTradeskill, idSchematic)`

Gets a list of the catalysts that are in the player's inventory and can be used with the specified schematic.

| parameter | type | meaning |
|---|---|---|
| `eTradeskill` | CraftingLib.CodeEnumTradeskill | The tradeskill that the schematic belongs to. |
| `idSchematic` | Integer | The function will get a list of the catalysts that can be used with the schematic with this id. |

**Returns** — `Table` An array that contains both the catalyst items that can be used with the schematic and the number that the player has in their inventory.

### `GetAvailableMicrochips(idSchematic, eUnitProperty, nOffset, nCount, nPowerCoreId)`

`deprecated flag set` Gets a list of the microchips that can be used with the specified schematic.

| parameter | type | meaning |
|---|---|---|
| `idSchematic` | Integer | The schematic that the function will poll for the microchips that can be used. |
| `eUnitProperty` | Unit.CodeEnumProperties | The microchips that are returned all share this property. |
| `nOffset` | Integer | The starting index of the returned table. |
| `nCount` | Integer | The number of entries in the table that is returned by the function.  This value defaults to 1 if none is passed in. |
| `nPowerCoreId` | Integer | The item id of the power core that is slotted for the recipe.  This will affect the microchips that are returned.  If no value is passed in, it defaults to 0. |

**Returns** — `Item` A table that contains a list of microchips that are available for the schematic.

### `GetAvailablePowerCores(idSchematic)`

Gets a list of power cores that can be used with the specified schematic.

| parameter | type | meaning |
|---|---|---|
| `idSchematic` | Integer | The function will return a list of power cores that are compatable with the schematic with this id. |

**Returns** — `Item` A table that contains the item information for power cores that can be used for the specified schematic.

### `GetAvailableProperties()`

Gets details of of all craftable properties. During a crafting session then this will include the properties that the player has learned.

**Returns** — `Table` An array of tables representing each group of properties.

### `GetCurrentCraft()`

If the player has an unfinished crafting attempt, this function will return information on that craft.

**Returns** — `Table` A table that contains information on the player's last crafting attempt.  The variables in the table will differ based on what type of schematic the player was attempting to craft.

### `GetCurrentOverchargeInfo(arMicrochipIds, arThresholds)`

`deprecated flag set` Gets information on the current overcharge and various overcharge limits of the current Circuit Board schematic.

| parameter | type | meaning |
|---|---|---|
| `arMicrochipIds` | Integer | An array that contains the item ids of each microchip set in the schematic. |
| `arThresholds` | Integer | An array that contains the thresholds used for each microchip slot. |

**Returns** — `Table` A table that contains information on all things overcharge related to the current schematic.

### `GetEngravingInfo(itemSource)`

Gets information about adding, clearing, rerolling, and unlocking Rune Slots in an item.

| parameter | type | meaning |
|---|---|---|
| `itemSource` | Item | The item that the function will query for information on its Rune Slots. |

**Returns** — `Table` A table that contains information on the requirements to modify an item's Rune Slots.

### `GetItemsWithRuneSlots(bIncludeEquipped, bIncludeBags)`

Gets a list of each item with rune slots that the player owns.

| parameter | type | meaning |
|---|---|---|
| `bIncludeEquipped` | Boolean | Whether items that the player has equipped should be included in the list or not. |
| `bIncludeBags` | Boolean | Whether items that are in the player's bags should be included in the list or not. |

**Returns** — `Item` An array of items that have rune slots and are in the specified locations.

### `GetItemsWithRuneSlots()`

`deprecated flag set` *no description in the client's documentation*

### `GetKnownTradeskills()`

Gets the id numbers and names of the tradeskills known by the character.

**Returns** — `Table` The names and id numbers of tradeskills that are active for the character.

### `GetModSchematicInfo(itemCrafting)`

`deprecated flag set` Gets information on the item's schematic and microchip sockets.

| parameter | type | meaning |
|---|---|---|
| `itemCrafting` | Item | The item that the player is trying to craft. |

**Returns** — `Table` 

> Carbine's own note: Pretty sure this is depricated...

### `GetPreviewInfo(nSchematicId, tCrafting)`

Gets information to draw a preview of the item that will be created by the specified schematic.

| parameter | type | meaning |
|---|---|---|
| `nSchematicId` | Integer | The id number for the schematic that we want to preview. |
| `tCrafting` | Table | The parameters representing the player's chooses while crafting. |

**Returns** — `Item` The expected resulting item based on the provided parameters.  If nSchematicId is also the current crafting schematic then the this result be more complete.

### `GetPropertyChipType()`

`deprecated flag set` *no description in the client's documentation*

> Carbine's own note: This doesn't appear to be called anywhere in our addons.  Probably depricated.

### `GetRelearnCooldown()`

Gets the amount of time (in milliseconds) before the player can swap their tradeskills.

**Returns** — `Integer` The amount of time (in milliseconds) before the player can swap their tradeskills again.

> Carbine's own note: May be depricated.

### `GetRelearnCost(eTradeskillId)`

The amount of currency the player will have to spend to swap one of their tradeskills with another.

| parameter | type | meaning |
|---|---|---|
| `eTradeskillId` | CraftingLib.CodeEnumTradeskill | The id of the tradeskill that the player wants to learn. |

**Returns** — `Money` The price to swap tradeskills.

### `GetRuneSetSchematicFilters()`

*no description in the client's documentation*

### `GetRuneSetSchematicList()`

*no description in the client's documentation*

### `GetRuneSets()`

*no description in the client's documentation*

### `GetRunecraftingLevels()`

*no description in the client's documentation*

### `GetRunecraftingPropertyIds()`

*no description in the client's documentation*

### `GetRunecraftingSchematicFilters()`

*no description in the client's documentation*

### `GetRunecraftingSchematicList()`

*no description in the client's documentation*

### `GetSchematicCraftableCount(idSchematic)`

`deprecated flag set` Gets the number of times a specified schematic can be crafted based on the items in the player's inventory, supply satchel, and bank.

| parameter | type | meaning |
|---|---|---|
| `idSchematic` | Integer | The id number of the schematic. |

**Returns** — `Integer` The number of times the schematic can be created based on the items in the player's inventory, supply satchel, and bank.

### `GetSchematicInfo(idSchematic)`

Gets information on a specific schematic.

| parameter | type | meaning |
|---|---|---|
| `idSchematic` | Integer | The id number of the schematic that the function will look at. |

**Returns** — `Table` A table containing detailed information on the specified schematic, including information on any sub-schematics the schematic may have.

### `GetSchematicList(eTradeskillId, nItemCategory, eTier, bShowUnknown)`

Gets a list of schematics that meet the requirements that are passed into this function.

| parameter | type | meaning |
|---|---|---|
| `eTradeskillId` | CraftingLib.CodeEnumTradeskill | The function will return the schematics that the player knows for this tradeskill. |
| `nItemCategory` | Integer | The function will only return schematics that create items that fall under this category. |
| `eTier` | CraftingLib.CodeEnumTradeskillTier | The function will return schematics that belong to this tradeskill tier. |
| `bShowUnknown` | Boolean | Whether the function should return schematics that the player has not unlocked or not. |

**Returns** — `Table` An array that contains info on each of the schematics that meet the requirements passed into the function.

> Carbine's own note: We could really use an enum for item categories.

### `GetTierForAchievementCategory(idCategory)`

Gets the tradeskill tier that matches the achievement category that is passed in.

| parameter | type | meaning |
|---|---|---|
| `idCategory` | Integer | The id for the achievement category that the function will match to a tradeskill tier. |

**Returns** — `CraftingLib.CodeEnumTradeskillTier` The tier that corresponds with the achievement category that was passed in.

### `GetTradeskillInfo(eTradeskillId)`

Returns a table with info about the chosen tradeskill

| parameter | type | meaning |
|---|---|---|
| `eTradeskillId` | CraftingLib.CodeEnumTradeskill | The id for the tradeskill that the function will return info on. |

**Returns** — `Table` Detailed information on the tradeskill, including its description, XP requirements, requirements to relearn, and talents.

> Carbine's own note: tTalentTiers needs some format work.

### `GetTradeskillTalentRespecCost(eTradeskillId)`

Gets the amount and type of currency needed to reset the tradeskill's talents.

| parameter | type | meaning |
|---|---|---|
| `eTradeskillId` | CraftingLib.CodeEnumTradeskill | The function will check the talent respec cost for this tradeskill. |

**Returns** — `Money` The type and amount of currency needed to reset the tradeskill's talents.

### `GetTradeskillTalents(eTradeskillId, bDebugPrint)`

Gets a list of all the talents for a particular tradeskill.

| parameter | type | meaning |
|---|---|---|
| `eTradeskillId` | CraftingLib.CodeEnumTradeskill | The function will get the talents for the tradeskill with this ID. |
| `bDebugPrint` | Boolean | If this is set to true, then the player will see debug information in their chat log. |

**Returns** — `Table` Information on each of the talent tiers for the tradeskill that was passed in to this function.

### `GetTradeskillTierXp(eTradeskillId, eTradeskillTier)`

Gets the amount of XP required to reach a specific tradeskill tier.

| parameter | type | meaning |
|---|---|---|
| `eTradeskillId` | CraftingLib.CodeEnumTradeskill | The id number of the Tradeskill that this function query. |
| `eTradeskillTier` | CraftingLib.CodeEnumTradeskillTier | The function will return the XP amount required to reach this tier. |

**Returns** — `Integer` The amount of XP required to reach the tradeskill / tier combination that was passed into the function.

### `GetUniversalSchematicsOwned()`

*no description in the client's documentation*

### `GetValidRuneItems(itemSelected, nSlot)`

Gets a list of all of the valid runes for a specific rune slot.  This list filters based on slot type and removes duplicate runes.

| parameter | type | meaning |
|---|---|---|
| `itemSelected` | Item | The function will return the valid runes for this item. |
| `nSlot` | Integer | The function will return all of the valid runes for the rune slot at this index. |

**Returns** — `Item` An array of runes that can be set to the specified rune slot.

### `GetValidSocketItems(idSchematic, nSocketIdx)`

`deprecated flag set` Gets a list of microchips that are valid for a specific socket in a schematic.

| parameter | type | meaning |
|---|---|---|
| `idSchematic` | Integer | The function will use the schematic with this id, in combination with the socket index, to get the list of valid items that can be added to the socket. |
| `nSocketIdx` | Integer | The function will get a list of items that can be added to this socket. |

**Returns** — `Table` A table that contains an array with every microchip in it.

> Carbine's own note: This very well may be depricated and replaced by CraftingLib.GetAvailableMicrochips

### `InstallRuneIntoSlot(itemSource, tInstalledRunes)`

Attempts to update the runes that should be installed on an item.

| parameter | type | meaning |
|---|---|---|
| `itemSource` | Item | The item that the rune will be installed in. |
| `tInstalledRunes` | Integer | An array of item ids for runes that should be installed on the item after the operation is complete. |

### `IsAtCraftingStation()`

Checks if the player is within range of a crafting station.

**Returns** — `Boolean` Determines whether the player is within range of a crafting station or not.

### `IsAtEngravingStation()`

*no description in the client's documentation*

### `IsAtMasterCraftsman()`

*no description in the client's documentation*

### `LearnTradeskill(eTradeskillId, eDroppedTradeskillId)`

Grants the character the chosen tradeskill.  If the character is already at the maximum number of tradeskills allowed, this function also drops a chosen tradeskill.

| parameter | type | meaning |
|---|---|---|
| `eTradeskillId` | CraftingLib.CodeEnumTradeskill | The id of the Tradeskill that the player will learn. |
| `eDroppedTradeskillId` | CraftingLib.CodeEnumTradeskill | The id of the tradeskill that the player wants to drop in order to learn the new one. |

### `PickTradeskillTalent(eTradeskillId, nTalentTier, idTalent)`

Attempts to activate the specified talent.

| parameter | type | meaning |
|---|---|---|
| `eTradeskillId` | CraftingLib.CodeEnumTradeskill | The id of the tradeskill that the talent belongs to. |
| `nTalentTier` | Integer | The talent tier that the talent belongs to. |
| `idTalent` | Integer | The id number for the talent that was chosen. |

### `RerollRuneSlot(itemSource, nSlotIdx)`

`deprecated flag set` Attempts to change a rune slot to a different type.

| parameter | type | meaning |
|---|---|---|
| `itemSource` | Item | The item that contains the rune slot that the function will attempt to reroll. |
| `nSlotIdx` | Integer | The index of the rune slot that the function will attempt to reroll. |

### `ResetTradeskillTalents(eTradeskillId)`

Attempts to reset the talents that are set for the specified tradeskill.

| parameter | type | meaning |
|---|---|---|
| `eTradeskillId` | CraftingLib.CodeEnumTradeskill | The function will attempt to reset the talents of the tradeskill with this id. |

### `ShowTradeskillTutorial()`

Starts up the tutorial for tradeskills if tutorials are not disabled and the tutorial is not flagged as "seen".

### `UnlockRuneSlot(itemSource, nSlotIdx)`

`deprecated flag set` Attempts to unlock a rune slot on an item.

| parameter | type | meaning |
|---|---|---|
| `itemSource` | Item | The function will attempt to unlock a rune slot that belongs to this item. |
| `nSlotIdx` | Integer | The index of the rune slot that the function will attempt to unlock. |

### `ValidateSocketItem(idSchematic, nSocketIdx, idInventory)`

`deprecated flag set` *no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `idSchematic` | Integer | The id for the schematic that the socket belongs to. |
| `nSocketIdx` | Integer | The index of the socket that the function will validate. |
| `idInventory` | Integer | The id number for the inventory slot that this item is in. |

> Carbine's own note: Probably depricated.  We aren't using it anywhere.  I also don't think this is returning anything.

### `kfCoordinateBonusLoyaltyRadius()`

`deprecated flag set` *no description in the client's documentation*

