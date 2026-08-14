# Achievement

*Object, documented by the client itself.*

Achievements are tasks that can be completed to gain various rewards.  These include the standard Achievements that you find in the AchievementLog, as well as the elements of the Tradeskill Tech Tree.

**31 calls.** 3 carry `Deprecated="true"` — reported, not filtered, because that flag is set on entries known to be alive in 16042.

### `GetCategory()`

Returns the name of the category that the achievement belongs to.

**Returns** — `String` The name of the achievement's parent category

### `GetCategoryFullName()`

Returns the long version of the name of the category that the achievement belongs to

**Returns** — `String` 

### `GetCategoryId()`

Returns the id number for the category that the achievement belongs to

**Returns** — `Integer` The Id number for the Achievement's category

### `GetChecklistItems()`

Returns a list of things required to complete this achievement

**Returns** — `Table` 

### `GetChildTier()`

Returns the previous step of a multi-stage achievement.

**Returns** — `Achievement` 

### `GetCurrencySystem()`

Gets the type of currency required to progress the spefied Achievement.

**Returns** — `Money.CodeEnumCurrencyType` The type of money the player

### `GetDateCompleted()`

Returns a string with the date that the achievement was completed.  The formatting for the date varies based on which language is being used on the  client

**Returns** — `String` The date that the achievement was completed.  This date is localized for different regions.

### `GetDescription()`

Returns the description text for the achievement when it is completed.    This function is not to be confused with Achievement:GetProgressText(), which  returns the description text for the achievement before it is complete

**Returns** — `String` The text for the completed achievement

### `GetGroup()`

Gets the name of the tradeskill that the achievement belongs to, if any.

**Returns** — `String` 

### `GetId()`

Returns the achievement's ID number.

**Returns** — `Integer` The ID number of the Achievement

### `GetName()`

Returns the name of the achievement

**Returns** — `String` The name of the achievement calling this function

### `GetNumCompleted()`

Returns the character's progress on this achievement.

**Returns** — `Integer` 

### `GetNumNeeded()`

Returns the amount of progress that is required to complete this achievement

**Returns** — `Integer` 

### `GetParentCategoryId()`

`deprecated flag set` *no description in the client's documentation*

### `GetParentTier()`

Returns the parent achievement of a multi-tier achievement.

**Returns** — `Achievement` 

### `GetPoints()`

Returns the number of achievement points granted when the achievement is completed

**Returns** — `Integer` 

### `GetProgressText()`

Returns the description text that the achievement shows when it is not complete.  This function is not to be confused with Achievement:GetDescription(),  which returns the text for the achievement when it is complete

**Returns** — `String` The text for the incomplete achievement

### `GetRewards()`

Returns any title that is granted when the achievement is completed.

**Returns** — `CharacterTitle` 

### `GetSubGroup()`

Returns the name of the subgroup that the achievement belongs to.

**Returns** — `String` 

### `GetSubGroupId()`

Returns the id number of the subgroup that the achievement belongs to.

**Returns** — `Integer` 

### `GetTradeskillLayout()`

Returns the position information for the achievement and its parents.

**Returns** — `Table` 

### `GetTradeskillRewards()`

Returns a description of various rewards that a tradeskill achievement grants

**Returns** — `Table` 

### `GetTradeskillSchematicsRequired()`

Returns a list of schematic ids that the character must know before unlocking this Achievement.

**Returns** — `Integer` An array of schematic ids the character must know before the achievement is unlocked.

### `GetWorldZoneId()`

Returns the zone id where this achievement can be completed.

**Returns** — `Integer` 

### `IsChecklist()`

Determines if the Achievement requires multiple different steps to complete it

**Returns** — `Boolean` Whether the achievmemnt is a checklist or not.

### `IsComplete()`

Determines whether or not the Achievement has been completed.

**Returns** — `Boolean` 

### `IsCurrencyShown()`

Determines whether the achievent requires currency to be completed.

**Returns** — `Boolean` If the achievement requires currency, this will return true.

### `IsGuildAchievement()`

Determines if an Achievement is a Guild Achievement

**Returns** — `Boolean` 

### `__eq()`

`deprecated flag set` *no description in the client's documentation*

### `__gc()`

`deprecated flag set` Manually calls the Achievement's garbage collector.

### `is(oVariable)`

Determines whether the given variable is an Achievement

| parameter | type | meaning |
|---|---|---|
| `oVariable` | Any | The variable that is being checked. |

**Returns** — `Boolean` 

