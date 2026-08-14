# GroupLib

*Library, documented by the client itself.*

**54 calls.**

### `AcceptInvite(strMessage)`

Runs m_clientGroup's AcceptInvite method with strMessage.

| parameter | type | meaning |
|---|---|---|
| `strMessage` | String |  |

### `AcceptMentoring()`

*no description in the client's documentation*

### `AcceptRequest()`

*no description in the client's documentation*

### `AmILeader()`

Does a lua_pushboolean if CharacterUnit is the leader.

### `CanGotoGroupInstance()`

*no description in the client's documentation*

### `CancelMentoring()`

*no description in the client's documentation*

### `CloseMentoringAOIDialog()`

*no description in the client's documentation*

### `CloseMentoringDialog()`

*no description in the client's documentation*

### `ConvertToRaid()`

*no description in the client's documentation*

### `DeclineInvite()`

*no description in the client's documentation*

### `DenyRequest()`

*no description in the client's documentation*

### `DisbandGroup(strMessage)`

Runs m_clientGroup's DisbandGroup method.

| parameter | type | meaning |
|---|---|---|
| `strMessage` | String |  |

### `GetGroupMaxSize()`

Does a lua_pushinteger of GetGroupmaxSize.

### `GetGroupMember(nGroupIndex)`

Does a PushGroupMemberToLua of the group member specified by nGroupIndex, else nil.

| parameter | type | meaning |
|---|---|---|
| `nGroupIndex` | Integer |  |

### `GetInstanceDifficulty()`

*no description in the client's documentation*

### `GetInvite()`

*no description in the client's documentation*

### `GetJoinRequestMethod()`

*no description in the client's documentation*

### `GetLootRules()`

*no description in the client's documentation*

### `GetMemberCount()`

Does a lua_pushinteger of GetMemberCounty.

### `GetMemberVisibility()`

*no description in the client's documentation*

### `GetMentoringList()`

*no description in the client's documentation*

### `GetReferralMethod()`

*no description in the client's documentation*

### `GetUnitForGroupMember(nGroupIndex)`

Returns a new unit that is a copy of the group member specified by nGroupIndex.

| parameter | type | meaning |
|---|---|---|
| `nGroupIndex` | Integer |  |

### `GotoGroupInstance()`

*no description in the client's documentation*

### `InGroup()`

Does a lua_pushboolean of InGroup.

### `InInstance()`

*no description in the client's documentation*

### `InInstanceWithMember()`

*no description in the client's documentation*

### `InRaid()`

*no description in the client's documentation*

### `Invite(strPlayerName, strRealmName, strMessage)`

Runs m_clientGroup's Invite method with strPlayerName, strRealmName, and strMessage.

| parameter | type | meaning |
|---|---|---|
| `strPlayerName` | String |  |
| `strRealmName` | String |  |
| `strMessage` | String |  |

### `IsMemberInGroupInstance()`

*no description in the client's documentation*

### `IsReadyCheckOnCooldown()`

*no description in the client's documentation*

### `Join()`

*no description in the client's documentation*

### `Kick(nIndex, strMessage)`

Runs m_clientGroup's Kick method specified by nIndex and with strMessage.

| parameter | type | meaning |
|---|---|---|
| `nIndex` | Integer |  |
| `strMessage` | String |  |

### `LeaveGroup(strMessage)`

Runs m_clientGroup's DenyInvite method with strMessage.

| parameter | type | meaning |
|---|---|---|
| `strMessage` | String |  |

### `PrepareInfractionReportInvite()`

*no description in the client's documentation*

### `Promote(nIndex)`

Runs m_clientGroup's Promote method specified by nIndex.

| parameter | type | meaning |
|---|---|---|
| `nIndex` | Integer |  |

### `ReadyCheck()`

*no description in the client's documentation*

### `SetCanMark()`

*no description in the client's documentation*

### `SetInstanceDifficulty()`

*no description in the client's documentation*

### `SetInvitePermission()`

*no description in the client's documentation*

### `SetJoinRequestMethod()`

*no description in the client's documentation*

### `SetKickPermission()`

*no description in the client's documentation*

### `SetLootRules()`

*no description in the client's documentation*

### `SetMainAssist()`

*no description in the client's documentation*

### `SetMainTank()`

*no description in the client's documentation*

### `SetOrder()`

*no description in the client's documentation*

### `SetRaidAssistant()`

*no description in the client's documentation*

### `SetReady()`

*no description in the client's documentation*

### `SetReferralMethod()`

*no description in the client's documentation*

### `SetRoleDPS()`

*no description in the client's documentation*

### `SetRoleHealer()`

*no description in the client's documentation*

### `SetRoleLocked()`

*no description in the client's documentation*

### `SetRoleTank()`

*no description in the client's documentation*

### `SwapOrder()`

*no description in the client's documentation*

