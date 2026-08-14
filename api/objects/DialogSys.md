# DialogSys

*Object, documented by the client itself.*

Dialogs are the chat bubbles that appear when speaking with an NPC.  They can be used for accepting and turning in quests and other conversations with NPCs.  This library allows the player to get information on the currently displayed dialog.

**9 calls.**

### `End()`

Cancels the current dialog.

### `GetCommCreatureId()`

Gets the id number of the NPC associated with the current dialog.

**Returns** — `Integer` The id number of the NPC that is tied to the dialog.

### `GetNPC()`

Gets the unit associated with the dialog.

**Returns** — `Unit` The unit associated with the dialog.

### `GetNPCText(idQuest)`

Gets the string that contains the NPC's text.  This will also play any VO associated with this dialog.

| parameter | type | meaning |
|---|---|---|
| `idQuest` | Integer | The id number of the quest that the dialog is associated with. |

**Returns** — `string` The text that the dialog should show for the NPC.

### `GetResponseText()`

Gets the text that the player is responding to.

**Returns** — `String` The text that the player's responses o

### `GetResponses(idQuest)`

Gets a list of possible responses that the player can send.

| parameter | type | meaning |
|---|---|---|
| `idQuest` | Integer | The id number of the quest that is giving the player responses. |

**Returns** — `String` The list of responses the player can select for the dialog.

### `GetState()`

Gets the dialog's current state.

**Returns** — `Integer` The dialog's current state.  This value lines up with the DialogSys_DialogState set of constants.

> Carbine's own note: Need to make DialogSys.DialogState an enum.

### `GetViewableQuest(idQuest)`

Grabs the quest with the specified id if it is the one that the dialog is using.

| parameter | type | meaning |
|---|---|---|
| `idQuest` | Integer | The id number of the quest that the function will try to match with any quest that the current dialog is displaying. |

**Returns** — `Quest` The quest with the specified id.  If the dialog was not showing a quest or was showing a quest with a different id, this will be nil.

### `IsItemQuestGiver()`

Checks if the dialog was triggered by an item that is granting a quest.

**Returns** — `Boolean` Whether the quest is granted by an item or not.

