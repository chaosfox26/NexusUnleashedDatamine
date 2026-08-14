# CommodityOrder

*Object, documented by the client itself.*

A buy or sell order on the commodities exchange.

**21 calls.** 4 carry `Deprecated="true"` — reported, not filtered, because that flag is set on entries known to be alive in 16042.

### `CanPost()`

Determines if the CommodityOrder can be posted.

**Returns** — `Boolean` Whether the CommodityOrder can be posted or not.

### `Cancel()`

Cancels an active CommodityOrder

### `GetCount()`

Gets the number of items left in the CommodityOrder

**Returns** — `Integer` The number of items that the CommodityOrder will try to buy or sell before it ends.

### `GetExpirationTime()`

Gets the number of seconds between Jan 1st, 1970 and when the commodity order will expire.

**Returns** — `Integer` The number of seconds between Jan 1st, 1970 and when the commodity order will expire.

> Carbine's own note: We should really be getting the exact number of seconds before passing this to Lua

### `GetItem()`

Gets the item that the CommodityOrder is trying to buy or sell.

**Returns** — `Item` The item that the CommodityOrder is looking for or selling.

### `GetListTime()`

Gets the amount of time between Jan 1st, 1970 and when the Commodity Order was posted, in seconds.

**Returns** — `Time` The number of seconds between Jan 1st, 1970 and when the Commodity Order was posted

> Carbine's own note: Why are Time objects so bad!?!?!

### `GetPricePerUnit()`

Gets the amount of money that the CommodityOrder is buying or selling its associated item for.

**Returns** — `Money` How much the Commodity Order is trying to buy or sell its item for.

### `GetReservePricePerUnit()`

`deprecated flag set` *no description in the client's documentation*

> Carbine's own note: Unsure, but I don't think these have a reserve price.

### `GetTax()`

Gets the amount of money that the player has to pay to post a Sell order.

**Returns** — `Money` The amount of money that is required to post the sell order.

### `IsBuy()`

Determines if a CommodityOrder is a buy order or sell order.

**Returns** — `Boolean` If this is true, then the order is a buy order.  Otherwise, it's a sell order.

### `IsForceImmediate()`

Determines if the buy or sell order is set up to find the CommodityOrder of the opposite type with the best price for the same item so it completes immediately.

**Returns** — `Boolean` Whether the CommodityOrder is trying to buy or sell the item immediately.

### `IsPosted()`

Determines if the CommodityOrder is already posted or not.

**Returns** — `Boolean` Whether the CommodityOrder was already posted or not.

### `Post()`

`deprecated flag set` Attempts to post the CommodityOrder on the Commodities Market.

### `SetCount(nNewCount)`

Sets the number of items that the CommodityOrder is looking to buy or sell before it is completed.

| parameter | type | meaning |
|---|---|---|
| `nNewCount` | Integer | The value that the function will try to change the CommodityOrder's count to. |

**Returns** — `Boolean` Whether the count was successfully updated or not.

### `SetForceImmediate(bSellNow)`

Changes the CommodityOrder so it attempts to buy or sell its items for the best price when it is posted.

| parameter | type | meaning |
|---|---|---|
| `bSellNow` | Boolean | The value that the CommodityOrder's "force immediate" flag will be changed to. |

**Returns** — `Boolean` Whether the CommodityOrder's "force immediate" flag was successfully set or not.

### `SetPrices(monPrice)`

Sets the price that the CommodityOrder will try to buy or sell its items for.

| parameter | type | meaning |
|---|---|---|
| `monPrice` | Money | The amount that the commodity order will attempt to buy or sell its items for per unit. |

**Returns** — `Boolean` Whether the price was successfully set or not.

### `__eq(orderCompare)`

`deprecated flag set` Checks whether the given CommodityOrder is equal to the one that called this function.

| parameter | type | meaning |
|---|---|---|
| `orderCompare` | CommodityOrder | The CommodityOrder that will be compared to the one that called this function. |

**Returns** — `Boolean` Whether the two CommodityOrders are the same.

### `__gc()`

`deprecated flag set` The garbage collection function for the CommodityOrder.  This should never have to be called from Lua.

### `is(oVariable)`

Determines if a variable is a CommodityOrder or not.

| parameter | type | meaning |
|---|---|---|
| `oVariable` | Variable | The variable that the function will check. |

**Returns** — `Boolean` Whether the variable is a CommodityOrder or not.

### `newBuyOrder(itemTarget)`

Creates a new Buy order for the given item.

| parameter | type | meaning |
|---|---|---|
| `itemTarget` | Item | The item that the buy order will try to purchase. |

**Returns** — `CommodityOrder` The new buy order that was created.

### `newSellOrder(itemSelling)`

Creates a new Sell order for the given item.

| parameter | type | meaning |
|---|---|---|
| `itemSelling` | Item | The item that the sell order will attempt to sell. |

**Returns** — `CommodityOrder` A new Sell order for the given item.

