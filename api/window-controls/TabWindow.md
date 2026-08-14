# TabWindow

*Window control, documented by the client itself.*

**6 calls.**

### `AttachTab(pAttachee, bStayOnTop)`

Attachs pAttachee to the caller and sets bStayOnTop.

| parameter | type | meaning |
|---|---|---|
| `pAttachee` | TabWindow |  |
| `bStayOnTop` | Bool |  |

### `Detach()`

Detaches the caller from its window.

### `IsAttached()`

*no description in the client's documentation*

### `IsAttachedToTab()`

*no description in the client's documentation*

### `IsLocked()`

Does a lua_pushboolean of the caller's IsLocked as a boolean.

### `Lock(bLock)`

Sets the caller's m_bLocked to bLock.

| parameter | type | meaning |
|---|---|---|
| `bLock` | Boolean |  |

