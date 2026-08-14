# AbilityItemWindow

*Window control, documented by the client itself.*

**6 calls.**

### `GetAbilityDescription()`

Does a lua_pushwstring of the ability's description from the tool tip id, or "" if the ability is not found.

### `GetAbilityId()`

Does a lua_pushinteger of the caller's m_iSpellId.

### `GetAbilityName()`

Does a lua_pushwstring of the ability's name from the name id, or "" if the ability is not found.

### `GetAbilityTierId()`

*no description in the client's documentation*

### `SetAbilityId(nSpellId)`

Sets the caller's ability id to nSpellId.

| parameter | type | meaning |
|---|---|---|
| `nSpellId` | Integer |  |

### `SetSelected(bSelected)`

Sets the caller's m_bSelected boolean to bSelected.

| parameter | type | meaning |
|---|---|---|
| `bSelected` | Boolean |  |

