# ActionSetLib

*Library, documented by the client itself.*

This library contains functions for validating and saving the player's Limited Action Set.

**6 calls.** 3 carry `Deprecated="true"` — reported, not filtered, because that flag is set on entries known to be alive in 16042.

### `DoesActionSetMeetRequirements()`

`deprecated flag set` *no description in the client's documentation*

**Returns** — `ActionSetLib.CodeEnumLimitedActionSetResult` Either the reason that the Action Set is invalid, or OK if it is valid.

> Carbine's own note: Not quite sure what this is... We're checking categories to make sure that the Action Set Lib doesn't require certain types of abilities.

### `GetCurrentActionSet()`

Gets a list of the spell ids used in the player's current action set.

**Returns** — `Integer` A list of spell ids for the player's current action set.  If a slot has no spell assigned to it, the id is 0.

### `IsSlotUnlocked(nSlotIdx)`

Determines if the specified slot is unlocked for the player.

| parameter | type | meaning |
|---|---|---|
| `nSlotIdx` | Integer | The slot number that the function should check. |

**Returns** — `ActionSetLib.CodeEnumLimitedActionSetResult` This value will be Ok if the slot is unlocked or SlotUnlockPrereqFalse if it is locked.

### `IsSpellCompatibleWithActionSet(idSpell, arActionSet)`

`deprecated flag set` Checks to make sure that a spell is compatible with an action set.

| parameter | type | meaning |
|---|---|---|
| `idSpell` | Integer | The id number of the spell that the UI wants to place in the action set. |
| `arActionSet` | Integer | An array of spell ids in the current action set.  The array's index lines up with the slot with the same number. |

**Returns** — `ActionSetLib.CodeEnumLimitedActionSetResult` The result of the check.  If the spell is valid in the action set, the return value will be Ok.  Otherwise, this value will contain the error that would prevent the spell from being added to the action set.

### `IsSpellCompatibleWithSlot(idSpell, nSlotIdx)`

`deprecated flag set` Checks to make sure that a spell is compatible with the specified slot in the action bar.

| parameter | type | meaning |
|---|---|---|
| `idSpell` | Integer | The id number for the spell that the function is validating against the action bar slot. |
| `nSlotIdx` | Integer | The action bar slot that the function is checking the spell against. |

**Returns** — `ActionSetLib.CodeEnumLimitedActionSetResult` The result of the validation.  If the spell can be added to the slot, this value is Ok.  Otherwise, it contains the error that explains why the spell could not be added to the slot.

### `RequestActionSetChanges(arActionSet)`

Attempts to make changes to the current action set.

| parameter | type | meaning |
|---|---|---|
| `arActionSet` | Integer | An array of spell ids that represent the proposed action set.  The array's index lines up with the slot number in the action bar. |

**Returns** — `Table` A table that contains the result and other data that is relevant to the result.

