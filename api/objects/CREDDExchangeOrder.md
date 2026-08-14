# CREDDExchangeOrder

*Object, documented by the client itself.*

Individual orders on the CREDD Exchange.

**14 calls.** 2 carry `Deprecated="true"` — reported, not filtered, because that flag is set on entries known to be alive in 16042.

### `CanPost()`

Validates that the order is set for a valid number ( > 0 ) of credits and is not currently posted on the CREDD Exchange.

**Returns** — `Boolean` Whether the order can be posted on the CREDD Exchange or not.

### `Cancel()`

Removes the order from the CREDD Exchange.

### `GetExpirationTime()`

Gets the amount of time that the order will remain on the CREDD Exchange.

**Returns** — `Time` A Time object that states when the order will expire.

### `GetListTime()`

Gets the time that the order was posted.

**Returns** — `Time` A time object for when the order was posted.

### `GetPrice()`

Gets the price that the order was set for.

**Returns** — `Money` The amount and type of money that the order is requesting or offering for a CREDD.

### `IsBuy()`

Determines if the order is a buy order.

**Returns** — `Boolean` Whether the order is a buy order or not.

### `IsPosted()`

Checks if the order is posted on the CREDD Exchange.

**Returns** — `Boolean` Whether the order is posted on the CREDD Exchange or not.

### `Post()`

Posts the order on the CREDD Exchange.

### `SetPrice(monPrice)`

Sets the price that the order asks for once it is posted on the CREDD Exchange.

| parameter | type | meaning |
|---|---|---|
| `monPrice` | Money | The amount of money that the order will pay for / accept for CREDD. |

**Returns** — `Boolean` Whether the price was set successfully or not.

### `__eq(crdCompare)`

`deprecated flag set` Determines if another CREDDExchangeOrder is the same as this one.

| parameter | type | meaning |
|---|---|---|
| `crdCompare` | CREDDExchangeOrder | The CREDDExchangeOrder that is being compared to the one calling this function. |

**Returns** — `Boolean` Whether the two CREDDExchangeOrders are the same order or not.

### `__gc()`

`deprecated flag set` Forces the garbage collector to be called on the CREDDExchangeOrder that called the function.

### `is(oVariable)`

Checks if the variable that was passed in is a CREDDExchangeOrder.

| parameter | type | meaning |
|---|---|---|
| `oVariable` | Variable | The variable that this function will check. |

**Returns** — `Boolean` Whether the variable that was passed in is a CREDDExchangeOrder or not.

### `newBuyOrder()`

Creates a new CREDDExchangeOrder that is a buy order.

**Returns** — `CREDDExchangeOrder` A new CREDD Exchange buy order.

### `newSellOrder()`

Creates a new CREDDExchangeOrder that is a sell order.

**Returns** — `CREDDExchangeOrder` A new sell order for the CREDD Exchange.

