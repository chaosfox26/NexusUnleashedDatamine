# CharacterTitle

*Object, documented by the client itself.*

These are the titles that the character can set for themselves.  These do not include guild tags.

**13 calls.** 2 carry `Deprecated="true"` — reported, not filtered, because that flag is set on entries known to be alive in 16042.

### `CanUseTitle()`

Determines whether or not the player can use the specified title.

**Returns** — `Boolean` Whether the player can use the title or not.

### `CannotRemove()`

Determines whether the player is able to remove this CharacterTitle.

**Returns** — `Boolean` Whether the player is able to remove this CharacterTitle or not

> Carbine's own note: There are currently no non-testing titles with this flag.  Is it still something that can be set?

### `GetAvailableTitles()`

Gets a list of all of the titles that the player has unlocked.

**Returns** — `CharacterTitle` An array of all of the titles that the player has unlocked.

> Carbine's own note: Not using LuaTables in code.

### `GetCategory()`

Gets the category that the CharacterTitle falls under.

**Returns** — `String` The CharacterTitle's category.

### `GetForUnit(unitChecked)`

Checks what a unit's name would look like with the CharacterTitle.

| parameter | type | meaning |
|---|---|---|
| `unitChecked` | Unit | The function will add the CharacterTitle to this unit's name. |

**Returns** — `String` The unit's name, if the CharacterTitle was applyed to it.

### `GetLifetime()`

Gets the amount of time, in milliseconds, that the title will be active before it is removed from the player.

**Returns** — `Integer` How long the title will remain active, in milliseconds.

> Carbine's own note: Why is this in milliseconds?  Is this a thing?

### `GetSpell()`

Gets the spell that is granted to the player while the title is active.

**Returns** — `Spell` The spell that is granted to the player while the title is active.

### `GetTitle()`

Gets the string that is added to the player's name while the title is active.

**Returns** — `String` The string that is added to the player's name when the title is active.

### `IsActiveTitle(titleChecked)`

Checks whether the a title is the one that the player has set as the active title.

| parameter | type | meaning |
|---|---|---|
| `titleChecked` | CharacterTitle | The function will check if this title is currently active. |

**Returns** — `Boolean` Whether the CharacterTitle is the active title.

### `SetTitle(titleActivated)`

Sends a request to the server to make a CharacterTitle the active title.

| parameter | type | meaning |
|---|---|---|
| `titleActivated` | CharacterTitle | The title that the function will make active. |

### `__eq(titleComparison)`

`deprecated flag set` Compares a CharacterTitle to the one that called this function to make sure that they are equal.

| parameter | type | meaning |
|---|---|---|
| `titleComparison` | CharacterTitle | The function will compare this CharacterTitle to the one that the function was called from. |

**Returns** — `Boolean` Whether the CharacterTitles were the same or not.

### `__gc()`

`deprecated flag set` CharacterTitle's garbage collection function.  This will delete the CharacterTitle from memory.

### `is(oVariable)`

Determines whether a variable is a CharacterTitle or not.

| parameter | type | meaning |
|---|---|---|
| `oVariable` | Variable | The variable that the function will check. |

**Returns** — `Boolean` Whether the variable is a CharacterTitle or not.

