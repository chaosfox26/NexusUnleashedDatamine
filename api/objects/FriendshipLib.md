# FriendshipLib

*Object, documented by the client itself.*

A library that contains functions for interacting with the game's Friend and Account Friend systems.  

**41 calls.**

### `AccountAddByEmail(strAddress, strNote)`

Attempts to send an account friend invite to the account that is registered to the specified email address.

| parameter | type | meaning |
|---|---|---|
| `strAddress` | String | The email address associated with the account that the player wants to send the invite to. |
| `strNote` | String | A note that will be sent to the player that receives the account friend invite. |

### `AccountAddByUpgrade(idFriend, strNote)`

Attempts to send an invitation to upgrade a Friend to an Account Friend.

| parameter | type | meaning |
|---|---|---|
| `idFriend` | Integer | The Friend id of the player that will receive the Account Friend Invite. |
| `strNote` | String | A note that the person who receives the Account Friend invite will see in the invite. |

### `AccountInviteMarkSeen()`

Marks an account invite as "Seen" by the system.

### `AccountInviteRespond(idFriend, bAccepted)`

Sends a response to an Account Invite that the player has received.

| parameter | type | meaning |
|---|---|---|
| `idFriend` | Integer | The id of the friend invite that the player is responding to. |
| `bAccepted` | Boolean | Whether the player accepted the invite or not. |

### `AccountRemove(idFriend)`

Removes the specified Account Friend from the player's friends' list

| parameter | type | meaning |
|---|---|---|
| `idFriend` | Integer | The Friend id of the Account Friend that the player wants to remove. |

### `AddByGroupIndex(eType, nMemberIdx)`

Attempts to change the friendship status of a player in your current group.

| parameter | type | meaning |
|---|---|---|
| `eType` | Integer | The friendship status that the player wants to add to the specified group member.  This value lines up with the FriendshipLib.CharacterFriendshipType set of constants. |
| `nMemberIdx` | Integer | The index of the player within the group. |

### `AddByName(eFriendshipType, strName, strRealmName, strNote)`

Changes the friendship type with the  player with the specified name.

| parameter | type | meaning |
|---|---|---|
| `eFriendshipType` | Integer | The friendship type that the player will change to.  This value lines up with FriendshipLib.CharacterFriendshipType set of constants. |
| `strName` | String | The name of the player whose friendship type will be updated. |
| `strRealmName` | String | The name of the realm that the player is on.  This is only necessary for players that are not on the same realm. |
| `strNote` | String | A note that will be sent to the specified player if the friendship type is either Friend or Account Friend.  This note will be visible in the invite that the player receives. |

### `AddBySuggested()`

*no description in the client's documentation*

### `AddByUnit()`

*no description in the client's documentation*

### `GetAccountById()`

*no description in the client's documentation*

### `GetAccountInviteById()`

*no description in the client's documentation*

### `GetAccountInviteList()`

*no description in the client's documentation*

### `GetAccountList()`

*no description in the client's documentation*

### `GetById()`

*no description in the client's documentation*

### `GetInviteById()`

*no description in the client's documentation*

### `GetInviteList()`

*no description in the client's documentation*

### `GetList()`

*no description in the client's documentation*

### `GetLocations()`

*no description in the client's documentation*

### `GetPersonalStatus()`

*no description in the client's documentation*

### `GetSuggestedById()`

*no description in the client's documentation*

### `GetSuggestedList()`

*no description in the client's documentation*

### `GetUnitById()`

*no description in the client's documentation*

### `InviteMarkSeen()`

*no description in the client's documentation*

### `IsLoaded()`

*no description in the client's documentation*

### `IsLocked()`

*no description in the client's documentation*

### `NeighborInvite()`

*no description in the client's documentation*

### `PrepareInfractionReportInvite()`

*no description in the client's documentation*

### `Remove()`

*no description in the client's documentation*

### `RespondToInvite()`

*no description in the client's documentation*

### `SetAutoResponseMessages()`

*no description in the client's documentation*

### `SetAwayFromKeyboardMessage()`

*no description in the client's documentation*

### `SetDoNotDisturbMessage()`

*no description in the client's documentation*

### `SetFriendPrivateData()`

*no description in the client's documentation*

### `SetLock()`

*no description in the client's documentation*

### `SetNote()`

*no description in the client's documentation*

### `SetPersonalIgnoreStrangersState()`

*no description in the client's documentation*

### `SetPersonalPresenceState()`

*no description in the client's documentation*

### `SetPublicDisplayName()`

*no description in the client's documentation*

### `SetPublicNote()`

*no description in the client's documentation*

### `SetType()`

*no description in the client's documentation*

### `VisitResidence()`

*no description in the client's documentation*

