# Button

*Window control, documented by the client itself.*

**14 calls.**

### `AttachWindow()`

*no description in the client's documentation*

### `ChangeArt(strButtonBase)`

Updates the art of the button. The art is updated if a button is passed. The button's string is also updated with the passed parameter.

| parameter | type | meaning |
|---|---|---|
| `strButtonBase` | Varies - String or Button |  |

### `GetContentId()`

Does a lua_pushinteger of the caller's content Id as an integer.

### `GetContentType()`

Does a lua_pushwstring of the caller's content type as a string.

### `IsChecked()`

Does a lua_pushboolean of the caller's IsChecked as a boolean.

### `SetCheck(bCheck)`

Sets the caller's check to bCheck.

| parameter | type | meaning |
|---|---|---|
| `bCheck` | Bool |  |

### `SetContentId(nContentId)`

Sets the caller's content id to uContentId.

| parameter | type | meaning |
|---|---|---|
| `nContentId` | Integer |  |

### `SetContentType(strContentType)`

Sets the caller's content type to sContentType.

| parameter | type | meaning |
|---|---|---|
| `strContentType` | String |  |

### `SetDisabledTextColor(clr)`

Sets the caller's m_crStateText in the BS_Disabled state to clr.

| parameter | type | meaning |
|---|---|---|
| `clr` | CColor |  |

### `SetFlybyTextColor(clr)`

Sets the caller's m_crStateText in the BS_Flyby state to clr.

| parameter | type | meaning |
|---|---|---|
| `clr` | CColor |  |

### `SetInnerMargin()`

*no description in the client's documentation*

### `SetNormalTextColor(clr)`

Sets the caller's m_crStateText in the BS_Normal state to clr.

| parameter | type | meaning |
|---|---|---|
| `clr` | CColor |  |

### `SetPressedFlybyTextColor(clr)`

Sets the caller's m_crStateText in the BS_PressedFlyby state to clr.

| parameter | type | meaning |
|---|---|---|
| `clr` | CColor |  |

### `SetPressedTextColor(clr)`

Sets the caller's m_crStateText in the BS_Pressed state to clr.

| parameter | type | meaning |
|---|---|---|
| `clr` | CColor |  |

