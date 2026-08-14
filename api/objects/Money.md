# Money

*Object, documented by the client itself.*

**21 calls.** 1 carry `Deprecated="true"` — reported, not filtered, because that flag is set on entries known to be alive in 16042.

### `AddToTooltip(self, strText, strColor, strSize, strAlign)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `self` | XmlDocumentRef |  |
| `strText` | String |  |
| `strColor` | String |  |
| `strSize` | String |  |
| `strAlign` | String |  |

### `AppendToTooltip(self)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `self` | XmlDocumentRef |  |

### `GetAccountCurrencyType()`

*no description in the client's documentation*

### `GetAltType()`

*no description in the client's documentation*

### `GetAmount()`

Does a lua_pushinteger of the amount specified by currencyValue.

### `GetDenomAmounts()`

Does a lua_newtable with an index and the denom amounts.

### `GetDenomInfo()`

Does a lua_newtable with an index, amount, name, rate, textWidth, and sprite.

### `GetExchangeItem()`

*no description in the client's documentation*

### `GetMoneyString(bSkipZeros)`

Does a lua_pushwstring of the localized money amount.

| parameter | type | meaning |
|---|---|---|
| `bSkipZeros` | Boolean |  |

### `GetMoneyType()`

Does a lua_pushinteger of the type.

### `GetTypeString()`

Does a lua_pushwstring of the localized id type.

### `IsZero()`

Does a lua_pushboolean if the amount equals 0 specified by currencyValue.

### `Multiply()`

*no description in the client's documentation*

### `SetAccountCurrencyType()`

*no description in the client's documentation*

### `SetAltType()`

*no description in the client's documentation*

### `SetAmount(nNewAmount)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `nNewAmount` | Integer |  |

### `SetExchangeItem()`

*no description in the client's documentation*

### `SetMoneyType(nNewType)`

Sets the type to an enum ECurrencyType specified by nNewType.

| parameter | type | meaning |
|---|---|---|
| `nNewType` | Integer for enum ECurrencyType. A mapping is available earlier in the page. |  |

### `__eq()`

`deprecated flag set` *no description in the client's documentation*

### `is()`

*no description in the client's documentation*

### `new()`

*no description in the client's documentation*

