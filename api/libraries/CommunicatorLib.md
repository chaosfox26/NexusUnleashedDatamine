# CommunicatorLib

*Library, documented by the client itself.*

A library that provides addons a way to manipulate communicator messages sent by NPCs.

**12 calls.** 1 carry `Deprecated="true"` — reported, not filtered, because that flag is set on entries known to be alive in 16042.

### `CallContact(queCalling)`

Begin the communicator message with the NPC associated with the specified quest.

| parameter | type | meaning |
|---|---|---|
| `queCalling` | Quest | The quest that the player is trying to accept or turn in via the communicator. |

### `CallbackLastContact()`

Begin a communicator message with the NPC that sent the most recent message.

### `Close()`

Closes the communicator message that is currently open.

### `CommunicatorBackground_TheEntity()`

`deprecated flag set` *no description in the client's documentation*

### `GetMessageLayoutForQuest(queSource)`

Gets information regarding the layout of the portrait portion of a communicator message that is tied to a quest.

| parameter | type | meaning |
|---|---|---|
| `queSource` | Quest | The quest that the communicator message is tied to. |

**Returns** — `Table` 

> Carbine's own note: Lots of constants being used here.

### `GetMessageLayoutForSpam(idMessage)`

Gets information regarding how the background on a spam message should be layed out.

| parameter | type | meaning |
|---|---|---|
| `idMessage` | Integer | The id number for the spam message being queried. |

**Returns** — `Table` 

> Carbine's own note: Lots of constants to convert to enums.

### `GetPathMissionDelivered(idMessage)`

Gets the Path Mission that the player unlocks via the communicator message.

| parameter | type | meaning |
|---|---|---|
| `idMessage` | Integer | The id number for the communicator message. |

**Returns** — `PathMission` The Path Mission that is unlocked for the player via the communicator message with the specified id.

> Carbine's own note: May be depricated?

### `IgnoreCallback()`

Cancel an incoming communicator message.

### `IsVisible()`

Determines whether or not a communicator message is currently being displayed.

**Returns** — `Boolean` If the communicator message is being displayed, this value will be true.

### `PlaySpamVo(idMessage)`

Plays the voice over for the specified communicator message.

| parameter | type | meaning |
|---|---|---|
| `idMessage` | Integer | The id number for the communicator message that should play its Voice Over. |

**Returns** — `Boolean` Whether there was actually a voice over to play or not.

### `QueueMessage()`

*no description in the client's documentation*

### `QueueNextCall(idMessage)`

Add the specified message to the message queue.

| parameter | type | meaning |
|---|---|---|
| `idMessage` | Integer | The id number of the message that will be thrown on the queue. |

