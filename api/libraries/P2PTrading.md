# P2PTrading

*Library, documented by the client itself.*

**16 calls.**

### `AcceptInvite()`

Does a lua_pushinteger of P2PTradeAcceptInvite.

### `AddItem(nInventoryItem)`

Does a lua_pushinteger of the result of P2PTradeAddItem of item location specified by nInventoryItem.

| parameter | type | meaning |
|---|---|---|
| `nInventoryItem` | Integer |  |

### `AmICommitted()`

Does a lua_pushboolean of GetCharacterUnit's trade bCommited.

### `CanInitiateTrade(unitP)`

Does a lua_pushinteger of the result of CanInitiateP2PTrade, or a boolean false if null.

| parameter | type | meaning |
|---|---|---|
| `unitP` | CUnit |  |

### `CancelTrade()`

Does a lua_pushinteger of the result of P2PTradeCancel.

### `DeclineInvite()`

Does a lua_pushinteger of P2PTradeDeclineInvite.

### `GetMyTradeMoney()`

*no description in the client's documentation*

### `GetPartnerTradeMoney()`

*no description in the client's documentation*

### `GetTradeItems()`

Does a lua_newtable with an index and tradeable items.

### `InitiateTrade(unitP)`

Does a lua_pushinteger of the result of P2PTradeInitiate.

| parameter | type | meaning |
|---|---|---|
| `unitP` | CUnit |  |

### `IsPartnerCommitted()`

Does a lua_pushboolean of the trade partner's bCommited.

### `IsTrading()`

Does a lua_pushboolean of IsP2PTrading.

### `PrepareInfractionReport()`

*no description in the client's documentation*

### `RemoveItem(nInventoryItem)`

Does a lua_pushinteger of the result of P2PTradeRemoveItem of item location specified by nInventoryItem.

| parameter | type | meaning |
|---|---|---|
| `nInventoryItem` | Integer |  |

### `SetMoney()`

*no description in the client's documentation*

### `UnCommit()`

*no description in the client's documentation*

