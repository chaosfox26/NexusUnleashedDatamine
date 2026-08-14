# CashWindow

*Window control, documented by the client itself.*

**10 calls.**

### `GetAMLDocForAmount(nAmount, bUseZeroes, clr, strFont)`

Does a lua_pushwstring of the result of the caller's GenerateAMLDoc specified by nAmount, bUseZeroes, clr, and strFont.

| parameter | type | meaning |
|---|---|---|
| `nAmount` | Integer |  |
| `bUseZeroes` | Boolean |  |
| `clr` | CColor |  |
| `strFont` | String |  |

### `GetAMLDocForPrice(nAmount1, nCurrencyType1, nAmount2, nCurrencyType2, bDisabled, strFont)`

Does a lua_pushwstring of the result of the caller's GenerateAMLDoc specified by the parameters. The price is calculated with the first four integers.

| parameter | type | meaning |
|---|---|---|
| `nAmount1` | Integer |  |
| `nCurrencyType1` | Integer |  |
| `nAmount2` | Integer |  |
| `nCurrencyType2` | Integer |  |
| `bDisabled` | Boolean |  |
| `strFont` | String |  |

### `GetAmount()`

Does a lua_pushinteger of the caller's amount.

### `GetAmountLimit()`

*no description in the client's documentation*

### `GetCurrency()`

Returns a new LuaGameTypes_Money of the caller's value.

### `GetDisplayWidth()`

*no description in the client's documentation*

### `SetAmount(nAmount, bInstant)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `nAmount` | Integer |  |
| `bInstant` | Boolean |  |

### `SetAmountLimit()`

*no description in the client's documentation*

### `SetExchangeItem()`

*no description in the client's documentation*

### `SetMoneySystem(nWhich)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `nWhich` | ECurrencyType |  |

