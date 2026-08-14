# CColor

*Object, documented by the client itself.*

CColors are an older way of using colors in addons.  All colors are in ARGB format, with all values being between 0.0 and 1.0. While this functionality is not yet depricated, it may be in the future.  We highly recommend that developers use ApolloColors instead.

**14 calls.** 9 carry `Deprecated="true"` — reported, not filtered, because that flag is set on entries known to be alive in 16042.

### `Complement()`

Creates a new CColor that is complementary to the one that calls this function.

**Returns** — `CColor` A color that complements the one that called the function.

### `Complement(ccBaseColor)`

Returns a CColor that complements the color that is passed in.

| parameter | type | meaning |
|---|---|---|
| `ccBaseColor` | CColor | The color that the complement is made from. |

**Returns** — `CColor` A color that complements the one that was passed in.

### `Saturate()`

Locks the values in the color to values between 0.0 and 1.0.

**Returns** — `CColor` A new color that has been bound to values between 0.0 and 1.0.

### `__add(ccModifier)`

`deprecated flag set` Adds another CColor's values to the CColor that called this function.

| parameter | type | meaning |
|---|---|---|
| `ccModifier` | CColor | The CColor that the current CColor will be modified by. |

**Returns** — `CColor` The sum of the two CColors.

### `__div(fScale)`

`deprecated flag set` Scales each value in the CColor by the given amount.

| parameter | type | meaning |
|---|---|---|
| `fScale` | Float | The amount that each value in the CColor will be scaled by. |

**Returns** — `CColor` The modified CColor.

### `__eq(ccCompare)`

`deprecated flag set` Checks if a CColor matches this CColor.

| parameter | type | meaning |
|---|---|---|
| `ccCompare` | CColor | The CColor that is being compared to the one that called the function. |

**Returns** — `Boolean` Whether the two CColors matched or not.

### `__index(strIndex)`

`deprecated flag set` Gets the CColor's value for one of its primary colors or alpha.

| parameter | type | meaning |
|---|---|---|
| `strIndex` | String | The index of the value that the function will return.  This can be: "r" = red value "b" = blue value "g" = green value "a" = alpha value |

### `__mul(fScale, ccMultiplier)`

`deprecated flag set` Scales the values in the CColor by the value passed in.

| parameter | type | meaning |
|---|---|---|
| `fScale` | Float | The amount that each value in the CColor will be scaled by.  Only a float or CColor needs to be passed in. |
| `ccMultiplier` | CColor | The CColor that the source color is multiplied by.  Each value is multiplied by the corresponding value, so red x red, blue x blue, etc.  Only a float or CColor should be passed in to the function, not both. |

**Returns** — `CColor` The result of multiplying the original CColor with the value that was passed in.

### `__newindex(strIndex, fValue)`

`deprecated flag set` Sets one of the CColor's color values.

| parameter | type | meaning |
|---|---|---|
| `strIndex` | String | The color value that the function will update. "r" = red "g" = green "b" = blue "a" = alpha |
| `fValue` | Float | The color's new value. |

**Returns** — `String` An error string is sent if an invalid index is used.  Otherwise, this function has no return value.

### `__sub(ccSubtractor)`

`deprecated flag set` Subtracts a CColor's values from the CColor that called the function.

| parameter | type | meaning |
|---|---|---|
| `ccSubtractor` | CColor | The color values of the CColor that called the function are subtracted by this CColor's color values. |

**Returns** — `CColor` The CColor made up of the difference of the two CColors.

### `__tostring()`

`deprecated flag set` Converts a CColor to a string with the CColor's values

**Returns** — `String` A string with the CColor's values.  The string's format is "CColor(alpha,red,green,blue)

### `__unm()`

`deprecated flag set` Multiplies each of the CColor's color values by -1.

**Returns** — `CColor` The new CColor created by the function.

### `is(oVariable)`

Detects whether a variable is a CColor or not.

| parameter | type | meaning |
|---|---|---|
| `oVariable` | Variable | The variable that the function will check. |

**Returns** — `Boolean` Whether the variable is a CColor or not.

### `new(r, g, b, a)`

Creates a new CColor using the specified values.

| parameter | type | meaning |
|---|---|---|
| `r` | Float | The red value of the color. |
| `g` | Float | The green value of the color. |
| `b` | Float | The blue value of the color. |
| `a` | Float | The alpha value of the color.  This value defaults to 1.0 if no alpha value is passed in. |

**Returns** — `CColor` A CColor with the rgba values that were passed in.

