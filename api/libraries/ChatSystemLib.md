# ChatSystemLib

*Library, documented by the client itself.*

**8 calls.**

### `Command(strCommand)`

Processes the slash command that is sent through the function.

| parameter | type | meaning |
|---|---|---|
| `strCommand` | String | The command that the chat system will process, along with any parameters required by the command. |

### `GetChannels()`

Gets a list of channels that the player is in.

**Returns** — `ChatChannel` An array of ChatChannels that the player is currently in.

### `GetCommands()`

Gets a list of commands that are available to the player.

**Returns** — `String` An array that contains the names of all of the commands that are available to the player.

### `GetEmotes()`

Gets a list of all of the emote commands available to the player.

**Returns** — `String` An array of emote commands that the player can use.

### `JoinChannel(eChannel, strChannelName, strPassword, nOrder)`

Attempts to join the specified channel.

| parameter | type | meaning |
|---|---|---|
| `eChannel` | Integer | The channel that the player wants to join.  This value lines up with the ChatSystemLib.ChatChannel set of constants and is only used if the player is trying to join a channel that was set up by the game. |
| `strChannelName` | String | The name of the custom channel that the player is trying to join. |
| `strPassword` | String | The password that is required to join the chat channel. |
| `nOrder` | Integer | The channel number assigned to the new channel.  This will assign it to the next available channel number by default. |

### `PostOnChannel(eChannelId, strMessage, strSenderName, unitSource, bBubble)`

Posts a text message to a specific chat channel.

| parameter | type | meaning |
|---|---|---|
| `eChannelId` | Integer | The channel that the message will be posted to.  This value lines up with the ChatSystemLib.ChatChannel set of constants. |
| `strMessage` | String | The message that will be sent via the channel. |
| `strSenderName` | String | The name of the player or NPC that the channel will say that the message came from. |
| `unitSource` | Unit | The unit that the message came from. |
| `bBubble` | Boolean | Whether the unit should show a speech bubble or not. |

### `PrepareInfractionReport(idChatLine)`

Creates an IncidentReport based on a specified chat line.

| parameter | type | meaning |
|---|---|---|
| `idChatLine` | Integer | The id number for the chat line that the report will be created from. |

**Returns** — `rptChat` An IncidentReport that is populated with information pulled from the specified chat line.

### `SplitInput(strInput)`

Checks a string for a slash command and divides it into the command and its arguments.

| parameter | type | meaning |
|---|---|---|
| `strInput` | String | The string that the function will split. |

**Returns** — `Table` 

