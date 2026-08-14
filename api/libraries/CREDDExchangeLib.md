# CREDDExchangeLib

*Library, documented by the client itself.*

This library is one of the primary ways that the player interacts with the CREDD Exchange.  This does not include creating and fulfilling orders, which is handled by the ActionConfirmButton.

**3 calls.**

### `CancelOrder(crdOrder)`

Removes a CREDD Exchange Order from the Exchange.

| parameter | type | meaning |
|---|---|---|
| `crdOrder` | CREDDExchangeOrder | The order that the player wishes to cancel. |

### `GetCREDDHistory()`

Requests player's buy and sell history from the server.

### `RequestExchangeInfo()`

Requests a list for the CREDD Exchange's stats and CREDDExchangeOrders.

