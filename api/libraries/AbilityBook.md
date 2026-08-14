# AbilityBook

*Library, documented by the client itself.*

A library that contains a large number of functions that are centered around the Limited Action Set.

**24 calls.** 1 carry `Deprecated="true"` — reported, not filtered, because that flag is set on entries known to be alive in 16042.

### `ActivateSpell(idSpell, bActive)`

Sets the spell's activated state.  Spells are considered activated when they are able to be added to the player's limited action set.

| parameter | type | meaning |
|---|---|---|
| `idSpell` | Integer | The id for the ability being activated |
| `bActive` | Boolean | Whether the spell should be made active or inactive. |

**Returns** — `Boolean` Returns a boolean stating whether or not the spell was successfully activated.

### `ClearCachedEldanAugmentationSpec()`

Removes any changes that were made to players AMPs but were not saved.

### `ClearCachedLASUpdates()`

Clears any unsaved changes to the player's limited action set.

### `CommitEldanAugmentationSpec()`

Submits the currently selected AMPs so they are saved to the player's current spec.

### `GetAbilitiesList(eSpellType)`

Returns a table with information on each of the character's abilities.

| parameter | type | meaning |
|---|---|---|
| `eSpellType` | Spell.CodeEnumSpellTag | A number representing the spell's type.  Non-Combat abilities have either the Mount, Misc, or Path tags. |

**Returns** — `Table` An array of tables that contain information on each spell that the player has access to.

### `GetAbilityInfo(idSpell, eSpellType)`

Gives the UI  information on a specific spell.

| parameter | type | meaning |
|---|---|---|
| `idSpell` | Integer | The id number of the spell that is being queried. |
| `eSpellType` | Spell.CodeEnumSpellTag | The type of spell being queried.  This should match up with the type of spell that was used in the first argument. |

**Returns** — `Table` A table that contains information on the spell

### `GetAvailableLockedInPower()`

Gets the amount of unused AMP power the player has left in their current saved spec.  This value does not account for any changes that the player has made that have not been saved.

**Returns** — `Integer` The amount of unused AMP power in the current spec.

### `GetAvailablePower()`

Gets the amount of AMP power the player has left.  This value accounts for any changes that have not been saved.

**Returns** — `Integer` The number of AMP points the player has not spent.

### `GetCurrentSpec()`

Gets the number of the Action Set that the player is currently using.

**Returns** — `Integer` The number of the Action Set that the player is currently using.

### `GetEldanAugmentationData(nSpecIndex)`

Gets information for each AMP for the player's class.

| parameter | type | meaning |
|---|---|---|
| `nSpecIndex` | Integer | The index of the Action Set that the function should return the AMP data for.  If this value is not valid, the function will return False. |

**Returns** — `Table` The information for each category and each AMP.

> Carbine's own note: Why are we returning false in some cases?

### `GetEldanAugmentationResetData()`

*no description in the client's documentation*

**Returns** — `Table` 

> Carbine's own note: This is also returning false.  Unsure how we get this to return anything but false and 0.

### `GetEldanAugmentationRespecCost()`

Gets the cost to respec the character's AMPs, in copper.

**Returns** — `Integer` The number of credits required to reset the character's AMPs, in copper.

### `GetNumUnlockedSpecs()`

Gets the number of Action Sets the current player has unlocked.

**Returns** — `Integer` The number of Action Sets the player has unlocked.

### `GetSpellTierLevelRequirements()`

Gets the level requirememts for the player to learn each spell tier.

**Returns** — `Integer` The level the character has to be in order to unlock each tier of a spell.  Index 1 is the base spell, while 2 is Tier 1, etc.

### `GetTagsForSpell(idSpell)`

Gets the category that the spell belongs to.

| parameter | type | meaning |
|---|---|---|
| `idSpell` | Integer | The id number for the spell that is being checked. |

**Returns** — `String` An array of strings that contain the names of the categories that the spell belongs to.

### `GetTotalPower()`

Gets the total amount of AMP points availalble to the player.

**Returns** — `Integer` The total number of AMP points the player has.

### `IsLASChangeActive()`

Checks to make sure that the Change Spec ability is active.

**Returns** — `Boolean` Informs the UI whether the Limited Action Set can be chaged.

### `NextSpec()`

Cycles to the next Action Set available to the player.  If the player is already at their latest action set, it cycles to the first Action Set.

> Carbine's own note: This also has a case where it is returning false when it shouldnt.

### `PrevSpec()`

Cycles back to an earlier Action Set.  If the player is already at their first Action Set, it cycles to the last one.

### `RespecEldanAugmentations()`

Attempts to reset the player's AMPs for their current spec.

**Returns** — `Boolean` Whether the reset was successful or not.

### `SetCurrentSpec(nSpecNumber)`

Selects a specific Action Set for the player.

| parameter | type | meaning |
|---|---|---|
| `nSpecNumber` | Integer | The Action Set that the player will switch to. |

> Carbine's own note: We're returning false again when we don't return anything if it's successful...

### `UpdateEldanAugmentationSpec(nSpecIdx, nActivatedAmps, tUnlockedAmps)`

Saves the AMPs in the Action Set that the player has been working in.

| parameter | type | meaning |
|---|---|---|
| `nSpecIdx` | Integer | The Action Set number that is being updated. |
| `nActivatedAmps` | Integer | The number of activated AMPs in the Action Set. |
| `tUnlockedAmps` | Table | A table with a list of activated AMP ids, indexed by those ids. |

**Returns** — `Boolean` Whether the operation was successful or not.

### `UpdateSpellTier(idBaseSpell, nTier)`

Sets the spell to the specified tier in the cached copy of the Action Set.  This is not the saved copy, so any changes that are not saved are not permenantly set.

| parameter | type | meaning |
|---|---|---|
| `idBaseSpell` | Integer | The id number for the base spell. |
| `nTier` | Integer | The tier that the spell is being set to. |

> Carbine's own note: Another one that returns false when it fails but nothing when it passes

### `ValidateEldanAugmentationSpec(nSpecIdx, nUnlockedAmps, tUnlockedAMPIds)`

`deprecated flag set` Checks to make sure that the specified action set is valid and ready to be updated.

| parameter | type | meaning |
|---|---|---|
| `nSpecIdx` | Integer | The Action Set that the function is trying to save. |
| `nUnlockedAmps` | Integer | The number of AMPS that the player has activated. |
| `tUnlockedAMPIds` | Table | A table that contains the id numbers of every AMP that the player has activated. |

**Returns** — `ActionSetLib.CodeEnumLimitedActionSetResult` The result of the operation

> Carbine's own note: Failed operations are often returning false instead of enum values

