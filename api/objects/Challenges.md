# Challenges

*Object, documented by the client itself.*

Challenges are timed goals that the player will unlock as they kill NPCs and explore Nexus.  Most challenges are repeatable and offer rewards, such as crafting materials, decor, and equipment.

**34 calls.** 4 carry `Deprecated="true"` — reported, not filtered, because that flag is set on entries known to be alive in 16042.

### `GetAllTierCounts()`

Returns the goal number for each tier of the Challenge

**Returns** — `Table` An array that contains the amount of progress that the player must reach for each of the Challenge's tiers.

### `GetCompletionCount()`

Gets the number of times the player has completed the challenge.

**Returns** — `Integer` The number of times the player has completed the challenge.

### `GetCompletionTotal()`

Gets the number of times this Challenge can be completed.

**Returns** — `Integer` The number of times the player can complete the challenge.  If this value is -1, then the challenge can be completed an infinate number of times.

### `GetCurrentCount()`

Gets the player's progress towards this Challenge.

**Returns** — `Integer` The amount of progress the player has made towards the current challenge.

### `GetCurrentTier()`

Gets the tier of this Challenge that the player is working towards.

**Returns** — `Integer` The challege tier that the player is working towards.

### `GetDescription()`

Gets the text that describes the challenge.

**Returns** — `String` The Challenge's description.

### `GetDisplayTier()`

Returns the current tier for the Challenge that the UI should display as active.

**Returns** — `Integer` The tier that the UI should display as active.

### `GetDistance()`

*no description in the client's documentation*

### `GetDuration()`

*no description in the client's documentation*

### `GetId()`

Returns the id number of the challenge

**Returns** — `Integer` The Challenge's id number.

### `GetLastRewardTier()`

Returns the last tier of the Challenge that the player completed during the current attempt.

**Returns** — `Integer` The last tier that was completed of the challenge during the current attempt.

### `GetMapLocation()`

The location that the hint arrow points the player towards for the challenge.

**Returns** — `Table` The X, Y, and Z coordinates that the hint arrow leads the player to.

### `GetMapRegions()`

Gets the point that the helper arrow leads to and a list of all of the hexes that the challenge uses.

**Returns** — `Table` A list that contains map info on the challenge.

### `GetMapStartLocation()`

Gets the coordinates where the Challenge can be started

**Returns** — `Table` The coordinates where the challenge can be started.

### `GetMapStartRegions()`

Returns the coordinates for the hexes where the Challenge takes place

**Returns** — `Vector2` An array of hex coordinates where the objectives for the challenge can be found.

### `GetName()`

Gets the challenge's name.

**Returns** — `String` The name of the challenge.

### `GetRewardTrack()`

*no description in the client's documentation*

### `GetStartLocationRestrictionId()`

Returns the location id that the player must be in to start the challenge.  This value can be used with GameLib.IsInLocation() to determine if the player is in the correct location to start a challenge.

**Returns** — `Integer` The id number of the challenge's start location.

### `GetTimeStr()`

`deprecated flag set` Gets the challenge's current timer and returns it in string form.

**Returns** — `String` The amount of time left on the timer, in "minute:second" format.

### `GetTimer()`

*no description in the client's documentation*

### `GetTotalCount()`

Gets the total amount of progress the player has to earn to complete the current tier of the challenge.

**Returns** — `Integer` The amount of progress needed to complete the current challenge tier.  This value is 100 for percentage based progress, or a smaller number for challenges that require a fixed amount of progress.

### `GetType()`

Gets a challenge's type.

**Returns** — `Integer` The challenge's type.  This corresponds with the ChallengeLib.ChallengeType set of int constants.

> Carbine's own note: ChallengeLib.ChallengeType needs to be turned into an enum.

### `GetZoneInfo()`

Gets information on the zone where the challenge is found.

**Returns** — `Table` A table with information on where the challenge is located.

### `GetZoneRestrictionInfo()`

Gets information on the area that the challenge is restricted to.

**Returns** — `Table` A table with information on the area that the challenge is restricted to.

### `IsActivated()`

Finds out whether the challenge is currently running or not.

**Returns** — `Boolean` Whether the challenge is currently running or not.

### `IsFullyComplete()`

Determines if the challenge has been completed the maximum number of times or not.

**Returns** — `Boolean` Whether the challenge has been completed the maximum number of times or not.

### `IsInCooldown()`

Determines whether the challenge is currently on cooldown.

**Returns** — `Boolean` Whether the challenge is on cooldown or not.

### `IsTimeTiered()`

Determines whether the reward tiers are based on the player's completion time or not.

**Returns** — `Boolean` Whether the reward tiers are based on the player's completion time or not.

### `NeedsHintArrow()`

Determines whether the challenge has a set starting area or zone restrictions.

**Returns** — `Boolean` Whether the challenge needs to have a hint arrow or not.

### `ShouldCollectReward()`

`deprecated flag set` Determines if the player has not collected their reward for the challenge.

**Returns** — `Boolean` Whether the player has an uncollected reward or not.

### `ShouldDisplayPercentProgress()`

Determines whether the challenge displays its progress as a percent or as an exact number.

**Returns** — `Boolean` Whether the player's progress should be shown as a percent or not.

### `__eq()`

`deprecated flag set` *no description in the client's documentation*

> Carbine's own note: Unsure if this is used or not.  Could not find any functionality for it.

### `__gc()`

`deprecated flag set` Challenge's garbage collection function.  This will delete the Challenge from memory.

### `is(oVariable)`

Determines if the variable is a Challenge or not.

| parameter | type | meaning |
|---|---|---|
| `oVariable` | Variable | The variable that the function will check. |

**Returns** — `Boolean` Whether the variable is a Challenge or not.

