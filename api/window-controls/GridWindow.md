# GridWindow

*Window control, documented by the client itself.*

**40 calls.**

### `AddCol()`

*no description in the client's documentation*

### `AddRow(strText, strImage, newLuaData)`

Adds a row to the caller. If newLuaData is set, this will push it on the stack and ref it as well.

| parameter | type | meaning |
|---|---|---|
| `strText` | String |  |
| `strImage` | String |  |
| `newLuaData` | LuaData |  |

### `DeleteAll()`

Deletes all rows and resets the count, current selection, the focus, and the tooltip.

### `DeleteAllRowsAndColumns()`

*no description in the client's documentation*

### `DeleteRow(nRow)`

Deletes the row at iRow if found and updates the caller's rowMax.

| parameter | type | meaning |
|---|---|---|
| `nRow` | UINT |  |

### `DeleteRowsByData(luaData)`

Deletes the row that lua_equals luaData if found and updates the caller's rowMax.

| parameter | type | meaning |
|---|---|---|
| `luaData` | LuaData |  |

### `EnableCell(nRow, nCol, newEnable)`

Sets the enable of the caller's cell at iRow and iCol to newEnable.

| parameter | type | meaning |
|---|---|---|
| `nRow` | Integer |  |
| `nCol` | Integer |  |
| `newEnable` | bool |  |

### `EnableRow(nRow, newEnable)`

Sets all enable of all the caller's cell at iRow to newEnable.

| parameter | type | meaning |
|---|---|---|
| `nRow` | Integer |  |
| `newEnable` | bool |  |

### `EnsureCellVisible(nRow, nCol)`

Insures the right, left, bottom, and top of the caller's cell at iRow and iCol are visible in the clip area. Updates the HScrollPos and VScrollPos.

| parameter | type | meaning |
|---|---|---|
| `nRow` | Integer |  |
| `nCol` | Integer |  |

### `GetCellData()`

*no description in the client's documentation*

### `GetCellLuaData()`

*no description in the client's documentation*

### `GetCellText()`

*no description in the client's documentation*

### `GetColumnCount()`

Does a lua_pushinteger of the caller's column count as an integer.

### `GetColumnWidth()`

*no description in the client's documentation*

### `GetCurrentColumn()`

Does a lua_pushinteger of the caller's current column as an integer, will do a lua_pushnil if the current column is -1.

### `GetCurrentRow()`

Does a lua_pushinteger of the caller's current row as an integer, will do a lua_pushnil if the current row is -1.

### `GetFocusColumn()`

Does a lua_pushinteger of the caller's focus column as an integer, will do a lua_pushnil if the focus column is -1.

### `GetFocusRow()`

Does a lua_pushinteger of the caller's focus row as an integer, will do a lua_pushnil if the focus row is -1.

### `GetRowCount()`

Does a lua_pushinteger of the caller's row count as an integer.

### `GetSortColumn()`

*no description in the client's documentation*

### `HitTest(ptX, ptY)`

Determines if ptX and ptY are a validCell of the caller and determines the iRow and iCol if possible.

| parameter | type | meaning |
|---|---|---|
| `ptX` | Integer |  |
| `ptY` | Integer |  |

### `IsCellSelected(nRow, nCol)`

Does a lua_pushboolean if the caller's cell at iRow and iCol is selected.

| parameter | type | meaning |
|---|---|---|
| `nRow` | Integer |  |
| `nCol` | Integer |  |

### `IsSortAscending()`

*no description in the client's documentation*

### `SelectCell(nRow, nCol)`

Selects the caller's cell at iRow and iCol.

| parameter | type | meaning |
|---|---|---|
| `nRow` | Integer |  |
| `nCol` | Integer |  |

### `SelectCellByData(bEqual, bFireEvent)`

Scans through the caller's cells trying to match bEqual. If a match is found and bFireEvent is true, the cell is selected.

| parameter | type | meaning |
|---|---|---|
| `bEqual` | bool |  |
| `bFireEvent` | bool |  |

### `SetCellBGBase()`

*no description in the client's documentation*

### `SetCellData(nRow, nCol, strText, strImage, newLuaData)`

Sets the data at the caller's cell at iRow and iCol to sText, sImage, and luaData. If newLuaData is set, this will push it on the stack and ref it as well.

| parameter | type | meaning |
|---|---|---|
| `nRow` | Integer |  |
| `nCol` | Integer |  |
| `strText` | String |  |
| `strImage` | String |  |
| `newLuaData` | LuaData |  |

### `SetCellDoc(nRow, nCol, strText)`

Loads an xml document into buffer at sText, then sets the caller's cell at iRow and iCol to the document, creating a new one if not allocated.

| parameter | type | meaning |
|---|---|---|
| `nRow` | Integer |  |
| `nCol` | Integer |  |
| `strText` | String |  |

### `SetCellIconOverlays(nRow, nCol, strLeft, strRight)`

Sets the icon overlay at the caller's cell at iRow and iCol to strLeft and strRight.

| parameter | type | meaning |
|---|---|---|
| `nRow` | Integer |  |
| `nCol` | Integer |  |
| `strLeft` | String |  |
| `strRight` | String |  |

### `SetCellImage(nRow, nCol, strImage)`

Sets the cellimage of the caller's cell at iRow and iCol to sImage.

| parameter | type | meaning |
|---|---|---|
| `nRow` | Integer |  |
| `nCol` | Integer |  |
| `strImage` | String |  |

### `SetCellImageColor()`

*no description in the client's documentation*

### `SetCellLuaData()`

*no description in the client's documentation*

### `SetCellSortText()`

*no description in the client's documentation*

### `SetCellText(nRow, nCol, strText)`

Sets the celltext of the caller's cell at iRow and iCol to sText.

| parameter | type | meaning |
|---|---|---|
| `nRow` | Integer |  |
| `nCol` | Integer |  |
| `strText` | String |  |

### `SetColumnText(nCol, strText)`

Sets the column text of the caller's cell at iCol to sText.

| parameter | type | meaning |
|---|---|---|
| `nCol` | Integer |  |
| `strText` | String |  |

### `SetColumnWidth()`

*no description in the client's documentation*

### `SetCurrentColumn(nCol)`

Sets the selection to caller's column at iCol.

| parameter | type | meaning |
|---|---|---|
| `nCol` | Integer |  |

### `SetCurrentRow(nRow)`

Sets the selection to caller's column at iRow.

| parameter | type | meaning |
|---|---|---|
| `nRow` | Integer |  |

### `SetHeaderBGBase()`

*no description in the client's documentation*

### `SetSortColumn()`

*no description in the client's documentation*

