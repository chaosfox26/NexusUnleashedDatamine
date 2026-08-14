# Episode

*Object, documented by the client itself.*

Episodes are a set of quests that are linked by a storyline or area.

**23 calls.** 3 carry `Deprecated="true"` — reported, not filtered, because that flag is set on entries known to be alive in 16042.

### `EpisodeState_Complete()`

`deprecated flag set` *no description in the client's documentation*

### `GetAllQuests(idQuestCategory)`

Gets a list of all of the quests in the Episode that match the passed in category id and that have been unlocked by the player.

| parameter | type | meaning |
|---|---|---|
| `idQuestCategory` | Integer | The function will return all quests with this category. |

**Returns** — `Quest` An array of quests that have the same category as the one that was passed in and have been unlocked by the player.

### `GetCategories()`

Gets a list of all of the QuestCategories that are used by quests in the Episode.

**Returns** — `QuestCategory` An array of QuestCategories that are used by quests in the Episode.

### `GetConLevel()`

Gets the level that the player is expected to be in order to complete the Episode.

**Returns** — `Integer` The level that the player is expected to be to complete the Episode.

> Carbine's own note: This doesn't seem to be used anymore.  Maybe it's depricated?

### `GetDesc()`

Gets the description that should be shown for the Episode when it is incomplete.

**Returns** — `String` The string that should be used as the Episode's description while it is incomplete.

### `GetHub()`

*no description in the client's documentation*

### `GetId()`

Gets the Episode's id.

**Returns** — `Integer` The Episode's id.

### `GetProgress(idQuestCategory)`

Gets information on the player's progress towards completing every quest of a specific category in this Episode.

| parameter | type | meaning |
|---|---|---|
| `idQuestCategory` | Integer | The function will get the Episode's progress for Quests whose category uses this id. |

**Returns** — `Table` A count of how many Quests the player has completed and how many the Episode has for the specified category.

### `GetQuest(idQuest)`

Gets the Quest with the specified id if it is in this Episode.

| parameter | type | meaning |
|---|---|---|
| `idQuest` | Integer | The id of the Quest that the function will look for. |

**Returns** — `Quest` The Quest whose id matches the one passed in.

### `GetState()`

Gets the Episode's current state.

**Returns** — `Integer` The Episode's current state.  This value corresponds with the Episode.EpisodeState set of constants.

> Carbine's own note: Episode.EpisodeState constants should be enums

### `GetSummary()`

Gets the description that should be shown for the Episode once it's complete.

**Returns** — `String` The string that should be shown for the Episode's description once it's in the Completed state.

### `GetTitle()`

Gets the Episode's title.

**Returns** — `String` The Episode's title.

### `GetTrackedQuests(idQuestCategory, bSortByDistance)`

Gets a list of tracked quests that have the specified QuestCategory and are part of the Episode.

| parameter | type | meaning |
|---|---|---|
| `idQuestCategory` | Integer | The id of the QuestCategory that the function will use to filter the results. |
| `bSortByDistance` | Boolean | Whether the function should sort the results by distance, with the closest quests coming first in the list. |

**Returns** — `Quest` An array of Quests that are part of the Episode and have a QuestCategory whose id matches the one passed in.

### `GetVisibleQuests(bShowCompleted, bShowOutLeveled, bSortByName, idQuestCategory)`

Gets a list of Quests that are part of the Episode and match the filters that are flagged with the variables that are passed in

| parameter | type | meaning |
|---|---|---|
| `bShowCompleted` | Boolean | Whether completed quests should be added to the list or not. |
| `bShowOutLeveled` | Boolean | Whether Quests whose con level are 10 below the player's effective level should be added to the list or not. |
| `bSortByName` | Boolean | Whether the list should be sorted alphabetically by name or not. |
| `idQuestCategory` | Integer | The Quests that are returned will be filtered by this QuestCategory id. |

**Returns** — `Quest` An array of Quests that has been filtered and possibly sorted by the variables that were passed into the function.

### `GetZoneId()`

Gets the id number of the zone that the Episode takes place in.

**Returns** — `Integer` The id number of the zone that the Episode is in.

### `GetZoneName()`

Gets the name of the zone that the Episode is found in.

**Returns** — `String` The name of the zone that the episode is in.

### `IsRegionalStory()`

Checks if the Episode is a Regional Story.  Regional Stories are Episodes that take place in a specific region within a zone, but do not breadcrumb to other areas.

**Returns** — `Boolean` Whether the Episode is a Regional Story or not.

### `IsTaskOnly()`

Determines if the Episode only has Tasks.  Tasks are Quests that are not part of any larger chain.

**Returns** — `Boolean` Whether the Episode's Quests are all Tasks or not.

### `IsWorldStory()`

Determines if the Episode is a World Story or not.  World Stories are quest chains that span multiple zones.

**Returns** — `Boolean` Whether the Episode is a World Story or not.

### `IsZoneStory()`

Determines if the Episode is a Zone Story or not.  Zone Stories are Episodes that span an entire zone.

**Returns** — `Boolean` Whether the Episode is a Zone Story or not.

### `__eq(epiCompare)`

`deprecated flag set` Determines if two Episodes are the same.

| parameter | type | meaning |
|---|---|---|
| `epiCompare` | Episode | The episode being compared to this Episode. |

**Returns** — `Boolean` Whether the two Episodes are the same or not.

### `__gc()`

`deprecated flag set` Manually calls the garbage collector on this Episode.

### `is(oVariable)`

Checks whether the variable that is passed in is an Episode or not.

| parameter | type | meaning |
|---|---|---|
| `oVariable` | Variable | The variable that the function will check.  This variable can be of any type. |

**Returns** — `Boolean` Whether the variable that was passed in is an Episode or not.

