# Spinner

*Window control, documented by the client itself.*

**6 calls.**

### `GetMax()`

*no description in the client's documentation*

### `GetMin()`

*no description in the client's documentation*

### `GetValue()`

Does a lua_pushnumber of the caller's value as a float.

### `SetIncRates(tThresholdsAndRates)`

Sets the caller's rates to the entries in tThresholdsAndRates.

| parameter | type | meaning |
|---|---|---|
| `tThresholdsAndRates` | Table |  |

### `SetMinMax(fMin, fMax, nNumDecimals)`

Sets the caller's properties to fMin, fMax, and iNumDecimals.

| parameter | type | meaning |
|---|---|---|
| `fMin` | Float |  |
| `fMax` | Float |  |
| `nNumDecimals` | Integer |  |

### `SetValue(fValue)`

Sets the caller's value to fValue.

| parameter | type | meaning |
|---|---|---|
| `fValue` | Float |  |

