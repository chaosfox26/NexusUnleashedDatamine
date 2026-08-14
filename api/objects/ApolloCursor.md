# ApolloCursor

*Object, documented by the client itself.*

ApolloCursors are the sprites that are used on the cursor in different situations.

**4 calls.** 1 carry `Deprecated="true"` — reported, not filtered, because that flag is set on entries known to be alive in 16042.

### `GetCursor(strCursorName)`

Returns the ApolloCursor with the specified name.

| parameter | type | meaning |
|---|---|---|
| `strCursorName` | String | The name of the cursor that should be returned. |

**Returns** — `ApolloCursor` The cursor that was requested.  If no cursor was found, this returns nil.

### `__gc()`

`deprecated flag set` The ApolloCursor's garbage collection function.  This will delete the ApolloCursor and free up the memory used for it.

> Carbine's own note: Is there ever a reason to explicitly call this?

### `is(oVariable)`

Determines if the variable is an ApolloCursor.

| parameter | type | meaning |
|---|---|---|
| `oVariable` | Variable | The variable that the function will check. |

**Returns** — `Boolean` Whether the variable is an ApolloCursor or not.

### `new()`

Creates a new ApolloCursor with no cursor set.

**Returns** — `ApolloCursor` A fresh, empty ApolloCursor.

