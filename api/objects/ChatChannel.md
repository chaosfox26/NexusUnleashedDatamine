# ChatChannel

*Object, documented by the client itself.*

One of the channels that chat messages can be sent to.

**29 calls.** 29 carry `Deprecated="true"` — reported, not filtered, because that flag is set on entries known to be alive in 16042.

### `CanLeave()`

`deprecated flag set` Checks if the player is able to leave the ChatChannel.

**Returns** — `Boolean` Whether the player is able to leave the ChatChannel or not.

### `CanSend()`

`deprecated flag set` Determines if the player is able to send messages on this ChatChannel.

**Returns** — `Boolean` Whether the player is able to send chat messages on this ChatChannel or not.

### `GetAbbreviation()`

`deprecated flag set` Gets an abbreviation for the ChatChannel that can be used in slash commands to quickly select the channel.

**Returns** — `String` The ChatChannel's abbreviation.

### `GetAlternate(nIndex)`

`deprecated flag set` Checks for alternate abbreviations for the ChatChannel.

| parameter | type | meaning |
|---|---|---|
| `nIndex` | Integer | The index of the alternate abbreviation for the ChatChannel. |

**Returns** — `String` The alternate abbreviation for the ChatChannel.

### `GetBans()`

`deprecated flag set` Gets a list of players who are banned in this ChatChannel.

**Returns** — `Table` An array of information about the players that have been banned from the channel.

### `GetCommand()`

`deprecated flag set` Gets the slash command used to select the ChatChannel.

**Returns** — `String` The command used to select the ChatChannel.

### `GetData()`

`deprecated flag set` Gets the data that was added to the channel with SetData()

**Returns** — `Variable` The data that was added to the ChatChannel with SetData.

### `GetMembers()`

`deprecated flag set` Gets a list of players that are in the ChatChannel.

**Returns** — `Table` An array that contains information on all of the players that are in the ChatChannel.

### `GetName()`

`deprecated flag set` Gets the ChatChannel's name.

**Returns** — `String` The name of the ChatChannel.

### `GetProfanity()`

`deprecated flag set` Checks whether the Profanity Filter is turned on for the ChatChannel.

**Returns** — `Boolean` Whether the Profanity Filter is turned on for the ChatChannel.

### `GetType()`

`deprecated flag set` Gets the ChatChannel's id number.

**Returns** — `Integer` The channel's id number.

### `IsCustom()`

`deprecated flag set` Determines if the ChatChannel is a player made channel.

**Returns** — `Boolean` Whether the ChatChannel is a player made channel or not.

### `IsModerator()`

`deprecated flag set` Checks if the player is a moderator of the ChatChannel.

**Returns** — `Boolean` Whether the player is a moderator of the ChatChannel.

### `IsMuted()`

`deprecated flag set` Determines if the player is muted in the ChatChannel.

**Returns** — `Boolean` Whether the player is muted or not.

### `IsOwner()`

`deprecated flag set` Determines if the player owns the ChatChannel.

**Returns** — `Boolean` Whether the player owns the ChatChannel.

### `Kick(strPlayerName)`

`deprecated flag set` Attempts to remove a player from the ChatChannel.

| parameter | type | meaning |
|---|---|---|
| `strPlayerName` | String | The name of the player that the function will attempt to remove from the ChatChannel. |

### `Leave()`

`deprecated flag set` Attempts to remove the player from the ChatChannel.

### `PassOwner(strPlayerName)`

`deprecated flag set` Attempts to make another player the owner of the ChatChannel.

| parameter | type | meaning |
|---|---|---|
| `strPlayerName` | String | The name of the player that the function will attempt to transfer ownership to. |

### `Post(strMessage, strSenderName, unitSpeaker, bTextBubble)`

`deprecated flag set` Attempts to send a string to all members of the ChatChannel.

| parameter | type | meaning |
|---|---|---|
| `strMessage` | String | The message that will be sent through the ChatChannel. |
| `strSenderName` | String | The name of the player that sent the message.  This value defaults to an empty string. |
| `unitSpeaker` | Unit | The unit that entered the message. |
| `bTextBubble` | Boolean | Whether a text bubble should be shown for this piece of text. |

### `RequestMembers()`

`deprecated flag set` Requests a list of the players in the ChatChannel.

### `Send(strMessage)`

`deprecated flag set` Sends a message over the ChatChannel.

| parameter | type | meaning |
|---|---|---|
| `strMessage` | String | The message that will be sent over the ChatChannel. |

### `SetData(oVariable)`

`deprecated flag set` Saves data in the ChatChannel.  This data can be accessed again by calling the GetData function.

| parameter | type | meaning |
|---|---|---|
| `oVariable` | Variable | The data that will be tied to the ChatChannel. |

### `SetModerator(strPlayerName, bMakeModerator)`

`deprecated flag set` Attempts to set a player's Moderator status in the ChatChannel.

| parameter | type | meaning |
|---|---|---|
| `strPlayerName` | String | The name of the player whose Moderator status will be updated by this function. |
| `bMakeModerator` | Boolean | Whether the player's Moderator flag should be granted (true) or removed (false).  This defaults to false if no value is passed in. |

### `SetMute(strPlayerName, bMuted)`

`deprecated flag set` Attempts to set a player's Mute status for the ChatChannel.

| parameter | type | meaning |
|---|---|---|
| `strPlayerName` | String | The player whose Mute flag should be changed by the function. |
| `bMuted` | Boolean | Whether the Mute flag should be added to the player (true) or removed (false).  This defaults to false if no value is passed in. |

### `SetPassword(strPassword)`

`deprecated flag set` Attempts to add a password to the ChatChannel or modify an existing one.

| parameter | type | meaning |
|---|---|---|
| `strPassword` | String | The ChatChannel's new password. |

### `SetProfanity(bProfanityFilterOn)`

`deprecated flag set` Attempts to change the ChatChannel's Profanity Filter status.

| parameter | type | meaning |
|---|---|---|
| `bProfanityFilterOn` | Boolean | Whether the Profanity Filter should be turned on or off for the channel. |

### `__eq(chanComparison)`

`deprecated flag set` Checks whether a ChatChannel is equal to the ChatChannel that called this function.

| parameter | type | meaning |
|---|---|---|
| `chanComparison` | ChatChannel | The ChatChannel that will be compared to the one that called this function. |

**Returns** — `Boolean` Whether the two ChatChannels are equal or not.

### `__gc()`

`deprecated flag set` ChatChannel's garbage collection function.  This will delete the ChatChannel from memory.

### `is(oVariable)`

`deprecated flag set` Checks whether a variable is a ChatChannel or not.

| parameter | type | meaning |
|---|---|---|
| `oVariable` | Variable | The function will verify that this variable is a ChatChannel. |

**Returns** — `Boolean` Whether the variable is a ChatChannel or not.

