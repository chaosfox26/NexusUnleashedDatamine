# Quest

*Object, documented by the client itself.*

**85 calls.** 4 carry `Deprecated="true"` — reported, not filtered, because that flag is set on entries known to be alive in 16042.

### `Abandon()`

Runs the caller's AbandonQuest method.

### `AcceptShare()`

Runs m_clientGroup's AcceptSharedQuest method with true.

### `CalcRewardXP()`

Does a lua_pushinteger of GetXp.

### `CanAbandon()`

Does a lua_pushboolean of IsInAbandonableState.

### `CanCompleteObjective(iReq)`

Does a lua_boolean of CanCompleteObjective specified by iReq.

| parameter | type | meaning |
|---|---|---|
| `iReq` | Integer |  |

### `CanShare()`

Does a lua_pushboolean of CanShare.

### `DisplayObjectiveProgressBar()`

*no description in the client's documentation*

### `GetActiveQuest()`

*no description in the client's documentation*

### `GetCallbackList()`

*no description in the client's documentation*

### `GetCategory()`

*no description in the client's documentation*

### `GetChatLinkString()`

*no description in the client's documentation*

### `GetColoredDifficulty()`

*no description in the client's documentation*

### `GetCompletedSummary()`

Does a lua_pushstring of the quest completed summary after a UCS2ToUTF8.

### `GetCompletionObjectiveShortText()`

*no description in the client's documentation*

### `GetCompletionObjectiveText()`

*no description in the client's documentation*

### `GetConLevel()`

Does a lua_pushinteger of conLevel.

### `GetContactInfo()`

Does several updates and lua pushes, including creatureId, IdName, and spriteName at the end.

### `GetDistance()`

*no description in the client's documentation*

### `GetEpisode()`

*no description in the client's documentation*

### `GetGroup()`

Does a lua_pushstring of the group name after a UCS2ToUTF8.

### `GetId()`

Does a lua_pushinteger of the id.

### `GetIntroductionText()`

*no description in the client's documentation*

### `GetMapRegions()`

*no description in the client's documentation*

### `GetMinLevel()`

*no description in the client's documentation*

### `GetMoreInfoText()`

*no description in the client's documentation*

### `GetObjectiveCompleted(iReq)`

Does a lua_pushinteger of GetNumCompleted specified by iReq, or 0 if null.

| parameter | type | meaning |
|---|---|---|
| `iReq` | Integer |  |

### `GetObjectiveCount()`

Does a lua_pushinteger of GetNumObjectives.

### `GetObjectiveDescription(iReq)`

Does a lua_pushstring of a UCS2ToUTF8 description specified by iReq, or empty string if null.

| parameter | type | meaning |
|---|---|---|
| `iReq` | Integer |  |

### `GetObjectiveMaxTime()`

*no description in the client's documentation*

### `GetObjectiveNeeded(iReq)`

Does a lua_pushinteger of GetNumRequired specified by iReq, or 0 if null.

| parameter | type | meaning |
|---|---|---|
| `iReq` | Integer |  |

### `GetObjectiveShortDescription()`

*no description in the client's documentation*

### `GetObjectiveTimeRemaining(iReq)`

Does a lua_pushinteger of IsObjectiveTimed of an objective specified by iReq.

| parameter | type | meaning |
|---|---|---|
| `iReq` | Integer |  |

### `GetPathQuestType()`

*no description in the client's documentation*

### `GetQuestItemCount()`

Does a lua_pushinteger of the quest item count.

### `GetQuestItemData(iIndex)`

Does a lua_newtable with item and num specified by iIndex.

| parameter | type | meaning |
|---|---|---|
| `iIndex` | Integer |  |

### `GetQuestTimeRemaining()`

Does a lua_pushinteger of GetQuestTimeRemaining.

### `GetRepeatPeriod()`

*no description in the client's documentation*

### `GetRewardData()`

Does two lua_newtables describing fields relating to the reward and money of the quest.

### `GetSpell()`

*no description in the client's documentation*

### `GetState()`

Does a lua_pushinteger of the quest state.

### `GetSubType()`

*no description in the client's documentation*

### `GetSummary()`

Does a lua_pushstring of the quest summary after a UCS2ToUTF8.

### `GetTitle()`

Does a lua_pushstring of the quest title after a UCS2ToUTF8.

### `GetTrackBlinkTime()`

Does a lua_pushnumber of blink time / 1000.0.

### `GetTradeskillSchematicsRequired()`

*no description in the client's documentation*

### `GetType()`

*no description in the client's documentation*

### `GetVisibleObjectiveData()`

Does a lua_newtable with index, description, needed, completed, and isReward.

### `GetZoneId()`

*no description in the client's documentation*

### `IsAbleToAdvanceInRaid()`

*no description in the client's documentation*

### `IsActiveQuest()`

Does a lua_pushboolean if quest is active for the player and tracked.

### `IsBreadcrumb()`

*no description in the client's documentation*

### `IsCommunicatorReceived()`

*no description in the client's documentation*

### `IsCommunicatorReceivedFromRec()`

*no description in the client's documentation*

### `IsContract()`

*no description in the client's documentation*

### `IsIgnored()`

*no description in the client's documentation*

### `IsImbuementQuest()`

*no description in the client's documentation*

### `IsInLog()`

Does a lua_pushboolean of IsVisibleInLog.

### `IsInactive()`

*no description in the client's documentation*

### `IsKnown()`

Does a lua_pushboolean if quest state is known.

### `IsMentioned()`

Does a lua_pushboolean if quest data is mentioned.

### `IsMoreInfoNonSequential()`

*no description in the client's documentation*

### `IsObjectiveTimed(iReq)`

Does a lua_pushboolean of IsObjectiveTimed of an objective specified by iReq.

| parameter | type | meaning |
|---|---|---|
| `iReq` | Integer |  |

### `IsOnlyAdvanceInPvp()`

*no description in the client's documentation*

### `IsOptionalForEpisode()`

*no description in the client's documentation*

### `IsPathQuest()`

*no description in the client's documentation*

### `IsQuestTimed()`

Does a lua_pushboolean of IsQuestTimed.

### `IsSelectedInLog()`

Does a lua_pushboolean of IsSelectedInLog.

### `IsTracked()`

Does a lua_pushboolean if quest data is tracked.

### `ObjectiveIsReward(iReq)`

Does a lua_boolean if iReq is < 0 or equal to the number of objectives.

| parameter | type | meaning |
|---|---|---|
| `iReq` | Integer |  |

### `ObjectiveIsVisible(iReq)`

Does a lua_boolean of IsObjectiveVisible specified by iReq, or empty string if null.

| parameter | type | meaning |
|---|---|---|
| `iReq` | Integer |  |

### `PulseTrackBlinkTime(uTime)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `uTime` | Float - that is immediately * 1000.0 and cast to a UINT32 |  |

### `RejectShare()`

Runs m_clientGroup's AcceptSharedQuest method with false.

### `SetActiveQuest(bActive)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `bActive` | Boolean |  |

### `SetSelectedInLog()`

Runs the quest log's SetSelectedQuestId method with the caller.

### `SetTracked(bTracked)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `bTracked` | Boolean |  |

### `Share()`

Runs m_clientGroup's ShareQuest with pLuaQuest's id.

### `ShowHintArrow()`

*no description in the client's documentation*

### `ToggleActiveQuest()`

*no description in the client's documentation*

### `ToggleIgnored()`

*no description in the client's documentation*

### `ToggleTracked()`

*no description in the client's documentation*

### `__eq()`

`deprecated flag set` *no description in the client's documentation*

### `__gc()`

`deprecated flag set` *no description in the client's documentation*

### `__gt()`

`deprecated flag set` *no description in the client's documentation*

### `__lt()`

`deprecated flag set` *no description in the client's documentation*

### `is()`

*no description in the client's documentation*

