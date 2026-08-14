# MiniMapWindow

*Window control, documented by the client itself.*

**25 calls.**

### `AddLine()`

*no description in the client's documentation*

### `AddObject(eType, tLoc, strName, tInfo, tFlags, oUnit)`

Does a lua_pushinteger describing the result of the AddObject call.

| parameter | type | meaning |
|---|---|---|
| `eType` | Integer |  |
| `tLoc` | Table | Contains the x, y, and z coordinates for the object to be placed |
| `strName` | String | The name of the object |
| `tInfo` | MMODisplayInfo | Determines what the object will look like on the minimap |
| `tFlags` | Table | A set of flags determining how the object should be drawn |
| `oUnit` | Object | The game object that is tied to the object on the minimap |

### `AddPathIndicator()`

No implementation yet

### `AddQuestIndicator(pQuest, strNum, iInfo, tCheckFlag)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `pQuest` | LuaQuest |  |
| `strNum` | String |  |
| `iInfo` | MMODisplayInfo |  |
| `tCheckFlag` | Used immediate in a CheckFlag call |  |

### `AddUnit(pUnit, iInfo, tCheckFlag)`

Does a lua_pushinteger describing the result of the AddUnit call.

| parameter | type | meaning |
|---|---|---|
| `pUnit` | CUnit |  |
| `iInfo` | MMODisplayInfo |  |
| `tCheckFlag` | Table | Used immediately in a CheckFlag call |

### `ClientPointToWorldLoc(nPointX, nPointY)`

Does a lua_newtable with x, y, and z.

| parameter | type | meaning |
|---|---|---|
| `nPointX` | Integer |  |
| `nPointY` | Integer |  |

### `CreateOverlayType()`

*no description in the client's documentation*

### `GetLineInfo()`

*no description in the client's documentation*

### `GetObjectsAtPoint(nPointX, nPointY)`

Returns the results of PushObjectsAtPoint nPointX and nPointY.

| parameter | type | meaning |
|---|---|---|
| `nPointX` | Integer |  |
| `nPointY` | Integer |  |

### `GetZoomLevel()`

*no description in the client's documentation*

### `HideObjectsByType()`

*no description in the client's documentation*

### `HideObjectsByUserData()`

*no description in the client's documentation*

### `RemoveAllLines()`

*no description in the client's documentation*

### `RemoveAllObjects()`

*no description in the client's documentation*

### `RemoveLine()`

*no description in the client's documentation*

### `RemoveObject(nObjectId)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `nObjectId` | Integer |  |

### `RemoveObjectsByType()`

*no description in the client's documentation*

### `RemoveObjectsByUserData()`

*no description in the client's documentation*

### `RemoveUnit(pUnitHandle)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `pUnitHandle` | CUnitHandle |  |

### `SetMapOrientation(nOrient)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `nOrient` | EMiniMapOrientation |  |

### `SetZoomLevel()`

*no description in the client's documentation*

### `ShowObjectsByType()`

*no description in the client's documentation*

### `ShowObjectsByUserData()`

*no description in the client's documentation*

### `ZoomIn()`

Runs the caller's Zoom In method.

### `ZoomOut()`

Runs the caller's Zoom Out method.

