# ApolloColor

*Object, documented by the client itself.*

ApolloColors are the primary way that the UI uses colors.  There are a number predefined colors, which can be found under Virtual colors section of Houston's color chooser.  Addon developers can also create their own ApolloColors using a string with the color's ARGB values in hex format.

**9 calls.** 3 carry `Deprecated="true"` — reported, not filtered, because that flag is set on entries known to be alive in 16042.

### `IsLinked()`

Determines whether the ApolloColor is using a virtual color or not.

**Returns** — `Boolean` Whether the ApolloColor is set to a virtual color or a hardcoded value.

### `IsSameColorAs(crChecking)`

Checks if two ApolloColors share the same color.

| parameter | type | meaning |
|---|---|---|
| `crChecking` | ApolloColor | The ApolloColor that we are checking against. |

**Returns** — `Boolean` Whether the ApolloColors share the same color.

### `SetColor(strColorName, crUpdatedValues)`

Sets a named ApolloColor to the value of a CColor.

| parameter | type | meaning |
|---|---|---|
| `strColorName` | String | The name of the ApolloColor that is being updated. |
| `crUpdatedValues` | CColor | The CColor that the ApolloColor is being updated to. |

**Returns** — `Boolean` Whether the ApolloColor was successfully updated or not.

### `ToTable()`

Returns a table with the ApolloColor's RGBA values.

**Returns** — `Table` The color's RGBA values.

### `__eq(crChecking)`

`deprecated flag set` Checks if two ApolloColors are the same.

| parameter | type | meaning |
|---|---|---|
| `crChecking` | ApolloColor | The ApolloColor that the function will check against. |

**Returns** — `Boolean` Whether the two ApolloColors are equal or not.

> Carbine's own note: Is this necessary when we have the IsSameColorAs function?

### `__gc()`

`deprecated flag set` ApolloColor's garbage collection function.  This will delete the ApolloColor from memory.

> Carbine's own note: Do we ever want to explicitly call a garbage collection function in Lua?

### `__index(strIndex)`

`deprecated flag set` Returns the ApolloColor's value at the specified index.

| parameter | type | meaning |
|---|---|---|
| `strIndex` | String | The index of the value that should be returned.  This will either be "r" for the color's red value, "b" for the color's blue value, "g" for the color's green value, or "a" for the color's alpha value. |

**Returns** — `Float` The color value at the specified index.

> Carbine's own note: Is this necessary when we can convert it to a table?

### `is(oVariable)`

Validates that the variable passed in is an ApolloColor.

| parameter | type | meaning |
|---|---|---|
| `oVariable` | Variable | The variable that we are checking. |

**Returns** — `Boolean` Whether the variable is an ApolloColor or not.

### `new()`

Creates a new ApolloColor object.

> Carbine's own note: This is a pain to write simply because there are so many different options for what kinds of variables can be passed in.

