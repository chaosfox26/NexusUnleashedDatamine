# PlayerPathLib

*Library, documented by the client itself.*

**29 calls.**

### `CanExplorerShowHint()`

*no description in the client's documentation*

### `ExplorerApplyRelicSpell()`

*no description in the client's documentation*

### `ExplorerShowHint()`

Displays a hint for the passed path mission

### `GetCurrentEpisode()`

Returns the PathEpisode that is currently active for the player

### `GetCurrentSettlerHubMission()`

*no description in the client's documentation*

### `GetCurrentSettlerInfrastructure()`

*no description in the client's documentation*

### `GetEpisodes()`

Returns a table with all of the PathEpisodes where the player has unlocked at least one PathMission

### `GetInfrastructureStatusForMission()`

*no description in the client's documentation*

### `GetPathEpisodeForZone()`

Does a PushEpisodeInfo of the episode Id at the current zone.

### `GetPathLevel()`

Returns the character's current path level

### `GetPathLevelCap()`

*no description in the client's documentation*

### `GetPathLevelData(nLevel)`

Does a lua_newtable with level, xp, and the rewards specified at nLevel, or nil if null.

| parameter | type | meaning |
|---|---|---|
| `nLevel` | Integer |  |

> Carbine's own note: note!

### `GetPathXP()`

Returns the total path XP that the player has earned

### `GetPathXPAtLevel()`

Returns the amount of path XP needed to reach a given path level

### `GetPathXPForLevel()`

Returns the amount of path XP the player has earned during the current path level

### `GetPathXPForNextLevel()`

Does a lua_pushinteger of the character's path xp for next level

### `GetPlayerPathType()`

Does a lua_pushinteger of GetPathType, or nil if null.

### `GetScannerName()`

*no description in the client's documentation*

### `GetSettlerHubValues()`

Does a lua_newtable with an index, name, value, and max of a settler's hub.

### `GetUnlockedPathLevelCap()`

*no description in the client's documentation*

### `PathAction()`

*no description in the client's documentation*

### `PathAction2()`

*no description in the client's documentation*

### `ScientistAllGetScanBotProfiles()`

*no description in the client's documentation*

### `ScientistGetScanBotProfile()`

*no description in the client's documentation*

### `ScientistGetScanBotUnit()`

*no description in the client's documentation*

### `ScientistHasScanBot()`

*no description in the client's documentation*

### `ScientistSetScanBotProfile()`

*no description in the client's documentation*

### `ScientistToggleScanBot()`

*no description in the client's documentation*

### `SetScannerName()`

*no description in the client's documentation*

