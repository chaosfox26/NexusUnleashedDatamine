# Apollo

*Library, documented by the client itself.*

A library that primarily contains system-level functionality, such as registering events, controling addons, detecting key presses, and manipulating console variables.

**69 calls.** 2 carry `Deprecated="true"` — reported, not filtered, because that flag is set on entries known to be alive in 16042.

### `AddAddonErrorText(oAddon, strAddToError)`

Adds a message to an addon's info.

| parameter | type | meaning |
|---|---|---|
| `oAddon` | String or Table | The addon that threw the error.  This can either be an instance of the addon itself or the addon's name. |
| `strAddToError` | String | The text that should be added to the addon's error list. |

> Carbine's own note: We should take either a string or table and not give the users the choice.

### `AlertAppWindow()`

Flashes the client's icon on the Windows taskbar if the game does not have focus.

### `AssetFileSizeString(strFilename)`

Gets the file size of the specified asset.

| parameter | type | meaning |
|---|---|---|
| `strFilename` | String | The file name of the asset. |

**Returns** — `String` The asset's size, in bytes.

### `AssetFileTimeString(strFilename)`

Gets the date and time that the asset was last updated.

| parameter | type | meaning |
|---|---|---|
| `strFilename` | String | The asset's file name. |

**Returns** — `String` A string that contains the date and time when the specified asset was last updated.

### `BeginClickStick(wndSource, strType, strSprite, nStartLocation)`

Causes the item or spell that the player clicked on to stick to the cursor until the player clicks again.  It is treated like drag-drop functionality, only the player does not have to hold a button until the end of the operation.

| parameter | type | meaning |
|---|---|---|
| `wndSource` | Window | The window where the click-stick operation began. |
| `strType` | String | The type of item that the click stick is affecting.  This value can be either "DDBagItem" or "DDSpellbookItem". |
| `strSprite` | String | The file name of the sprite that replaces the cursor while the click-stick operation is active. |
| `nStartLocation` | Integer | The location where the operation began. |

### `BeginDragDrop(wndSource, strType, strSprite, nStartLocation)`

Starts a drag-drop operation on the item that the player clicked on.

| parameter | type | meaning |
|---|---|---|
| `wndSource` | Window | The window where the operation began. |
| `strType` | String | The type of object that is being dragged in the operation.  This can be either "DDBagItem" or "DDSpellbookItem". |
| `strSprite` | String | The file name of the sprite that replaces the cursor during the operation. |
| `nStartLocation` | Integer | The location where the drag-drop operation started. |

### `CloseEscapableWindows()`

Closes all of the windows that have the Escapable flag turned on.

**Returns** — `Boolean` Whether any windows were closed or not.

### `CreateTimer(strTimerName, nInterval, bContinuous)`

Creates a timer that can be run from Lua.

| parameter | type | meaning |
|---|---|---|
| `strTimerName` | String | The name of the timer. |
| `nInterval` | Integer | How often the timer will fire. |
| `bContinuous` | Boolean | Whether the timer will constantly run or only fire once before needing to be restarted. |

### `DPF(strDebugMessage)`

Sends the string that is passed in to the client logs.

| parameter | type | meaning |
|---|---|---|
| `strDebugMessage` | String | The message that the function passes on to the client logs. |

### `DisableAddon(strAddonName)`

Disables the specified addon if it has any errors.  Disabled addons do not load after the UI is reloaded.

| parameter | type | meaning |
|---|---|---|
| `strAddonName` | String | The name of the addon that should be disabled. |

### `DoesSpriteExist(strSpriteName)`

Checks if a sprite with the given name exists in the Carbine sprite set.

| parameter | type | meaning |
|---|---|---|
| `strSpriteName` | String | The name of the sprite that the function looks for. |

**Returns** — `Boolean` Whether a sprite with the specified name was found or not.

### `FindWindowByName(strWindowName)`

Searches through all of the addons that are registered with Apollo for a window with the specified name.

| parameter | type | meaning |
|---|---|---|
| `strWindowName` | String | The name of the window that the function searches for. |

**Returns** — `Window` The window that was found by the search.

### `FormatNumber(oNumber, nDecimals, bCommas)`

Formats a number to include region-specific notations, such as commas/periods in integers with 4+ digits, and truncates the value to a specific number of decimal places.

| parameter | type | meaning |
|---|---|---|
| `oNumber` | Integer | The number that needs to be formatted.  This can be either an integer or float. |
| `nDecimals` | Integer | The number of decimal places to display |
| `bCommas` | Boolean | Determines whether or not commas should be shown in numbers with 4 or more digits |

**Returns** — `String` The formatted number with all relevant punctuation

### `GetAPIVersion()`

Gets the current API version used by the game.

**Returns** — `Integer` Apollo's current API version.

### `GetAddon(strAddonName)`

Gets all of the functions and variables from the instance of the specified addon that is currently running.

| parameter | type | meaning |
|---|---|---|
| `strAddonName` | String | The name of the addon that the function will try to find. |

**Returns** — `oAllTheThings` All of the addon level variables contained in the addon, as well as a metatable with all of the addon's functions.

### `GetAddonInfo(strAddonName)`

Gets a lot of performance information and a list of errors for the specified addon.

| parameter | type | meaning |
|---|---|---|
| `strAddonName` | String | The name of the addon. |

**Returns** — `Table` A table that contains a large amount of information on the addon.

### `GetAssetFolder()`

Gets the name of the folder that contains all of the default UI's assets.

**Returns** — `String` The default UI's asset folder.

### `GetConsoleVariable(strVarName)`

Gets the value of the specified console variable.

| parameter | type | meaning |
|---|---|---|
| `strVarName` | String | The name of the console variable whose value is requested. |

**Returns** — `Value` This value can be of any basic type (integer, float, boolean, string, nil), depending on which console variable is requested.

### `GetDisplaySize()`

Gets the size of the client, as well as the size of the viewable portion of the client window.

**Returns** — `Table` The width and height of the window and the viewable portion of the window, as well as the scale that everything is drawn to.

### `GetGameFonts()`

Gets a list of all of the fonts that come with the game.  Each font is made up of a typeface and a font size.

**Returns** — `Table` An array with information of all of the fonts that are packaged with the game.

### `GetMaxResolutionWidth()`

Returns the maximum width that the client can be set to.

**Returns** — `Integer` The maximum resolution width.

### `GetMetaKeysDown()`

Gets a bit flag that tells which meta keys are currently pressed.

**Returns** — `Integer` A bit flag of the Meta Keys that are currently pressed down.  The value lines up with the GameLib.CodeEnumInputModifier enum.

### `GetMinResolutionWidth()`

The minimum resolution width that the client can be set to.

**Returns** — `Integer` The minimum resolution width.

### `GetMouse()`

Gets the mouse's position in screen coordinates.

**Returns** — `Table` The mouse's current coordinates in screen space.

### `GetMouseTargetWindow()`

Gets the window that the mouse is currently hovering over.

**Returns** — `Window` The top-most window that the mouse is hovering over.

### `GetMoveMetaKey()`

Gets the meta key that is bound to the Sprint action.

**Returns** — `GameLib.CodeEnumInputModifier` The meta key that is bound to the Sprint action.

### `GetObjectSize(oVariable)`

Gets the memory size of an object.

| parameter | type | meaning |
|---|---|---|
| `oVariable` | Variable | The function will return the size of this variable.  Any variable type can be passed in. |

**Returns** — `Integer` The size of the variable, in bytes.

### `GetPackage(strPackageName)`

Returns information on a package that was registered with Apollo.

| parameter | type | meaning |
|---|---|---|
| `strPackageName` | String | The name of the package. |

**Returns** — `Table` Information about the package.

### `GetScreenSize()`

`deprecated flag set` Gets the size of the client window.  This function has been replaced by Apollo.GetDisplaySize()

### `GetStrata()`

Gets an array of all of the window strata that are in use.

**Returns** — `String` The names of each strata that a window can be drawn in.

### `GetString(strCheck)`

Gets the localized string for the given string or id number.

| parameter | type | meaning |
|---|---|---|
| `strCheck` | String or Integer | The string or id that will poll the string. |

**Returns** — `String` The localized string that corresponds

### `GetTextWidth(strFontName, strInput)`

Gets the number of pixels it takes to draw a specific piece of text with a specific font.

| parameter | type | meaning |
|---|---|---|
| `strFontName` | String | The name of the font that to use in the width check. |
| `strInput` | String | The text that the function is checking. |

**Returns** — `Integer` The width, in pixels, that it takes to draw the text with the given font.

### `GetTickCount()`

Gets the number of milliseconds since the system was started.

**Returns** — `Integer` The number of milliseconds that have elapsed since the system was started (up to 49.7 days)

### `GetWindowsInStratum(strStratum)`

Gets all of the windows in a specific stratum.

| parameter | type | meaning |
|---|---|---|
| `strStratum` | String | The function returns the windows found in the stratum whose name matches this string. |

**Returns** — `Window` An array of windows found in the given stratum.

### `IsAltKeyDown()`

Gets the state of the Alt key.

**Returns** — `Boolean` Whether the Alt key is down or not.

### `IsCapsLockOn()`

Gets the state of the Caps Lock button.

**Returns** — `Boolean` Whether Caps Lock is on or not.

### `IsControlKeyDown()`

Gets the state of the Control key.

**Returns** — `Boolean` Whether the Control key is down or not.

### `IsShiftKeyDown()`

Gets the state of the Shift key.

**Returns** — `Boolean` Whether the Shift key is down or not.

### `IsSpriteLoaded(strSpriteName)`

Checks whether a specific sprite is loaded or not

| parameter | type | meaning |
|---|---|---|
| `strSpriteName` | String | The name of the sprite that the function is looking for. |

**Returns** — `Boolean` Whether the sprite is loaded or not.

### `IsWindowSubclassRegistered(strSubclassName)`

Determines whether the specified Window Subclass has been registered with Apollo.

| parameter | type | meaning |
|---|---|---|
| `strSubclassName` | String | The name of the Window Subclass that the function will look for. |

**Returns** — `Boolean` Whether the Subclass is registered or not.

### `LinkAddon(tTarget, tSource)`

Associates a module with a parent module in Apollo.  This allows Apollo to manage the addon's memory better.

| parameter | type | meaning |
|---|---|---|
| `tTarget` | Table | The "self" of the module that the function will link to. |
| `tSource` | Table | The "self" of the module that is calling the function. |

### `LoadAnimations(strFileName)`

Attempts to load a specific animation file.

| parameter | type | meaning |
|---|---|---|
| `strFileName` | String | The file name of the animation that the function will try to load. |

**Returns** — `Boolean` Whether the animation was successfully loaded or not.

> Carbine's own note: Does this still have a use?

### `LoadForm(strFile, strFormName, wndParent, tLuaEventHandler)`

Loads a window from the specified form

| parameter | type | meaning |
|---|---|---|
| `strFile` | String or XmlDoc | The path to the XML document that contains the window, or the pre-loaded XML form. |
| `strFormName` | String | The name of the window form that the function will try to load. |
| `wndParent` | Window | The newly loaded window will be a child of this window. |
| `tLuaEventHandler` | Table | The Lua object that owns the window.  This value is usually "self", meaning the window that called the function. |

**Returns** — `Window` The window object that was loaded.

### `LoadGlobalAnchors(strFile)`

Loads the global anchors for the specified file.

| parameter | type | meaning |
|---|---|---|
| `strFile` | String |  |

> Carbine's own note: Unused, so unsure of how/when we'd need this.

### `LoadSprites(strFile, strDoc)`

Loads a sprite set.

| parameter | type | meaning |
|---|---|---|
| `strFile` | String or XmlDoc | The name of the form that contains the sprites, or the XmlDoc that contains them. |
| `strDoc` | String | The name of the spriteDoc.  This variable is optional. |

> Carbine's own note: Really need to figure out what exactly this does.

### `LoadTemplates()`

*no description in the client's documentation*

> Carbine's own note: Not quite sure what's going on with this one...

### `NoOp()`

`deprecated flag set` Does absolutely nothing.

### `ParseInput(strInput)`

Parses the input for slash commands.  If the first character is not a "/", it will not recognize the text as a slash command and will print it to the Say chat channel.

| parameter | type | meaning |
|---|---|---|
| `strInput` | String | The string that the function will parse. |

**Returns** — `String` Returns the string for Console_CommandNotFound if the slash command that was passed in was invalid.  Otherwise, this returns an empty string.

### `RegisterAddon(tAddon, bHasConfigureFunction, arDependencies)`

Registers an addon to be loaded by Apollo.  Addons that are not registered do not work.

| parameter | type | meaning |
|---|---|---|
| `tAddon` | Table | The instance of the addon that is registering with Apollo.  This is represented by "self". |
| `bHasConfigureFunction` | Boolean | Whether addon has a Configure button in the Esc menu.  If this value is true, then the addon needs an OnConfigure() function to handle the button signal event. |
| `arDependencies` | String | An array of addon names that must be loaded before this addon can be successfully loaded. |

### `RegisterEventHandler(strEventName, strFunctionName, tLuaEventHandler)`

Matches an event that is fired with the Lua function that will handle the event.

| parameter | type | meaning |
|---|---|---|
| `strEventName` | String | The name of the event to be handled. |
| `strFunctionName` | String | The name of the function that will be called when the event is fired. |
| `tLuaEventHandler` | Table | The addon's "self". |

### `RegisterPackage(tPackage, strModule, nVersion, arDependencies)`

Registers a package with Apollo so it can be used by other addons.

| parameter | type | meaning |
|---|---|---|
| `tPackage` | Table | The instance of the package that is registering with Apollo.  This is usually represented by "self". |
| `strModule` | String | The name of the package. |
| `nVersion` | Integer | The packages version. |
| `arDependencies` | String | An array of addon or package names that must be loaded before this addon loads. |

### `RegisterSlashCommand(strCommand, strFunction, tAddonHandler)`

Registers a slash command with Apollo and sets up a function to handle the event fired when the command is used.

| parameter | type | meaning |
|---|---|---|
| `strCommand` | String | The slash command that will get registered with Apollo.  This string should contain everything that comes after the / in the command. |
| `strFunction` | String | The function that will handle the event that gets fired when the slash command is used. |
| `tAddonHandler` | Table | The instance of the addon that will handle the event fired by the slash command.  This is usually the addon's "self". |

### `RegisterTimerHandler(strTimerName, strFunction, tAddon)`

Pairs a timer with a function that will be called whenever the timer's interval expires.

| parameter | type | meaning |
|---|---|---|
| `strTimerName` | String | The name of the timer that the function will pair with the handler function. |
| `strFunction` | String | The function that will be called whenever the timer's interval expires. |
| `tAddon` | Table | The instance of the addon that will handle the event fired when the timer's interval expires.  This is usually the addon's "self". |

### `RegisterWindowSubclass(strSubclassName, tAddon, tEvents)`

Registers a Window Subclass with Apollo.

| parameter | type | meaning |
|---|---|---|
| `strSubclassName` | String | The name of the Subclass. |
| `tAddon` | Table | The instance of the module that is being registered.  This is usually the module's "self". |
| `tEvents` | Table | An array of Event/Function Handler pairs that the Subclass wants to register with. |

**Returns** — `Boolean` Whether the subclass was sucessfully registered with Apollo or not.

### `RemoveEventHandler(strEventName, tModule)`

Removes an event handler from Apollo.  This is primarily done for memory management purposes.

| parameter | type | meaning |
|---|---|---|
| `strEventName` | String | The event that the module will stop handling. |
| `tModule` | Table | The instance of the module that will stop handling the event.  This is usually the module's "self". |

### `ResetConsoleVariable(strConsoleVariableName)`

Returns a console variable to its default value.

| parameter | type | meaning |
|---|---|---|
| `strConsoleVariableName` | String | The name of the console variable that will be reset to its default. |

### `SetConsoleVariable(strVariable, oValue)`

Sets a console variable to a given value.

| parameter | type | meaning |
|---|---|---|
| `strVariable` | String | The name of the console variable that the function will update. |
| `oValue` | CColor, String, Integer, Float, or Boolean | The new value of the console variable.  The type of variable used must match the type needed by the Console Variable. |

### `SetCursor(acCursor)`

Changes the cursor to another ApolloCursor.

| parameter | type | meaning |
|---|---|---|
| `acCursor` | ApolloCursor | The cursor that will be shown after the function is called. |

### `SetGlobalAnchor(strName, fPoint, nOffset, bOverwrite)`

Creates a named anchor that can be used for setting up windows for other addons.

| parameter | type | meaning |
|---|---|---|
| `strName` | String | The name of the anchor. |
| `fPoint` | Float | The anchor point for this anchor. |
| `nOffset` | Integer | The offset from the anchor point that the named anchor should be set to. |
| `bOverwrite` | Boolean | Whether the function should overwrite any named anchors with the same name. |

### `SetMaxResolutionWidth(nWidth)`

Sets the maximum resolution width for the client.

| parameter | type | meaning |
|---|---|---|
| `nWidth` | Integer | The maximum resolution width that the client can be set to. |

### `SetMinResolutionWidth(nWidth)`

Sets the minimum resolution width that the client can be set to.

| parameter | type | meaning |
|---|---|---|
| `nWidth` | Integer | The minimum width that the client can be set to. |

### `SetMoveMetaKey(eMetaKey)`

Changes the meta key used for sprinting.

| parameter | type | meaning |
|---|---|---|
| `eMetaKey` | GameLib.CodeEnumInputModifier | The meta key that the sprint action should be bound to. |

### `SetNavTextAnchor(nXAnchor, bGrowRight, nYAnchor, bGrowDown)`

Changes how and where a tooltip is drawn.

| parameter | type | meaning |
|---|---|---|
| `nXAnchor` | Integer | The tooltip anchor point's x coordinate. |
| `bGrowRight` | Boolean | If this is true, then the tooltip will be drawn to the right of the anchor point.  If it is false, it will be drawn to the left. |
| `nYAnchor` | Integer | The tooltip anchor point's y coordinate. |
| `bGrowDown` | Boolean | If this is true, then the tooltip will be drawn below the anchor point.  If it is false, it will be drawn above it. |

### `StartTimer(strTimerName)`

Starts a timer that is not currently running.

| parameter | type | meaning |
|---|---|---|
| `strTimerName` | String | The name of the timer that the function should start. |

### `StopTimer(strTimerName)`

Stops a timer that is currently running.

| parameter | type | meaning |
|---|---|---|
| `strTimerName` | String | The name of the timer that the function should stop. |

### `StringLength()`

*no description in the client's documentation*

### `StringToLower(strInput)`

Changes all of the characters in a string to lower case.

| parameter | type | meaning |
|---|---|---|
| `strInput` | String | The string that will be changed to lower case. |

**Returns** — `String` The updated string.

> Carbine's own note: Need to find out what makes this different from string.lower()

### `SuspendAddon(strAddonName)`

Turns off an addon that is throwing errors until the UI is reloaded.

| parameter | type | meaning |
|---|---|---|
| `strAddonName` | String | The name of the addon that the function will try to suspend. |

### `UnlinkAddon(tTarget, tSource)`

Frees up the memory used by a linked addon.

| parameter | type | meaning |
|---|---|---|
| `tTarget` | Table | The addon that the module was linked to. |
| `tSource` | Table | The instance of the module that is being unlinked.  This is usually the module's "self". |

