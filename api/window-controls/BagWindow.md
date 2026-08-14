# BagWindow

*Window control, documented by the client itself.*

**28 calls.**

### `AreAnyItemsNew(nNewBagSlot)`

Does a lua_pushboolean if there are new items in a bag slot specified by nNewBagSlot.

| parameter | type | meaning |
|---|---|---|
| `nNewBagSlot` | Integer |  |

### `AssignBag(nData, nWhichBag)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `nData` | Integer |  |
| `nWhichBag` | Integer |  |

### `CanAssignBag(nSource, nDest)`

Does a lua_pushboolean if the bag can be assigned.

| parameter | type | meaning |
|---|---|---|
| `nSource` | Integer |  |
| `nDest` | Integer |  |

### `CanDropItemInBag(nData, nWhichBag)`

Does a lua_pushboolean if an item can be dropped in a bag.

| parameter | type | meaning |
|---|---|---|
| `nData` | Integer |  |
| `nWhichBag` | Integer |  |

### `CanRemoveBag(nWhichBag)`

Does a lua_pushboolean if the bag can be removed.

| parameter | type | meaning |
|---|---|---|
| `nWhichBag` | Integer |  |

### `DoAnyItemsBeginQuest()`

*no description in the client's documentation*

### `DropItemInBag(nData, nWhichBag)`

Does a lua_pushboolean of true if successful (was not trying to drop a bag in a bag or etc.)

| parameter | type | meaning |
|---|---|---|
| `nData` | Integer |  |
| `nWhichBag` | Integer |  |

### `GetBagCapacity()`

Does a lua_pushinteger of the caller's capacity.

### `GetBagId()`

Does a lua_pushinteger of the caller's id.

### `GetBagItem()`

*no description in the client's documentation*

### `GetInventoryIdForBag(nBag)`

Does a lua_pushinteger of the inventory id.

| parameter | type | meaning |
|---|---|---|
| `nBag` | Integer |  |

### `GetItem(nData)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `nData` | Integer |  |

### `GetTotalBagSlots()`

Does a lua_pushinteger of the total bag slots.

### `GetTotalEmptyBagSlots()`

Does a lua_pushinteger of the total empty bag slots.

### `IsBagEquipped(nWhichBag)`

Does a lua_pushboolean if a bag is equipped.

| parameter | type | meaning |
|---|---|---|
| `nWhichBag` | Integer |  |

### `IsItemABag(nData)`

Does a lua_pushboolean if nData is a bag.

| parameter | type | meaning |
|---|---|---|
| `nData` | Integer |  |

### `MarkAllItemsAsSeen()`

Runs the caller's MarkAllItems method.

### `SetBagId(nBagSlot)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `nBagSlot` | Integer |  |

### `SetBoxesPerRow(nBoxesPerRow)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `nBoxesPerRow` | Integer |  |

### `SetCannotUseColor()`

*no description in the client's documentation*

### `SetCannotUseSprite()`

*no description in the client's documentation*

### `SetItemSortComparer()`

*no description in the client's documentation*

### `SetNewItemOverlaySprite()`

*no description in the client's documentation*

### `SetNewQuestOverlaySprite()`

*no description in the client's documentation*

### `SetSort()`

*no description in the client's documentation*

### `SetSquareSize(nX, nY)`

Sets the square size of the caller to nX and nY.

| parameter | type | meaning |
|---|---|---|
| `nX` | Integer |  |
| `nY` | Integer |  |

### `StartSplitStack()`

*no description in the client's documentation*

### `SwapBagItems()`

Currently has no implementation

