# AchievementsLib

*Library, documented by the client itself.*

Contains a list of functions that are helpful for building and orgainzing the Achievements UI or anything that requires achievement information.

**12 calls.**

### `GetAchievementCategoryTree(bGetGuildAchievements)`

Gets a tree structure for the different types of achievements for the UI.  The heirarchy goes Categories > Groups > Subgroups.

| parameter | type | meaning |
|---|---|---|
| `bGetGuildAchievements` | Boolean | Whether the function should return Guild Achievements or not. |

**Returns** — `Table` A table with information on the categories, groups, and subgroups of achievements.

### `GetAchievementPoints()`

Returns the number of achievement points that the player has earned from completed achievements.

**Returns** — `Integer` The number of points the player has earned.

### `GetAchievementZones()`

Returns a list of all of the zones used in any achievement.

**Returns** — `Table` 

### `GetAchievements(bIsGuild)`

Gets a list of all achievements or guild achievements.

| parameter | type | meaning |
|---|---|---|
| `bIsGuild` | Boolean | Determines whether the function should return guild achievements or not. |

**Returns** — `Achievement` An array with every achievement of the specified type.

### `GetAchievementsForCategory(idCategory, bRecurse, bGetGuild)`

Gets a list of all the achievements for the given category.

| parameter | type | meaning |
|---|---|---|
| `idCategory` | Integer | The category of achievements that should be returned. |
| `bRecurse` | Boolean | Whether or not the function should recurse through the category's subcategories when searching. |
| `bGetGuild` | Boolean | Whether the function should return guild achievements or not. |

**Returns** — `Achievement` An array that contains all of the achievements for the given category (and subcategories if bRecurse was set to true)

### `GetCategoriesForZone()`

*no description in the client's documentation*

### `GetCategoryForMatchingGame()`

*no description in the client's documentation*

### `GetGuildAchievementPoints()`

Returns the number of Guild Achivement Points the player's current guild has earned.

**Returns** — `Integer` The number of Guild Achievement Points that the guild has earned.

### `GetRecentCompletedAchievements(nMaxCount, bGetGuild)`

Gets the latest achievements that the player has earned.

| parameter | type | meaning |
|---|---|---|
| `nMaxCount` | Integer | The maximum number of values you want the achievement to return. |
| `bGetGuild` | Boolean | Whether the function should return guild achievements or not. |

**Returns** — `Achievement` An array of the most recent achievements the player has earned, in order of most recent to least.

### `GetTradeskillAchievementCategoryTree(eTradeskill)`

Gets a list of all of the categories and subcategories for a tradeskill's tech tree.

| parameter | type | meaning |
|---|---|---|
| `eTradeskill` | CraftingLib.CodeEnumTradeskill | The function will return the tech tree for this tradeskill. |

**Returns** — `Table` A table containing the name of the tradeskill and its subcategories.

### `GetTradeskillAchievementLayout(nSubcategoryId)`

Gets a list of all of the achievements for a specific tradeskill rank.

| parameter | type | meaning |
|---|---|---|
| `nSubcategoryId` | Integer | The id number for the tradeskill's rank. |

**Returns** — `Achievement` An array of the achievements for the specified tradeskill rank.

### `GetTradeskillAchievements(eTradeskill)`

Gets all of the achievements for a specific tradeskill.

| parameter | type | meaning |
|---|---|---|
| `eTradeskill` | CraftingLib.CodeEnumTradeskill | The function will return the achievements for this tradeskill. |

**Returns** — `Achievement` An array that contains all of the achievements for the specified tradeskill

