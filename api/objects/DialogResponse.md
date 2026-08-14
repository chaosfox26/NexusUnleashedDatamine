# DialogResponse

*Object, documented by the client itself.*

DialogResponses are the various options that the player can select when conversing with NPCs and turning in quests.

**8 calls.** 1 carry `Deprecated="true"` — reported, not filtered, because that flag is set on entries known to be alive in 16042.

### `GetQuestId()`

Gets the id of the quest associated with this dialog.

**Returns** — `Integer` The id number of the quest associated with this dialog response.

### `GetRewardId()`

Gets the id of the reward associated with this dialog response.

**Returns** — `Integer` The id number of the reward associated with this response.

### `GetText()`

Gets the text for this DialogResponse.

**Returns** — `String` The DialogResponse's text.

### `GetType()`

Gets the DialogResponse's type.

**Returns** — `Integer` The response's type.  This value corresponds with the DialogResponse.DialogResponseType enum.

### `GetUniqueId()`

Gets the dialog's unique id number.

**Returns** — `Integer` The dialog's unique id number.

### `Select()`

Tells the client that the player has chosen this DialogResponse

### `__gc()`

`deprecated flag set` Forces the garbage collector to be called on this variable.

### `is(oVariable)`

Determines whether a variable is a DialogResponse or not.

| parameter | type | meaning |
|---|---|---|
| `oVariable` | Variable | The object that the function will check. |

**Returns** — `Boolean` Whether the object is a dialog response or not.

