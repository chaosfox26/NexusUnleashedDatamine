# TreeControl

*Window control, documented by the client itself.*

**26 calls.**

### `AddNode(hParentHandle, strText, strImage, newLuaData)`

Adds a node to the caller. If newLuaData is set, this will push it on the stack and ref it as well. Does a lua_pushinteger of the node's handle back on the stack as an integer.

| parameter | type | meaning |
|---|---|---|
| `hParentHandle` | Handle |  |
| `strText` | String |  |
| `strImage` | String |  |
| `newLuaData` | LuaData |  |

### `CollapseNode(hNodeHandle)`

Collapses the node in the caller corresponding to hNodeHandle.

| parameter | type | meaning |
|---|---|---|
| `hNodeHandle` | Handle |  |

### `DeleteAll()`

Deletes all of the caller's nodes.

### `DeleteChildren(hNodeHandle)`

Deletes the children of the node corresponding to hNodeHandle.

| parameter | type | meaning |
|---|---|---|
| `hNodeHandle` | Handle |  |

### `DeleteNode(hNodeHandle)`

Deletes the node corresponding to hNodeHandle.

| parameter | type | meaning |
|---|---|---|
| `hNodeHandle` | Handle |  |

### `ExpandNode(hNodeHandle)`

Expands the node corresponding to hNodeHandle.

| parameter | type | meaning |
|---|---|---|
| `hNodeHandle` | Handle |  |

### `GetColumnWidth()`

*no description in the client's documentation*

### `GetFirstChildNode(hNodeHandle)`

Does a lua_pushinteger of the first child node's ID as an integer corresponding to hNodeHandle.

| parameter | type | meaning |
|---|---|---|
| `hNodeHandle` | Handle |  |

### `GetFirstVisibleNode(hNodeHandle)`

Does a lua_pushinteger of the first visible node's ID as an integer corresponding to hNodeHandle.

| parameter | type | meaning |
|---|---|---|
| `hNodeHandle` | Handle |  |

### `GetNextSibling(hNodeHandle)`

Does a lua_pushinteger of the next sibling node's ID as an integer corresponding to hNodeHandle.

| parameter | type | meaning |
|---|---|---|
| `hNodeHandle` | Handle |  |

### `GetNextVisibleNode(hNodeHandle)`

Does a lua_pushinteger of the next visible node's ID as an integer corresponding to hNodeHandle.

| parameter | type | meaning |
|---|---|---|
| `hNodeHandle` | Handle |  |

### `GetNodeData(hNodeHandle)`

Does a lua_rawgeti of the node's data corresponding to hNodeHandle.

| parameter | type | meaning |
|---|---|---|
| `hNodeHandle` | Handle |  |

### `GetNodeText(hNodeHandle)`

Does a lua_pushstring of the node's text corresponding to hNodeHandle.

| parameter | type | meaning |
|---|---|---|
| `hNodeHandle` | Handle |  |

### `GetParentNode(hNodeHandle)`

Does a lua_pushinteger of the parent node's ID as an integer corresponding to hNodeHandle.

| parameter | type | meaning |
|---|---|---|
| `hNodeHandle` | Handle |  |

### `GetSelectedNode()`

Does a lua_pushinteger of the node's ID of the selected node.

### `HitTest(nXpos, nYpos)`

Does a lua_pushinteger of the node's ID at iXpos and iYpos as an integer. Does a lua_pushboolean of the test's result if a button was hit as a boolean.

| parameter | type | meaning |
|---|---|---|
| `nXpos` | Integer |  |
| `nYpos` | Integer |  |

### `NodeHasChildren()`

Does a lua_pushboolean of the node's HasChildren corresponding to hNodeHandle. Paramaters: hNodeHandle: Integer

### `SelectNode(hNodeHandle)`

Selects the node corresponding to hNodeHandle.

| parameter | type | meaning |
|---|---|---|
| `hNodeHandle` | Handle |  |

### `SetColumnWidth(nCol, nWidth)`

Sets the caller's nWidth of the column corresponding to iCol.

| parameter | type | meaning |
|---|---|---|
| `nCol` | Integer |  |
| `nWidth` | Integer |  |

### `SetHeaderImage()`

*no description in the client's documentation*

### `SetHeaderText()`

*no description in the client's documentation*

### `SetHeaderTextColor()`

*no description in the client's documentation*

### `SetMinimumNodeHeight(hNodeHandle, nMinHeight)`

Sets the MinimumNodeHeight to iMinHeight of the node corresponding to hNodeHandle.

| parameter | type | meaning |
|---|---|---|
| `hNodeHandle` | Handle |  |
| `nMinHeight` | Handle |  |

### `SetNodeImage(hNodeHandle, strText)`

Sets the Image to sText of the node corresponding to hNodeHandle.

| parameter | type | meaning |
|---|---|---|
| `hNodeHandle` | Handle |  |
| `strText` | String |  |

### `SetNodeText(hNodeHandle, strText)`

Sets the Text to sText of the node corresponding to hNodeHandle.

| parameter | type | meaning |
|---|---|---|
| `hNodeHandle` | Handle |  |
| `strText` | String |  |

### `SetNodeTextColor(hNodeHandle, clr)`

Sets the color to clr of the node corresponding to hNodeHandle.

| parameter | type | meaning |
|---|---|---|
| `hNodeHandle` | Handle |  |
| `clr` | CColor |  |

