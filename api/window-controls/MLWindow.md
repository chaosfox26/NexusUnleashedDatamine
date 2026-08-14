# MLWindow

*Window control, documented by the client itself.*

**8 calls.**

### `BeginDoogie(fRate)`

Starts printing text character by character at a rate of fRate.

| parameter | type | meaning |
|---|---|---|
| `fRate` | Float |  |

### `GetContentSize()`

Does lua_pushintegers of the caller's size.x and size.y as integers.

### `IsReadyToDraw()`

Does a lua_pushboolean if there is a wait for load as a boolean.

### `PauseDoogie(bPauseDoogie)`

Pauses a character by character text printing animation if bPauseDoogie is true.

| parameter | type | meaning |
|---|---|---|
| `bPauseDoogie` | Bool |  |

### `SetAML(strAMLString)`

Sets the caller's m_doc's text to a UTF8ToUCS2 conversion of sAMLString.

| parameter | type | meaning |
|---|---|---|
| `strAMLString` | String |  |

### `SetDoc(pDoc)`

Sets the caller's m_doc's doc to pDoc and parses the doc.

| parameter | type | meaning |
|---|---|---|
| `pDoc` | XmlDocumentRef |  |

### `SetHeightToContentHeight(nBuffer)`

Sets the caller's height size to iBuffer. Does lua_pushintegers of the caller's size.x and size.y as integers.

| parameter | type | meaning |
|---|---|---|
| `nBuffer` | INT32 |  |

### `StopDoogie()`

Stops a character by character text printing animation.

