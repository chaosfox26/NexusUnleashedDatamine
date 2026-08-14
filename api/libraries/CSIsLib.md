# CSIsLib

*Library, documented by the client itself.*

Allows the UI to interact with Client Side Interaction minigames, such as patern matching and timed clicking.

**7 calls.**

### `CSIProcessInteraction(mouseDown)`

Processes the user's input for the Client Side Interaction.  Different types of Client Side Interactions behave differently

| parameter | type | meaning |
|---|---|---|
| `mouseDown` | Boolean | Determines how to update the Client Side Interaction. For Yes/No Interactions:  true indicates that the user clicked yes, false indicates no For PressAndHold:  true indicates that the button was pressed down, false indicates that the button is up For RapidTapping: true indicates that the button was pressed down |

### `CancelActiveCSI()`

Stops the current Client Side Interaction

### `GetActiveCSI()`

Gets a table containing information on the active CSI.  Returns nil if there is no active CSI.

**Returns** — `Table` A table containing information on the current Client Side Interaction.

### `GetTimeRemainingForActiveCSI()`

Gets the time remaining before the user fails the current CSI.

**Returns** — `Float` The time remaining before the user fails, in seconds

### `IsCSIRunning()`

Determines if the active CSI has been started.

**Returns** — `Boolean` Whether the active CSI is running or not.

### `SelectCSIOption(option)`

Enters the user's input for the current Client Side Interaction.  This includes final keypad entries for the Keypad interactions and the Id of the buttons pressed in Memory interactions

| parameter | type | meaning |
|---|---|---|
| `option` | Integer | The number that was input for the Client Side Interaction.  This includes the number for keypad entries and the Id number for Memory selections |

### `StartActiveCSI()`

Starts the currently active CSI.

