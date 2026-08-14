# ChallengesLib

*Library, documented by the client itself.*

A library that allows the UI to interact with the challenge system.

**19 calls.** 7 carry `Deprecated="true"` — reported, not filtered, because that flag is set on entries known to be alive in 16042.

### `AbandonChallenge(idChallenge)`

Abandons the challenge with the specified id.

| parameter | type | meaning |
|---|---|---|
| `idChallenge` | Integer | The id number of the challenge that will be abandoned. |

### `AcceptRewards(idChallenge)`

`deprecated flag set` Attempts to collect a reward from a challenge.

| parameter | type | meaning |
|---|---|---|
| `idChallenge` | Integer | The function will attempt to grant the player the reward from the challenge with this id. |

### `AcceptSharedChallenge(idChallenge)`

`deprecated flag set` Accepts a challenge that another player has shared with the player.

| parameter | type | meaning |
|---|---|---|
| `idChallenge` | Integer | The id number for the challenge that was shared with the player. |

### `ActivateChallenge(idChallenge)`

Activates the challenge with the specified id.

| parameter | type | meaning |
|---|---|---|
| `idChallenge` | Integer | The id number of the challenge that the player wants to activate. |

### `AtChallengeStartLocation()`

*no description in the client's documentation*

### `ChallengeTier()`

`deprecated flag set` *no description in the client's documentation*

### `GenerateRewardList(idChallenge)`

`deprecated flag set` Requests the challenge reward list for the specified quest from the server.

| parameter | type | meaning |
|---|---|---|
| `idChallenge` | Integer | The function will request the challenge reward list for the challenge with this id number. |

### `GetActiveChallengeList()`

Gets a list of all of the challenges that the player has unlocked.

**Returns** — `Table` A map of all of the player's unlocked challenges, indexed by Id.

> Carbine's own note: This is either poorly named or not providing the advertised functionality.

### `GetLootBonusMultiplier(nTier)`

`deprecated flag set` Gets the bonus multiplier that a player can attach to a specific reward for a particular challenge tier.

| parameter | type | meaning |
|---|---|---|
| `nTier` | Integer | The function will return the multiplier for this reward tier. |

**Returns** — `Integer` The multiplier that is granted to whatever reward the player selects in the challenge reward list.

### `GetRewardList(idChallenge)`

`deprecated flag set` *no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `idChallenge` | Integer | The function will return the reward list for this challenge. |

**Returns** — `Table` A mostly-array that contains information on the different rewards that the quest can grant.  It is not a true array since strChallengeName is an index in the top level table, and not in any of the sub tables in the array.

### `GetRewardTrackByZone()`

*no description in the client's documentation*

### `GetRewardTrackInfo()`

*no description in the client's documentation*

### `GetRewardTrackPoints()`

*no description in the client's documentation*

### `GetTierName(nTier)`

Gets the name for the specified challenge tier.

| parameter | type | meaning |
|---|---|---|
| `nTier` | Integer | The function will get the name of this tier. |

**Returns** — `String` The name of the challenge tier.  If the tier number that was passed in was invalid, this will be an empty string.

### `GetTimeRemaining(idChallenge, eTimerFlags)`

Gets the amount of time left for a specific timer used by the specified challenge.

| parameter | type | meaning |
|---|---|---|
| `idChallenge` | Integer | The function will get the remaining time for the challenge with this id number. |
| `eTimerFlags` | Integer | The type of timer that the function is searching for.  The different types of timers are found in the ChallengesLib.ChallengeTimerFlags set of contstants. |

**Returns** — `String` The amount of time left for the challenge's timer, in string form.

### `ProcessRewards(idChallenge, nRewardIdx)`

`deprecated flag set` Tells the server to choose the reward that the player will receive from the challenge.

| parameter | type | meaning |
|---|---|---|
| `idChallenge` | Integer | The server will attempt to choose the reward for the challenge with this id number. |
| `nRewardIdx` | Integer | The reward number that the player selected to receive the bonus multiplier. |

### `RejectSharedChallenge(idChallenge)`

Declines a shared challenge.

| parameter | type | meaning |
|---|---|---|
| `idChallenge` | Integer | The id number for the challenge that the function will reject. |

### `ShowAbandonChallenge(idChallenge)`

Fires the ChallengeAbandoned event with a confirmation message.

| parameter | type | meaning |
|---|---|---|
| `idChallenge` | Integer | The id number of the challenge that the player is trying to abandon. |

> Carbine's own note: The event that is fired seems odd considering that it does not actually abandon the challenge.

### `ShowHintArrow(idChallenge)`

Shows the hint arrow that points to the area where the specified challenge takes place.

| parameter | type | meaning |
|---|---|---|
| `idChallenge` | Integer | The id number of the challenge that should show its hint arrow. |

