# CustomerSurveyTypeLib

*Object, documented by the client itself.*

Surveys that are sent out to players during betas and on the PTR.  These are disabled in the live game.

**12 calls.** 2 carry `Deprecated="true"` — reported, not filtered, because that flag is set on entries known to be alive in 16042.

### `Cancel()`

Cancels the current survey.  If the survey stopped the player from leaving the game, they will now be able to leave.

### `GetComment()`

Gets the text from the Comment section of the survey.

**Returns** — `String` The text that is in the Comment section of the survey.

### `GetQuestions(nIndex)`

Gets the text for the questions on the survey.

| parameter | type | meaning |
|---|---|---|
| `nIndex` | Integer | If this is passed in, the function will return a single string for the question at this index. |

**Returns** — `String` An array of all of the survey's questions.  If nIndex was set, this will be a single string and not an array.

### `GetResults(nIndex)`

Gets a list of the player's responses to the survey.

| parameter | type | meaning |
|---|---|---|
| `nIndex` | Integer | If this is passed in, the function will only return the result for the question at this index. |

**Returns** — `Integer` An array of integers with the player's responses to the survey.  If nIndex was set, then this will be a single integer instead of an array.

### `GetSurveyType()`

Gets the survey's type.

**Returns** — `CustomerSurveyLib.CodeEnumSurveyType` The survey's type.

### `GetTitle()`

Gets the survey's title.

**Returns** — `String` The survey's title.

### `SendResult()`

Attempts to send the CustomerSurvey to Carbine.

**Returns** — `Boolean` Whether the CustomerSurvey was successfully sent or not.

### `SetComment(strComment)`

Sets the survey's comment section.

| parameter | type | meaning |
|---|---|---|
| `strComment` | String | The text that will become the survey's comment. |

> Carbine's own note: This is returning 1 when it probably shouldn't be.

### `SetResults(arResponses)`

Sets a result for each question in the survey.

| parameter | type | meaning |
|---|---|---|
| `arResponses` | Integer | An array that contains responses for each of the survey's questions. |

> Carbine's own note: This is returning 1 for some reason.  It probably shouldn't be.

### `SetResults(nQuestion, nResponse)`

`deprecated flag set` Sets the result for a specific question in the survey.

| parameter | type | meaning |
|---|---|---|
| `nQuestion` | Integer | The index for the question that the response belongs to. |
| `nResponse` | Integer | The index of the response. |

> Carbine's own note: This returns 1 and it probably shouldn't.

### `__eq(svyCompare)`

`deprecated flag set` Determines if two CustomerSurveys are the same.

| parameter | type | meaning |
|---|---|---|
| `svyCompare` | CustomerSurveyTypeLib | The CustomerSurvey that is being compared to the one that called this function. |

**Returns** — `Boolean` Whether the two CustomerSurveys are the same or not.

### `isCustomerSurvey()`

Checks if this variable is a CustomerSurvey.

**Returns** — `Boolean` Whether this is a CustomerSurvey or not.

> Carbine's own note: This is a method.  If it wasn't a CustomerSurvey, it wouldn't be able to call this.

