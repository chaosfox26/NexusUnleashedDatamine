# SliderBar

*Window control, documented by the client itself.*

**4 calls.**

### `GetValue()`

Does a lua_pushnumber of the caller's value as a float.

### `IsThumbDragging()`

*no description in the client's documentation*

### `SetMinMax(fMin, fMax, fTickAmount)`

Sets the caller's properties to fMin, fMax, and fTickAmount.

| parameter | type | meaning |
|---|---|---|
| `fMin` | Float |  |
| `fMax` | Float |  |
| `fTickAmount` | Float |  |

### `SetValue(fValue)`

Set the caller's value to fValue.

| parameter | type | meaning |
|---|---|---|
| `fValue` | Float |  |

