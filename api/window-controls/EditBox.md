# EditBox

*Window control, documented by the client itself.*

**19 calls.** 1 carry `Deprecated="true"` — reported, not filtered, because that flag is set on entries known to be alive in 16042.

### `AddHistoryString(strHistoryString)`

Adds to the caller's string list the parameter sHistoryString.

| parameter | type | meaning |
|---|---|---|
| `strHistoryString` | String |  |

### `AddLink()`

*no description in the client's documentation*

### `ClearHistoryStrings()`

Clears the caller's string list.

### `ClearText()`

Sets the caller's text to null then collapses and moves the caller's window rectangle.

### `CopyTextToClipboard()`

`deprecated flag set` Calls OnCopy() which copies the caller's text to clipboard.

### `GetAllLinks()`

*no description in the client's documentation*

### `GetHistoryStrings()`

Does a lua push of the caller's string list count number and string.

### `GetMaxTextLength()`

*no description in the client's documentation*

### `GetSel()`

*no description in the client's documentation*

### `GetText()`

Does a lua_pushwstring of the caller's m_pText as a string.

### `HitTest()`

*no description in the client's documentation*

### `InsertText()`

*no description in the client's documentation*

### `PasteTextFromClipboard()`

Calls OnPaste() which pastes the clipboard's contents into the caller's text.

### `RemoveLinks()`

*no description in the client's documentation*

### `SetMaxTextLength()`

*no description in the client's documentation*

### `SetPrompt()`

*no description in the client's documentation*

### `SetPromptColor()`

*no description in the client's documentation*

### `SetSel(nBegin, nEnd)`

Sets the caller's selection range starting with iBegin and ending with iEnd.

| parameter | type | meaning |
|---|---|---|
| `nBegin` | Integer |  |
| `nEnd` | Integer |  |

### `SetText(strText)`

Sets the caller's text to sText.

| parameter | type | meaning |
|---|---|---|
| `strText` | String |  |

