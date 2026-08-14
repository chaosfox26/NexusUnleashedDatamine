# CustomerSurveyLib

*Library, documented by the client itself.*

A library that allows the player to interact with queued customer surveys.

**2 calls.**

### `GetPending(nIndex)`

Gets a pending customer survey that the player has not filled out.

| parameter | type | meaning |
|---|---|---|
| `nIndex` | Integer | The index of the survey that will be returned.  If no value is provided, the function will get the first pending survey. |

**Returns** — `CustomerSurveyTypeLib` The pending survey.

### `GetPendingCount()`

Gets the number of surveys that are waiting to be filled out by the player.

**Returns** — `Integer` The number of surveys that are waiting to be filled out by the player.

