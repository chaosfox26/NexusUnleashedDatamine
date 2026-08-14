# MacrosLib

*Library, documented by the client itself.*

**8 calls.**

### `CreateMacro()`

Does a lua_pushinteger of the new macro's id.

### `DeleteMacro(nId)`

Runs DeleteMacro specified by nId.

| parameter | type | meaning |
|---|---|---|
| `nId` | Integer |  |

### `DoMacro(nId)`

Runs DoMacro specified by nId.

| parameter | type | meaning |
|---|---|---|
| `nId` | Integer |  |

### `GetMacro(nId)`

Does a LuaPushMacro specified by nId.

| parameter | type | meaning |
|---|---|---|
| `nId` | Integer |  |

### `GetMacroIconList()`

Does a lua_newtable with an index and spritenames of the macro icons.

### `GetMacrosList()`

Does a LuaPushMacro with an index of the macros.

### `SaveMacros()`

Does a lua_pushboolean of the save's result.

### `SetMacroData(nId, bGlobal, strName, strIcon, strCommands)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `nId` | Integer |  |
| `bGlobal` | Boolean |  |
| `strName` | String |  |
| `strIcon` | String |  |
| `strCommands` | String |  |

