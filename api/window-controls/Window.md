# Window

*Window control, documented by the client itself.*

**153 calls.** 4 carry `Deprecated="true"` — reported, not filtered, because that flag is set on entries known to be alive in 16042.

### `AddEventHandler()`

*no description in the client's documentation*

### `AddPixie(iLayer, bLine, bRestart, strText, strFont, flagsText, fWidth, strSprite, fRotation, loc, cr, crText)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `iLayer` | Integer | The pixie layer that the picie should be created at |
| `bLine` | Boolean | Draws the pixie as a line |
| `bRestart` | Boolean |  |
| `strText` | String | The text to add to the pixie |
| `strFont` | String | The font to use for the pixie |
| `flagsText` | Table | The flags for the the text |
| `fWidth` | Float | The width of the pixie.  This is only used if the pixie is drawn as a line. |
| `strSprite` | String | The name of the sprite used for the pixie.  This is only used for pixies that aren't drawn as a line. |
| `fRotation` | Float | The number of degrees the pixie is rotated.  This is only used for pixies that are not drawn as a line. |
| `loc` | Table | The boundaries of the pixie.  This table contains the offsets and points for the boundary. |
| `cr` | CColor | The color of the pixie |
| `crText` | CColor | The color of the text in the pixie |

**Returns** — `Integer` The pixie's ID number

> Carbine's own note: Desperately needs coding standard fix

### `AddStyle(strStyle)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `strStyle` | String |  |

### `AddStyleEx(strStyle)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `strStyle` | String |  |

### `ArrangeChildrenHorz(nOrigin)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `nOrigin` | Integer |  |

### `ArrangeChildrenTiles(nOrigin)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `nOrigin` | Integer |  |

### `ArrangeChildrenVert(nOrigin)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `nOrigin` | Integer |  |

### `AttachAnim(strAnimDataId)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `strAnimDataId` | String |  |

### `BringChildToTop(wndChild)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `wndChild` | Window |  |

### `BringDescendantToTop(wndDescendant)`

Bring specified descendant window to top to ensure that it will be processed for window messages (e.g. mouse clicks) the earliest possible.

| parameter | type | meaning |
|---|---|---|
| `wndDescendant` | Window | A descendant window under the current window to be brought to the top for window message processing |

### `ClearFocus()`

Runs the caller's ClearFous method.

### `ClearInterrupt()`

*no description in the client's documentation*

### `ClientPointToWindowPoint(nPosX, nPosY)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `nPosX` | Integer |  |
| `nPosY` | Integer |  |

### `Close()`

Runs the caller's Close method.

### `Contains(nPosX, nPosY)`

Does a lua_pushboolean if the caller contains the point at iPosX and iPosY.

| parameter | type | meaning |
|---|---|---|
| `nPosX` | Integer |  |
| `nPosY` | Integer |  |

### `ContainsMouse()`

Does a lua_pushboolean if the caller contains the point at the current mouse location.

### `Destroy()`

Calls Destroy() on the caller.

### `DestroyAllPixies()`

*no description in the client's documentation*

### `DestroyChildren()`

Calls Destroy() on the caller's children.

### `DestroyPixie()`

*no description in the client's documentation*

### `DetachAnim()`

Runs the caller's release method on m_pAnimPlayer.

### `Enable(bEnable)`

Sets the caller's m_bEnabled boolean to bEnable.

| parameter | type | meaning |
|---|---|---|
| `bEnable` | Boolean |  |

### `EnsureChildVisible(wndChild)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `wndChild` | Window |  |

### `FindChild(strName)`

Returns the child of this window that has the specified name.

| parameter | type | meaning |
|---|---|---|
| `strName` | String | The name of the child window |

**Returns** — `Window` The child window with strName if found. Otherwise, this returns nil.

### `FindChildByUserData()`

*no description in the client's documentation*

### `GetAnchorOffsets()`

Does a lua_pushinteger of the Offset Anchor's Left, Top, Right, then Bottom.

### `GetAnchorPoints()`

Does a lua_pushnumber of the Anchor's Left, Top, Right, then Bottom.

### `GetAnimElapsedTime()`

Does a lua_pushnumber of the caller's ElapsedTime.

### `GetBGColor()`

Runs the caller's GetBGColor method in a CColor_new.

### `GetBGOpacity()`

*no description in the client's documentation*

### `GetChildren()`

*no description in the client's documentation*

### `GetClientRect()`

*no description in the client's documentation*

### `GetData()`

Does a lua_rawgeti on the caller's m_iLuaDataRefId.

### `GetFrame()`

*no description in the client's documentation*

### `GetGlobalRadioSel(strRadio)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `strRadio` | String |  |

### `GetGlobalRadioSelButton(strRadio)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `strRadio` | String |  |

### `GetHScrollPos()`

Does a lua_pushinteger of the caller's HScrollPos.

### `GetHScrollRange()`

Does a lua_pushinteger of the caller's m_sbHorz range.

### `GetHeight()`

Return the height of the window

**Returns** — `Integer` The height of the window in pixels

### `GetId()`

Does a lua_pushinteger on the caller's Id.

### `GetLocation()`

Returns a new WindowLocation specified by the current window location.

### `GetMouse()`

Does a lua_newtable with the x and y value of the mouse.

### `GetNCOpacity()`

*no description in the client's documentation*

### `GetName()`

Does a lua_pushwstring of the caller's name, sending "" if null.

### `GetOpacity()`

Does a lua.PushDouble of the caller's opacity.

### `GetOriginalLocation()`

*no description in the client's documentation*

### `GetParent()`

Returns the caller's parent, or does a lua_pushnil if null.

### `GetPixieInfo()`

*no description in the client's documentation*

### `GetPos()`

Does a lua_pushinteger of the caller's min x and min y.

### `GetRadioSel(strRadio)`

Does a lua_pushinteger of the radio selection corresponding to sRadio.

| parameter | type | meaning |
|---|---|---|
| `strRadio` | String |  |

### `GetRadioSelButton(strRadio)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `strRadio` | String |  |

### `GetRect()`

Get the rect of the window

### `GetRotation()`

Does a lua_pushnumber of the caller's rotation after a RadiansToDegrees.

### `GetScale()`

Does a lua_pushnumber of the caller's scale.

### `GetSizingMaximum()`

*no description in the client's documentation*

### `GetSizingMinimum()`

*no description in the client's documentation*

### `GetSprite()`

Does a lua_pushwstring of the SpriteInfo's name, or "" if it is null.

### `GetText()`

Does a lua_pushwstring of the caller's text.

### `GetTextColor()`

*no description in the client's documentation*

### `GetTransLocation()`

*no description in the client's documentation*

### `GetVScrollPos()`

Does a lua_pushinteger of the caller's VScrollPos.

### `GetVScrollRange()`

Does a lua_pushinteger of the caller's m_sbVert range.

### `GetWidth()`

Return the width of the window

**Returns** — `Integer` The width of the window in pixels

### `GetWindowSubclass()`

*no description in the client's documentation*

### `HasTooltip()`

*no description in the client's documentation*

### `HasTooltipSecondary()`

*no description in the client's documentation*

### `Invoke()`

*no description in the client's documentation*

### `IsAnimPlaying()`

Does a lua_pushboolean of the caller's IsPlaying boolean.

### `IsChildOfMouseTarget()`

*no description in the client's documentation*

### `IsEnabled()`

Does a lua_pushboolean of the caller's enable boolean.

### `IsMouseTarget()`

*no description in the client's documentation*

### `IsParentOfMouseTarget()`

*no description in the client's documentation*

### `IsShown()`

Does a lua_pushboolean of the caller's IsShown boolean.

### `IsStyleExOn()`

*no description in the client's documentation*

### `IsStyleOn()`

*no description in the client's documentation*

### `IsValid()`

*no description in the client's documentation*

### `IsVisible()`

Does a lua_pushboolean of the caller's IsVisible boolean.

### `LoadTooltipForm(strFile, strForm, tTable)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `strFile` | String |  |
| `strForm` | String |  |
| `tTable` | LuaTable | (Optional) |

### `LoadTooltipFormSecondary(strFile, strForm, tTable)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `strFile` | String |  |
| `strForm` | String |  |
| `tTable` | LuaTable | (Optional) |

### `Move(nLeft, nTop, nWidth, nHeight)`

Move and resize the window

| parameter | type | meaning |
|---|---|---|
| `nLeft` | Integer |  |
| `nTop` | Integer |  |
| `nWidth` | Integer |  |
| `nHeight` | Integer |  |

### `MoveMethod()`

`deprecated flag set` *no description in the client's documentation*

### `MoveToLoc()`

Should be deprecated

### `MoveToLocation(wndLoc)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `wndLoc` | WindowLocation |  |

### `PauseAnim()`

Runs the caller's pause method on m_pAnimPlayer.

### `PlayAnim(fDelay)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `fDelay` | Float |  |

### `RecalculateContentExtents()`

*no description in the client's documentation*

### `RemoveEventHandler()`

*no description in the client's documentation*

### `RemoveStyle(strStyle)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `strStyle` | String |  |

### `RemoveStyleEx(strStyle)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `strStyle` | String |  |

### `Reposition()`

Runs the caller's Reposition method.

### `ResetSubclass()`

*no description in the client's documentation*

### `RestartPixieSprite()`

*no description in the client's documentation*

### `SendChildToBottom()`

*no description in the client's documentation*

### `SetAnchorOffsets(nLeft, nTop, nRight, nBottom)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `nLeft` | Integer |  |
| `nTop` | Integer |  |
| `nRight` | Integer |  |
| `nBottom` | Integer |  |

### `SetAnchorPoints(nLeft, nTop, nRight, nBottom)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `nLeft` | Integer |  |
| `nTop` | Integer |  |
| `nRight` | Integer |  |
| `nBottom` | Integer |  |

### `SetAnimElapsedTime(fTime)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `fTime` | Float |  |

### `SetAnimPlaybackRate(fRate)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `fRate` | Float |  |

### `SetBGColor(clr)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `clr` | CColor |  |

### `SetBGOpacity()`

*no description in the client's documentation*

### `SetCanResize()`

*no description in the client's documentation*

### `SetClientSprite(wndB)`

Sets the caller's ClientSprite to wndB's ClientSprite.

| parameter | type | meaning |
|---|---|---|
| `wndB` | Window |  |

### `SetData(lData)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `lData` | LuaData |  |

### `SetFocus()`

Runs the caller's SetFocus method.

### `SetFont(strText)`

Sets the font by alias on the caller after running a UTF8ToUCS2 on strText.

| parameter | type | meaning |
|---|---|---|
| `strText` | String |  |

### `SetGlobalRadioSel(strRadio)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `strRadio` | String |  |

### `SetHScrollInfo(nRange, nPageSize, nIncrement)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `nRange` | Integer |  |
| `nPageSize` | Integer |  |
| `nIncrement` | Integer |  |

### `SetHScrollPos(nNewPos)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `nNewPos` | Integer |  |

### `SetInterrupt()`

*no description in the client's documentation*

### `SetLoaded(bLoaded)`

Sets the caller's m_bLoaded boolean to bLoaded.

| parameter | type | meaning |
|---|---|---|
| `bLoaded` | Boolean |  |

### `SetNCOpacity()`

*no description in the client's documentation*

### `SetName(strName)`

Sets the caller's name to sName.

| parameter | type | meaning |
|---|---|---|
| `strName` | String |  |

### `SetNamedAnchor(fPoint, nOffset, bOverwrite)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `fPoint` | Float |  |
| `nOffset` | Integer |  |
| `bOverwrite` | Boolean |  |

### `SetOpacity(fOpacity, fRate)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `fOpacity` | Float |  |
| `fRate` | Float |  |

### `SetRadioSel(strRadio, nSelection)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `strRadio` | String |  |
| `nSelection` | Integer |  |

### `SetRadioSelButton(strRadio, bButton)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `strRadio` | String |  |
| `bButton` | Button |  |

### `SetRotation(fNewRotation)`

Sets the caller's rotation to fNewRotation after a DegreesToRadians.

| parameter | type | meaning |
|---|---|---|
| `fNewRotation` | Float |  |

### `SetScale(fNewScale)`

Sets the caller's scale.

| parameter | type | meaning |
|---|---|---|
| `fNewScale` | Float |  |

### `SetSelfAnchor()`

*no description in the client's documentation*

### `SetSizingMaximum(nWidth, nHeight)`

Sets the caller's sizing maximum to iWidth and iHeight.

| parameter | type | meaning |
|---|---|---|
| `nWidth` | Integer |  |
| `nHeight` | Integer |  |

### `SetSizingMinimum(nWidth, nHeight)`

Sets the caller's sizing minimum to iWidth and iHeight.

| parameter | type | meaning |
|---|---|---|
| `nWidth` | Integer |  |
| `nHeight` | Integer |  |

### `SetSprite(strSprite)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `strSprite` | String |  |

### `SetSpriteProgress(fTime)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `fTime` | Float |  |

### `SetSpriteRate(fTime)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `fTime` | Float |  |

### `SetSpriteTargetDuration(fTime)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `fTime` | Float |  |

### `SetSpriteTime(fTime)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `fTime` | Float |  |

### `SetStyle(strText, bOn)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `strText` | String |  |
| `bOn` | Boolean | (Optional, Default to GetStyleBit on strText) |

### `SetStyleEx(strStyle)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `strStyle` | String |  |

### `SetText(strNewText)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `strNewText` | String |  |

### `SetTextColor(clr)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `clr` | CColor |  |

### `SetTextFlags(strText, bOn)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `strText` | String |  |
| `bOn` | Boolean | (Optional, Skipped if strText does not yields a StyleBit) |

### `SetTextRaw()`

*no description in the client's documentation*

### `SetTooltip(strTip)`

Sets the tooltip on the caller after running a UTF8ToUCS2 on strTip.

| parameter | type | meaning |
|---|---|---|
| `strTip` | String |  |

### `SetTooltipDoc(pXml)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `pXml` | XmlDocumentRef |  |

### `SetTooltipDocSecondary(pXml)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `pXml` | XmlDocumentRef |  |

### `SetTooltipForm()`

*no description in the client's documentation*

### `SetTooltipFormSecondary()`

*no description in the client's documentation*

### `SetTooltipToWindow(wndB)`

Sets the caller's tooltip doc and tooltip secondary doc to wndB's values.

| parameter | type | meaning |
|---|---|---|
| `wndB` | Window |  |

### `SetTooltipType(nType)`

Sets the tooltip type on the caller after casting nType to a ETooltipPositionType.

| parameter | type | meaning |
|---|---|---|
| `nType` | ETooltipPositionType |  |

### `SetVScrollInfo(nRange, nPageSize, nMinInc)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `nRange` | Integer |  |
| `nPageSize` | Integer |  |
| `nMinInc` | Integer |  |

### `SetVScrollPos(nNewPos)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `nNewPos` | Integer |  |

### `SetWindowSubclass()`

*no description in the client's documentation*

### `SetWindowTemplate()`

*no description in the client's documentation*

### `Show(bShow, bImmediate)`

Runs the caller's show method with bShow and bImmediate.

| parameter | type | meaning |
|---|---|---|
| `bShow` | Boolean |  |
| `bImmediate` | Boolean |  |

### `ToFront()`

Runs the caller's BringWindowToFront method.

### `TransitionMove(nMinX, nMinY, nOffX, nOffY, fRate, bContinuous)`

Calls a transition move with pLocBegin null and pLocEnd specified by dMinX, dMinY, dMinX+dOffX, dMinY+dOffY, fRate, and bContinuous.

| parameter | type | meaning |
|---|---|---|
| `nMinX` | Double |  |
| `nMinY` | Double |  |
| `nOffX` | Double |  |
| `nOffY` | Double |  |
| `fRate` | Float |  |
| `bContinuous` | Boolean |  |

### `TransitionMoveFrom(nMinX, nMinY, nOffX, nOffY, fRate, bContinuous)`

Calls a transition move with pLocEnd null and pLocBegin specified by dMinX, dMinY, dMinX+dOffX, dMinY+dOffY, fRate, and bContinuous.

| parameter | type | meaning |
|---|---|---|
| `nMinX` | Double |  |
| `nMinY` | Double |  |
| `nOffX` | Double |  |
| `nOffY` | Double |  |
| `fRate` | Float |  |
| `bContinuous` | Boolean |  |

### `TransitionPulse(fScale, fRate, bContinuous)`

`deprecated flag set` *no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `fScale` | Float |  |
| `fRate` | Float |  |
| `bContinuous` | Boolean |  |

### `UnpauseAnim()`

Runs the caller's unpause method on m_pAnimPlayer.

### `UpdatePixie()`

*no description in the client's documentation*

### `WindowPointToClientPoint(nPosX, nPosY)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `nPosX` | Integer |  |
| `nPosY` | Integer |  |

### `__eq()`

`deprecated flag set` *no description in the client's documentation*

### `__gc()`

`deprecated flag set` *no description in the client's documentation*

### `is()`

*no description in the client's documentation*

