# ZoneMapWindow

*Window control, documented by the client itself.*

**76 calls.**

### `AddLine()`

*no description in the client's documentation*

### `AddObject(tWorldLoc, strName, tInfo, tFlags)`

works like MiniMapWindow:AddObject, returns an id to the object

| parameter | type | meaning |
|---|---|---|
| `tWorldLoc` | WorldLocTable | World location to add the object |
| `strName` | String | Name of the object |
| `tInfo` | Table |  |
| `tFlags` | Table |  |

### `AddObjectByWorldLocId()`

*no description in the client's documentation*

### `AddRegion()`

*no description in the client's documentation*

### `AddUnit(unitId, tInfo, tFlags)`

works like MiniMapWindow::AddUnit, returns an id to the object (which is different than the unitId)

| parameter | type | meaning |
|---|---|---|
| `unitId` | Integer |  |
| `tInfo` | Table |  |
| `tFlags` | Table |  |

**Returns** — `Integer` id to the object (which is different than the unitId)

### `CanZoomZone()`

*no description in the client's documentation*

### `CenterOnPlayer()`

*no description in the client's documentation*

### `CreateOverlayType()`

*no description in the client's documentation*

### `GetAllLines()`

*no description in the client's documentation*

### `GetAllNemesisRegionInfo()`

*no description in the client's documentation*

### `GetAllSubZoneInfo()`

*no description in the client's documentation*

### `GetAllZoneInfo()`

*no description in the client's documentation*

### `GetContinentInfo(strContinent)`

return information (including a list of zones) of the continent referred to by strContinent

| parameter | type | meaning |
|---|---|---|
| `strContinent` | String | The name of the continent |

**Returns** — `Table` 

### `GetContinentZoneInfo()`

*no description in the client's documentation*

### `GetContinents()`

return an array of continents

**Returns** — `String` 

### `GetCurrentContinentIndex()`

*no description in the client's documentation*

### `GetDisplayMode()`

return the current display mode (1=Panning, 2=Scaled, 3=Continent)

**Returns** — `EDisplayMode` 

### `GetHexAtPoint(x, y)`

return the location of the hex in the given a point in the Window

| parameter | type | meaning |
|---|---|---|
| `x` | Integer | X position in the window |
| `y` | Integer | Y position in the window |

**Returns** — `Table` x, y values for which hex is located at the specified point

### `GetHexGroupHexes()`

*no description in the client's documentation*

### `GetLevelBandRegionInfo()`

*no description in the client's documentation*

### `GetLineInfo()`

*no description in the client's documentation*

### `GetLinesAt()`

*no description in the client's documentation*

### `GetNecessaryHexCount()`

Does a lua_pushinteger of the caller's m_nCurrentNecessary.

### `GetNemesisRegionInfo()`

*no description in the client's documentation*

### `GetObjectRadius()`

*no description in the client's documentation*

### `GetObjectsAt(nPointX, nPointY)`

Returns the results of PushRegionsAt nPointX and nPointY.

| parameter | type | meaning |
|---|---|---|
| `nPointX` | Integer |  |
| `nPointY` | Integer |  |

### `GetRegionsAt()`

*no description in the client's documentation*

### `GetRevealedHexCount()`

Does a lua_pushinteger of the caller's m_nCurrentRevealed.

### `GetWorldLocAtPoint(x, y)`

return a table with x,y,z values for the world location at the point(x,y).  The y-component will be set to 0.0 and the z-component represents the North/South axis.

| parameter | type | meaning |
|---|---|---|
| `x` | Integer | X position of a point in the window |
| `y` | Integer | Y position of a point in the window |

**Returns** — `WorldLocTable` The world location in x,y, z. The y-component will be set to 0.0 and the z-component represents the North/South axis.

### `GetZoneInfo(nZone)`

Does a lua_newtable with the zone corresponding to nZone with its Name, Index, North, South, East, and West.

| parameter | type | meaning |
|---|---|---|
| `nZone` | Integer |  |

### `HideObjectsByType()`

*no description in the client's documentation*

### `HideObjectsByUserData()`

*no description in the client's documentation*

### `HideRegionsByType()`

*no description in the client's documentation*

### `HideRegionsByUserData()`

*no description in the client's documentation*

### `HighlightRegionsByType()`

*no description in the client's documentation*

### `HighlightRegionsByUserData()`

*no description in the client's documentation*

### `IsShowLabelsOn()`

Does a lua_pushboolean if labels are on.

### `IsShowPlayerOn()`

*no description in the client's documentation*

### `IsShowingGhostWindow()`

*no description in the client's documentation*

### `IsZoneReady()`

Does a lua_pushboolean if the caller's zone is ready.

### `RemoveAllLines()`

*no description in the client's documentation*

### `RemoveAllObjects()`

Runs the caller's RemoveAllRegionsByType method on MapOverlay_UserDefined.

### `RemoveAllRegions()`

*no description in the client's documentation*

### `RemoveLine()`

*no description in the client's documentation*

### `RemoveObject(idObject)`

will remove the object that matches the idObject (including a unit)

| parameter | type | meaning |
|---|---|---|
| `idObject` | Integer | ID of the object |

### `RemoveObjectsByType()`

*no description in the client's documentation*

### `RemoveObjectsByUserData()`

*no description in the client's documentation*

### `RemoveRegionByType()`

*no description in the client's documentation*

### `RemoveRegionByUserData()`

*no description in the client's documentation*

### `RemoveUnit(idUnit)`

remove the unit that matches the idUnit (could be redundant since you can store the idObject and use that to remove the unit)

| parameter | type | meaning |
|---|---|---|
| `idUnit` | Integer | ID of the unit to be removed |

### `SetActiveHexEdgeSprite()`

*no description in the client's documentation*

### `SetActiveHexSprite()`

*no description in the client's documentation*

### `SetDisplayMode(eMode)`

set the display mode to eMode (1=Panning, 2=Scaled, 3=Continent)

| parameter | type | meaning |
|---|---|---|
| `eMode` | EDisplayMode | The display mode to be changed to |

### `SetGhostWindow()`

*no description in the client's documentation*

### `SetInactiveHexEdgeSprite()`

*no description in the client's documentation*

### `SetInactiveHexSprite()`

*no description in the client's documentation*

### `SetLabelBackerSprite()`

*no description in the client's documentation*

### `SetLabelTextColor()`

*no description in the client's documentation*

### `SetLineColor()`

*no description in the client's documentation*

### `SetMaxDisplayMode()`

*no description in the client's documentation*

### `SetMinDisplayMode()`

*no description in the client's documentation*

### `SetObjectRadius()`

*no description in the client's documentation*

### `SetObjectsVisibility()`

*no description in the client's documentation*

### `SetOverlayTypeInfo()`

*no description in the client's documentation*

### `SetPlayerArrowSprite(strSpriteName)`

Sets the sprite used for representing the player on the map

| parameter | type | meaning |
|---|---|---|
| `strSpriteName` | String | The name of the sprite to be used |

### `SetZone(nZone)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `nZone` | Integer |  |

### `ShowLabels(bShowLabels)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `bShowLabels` | Boolean |  |

### `ShowLevelBandLabels()`

*no description in the client's documentation*

### `ShowObjectsByType()`

*no description in the client's documentation*

### `ShowObjectsByUserData()`

*no description in the client's documentation*

### `ShowPlayer()`

*no description in the client's documentation*

### `ShowRegionsByType()`

*no description in the client's documentation*

### `ShowRegionsByUserData()`

*no description in the client's documentation*

### `TogglePOIs()`

*no description in the client's documentation*

### `UnhighlightRegionsByType()`

*no description in the client's documentation*

### `UnhighlightRegionsByUserData()`

*no description in the client's documentation*

