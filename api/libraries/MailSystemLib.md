# MailSystemLib

*Library, documented by the client itself.*

**26 calls.**

### `AtMailbox()`

Does a lua_pushboolean if CharacterUnit is in range of a mailbox.

### `DeleteMessage(pEmail)`

Runs pEmail's DeleteMessage.

| parameter | type | meaning |
|---|---|---|
| `pEmail` | CClientEmail | (May be passed by default with : operator) |

### `DeleteMultipleMessages()`

*no description in the client's documentation*

### `GetAttachmentMaxCount()`

*no description in the client's documentation*

### `GetExpirationTime(pEmail)`

Does a lua_pushnumber of the email's expiration time, or nil if null.

| parameter | type | meaning |
|---|---|---|
| `pEmail` | CClientEmail | (May be passed by default with : operator) |

### `GetIdStr()`

*no description in the client's documentation*

### `GetInbox()`

Does a lua_newtable of the inbox contents.

### `GetItemFromInventoryId(nSlot)`

Returns a new instance of an item that is a copy of an Inventory item specified by nSlot. // NOTE: This function should be moved to a LuaGameLibrary_InventorySystem

| parameter | type | meaning |
|---|---|---|
| `nSlot` | Integer |  |

### `GetMessageCharacterLimit()`

*no description in the client's documentation*

### `GetMessageInfo(pEmail)`

Does a lua_newtable of the email's info, or nil if null.

| parameter | type | meaning |
|---|---|---|
| `pEmail` | CClientEmail | (May be passed by default with : operator) |

### `GetNameCharacterLimit()`

*no description in the client's documentation*

### `GetRealmCharacterLimit()`

*no description in the client's documentation*

### `GetSendCost()`

*no description in the client's documentation*

### `GetSenderType()`

*no description in the client's documentation*

### `GetSubjectCharacterLimit()`

*no description in the client's documentation*

### `Is()`

*no description in the client's documentation*

### `IsThereUnreadMail()`

Does a lua_pushboolean if there is unread mail.

### `MarkAsRead(pEmail)`

Runs pEmail's MarkAsRead.

| parameter | type | meaning |
|---|---|---|
| `pEmail` | CClientEmail | (May be passed by default with : operator) |

### `MarkMultipleMessagesAsRead()`

*no description in the client's documentation*

### `PayCoD()`

*no description in the client's documentation*

### `PrepareInfractionReport()`

*no description in the client's documentation*

### `ReturnToSender()`

*no description in the client's documentation*

### `TakeAllAttachments(pEmail)`

Runs pEmail's TakeAllAttachments.

| parameter | type | meaning |
|---|---|---|
| `pEmail` | CClientEmail | (May be passed by default with : operator) |

### `TakeAllAttachmentsFromMultipleMessages()`

*no description in the client's documentation*

### `TakeAttachment()`

// Currently has no implementation

### `TakeMoney()`

*no description in the client's documentation*

