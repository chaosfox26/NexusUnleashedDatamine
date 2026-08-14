# Events, from the client's own documentation

**915 events**, with the arguments each one delivers.

Compare with `docs/client-systems/EVENTS.md`, which lists the 1,067 events the client's
own UI actually *registers handlers for*. An event documented here but never handled
there may still fire; an event handled there is definitely real.

### `AbilitiesWindowClose`

Fires when the Limited Action Set Builder window closes.

| argument | type | meaning |
|---|---|---|
| `bAtTrainer` | Boolean | Returns whether or not the player is at a training station when the window was closed. |

### `AbilityBookChange`

Fires when a change is made to the Action Set Builder.

### `AbilitySelected`

### `AcceptProgressInput`

Fires when CSIs turn player input on and off.  This is only used for the "Memory" CSI.

| argument | type | meaning |
|---|---|---|
| `bShouldAccept` | Boolean | Whether or not the CSI will accept user input. |

### `AccountCREDDRedeemed`

### `AccountCurrencyChanged`

### `AccountEntitlementUpdate`

Fires when a change is made to the current account's entitlements.

### `AccountInventoryUpdate`

Fires when the Account Inventory for the current account has changed.

### `AccountInventoryWindowShow`

### `AccountOperationResults`

| argument | type | meaning |
|---|---|---|
| `eOperation` | Integer |  |
| `eResult` | CREDDExchangeLib.CodeEnumAccountOperationResult | The result of the operation. |

> Carbine's own note: Need more info on what this is.

### `AccountPendingItemTook`

### `AccountPendingItemsClaimed`

### `AccountPendingItemsGifted`

### `AccountPendingItemsReturned`

### `AccountPendingItemsUpdate`

Fires when items are added or removed from the pending list for the player's account inventory.

### `AccountPrivilegeRestrictionUpdate`

### `AccountSupportTicketResult`

Informs the player if the ticket that they submitted successfully made it to the server or not.

| argument | type | meaning |
|---|---|---|
| `channelGM` | Channel | The chat channel where the message will be displayed. |
| `bSuccess` | Boolean | Whether or not the ticket was successfully sent. |

> Carbine's own note: Need more info on this one.  It seems to be the channel to display the success/fail message and whether or not it succeeded or failed, but it's hard to tell

### `AchievementGranted`

Fires when an achievement is completed.

| argument | type | meaning |
|---|---|---|
| `achComplete` | Achievement | The achievement that was completed. |

### `AchievementUpdated`

Fires when an progress is made towards an achievement's objective.

| argument | type | meaning |
|---|---|---|
| `achUpdated` | Achievement | The achievement that has been updated. |

### `ActionBarDescriptionSpell`

Displays information for a spell on the actionbar.

| argument | type | meaning |
|---|---|---|
| `splDisplayed` | Spell | The spell currently being displayed. |
| `tEffects` | Table | A table containing information about the spell. |
| `tReasons` | Table | A list of flags that may be referenced by Lua. |

> Carbine's own note: This is being fired to Lua all the time.  Why?  Make the Spell4CastResult table available since tReasons uses it?

### `ActionBarNonSpellShortcutAddFailed`

Fires when a non-spell fails to be placed on the action bar.

### `ActionSetError`

Fires when the player attempts to save an invalid action set.

| argument | type | meaning |
|---|---|---|
| `eResult` | ActionSetLib.CodeEnumLimitedActionSetResult | The message describing why there is an error in the current action set. |

### `ActivateCCStateStun`

Fires when the player is stunned.

| argument | type | meaning |
|---|---|---|
| `eChosenDirection` | Unit.CodeEnumCCStateStunVictimGameplay | The direction the player needs to press to get out of the CC State. |

### `ActorClicked`

### `ActorMouseEnter`

### `ActorMouseExit`

### `AddSpellShortcut`

Fires whenever a spell is granted to the player as part of a quest, challenge, public event, or path mission.

| argument | type | meaning |
|---|---|---|
| `splDisplayed` | Spell | The spell that is granted to the player. |
| `eReason` | Integer | The reason the spell was granted to the player. |
| `idSource` | Integer | The id of the quest, quest objective, challenge, public event, public event objective, or path mission that granted the spell to the player. |

> Carbine's own note: ESpellShortcutReason needs to be exposed to Lua for eReason.

### `AlertMailInfo`

Fires when the player gets new mail.

| argument | type | meaning |
|---|---|---|
| `tMessageInfo` | Table | A table containing information about the new piece of mail. |

### `AlternateTargetUnitChanged`

Fires when the player's focus target changes.

| argument | type | meaning |
|---|---|---|
| `unitFocus` | Unit | The player's new focus target. |

### `AnimEnded`

| argument | type | meaning |
|---|---|---|
| `strAnimDataId` | String |  |

### `AnimStarted`

| argument | type | meaning |
|---|---|---|
| `strAnimDataId` | String |  |

### `AnimStopped`

| argument | type | meaning |
|---|---|---|
| `strAnimDataId` | String |  |

### `AnimationFinished`

### `AppearanceChanged`

Fires whenever the player updates a costume, purchases a dye job on their equipment, or purchases a character customization change.

### `ApplicationWindowSizeChanged`

### `ApplyCCState`

Fires when a CC state is applied to a unit.

| argument | type | meaning |
|---|---|---|
| `eState` | Unit.CodeEnumCCState | A number representing the CC applied to the player. |
| `unitTarget` | Unit | The unit that is affected by the CC state. |

### `AttackMissed`

An event that is fired when a unit dodges an attack from another unit

| argument | type | meaning |
|---|---|---|
| `unitCaster` | Unit | The unit that performed the attack |
| `unitTarget` | Unit | The unit that was the target of the attack |
| `eMissType` | Integer | An enum that describes why the attack missed.  Uses the  GameLib.CodeEnumMissType enum list |

### `AuctionWindowClose`

Fires whent he player moves out of range of an Auctioneer NPC.

### `AvailableMail`

Fires mail is added to the player's inbox.

| argument | type | meaning |
|---|---|---|
| `arMail` | Integer | An array of mail IDs for the mail added to the player's inbox. |
| `bIsNewMail` | Boolean | Whether or not the messages added to the player's inbox are "new". |

> Carbine's own note: How is this different from AlertMailInfo?

### `BankSlotPurchased`

Fires when the player successfully purchases a bank slot.

### `BarberClose`

### `BarberOpen`

### `BonusEventsChanged`

### `BreathChanged`

Fires whenever the player's breath meter should change value.

| argument | type | meaning |
|---|---|---|
| `nCurrentBreath` | Integer | The player's current breath. |
| `nMaxBreath` | Integer | The maximum amount of breath the character can have. |

### `Breath_FlashEvent`

Fires when the player has run out of breath and starts taking damage.

| argument | type | meaning |
|---|---|---|
| `fHealthPercentRemaining` | Float | The percentage of remaining health the player has. |

### `BuffAdded`

### `BuffRemoved`

### `BuffUpdated`

### `ButtonCheck`

| argument | type | meaning |
|---|---|---|
| `eMouseButton` | EMouseButton | The mouse button being clicked. |

### `ButtonDown`

| argument | type | meaning |
|---|---|---|
| `eMouseButton` | EMouseButton | The mouse button being clicked. |

### `ButtonHoldBegin`

| argument | type | meaning |
|---|---|---|
| `eMouseButton` | EMouseButton | The mouse button being clicked. |

### `ButtonSignal`

| argument | type | meaning |
|---|---|---|
| `eMouseButton` | EMouseButton | The mouse button being clicked. |

### `ButtonUncheck`

| argument | type | meaning |
|---|---|---|
| `eMouseButton` | EMouseButton | The mouse button being clicked. |

### `ButtonUp`

| argument | type | meaning |
|---|---|---|
| `eMouseButton` | EMouseButton | The mouse button being clicked. |

### `ButtonUpCancel`

| argument | type | meaning |
|---|---|---|
| `eMouseButton` | EMouseButton | The mouse button being clicked. |

### `BuybackItemsUpdated`

Fires when there is a change in the list of Buyback items at a vendor.

### `CREDDExchangeInfoResults`

Returns results for the CREDDExchangeLib.RequestExchangeInfo() call from the server.

| argument | type | meaning |
|---|---|---|
| `tStats` | Table |  |
| `arOrders` | CREDDExchangeOrder | A table with all the CREDD buy and sell orders. |

### `CREDDExchangeOperationResults`

> Carbine's own note: Does not appear to be fired from code.

### `CREDDExchangeOrderSubmitted`

### `CREDDExchangeWindowClose`

Fires when the player changes their interaction target from a CREDD Exchange to another NPC, when a player moves far enough away from a CREDD Exchange, or after Event_CancelCREDDExchange() is called.

### `CREDDOperationHistoryResults`

Returns the results of the CREDDExchangeLib.GetCREDDHistory() call.

| argument | type | meaning |
|---|---|---|
| `tHistory` | Table |  |

### `CREDDRedeemResult`

### `CSIKeyPressed`

When the client side interaction input key is pressed or released

| argument | type | meaning |
|---|---|---|
| `bKeyDown` | Boolean | True when the key is down; false when the key is up. |

### `CanVacuumChange`

Fires when the player's ability to vacuum nearby loot has changed due to loot dropping, being vacuumed, or being removed from the world.

| argument | type | meaning |
|---|---|---|
| `bCanVacuum` | Boolean | Whether or not the ability to vacuum is active. |

### `CardFlipped`

### `CashWindowAmountChanged`

### `CasterResurrectedPlayer`

Fires when the current player is revived by another player.

| argument | type | meaning |
|---|---|---|
| `strCasterName` | String | The name of the player that resurrected the player. |

### `ChallengeAbandon`

Fires whenever the player abandons a challenge, clears their challenge data, or reqests that the challenge is abandoned via the ChallengesLib.ShowAbandonChallenge() function

| argument | type | meaning |
|---|---|---|
| `idChallenge` | Integer | The id number of the challenge that was abandoned. |
| `strDescription` | String | The challenge's fail message. |

### `ChallengeActivate`

Fires whenever a challenge is activated

| argument | type | meaning |
|---|---|---|
| `clgActivated` | Challenge | The challenge that was activated. |

### `ChallengeAreaRestriction`

Fires when the player attempts to start/retry a challenge while they are outside of the challenge's starting area.

| argument | type | meaning |
|---|---|---|
| `idChallenge` | Integer | The ID number for the challenge. |
| `strHeader` | String | The challenge's title. |
| `strDescription` | String | The message that should be displayed so the player knows they are outside of the challenge area. |
| `fDuration` | Float | The length of time (in seconds) that the message is displayed. |

### `ChallengeCompleted`

Fires whenever the player completes a challenge.

| argument | type | meaning |
|---|---|---|
| `idChallenge` | Integer | The id number of the challenge. |
| `strHeaderText` | String | The channel's name. |
| `strDescription` | String | The challenge's description text. |
| `nDuration` | Integer | The amount of time (in milliseconds) that the Challenge Complete window will appear on the screen. |

### `ChallengeCompletedSound`

Fires whenever we should play the sound for a completed challenge.

| argument | type | meaning |
|---|---|---|
| `idChallenge` | Integer | The id number of the challenge that was completed. |

### `ChallengeCooldownActive`

Fires when the player attempts to start a challenge that is on cooldown.

| argument | type | meaning |
|---|---|---|
| `idChallenge` | Integer | The id number of the challenge. |
| `strHeader` | String | The challenge's title. |
| `strErrorMsg` | String | The error message that should be shown for this event. |
| `nDuration` | Integer | The duration that the error message should be shown for (in milliseconds). |

> Carbine's own note: Possibly depricated?  It's hard to tell since I think we block the case where we'd receive this event in Lua

### `ChallengeFailArea`

Fires when a challenge fails because the player left the area.

| argument | type | meaning |
|---|---|---|
| `chalFailed` | Challenge | The challenge that was failed. |
| `strHeader` | String | The header for the "Fail" notification. |
| `strDescription` | String | The body of the "Fail" notification. |
| `nDuration` | Integer | How long the "Fail" notification should be shown (in milliseconds). |

### `ChallengeFailGeneric`

Fires if a player fails a challenge for reasons other than time or leaving the area.

| argument | type | meaning |
|---|---|---|
| `chalFailed` | Challenge | The challenge that the player failed. |
| `strHeader` | String | The header for the "Fail" notification. |
| `strDescription` | String | The body of the "Fail" notification. |
| `nDuration` | Integer | How long the "Fail" notification should be shown (in milliseconds). |

### `ChallengeFailSound`

Fires when the "Fail" sound should be played for a challenge.

| argument | type | meaning |
|---|---|---|
| `idChallenge` | Integer | The id number for the challenge that the sound is played for. |

### `ChallengeFailTime`

Fires when the player fails a challenge due to time running out before any tiers were reached.

| argument | type | meaning |
|---|---|---|
| `chalFailed` | Challenge | The challenge that was failed. |
| `strHeader` | String | The header for the "Fail" notification. |
| `strDescription` | String | The body of the "Fail" notification. |
| `nDuration` | Integer | How long the "Fail" notification should be displayed (in milliseconds). |

### `ChallengeFlashStartLocation`

Fires whenever the player leaves the challenge area and the challenge has a valid start location.  It tells the UI that it should attempt to lead the player back to the start location.

| argument | type | meaning |
|---|---|---|
| `idChallenge` | Integer | The id number for the challenge that fired the event. |
| `strDescription` | String | The message that should be communicated to the player when the UI receives this message. |
| `fDuration` | Float | How long the start location should flash, in seconds. |
| `tLocation` | Table | The coordinates that the player should be directed towards. |

### `ChallengeLeftArea`

Fires whenever the player leaves the challenge area.

| argument | type | meaning |
|---|---|---|
| `idChallenge` | Integer | The id number for the challenge that fired the event. |
| `strHeader` | String | The header that should be shown on the challenge tracker after this event is fired. |
| `strDescription` | String | The message that should be shown to the player after the event is fired. |
| `bShow` | Boolean |  |

### `ChallengeRewardListReady`

Fires when we have the information we need to populate the challenge's rewards.

| argument | type | meaning |
|---|---|---|
| `idChallenge` | Integer | The challenge that was completed. |
| `nRewardTier` | Integer | The challenge tier that the player completed.  1 is Bronze, 2 is Silver, 3 is Gold. |

> Carbine's own note: We could really use an enum for reward tiers

### `ChallengeRewardReady`

Fires when the challenge's reward has been determined.

| argument | type | meaning |
|---|---|---|
| `idChallenge` | Challenge | The id number of the challenge that was completed. |
| `nReward` | Integer | The reward number that the player received from the challenge. |

### `ChallengeShareTimedOut`

Fires when the player runs out of time to accept a shared challenge.

| argument | type | meaning |
|---|---|---|
| `idChallenge` | Integer | The id number of the challenge that was shared. |

> Carbine's own note: Is sharing challenges even a thing?

### `ChallengeShared`

Fired when a challenge is shared with the player.

| argument | type | meaning |
|---|---|---|
| `idChallenge` | Integer | The id number of the challenge being shared. |
| `idSharingPlayer` | Integer | The id number of the player who shared the challenge. |
| `nTimeToAccept` | Integer | The amount of time the player has to accept the challenge (in seconds). |

> Carbine's own note: Is this even possible anymore?

### `ChallengeTierAchieved`

Fires whenever the player completes a challenge tier.

| argument | type | meaning |
|---|---|---|
| `idChallenge` | Integer | The id number of the challenge. |
| `nTierCompleted` | Integer | The challenge tier that was completed.  1 = Bronze, 2 = Silver, 3 = Gold. |

> Carbine's own note: We could really use an enum for the tiers

### `ChallengeTimeUpdated`

### `ChallengeTypeAlreadyActive`

Fires whenever the player activates a challenge when they already have an active challenge of the same type.

| argument | type | meaning |
|---|---|---|
| `idActivating` | Integer | The id of the challenge that was activated. |
| `idAbandoned` | Integer | The id of the challenge that was abandoned. |

### `ChallengeUnlocked`

Fires whenever a new challenge is unlocked.

| argument | type | meaning |
|---|---|---|
| `clgUnlocked` | Challenge | The challenge that was unlocked. |

### `ChallengeUpdated`

Fires whenever progress is made on a challenge, when the player leaves and re-enters a challenge area, and whenever the player selects a challenge reward to receive their tier roll bonus.

| argument | type | meaning |
|---|---|---|
| `idChallenge` | Integer | The id number of the challenge that was updated. |

### `ChangeWorld`

Fires when the player is moved to a different zone or instance.

### `ChannelUpdate_Crafting`

### `ChannelUpdate_Loot`

### `ChannelUpdate_Progress`

### `CharacterBack`

### `CharacterCreateFailed`

Fires whenever the server rejected the player's attempt at character creation.

### `CharacterCreated`

Fires when the player's character is first placed in the world.

### `CharacterDelete`

### `CharacterDisabled`

### `CharacterEldanAugmentationsReset`

> Carbine's own note: Does not seem to fire when resetting the player's AMPs.  It is most likely depricated.

### `CharacterEldanAugmentationsUpdated`

Fires whenever the player selects an AMP or purchases an AMP reset.

> Carbine's own note: We may want to rename this event from Eldan Augmentations to AMPs

### `CharacterEntitlementUpdate`

> Carbine's own note: Need a way to test this to see how it works.

### `CharacterFlagsUpdated`

Fires whenever the player's state flags are updated.  Changing any of the following states will trigger this event: PvP Flag Block Friendships Limit Hazard Rez Ignore Duel Requests Hide Top Guild Holomark Hide Left Guild Holomark Hide Right Guild Holomark Hide Back Guild Holomark Disable Character Display Guild Holomark Near Require Name Change

### `CharacterList`

### `CharacterRecustomizationResult`

### `CharacterRename`

### `CharacterSelectFail`

### `CharacterUnlockedInlaidEldanAugmentation`

Fires whenever the player unlocks a new AMP.

### `ChatAccountTellFailed`

Fires whenever the player tries to send an account whisper to an invalid player.

| argument | type | meaning |
|---|---|---|
| `channelWhisper` | ChatChannelLib | The chat channel that the player tried to whisper from.  This should always be the "Account Whisper" channel. |
| `strName` | String | The name of the player who was intended to receive the account whisper. |

### `ChatAction`

Fires whenever an action is taken on a custom chat channel.  These actions include passing the owner of the channel to another player, adding or removing the Moderator status from a player, muting and unmuting a player, kicking a player from the channel, and adding/removing a password to the channel.

| argument | type | meaning |
|---|---|---|
| `channelSource` | ChatChannelLib | The channel that the action was applied to. |
| `eAction` | Integer | The action that fired the event.  This value lines up with the ChatSystemLib.ChatChannelAction set of constants. |
| `strActor` | String | The player who performed the action. |
| `strActedOn` | String | The target of the action. |

> Carbine's own note: ChatSystemLib.ChatChannelAction should be an enum, not int constants

### `ChatFlag`

> Carbine's own note: Unsure if this is a thing.  We aren't handling it anywhere in Lua and there's no API calls to get the channel's flags

### `ChatJoin`

Fires when the player joins a chat channel.

| argument | type | meaning |
|---|---|---|
| `chanJoined` | ChatChannelLib | The chat channel that the character just joined. |

### `ChatJoinResult`

Fires whenever the player fails to join a channel.

| argument | type | meaning |
|---|---|---|
| `chanJoin` | ChatChannelLib | The channel that the player attempted to join. |
| `eResult` | Integer | The reason why the player failed to join the channel.  This value lines up with the ChatSystemLib.ChatChannelResult system of int constants. |

> Carbine's own note: We need an enum for ChatSystemLib.ChatChannelResult

### `ChatLeave`

Fires when the player leaves or is kicked from a chat channel.

| argument | type | meaning |
|---|---|---|
| `chanLeft` | ChatChannelLib | The channel that the player left. |
| `bKicked` | Boolean | Whether or not the player was kicked from the channel |
| `bBanned` | Boolean | Whether or not the player was banned from the channel. |

### `ChatList`

Fired in response to the ChatChannel:RequestMembers() function.  Passes the channel that was polled for its members.

| argument | type | meaning |
|---|---|---|
| `channelSource` | ChatChannel | The channel that is being polled for its members. |

> Carbine's own note: Is this still needed since we have the channel:GetMembers() function?   We still have a handler for it, but nothing is calling Channel:RequestMembers() anymore.

### `ChatMessage`

Fires when a message is sent on a chat channel

| argument | type | meaning |
|---|---|---|
| `channelSource` | ChatChannel | The channel where the message should be displayed. |
| `tMessageInfo` | Table |  |

### `ChatReWhisper`

Fires when the Chat Re-Whisper keybinding is pressed.

> Carbine's own note: We are not using this at the moment, making the keybinding do nothing.

### `ChatReply`

Fires when the player uses the ChatReply keybinding.

### `ChatResult`

Fires when there is an error with a chat message that the player tried to send.

| argument | type | meaning |
|---|---|---|
| `channelSource` | ChatChannel | The channel where the original message was sent. |
| `eResult` | Integer | The error with the message that was sent.  This value lines up with the ChatSystemLib.ChatChannelResult constants. |

> Carbine's own note: Enum for ChatSystemLib.ChatChannelResult constants?

### `ChatTellFailed`

Fires whenever the player makes an unsuccessful tell

| argument | type | meaning |
|---|---|---|
| `channelSource` | ChatChannel | The channel that the player attempted to use for the failed tell.  This is likely the Whisper channel. |
| `strName` | String | The name of the player you attempted to send a whisper to. |

### `ChatZoneChange`

Fires when the Zone channel changes, such as when a player moves from one zone to another.

| argument | type | meaning |
|---|---|---|
| `strNewZone` | String | The name of the new zone that the player has moved into. |

### `CinematicsCancel`

| argument | type | meaning |
|---|---|---|
| `nParam` | Integer |  |

> Carbine's own note: This event doesn't seem to be called anywhere in C++

### `CinematicsNotify`

Notifies the player that a cinematic is starting

| argument | type | meaning |
|---|---|---|
| `strMessage` | String | The notification message that should be displayed. |
| `idParam` | Integer | The message's id. |

> Carbine's own note: Event doesn't seem to be fired.

### `CityDirectionClear`

Removes the specified direction marker from the map.

| argument | type | meaning |
|---|---|---|
| `idDirection` | Integer | The ID number for the direction that should be cleared. |

### `CityDirectionMarked`

Fires when a city direction marker is displayed on the map / minimap

| argument | type | meaning |
|---|---|---|
| `tLocationInfo` | Table |  |

### `CityDirectionsClose`

Fires when the City Directions UI closes.

### `CityDirectionsList`

Fires when the player interacts with a guard in a capital city.

### `ClearSpellThreshold`

Fires when the "Window of Opportunity" for spells with multiple uses (ex. Stalker's Nano Field, Esper's Psychic Frenzy) should close.  This can happen either because the timer ran out, the player used another ability, or the player activated the max number of times.

| argument | type | meaning |
|---|---|---|
| `idSpell` | Integer | The id number of the spell whose threshold needs to close. |

### `CloseCraftingWindow`

Fired when the UI explicity calls the Event_CloseCraftingWindow() function.

### `CloseTradeskillTrainerWindow`

Fired if the player interacts with another unit while interacting with a tradeskill trainer.  It's also fired when the Event_CloseTradeskillTrainerWindow() function is called in Lua.

### `CloseVendorWindow`

Fired when the player interacts with another unit while the Vendor UI is up, moves out of range of a vendor while the Vendor UI is open, or the Event_CloseVendorWindow() function is explicitly called in Lua.

### `ColorChanged`

Fired whent he player selects a color from the ColorPicker window

| argument | type | meaning |
|---|---|---|
| `crNewColor` | CColor | The color that was selected when this event was fired. |

> Carbine's own note: Uses CColor instead of ApolloColor

### `ColorChanged`

Fired whent he player selects a color from the ColorPicker window

| argument | type | meaning |
|---|---|---|
| `crNewColor` | CColor | The color that was selected when this event was fired. |

> Carbine's own note: Uses CColor instead of ApolloColor

### `CombatFloaters_Configure`

Fires when the player uses the /cfconfig command in chat

> Carbine's own note: We aren't using this anywhere in Lua.  Do we still want to keep it?

### `CombatLogAbsorption`

Fires whenever a unit is granted an absorb shield.

| argument | type | meaning |
|---|---|---|
| `tCombatLogInfo` | Table |  |

### `CombatLogBuildSwitch`

Fires when the player switches to a different action set.

| argument | type | meaning |
|---|---|---|
| `tLogInfo` | Table |  |

### `CombatLogCCState`

Fires whenever a player enters a crowd control state.

| argument | type | meaning |
|---|---|---|
| `tLogInfo` | Table |  |

> Carbine's own note: Why does bHideFloater usually return nil instead of false?

### `CombatLogCCStateBreak`

Fires when the player breaks out of a CC state.

| argument | type | meaning |
|---|---|---|
| `tLogInfo` | Table |  |

### `CombatLogCrafting`

Fires when the player finishes crafting an item using a non-simple craft schematic.

| argument | type | meaning |
|---|---|---|
| `tLogInfo` | Table |  |

### `CombatLogDamage`

Fires when a unit takes damage.

| argument | type | meaning |
|---|---|---|
| `tLogInfo` | Table |  |

> Carbine's own note: ESpellEffectType needs to be exposed to Apollo.  Need to find out wtf nRawDamage is.

### `CombatLogDamageShields`

### `CombatLogDatacube`

Fires when the player interacts with a datacube, journal, or TFBTF entry in the world.

| argument | type | meaning |
|---|---|---|
| `tLogInfo` | Table |  |

> Carbine's own note: Need to change DatacubeLib.DatacubeType int contstants to enums.

### `CombatLogDeath`

Fires when the player dies.

| argument | type | meaning |
|---|---|---|
| `tLogInfo` | Table |  |

> Carbine's own note: Why are we returning a table with only one element?

### `CombatLogDeflect`

Fires when a unit deflects an attack.

| argument | type | meaning |
|---|---|---|
| `tLogInfo` | Table |  |

### `CombatLogDelayDeath`

Fires when death missed his bus?

### `CombatLogDispel`

Fires when a buff or debuff is dispelled.

| argument | type | meaning |
|---|---|---|
| `unitCaster` | Unit | The unit that used the spell that triggered the event. |
| `unitCasterOwner` | Unit | The unit who owns unitCaster.  This only applies if unitCaster is a pet. |
| `unitTarget` | Unit | The unit that the buff/debuff was dispelled from. |
| `unitTargetOwner` | Unit | The unit that owns unitTarget.  This only applies if unitTarget is a pet. |
| `bRemoveSingleInstance` | Boolean | Whether or not a single stack of the buff is removed. |
| `nInstancesRemoved` | Integer | The number of stacks of the buff that are removed from the unit. |
| `splRemovedSpell` | Spell | The spell that was removed from the unit. |

> Carbine's own note: Is this used anymore? Why have bRemoveSingleInstance if we're listing the number removed?

### `CombatLogDurabilityLoss`

Fires when a player's equipment loses a point of durability.

| argument | type | meaning |
|---|---|---|
| `unitCaster` | Unit | The unit wearing the equipment that lost durability.  This will always be the current player. |
| `nAmount` | Integer | The amount of durability that was lost. |

> Carbine's own note: Does not appear to be fired anymore?

### `CombatLogElderPointsLimitReached`

Fires when the player reaches the daily cap of elder points.

| argument | type | meaning |
|---|---|---|
| `unitCaster` | Unit | The unit that reached their Elder Point Cap.  This should always be the current player. |

### `CombatLogEndGameCurrencies`

Fires whenever the player gains non-credit currencies.

| argument | type | meaning |
|---|---|---|
| `unitCaster` | Unit | The unit that gained the currency.  This is always the current player. |
| `monLoot` | Money | The currency that was gained. |

### `CombatLogExperience`

Fires whenever the player gaines experience or elder points.

| argument | type | meaning |
|---|---|---|
| `unitCaster` | Unit | The unit that gained the experience or elder points.  This will always be the current player. |
| `nXP` | Integer | The base amount of experience gained. |
| `nRestXP` | Integer | The amount of experience gained from the player's rested bonus. |
| `nEP` | Integer | The amount of elder points the player gained. |
| `nRestEP` | Integer | The amount of elder points gained from the player's rested bonus. |

### `CombatLogExtracting`

> Carbine's own note: What fires this?

### `CombatLogFallingDamage`

Fires whenever the player takes fall damage

| argument | type | meaning |
|---|---|---|
| `unitCaster` | Unit | The unit that took the falling damage.  This should always be the current player. |
| `nAmount` | Integer | The amount of damage the player took. |

### `CombatLogHeal`

Fires whenever a unit gets healed.

| argument | type | meaning |
|---|---|---|
| `unitCaster` | Unit | The unit who used the spell that caused the heal. |
| `unitCasterOwner` | Unit | The owner of unitCaster.  This only applies if unitCaster is a pet. |
| `unitTarget` | Unit | The unit that received the heal. |
| `unitTargetOwner` | Unit | The unit that owns unitTarget.  This only applies if unitTarget is a pet. |
| `nHealAmount` | Integer | The amount missing health that was healed for the target.  This value does not include overheals. |
| `nOverheal` | Integer | The amount of overhealing done by the spell. |
| `eCombatResult` | GameLib.CodeEnumCombatResult | A number representing any special things that went on with the spell, such as a critical hit. |
| `splCallingSpell` | Spell | The spell that was used for the heal. |
| `eEffectType` | Spell.CodeEnumSpellEffectType | The effect the spell has on the target. |

### `CombatLogImmunity`

> Carbine's own note: Unsure of a case where this will fire.

### `CombatLogInterrupted`

Fires when a unit is interrupted by a spell.  This includes if the player interrupted their own spell cast.

| argument | type | meaning |
|---|---|---|
| `unitCaster` | Unit | The unit that cast the spell that caused the interrupt. |
| `unitCasterOwner` | Unit | The owner of unitCaster.  This only applies if unitCaster is a pet. |
| `unitTarget` | Unit | The unit that was interrupted. |
| `unitTargetOwner` | Unit | The owner of unitTarget.  This only applies if unitTarget is a pet. |
| `eCombatResult` | Integer | The result the spell that was used. |
| `splCallingSpell` | Spell | The spell that was interrupted. |
| `splInterruptingSpell` | Spell | The spell that caused the interrupt. |
| `eCastResult` | Spell.CodeEnumCastResult | Explains why the spell was interrupted. |
| `strCastResult` | String | A string explaining why the spell was interrupted. |

### `CombatLogItemDestroy`

Fires when the player destroys an item.

| argument | type | meaning |
|---|---|---|
| `unitCaster` | Unit | The unit that destroyed the item. |
| `itemDestroyed` | Item | The item that was destroyed. |

### `CombatLogKillPVP`

Fires when a player assists in a PvP kill.

| argument | type | meaning |
|---|---|---|
| `unitCaster` | Unit | The unit that assisted in the kill. |
| `unitCasterOwner` | Unit | The unit that owns unitCaster.  This only applies if unitCaster is a pet. |
| `unitTarget` | Unit | The unit that was killed in PvP. |
| `unitTargetOwner` | Unit | The unit that owns unitTarget.  This only applies if unitTarget was a pet. |
| `eCombatResult` | GameLib.CodeEnumCombatResult | The result of using the ability. |
| `splCallingSpell` | Spell | The spell that killed the player. |

> Carbine's own note: Description based on use in CombatLog.  If it's wrong, then we should look into it.

### `CombatLogKillStreak`

Fires when the player gets multiple kills in quick succession.

| argument | type | meaning |
|---|---|---|
| `unitCaster` | Unit | The unit that got the kill streak.  This should either be the current player or one of their pets. |
| `unitCasterOwner` | Unit | The unit that owns unitCaster.  This only applies if unitCaster is a pet. |
| `eStatType` | CombatFloater.CodeEnumCombatMomentum | The type of streak the player is on. |
| `nStreakAmount` | Integer | The player's current streak count. |

### `CombatLogLAS`

Fires when a player changes their Limited Action Set.

| argument | type | meaning |
|---|---|---|
| `unitCaster` | Unit | The unit that changed their Limited Action Set.  This should always be the current player. |

### `CombatLogLifeSteal`

### `CombatLogLoot`

Fires whenever a player loots money or an item.  This will fire for each visible "item" looted in the world and each item distributed to the player via the group's looting system.

| argument | type | meaning |
|---|---|---|
| `unitCaster` | Unit | The unit that received the money or item. |
| `monLoot` | Money | The money object for the money that was looted.  If there was no money looted, this will be nil. |
| `itemLoot` | Item | The item that was looted.  If no item was looted in this event, this will be nil. |
| `nItemAmount` | Integer | The stack size of itemLooted for this event.  If money was looted in this event and not an item, this value will be 0. |

### `CombatLogModifyInterruptArmor`

Fires whenever a player gains or loses interrupt armor.

| argument | type | meaning |
|---|---|---|
| `unitCaster` | Unit | The unit who caused a player's interrupt armor to change |
| `unitCasterOwner` | Unit | The owner of unitCaster.  This is nil if unitCaster is not a pet. |
| `unitTarget` | Unit | The unit whose interrupt armor was changed. |
| `unitTargetOwner` | Unit | The player who owns unitTarget.  This is nil if unitTarget is not a pet. |
| `nAmount` | Integer | The change in the unit's interrupt armor. |

### `CombatLogModifying`

| argument | type | meaning |
|---|---|---|
| `unitCaster` | Unit | The unit that fired this event. |
| `itemHost` | Item |  |
| `itemRemoved` | Item |  |
| `itemAdded` | Item |  |

> Carbine's own note: Unknown functionality.  Possibly depricated.

### `CombatLogMount`

Fires if the player mounts or dismounts.

| argument | type | meaning |
|---|---|---|
| `unitCaster` | Unit | The player that mounted. |
| `bDismounted` | Boolean | Whether or not the player dismounted. |

### `CombatLogMultiHeal`

### `CombatLogMultiHit`

### `CombatLogMultiHitShields`

### `CombatLogPet`

Fires whenever a player summons or despawns a pet, or a pet dies.

| argument | type | meaning |
|---|---|---|
| `unitCaster` | Unit | The unit who used the ability to summon, kill, or despawn the pet. |
| `unitTarget` | Unit | The pet that was spawned. |
| `unitTargetOwner` | Unit | The unit that owns the pet.  This is the current player. |
| `bDismissed` | Boolean | Whether or not the pet was despawned. |
| `bKilled` | Boolean | Whether or not the pet was killed. |
| `eCombatResult` | GameLib.CodeEnumCombatResult | The end result of the spell that was used. |

### `CombatLogReflect`

### `CombatLogResurrect`

Fires whenever the player is rezzed.  This includes all methods of resurrection.

| argument | type | meaning |
|---|---|---|
| `unitCaster` | Unit | The unit that was resurrected. |

### `CombatLogStealth`

Fires whenever the player enters or leaves stealth.

| argument | type | meaning |
|---|---|---|
| `unitCaster` | Unit | The unit whose stealth state has changed. |
| `bExiting` | Boolean | Whether or not the player left stealth. |

### `CombatLogString`

Fires whenever a string is directly written in the combat log.  This event will always accompany another combat log event

| argument | type | meaning |
|---|---|---|
| `strLogMessage` | String | The message printed to the combat log. |

### `CombatLogTransference`

Fires whenever a spell does damage and heals the user at the same time.

| argument | type | meaning |
|---|---|---|
| `unitCaster` | Unit | The unit who used the spell that triggered the event. |
| `unitCasterOwner` | Unit | The player that owns unitCaster.  This only applies if unitCaster was a pet. |
| `unitTarget` | Unit | The unit that was affected by the spell that triggered this event. |
| `unitTargetOwner` | Unit | The unit who owns unitTarget.  This only applies if unitTarget is a pet. |
| `eCombatResult` | GameLib.CodeEnumCombatResult | The effect of the spell that triggered the event. |
| `splCallingSpell` | Spell | The spell that triggered the event. |
| `nDamageAmount` | Integer | The amount of damage done to unitTarget. |
| `eDamageType` | GameLib.CodeEnumDamageType | The type of damage done by the spell. |
| `nShield` | Integer | The amount of damage done to the target's shields. |
| `nAbsorption` | Integer | The amount of damage done to the target's absorption shield. |
| `nOverkill` | Integer | The amount of damage done over the target's max health. |
| `bTargetVulnerable` | Boolean | Whether or not the target is in a "Moment of Opportunity" state. |
| `tHealData` | Table |  |

### `CombatLogVitalModifier`

| argument | type | meaning |
|---|---|---|
| `unitCaster` | Unit | The unit that used the spell that caused the event to fire. |
| `unitCasterOwner` | Unit | The unit that owns unitCaster.  This only applies if unitCaster is a pet. |
| `unitTarget` | Unit | The unit that was the target of the spell. |
| `unitTargetOwner` | Unit | The unit that owns unitTarget.  This only applies if unitTarget is a pet. |
| `eCombatResult` | GameLib.CodeEnumCombatResult | The spell's effect on the target. |
| `splCallingSpell` | Spell | The spell that caused the event to fire. |
| `nAmount` | Integer | How much the specified vital is modified by. |
| `eVitalType` | GameLib.CodeEnumVital | The vital that is modified. |
| `bShowCombatLog` | Boolean | Whether or not this event should appear in the combat log. |

> Carbine's own note: Unsure what fires this.

### `CombatMomentum`

Fires whenever one of the player's "momentum" bonuses increases.

| argument | type | meaning |
|---|---|---|
| `eType` | CombatFloater.CodeEnumCombatMomentum | The type of momentum bonus that was increased. |
| `nCount` | Integer | The current count for the momentum bonus. |
| `strMessage` | String | A string for displaying the event. |

### `ComboBoxSelectionChanged`

### `ComboBoxSelectionChanging`

### `CommitCustomizationChangesResult`

### `CommodityAuctionFilledPartial`

Fires whenever a buy or sell order on the Commodities Exchange is partially filled by another player.

| argument | type | meaning |
|---|---|---|
| `nFilledCount` | Integer | How many items in the order were actually bought or sold. |
| `orderFilled` | CommodityOrder | The order that was partially filled. |

### `CommodityAuctionRemoved`

Fires whenever a buy or sell order is removed from the Commodities Exchange.

| argument | type | meaning |
|---|---|---|
| `eReason` | MarketplaceLib.AuctionEventType | The reason the auction was removed from the Commodities Exchange.  This will either be Fill, Expire, or Cancel. |
| `orderRemoved` | CommodityOrder | The order that was removed from the Commodities Exchange. |

### `CommodityAuctionsDisabled`

Fired when the Commodity Exchange gets disabled or enabled.

| argument | type | meaning |
|---|---|---|
| `bDisabled` | Boolean | Whether or not this event was fired because the Commodity Exchange is disabled. |

### `CommodityInfoResults`

Fires for each item returned by MarketplaceLib.RequestCommodityInfo().  It contains information on all of the buy and sell orders out for the item.

| argument | type | meaning |
|---|---|---|
| `idItem` | Integer | The id number for the item that the results are referencing. |
| `tStats` | Table |  |
| `arOrders` | CommodityOrder | A listing of all of the buy and sell orders open for the item. |

### `Communicator_EndIncoming`

Fires when an incoming communicator times out and becomes a "missed call"

### `Communicator_ShowQuestMsg`

| argument | type | meaning |
|---|---|---|
| `idMsg` | Integer | The id number for the message. |
| `idCreature` | Integer | The id number for the NPC that sent the communicator message. |
| `queShown` | Quest | The quest that the message will offer the player. |
| `strText` | String | The quest text that the message will show. |

### `Communicator_ShowQueuedMsg`

### `Communicator_ShowSpamMsg`

Fires if a communicator message is sent to the player but does not have a valid Quest tied to it.

| argument | type | meaning |
|---|---|---|
| `idMsg` | Integer | The id number of the communicator message. |
| `idCreature` | Integer | The id number of the creature that sent the message. |
| `strText` | String | The text that should be shown in the message. |
| `bPriorty` | Boolean | Whether the message should have priority over other messages. |

> Carbine's own note: Does not seem to be handled by the UI.  Will it ever be fired?

### `Communicator_SpamVOEnded`

Fires when a communicator's voice over ends.

> Carbine's own note: Like ShowSpamMsg, idk that this is actually used anymore.

### `Communicator_UpdateCallback`

Fires whenever a communicator message gets updated in response to a player abandoning, botching, or completing a quest.

| argument | type | meaning |
|---|---|---|
| `bHasCallback` | Boolean | Whether the player gets an immediate communicator message or not. |
| `bRedeemsQuest` | Boolean | Whether the callback allows the player to turn in a quest or not. |

### `CommunityRegistrarClose`

> Carbine's own note: This is new...haven't seen anything about this.

### `CommunityRegistrarOpen`

> Carbine's own note: This is new...haven't seen anything about this.

### `ContractBoardClose`

### `ContractBoardOpen`

### `ContractFloater`

### `ContractGoodQualityChanged`

### `ContractObjectiveUpdated`

### `ContractStateChanged`

### `CostumeCooldownComplete`

### `CostumeForgetResult`

### `CostumeSaveResult`

### `CostumeUnlockResult`

### `CraftingBotched`

### `CraftingDiscoveryHotCold`

Fires whenever the player completes a coordinate crafting session inside a discovery area.

| argument | type | meaning |
|---|---|---|
| `eHotColdResult` | CraftingLib.CodeEnumCraftingDiscoveryHotCold | Returns how close the previous crafting attempt was to a discoverable recipe. |
| `eDirection` | CraftingLib.CodeEnumCraftingDirection | The direction of the discoverable schematic from the previous result. |

### `CraftingExtractItem`

> Carbine's own note: This doesn't appear to be in code.

### `CraftingInterrupted`

Fires whenever a crafting attempt is interrupted by the player moving or other external source.

### `CraftingModItem`

Fires when the player is holding ALT and clicks on an item.  This fires when the mouse button is raised.

| argument | type | meaning |
|---|---|---|
| `itemMod` | Item | The item that the player is attempting to moddify. |

> Carbine's own note: The functionality tied to this event seems to be depricated.

### `CraftingSchematicComplete`

Fires when the player finishes crafting an item.

| argument | type | meaning |
|---|---|---|
| `idSchematic` | Integer | The id number for the schematic that was completed. |
| `bSuccess` | Boolean | Whether or not the crafting attempt was successful. |
| `nXPGained` | Integer | The amount of XP gained from the crafting attempt. |
| `arMaterials` | Integer | The id number of each material that is returned to the player. |
| `idResultSchematic` | Integer | The schematic id for the final item that is created.  This can be different from idSchematic when crafting a variant. |
| `idCraftedItem` | Integer | The item that was crafted from the schematic. |

### `CraftingSchematicInfoReceived`

> Carbine's own note: No longer appears to be called by anything in code.

### `CraftingSchematicLearned`

Fires when the player learns a new crafting schematic.

| argument | type | meaning |
|---|---|---|
| `eTradeskill` | CraftingLib.CodeEnumTradeskill | The tradeskill associated with the schematic. |
| `idSchematic` | Integer | The id number for the schematic that the player learned. |

### `CraftingSchematicList`

> Carbine's own note: Does not appear to be getting called in code.

### `CraftingStationClose`

Fired when the player stops interacting with or moves too far away from a crafting station.

### `CraftingUpdateCurrent`

Fires whenever the current crafting schematic is updated.  This includes starting/resuming a schematic, adding additives and catalysts, adding/removing/modifying microchips, and completing the craft.

### `CrystalTooltip`

### `DailyLoginUpdate`

### `DamageOrHealingDone`

Fires whenever damage or healing is done to a unit within the player's area of interest.

| argument | type | meaning |
|---|---|---|
| `unitCaster` | Unit | The unit that used the ability that caused the damage or healing. |
| `unitTarget` | Unit | The unit that received the damage or healing. |
| `eDamageType` | GameLib.CodeEnumDamageType | The type of damage that was done to the target. |
| `nHealthChange` | Integer | The amount that the target's health was changed by. |
| `nShieldAbsorbAmount` | Integer | The amount of damage that was absorbed by the unit's shields. |
| `nAbsorbedAmount` | Integer | The amount of damage that was absorbed by the unit's absorption shield. |
| `bIsCritical` | Boolean | Whether the damage or healing effect was a critical hit. |
| `strSpellName` | String | The name of the ability that caused the damage or healing. |

### `DamageOrHealingDone`

An event that gets fired whenever a unit takes damage or gets healed.

| argument | type | meaning |
|---|---|---|
| `unitCaster` | Unit | The unit who used the spell that caused the damage/healing |
| `unitTarget` | Unit | The unit that received the damage/healing |
| `eDamageType` | Integer | The type of damage done to the unit.  This enum corresponds with  GameLib.CodeEnumDamageType |
| `nHealth` | Integer | The amount of damage or healing done to the target's health |
| `nShields` | Integer | The amount of damage or healing done to the target's shields |
| `nAbsorb` | Integer | The amount of damage or healing done to the target's absorption |
| `bIsCritical` | Boolean | Whether or not the attack was a critical hit |
| `splUsed` | Spell | The spell that did the damage / healing to the target |

### `DashCastFail`

Fires when the player attempts to dash while they have no dash charges.

### `DashCastSuccess`

Fires when the player successfully dashes.

### `DashEnergyUpdated`

### `DatacubePlaybackEnded`

Fires when a datacube's VO ends or is forced to end.

### `DatacubeUpdated`

Fires when the player unlocks with a new datacube, journal entry, or Tales From Beyond the Fringe.

| argument | type | meaning |
|---|---|---|
| `idEntry` | Integer | The id number for the entry. |
| `bIsVolume` | Boolean | Whether or not the entry was unlocked by entering a trigger volume. |

> Carbine's own note: Also fires when all datacube info is forgotten.

### `DebugPrerequisite`

Fires when certain dev commands are used.  Displays the debug string for prereqs.

| argument | type | meaning |
|---|---|---|
| `outputStr` | String |  |

> Carbine's own note: Not player facing.

### `DecorPreviewClose`

Fires whenever a decor or plug preview window closes.

### `DecorPreviewOpen`

Fires whenever the player opens the decor or plug preview window.

| argument | type | meaning |
|---|---|---|
| `idItemDisplayed` | Integer | The id number for the plug or decor being previewed. |

### `DeleteItemRequested`

### `DialogClosing`

> Carbine's own note: Unknown usage.

### `Dialog_Close`

Fires whenever the player picks a dialog option that should close the dialog window.

### `Dialog_QuestShare`

Fires whenever a group member attempts to share a quest that the player does not have yet.

| argument | type | meaning |
|---|---|---|
| `queShared` | Quest | The quest that the player is attempting to share. |
| `unitSharingPlayer` | Unit | The unit that shared the quest. |

### `Dialog_ResponseText`

Fires whenever the player selects an option in the dialog text.

| argument | type | meaning |
|---|---|---|
| `strText` | String | The option that the player selected in the dialog tree. |

### `Dialog_ShowState`

Updates and displays the Dialog's contents and responses based on the provided Ids.

| argument | type | meaning |
|---|---|---|
| `nStateId` | Integer | The id of the state, such as DialogState_TopicChoice or DialogState_QuestAccept or DialogState_QuestComplete or more. |
| `queDialog` | Quest | The quest associated with the dialog tree. |

### `Dialog_ViewIntro`

> Carbine's own note: This does not appear to be called in code.

### `DisabledGameplaySystemNotification`

### `DragDrop`

| argument | type | meaning |
|---|---|---|
| `x` | Integer |  |
| `y` | Integer |  |
| `wndSource` | Window |  |
| `strType` | String |  |
| `iData` | Integer |  |
| `bDragDropHasBeenReset` | Boolean |  |

### `DragDropCancel`

| argument | type | meaning |
|---|---|---|
| `strType` | String |  |
| `iData` | Integer |  |
| `eReason` | EDragDropCancelReason |  |
| `bDragDropHasBeenReset` | Boolean |  |

### `DragDropClear`

### `DragDropEnd`

| argument | type | meaning |
|---|---|---|
| `strType` | String |  |
| `iData` | Integer |  |
| `bDragDropHasBeenReset` | Boolean |  |

### `DragDropNothingCursor`

| argument | type | meaning |
|---|---|---|
| `strType` | String |  |
| `iData` | Integer |  |

### `DragDropSysBegin`

Fires when the player starts a drag-drop operation by holding the mouse button down while the cursor is over a BagWindow or ActionBarButton.

| argument | type | meaning |
|---|---|---|
| `wndSource` | Window | The window that the object originated from. |
| `strType` | String | The type of object that will be affected by the drag-drop operation.  This should either be "DDBagItem" for items and "DDSpellbookItem" for spells. |
| `nStartLocation` | Integer | The location where the object was grabbed. |

### `DragDropSysEnd`

Fires whenever the player lets go of the mouse button during a drag-drop operation.

| argument | type | meaning |
|---|---|---|
| `strType` | String | The type of object that was dragged by the operation. |
| `nEndLocation` | Integer | The location where the object was dropped. |

### `DragDropTargetNotify`

| argument | type | meaning |
|---|---|---|
| `bMe` | Boolean |  |

### `DuelAccepted`

Fires whenever a player accepts a duel request.

| argument | type | meaning |
|---|---|---|
| `fCountdownTimer` | Float | The countdown timer before the duel starts (in seconds). |

### `DuelCancelWarning`

Fires whenever a player re-enters the dueling area while the "Left Area" warning is displayed.

### `DuelLeftArea`

Fires whenever the player leaves the dueling area.

| argument | type | meaning |
|---|---|---|
| `fWarningTime` | Float | The amount of time (in seconds) that the player has to re-enter the dueling area before they forfiet. |

### `DuelStateChanged`

Fires whenever the player's duel state changes.

| argument | type | meaning |
|---|---|---|
| `unitDueling` | Unit | The player's duel opponent. |
| `eDuelState` | GameLib.CodeEnumDuelState | The duel state that the player has entered. |

### `DyeLearned`

Fires whenever the player learns a new dye color.

| argument | type | meaning |
|---|---|---|
| `idDye` | Integer | The id number of the dye. |
| `arDyeInfo` | Integer | A list of ids for each dye the player has learned. |

### `EditBoxChanged`

| argument | type | meaning |
|---|---|---|
| `strText` | String | The new text |

### `EditBoxChanging`

| argument | type | meaning |
|---|---|---|
| `strNewText` | String |  |
| `strOldText` | String |  |
| `bAllowed` | Boolean |  |

### `EditBoxEscape`

### `EditBoxReturn`

| argument | type | meaning |
|---|---|---|
| `strText` | String |  |

### `EditBoxTab`

| argument | type | meaning |
|---|---|---|
| `strText` | String |  |

### `EditBoxTextTooLarge`

### `EldanForgeClose`

### `EldanForgeOpen`

### `EldanForgeRequested`

### `EldanForgeResult`

### `ElderPointsGained`

Fires whenever the player gains elder points.

| argument | type | meaning |
|---|---|---|
| `nAmount` | Integer | The base number of elder points the player gained. |
| `nRested` | Integer | The number of elder points granted by the player's rested bonus. |

### `ElderPointsLimitReached`

Fires whenever the player reaches their daily elder point cap.

### `EmailSent`

### `EmailSent`

### `EnteredCombat`

### `EpisodeStateChanged`

Fires whenever the episode becomes active or is completed.

| argument | type | meaning |
|---|---|---|
| `idEpisode` | Integer | The id number for the episode whose state changed. |
| `eOldState` | Integer | The episode's previous state.  This lines up with the Episode.EpisodeState set of int constants. |
| `eNewState` | Integer | The episode's new state.  This lines up with the Episode.EpisodeState set of int constants. |

> Carbine's own note: Episode.EpisodeState needs to be converted to an enum.

### `EquipItemRequested`

### `ErrorDialogSetSelection`

| argument | type | meaning |
|---|---|---|
| `index` | Integer |  |

> Carbine's own note: Could not find any references to this in code.

### `EscapeKeyPressed_Gacha`

### `ExperienceGained`

An event fired when a unit gains experience

| argument | type | meaning |
|---|---|---|
| `eReason` | Integer |  |
| `unitTarget` | Unit | The unit that gained the experience |
| `strText` | String | A localized string containing the amount of XP gained and any relevant notes on why the unit gained the XP.  Current modiefiers include "Bonus XP" for  killing clusters of NPCs, "Explorer's XP" for discovering new areas for the first time, and Rested XP for XP gained while the user had the Rested bonus. |
| `nDelay` | Integer | The delay before the unit gains XP from the event.  This is usually set for some time during an NPC's death animation. |

### `FactionFloater`

Fires whenever the player gains reputation with a faction and float text should be shown.

| argument | type | meaning |
|---|---|---|
| `unitTarget` | Unit | The unit who gained the reputation.  This should always be the current player. |
| `strMessage` | String | The string that should be displayed in the floating text. |
| `nAmount` | Integer | The amount of reputation gained. |
| `strFactionName` | String | The name of the faction that the player gained reputation with. |
| `idFaction` | Integer | The id number of the faction that the player gained reputation with. |

### `FlightPathUpdate`

Fires whenever the player learns a new flight path, a settler builds a flight path improvement, or a settler built flight path expires.

### `FlippedCardMouseEnter`

### `FlippedCardMouseLeave`

### `FloaterMultiHeal`

### `FloaterMultiHit`

### `FloaterTransference`

### `ForceResurrect`

Fires when the player's automatic release timer runs out while they are dead.

> Carbine's own note: There may be more cases.

### `FortuneCoinSpent`

### `FriendshipAccountCharacterLevelUpdate`

Fires whenever an account friend's character gains a level.

| argument | type | meaning |
|---|---|---|
| `idFriend` | Integer | The friend id of the player that gained a level. |

### `FriendshipAccountDataUpdate`

Fires whenever an account friend's nickname, presence, public note, or online/offline status changes.

| argument | type | meaning |
|---|---|---|
| `idFriend` | Integer | The account friend ID of the player. |

### `FriendshipAccountFriendRemoved`

Fires whenever one person on either side of an account friendship removes the other as an account friend.

| argument | type | meaning |
|---|---|---|
| `idFriend` | Integer | The friend id of the account friend that was removed. |

### `FriendshipAccountFriendsRecieved`

Fires whenever a player accepts an account friend invite that was sent to them, when another player accepts an account friend invite that they sent, or when the player logs in.

| argument | type | meaning |
|---|---|---|
| `arFriendInfo` | Table |  |

> Carbine's own note: FriendshipLib.AccountPresenceState needs to be converted to an enum

### `FriendshipAccountInviteRemoved`

Fires whenever the player declines an account friend invite from another player.

| argument | type | meaning |
|---|---|---|
| `idFriend` | Integer | The id number for the invite that was sent. |

### `FriendshipAccountInvitesRecieved`

Fired whenever the player receives an account friend invite from another player or when the player logs in.

| argument | type | meaning |
|---|---|---|
| `arInviteInfo` | Table |  |

> Carbine's own note: FriendshipLib.CharacterFriendshipType needs to be set as an enum. strInviteType needs to use proper naming convention.

### `FriendshipAccountPersonalStatusUpdate`

Fires if an account friend logs on or off, updates their presence, or updates their public note.

### `FriendshipAdd`

Fires whenever a new friend is added to the friends list.

| argument | type | meaning |
|---|---|---|
| `idFriend` | Integer | The friend id for the new friend. |

### `FriendshipInviteRemoved`

Fires whenever a player declines a friend invite from another player.

| argument | type | meaning |
|---|---|---|
| `idFriend` | Integer | The friend id of the invite that was removed. |

### `FriendshipInvitesRecieved`

Fires whenever the player receives a new friend invite.

| argument | type | meaning |
|---|---|---|
| `arInviteInfo` | Table |  |

> Carbine's own note: PlayerPathLib.PlayerPathType needs to be converted to an enum. Some variables need coding standard fix.

### `FriendshipLoaded`

Fires when the FriendshipLib has loaded.  This only occurrs when a character is logged in, not when reloading the UI.

### `FriendshipLocation`

Fired in response to FriendshipLib.GetLocations(). Returns all the necessary data to see the name of the zone that the player is in.

| argument | type | meaning |
|---|---|---|
| `arLocationInfo` | Table |  |

### `FriendshipPostRemove`

### `FriendshipRemove`

Fired whenever a friend is removed from the player's friends list.

| argument | type | meaning |
|---|---|---|
| `idFriend` | Integer | The friend id of the player that was removed from the friends list. |

### `FriendshipRequest`

> Carbine's own note: No implementation in code.

### `FriendshipResult`

Fires whenever an error is encountered when working with FriendsLib functionality.

| argument | type | meaning |
|---|---|---|
| `strName` | String | This value is always 0. |
| `eResult` | Integer | The type of error that was fired.  This lines up with the values in FriendshipLib.FriendshipResult. |

> Carbine's own note: FriendshipLib.FriendshipResult constants need to be changed to enums.

### `FriendshipSuggestedAdd`

Fired whenever a suggested player is added to the friends list.

| argument | type | meaning |
|---|---|---|
| `idFriend` | Integer | The friend id that was added to the friends list from the suggested list. |

### `FriendshipSuggestedRemove`

Fires whenever a player is removed from the Suggested Friends list.  This includes when players on the Suggested list are removed due to going over the maximum number of friends on that list.

| argument | type | meaning |
|---|---|---|
| `idFriend` | Integer | The friend id of the player that was removed from the friends list. |

### `FriendshipSuggestedUpdate`

Fires whenever a suggested friend's information updates. This is usually due to level changes.

| argument | type | meaning |
|---|---|---|
| `idFriend` | Integer | The id number of the suggested friend that was updated. |

### `FriendshipUpdate`

Fired whenever a friend's character gets updated, such as when their level changes.

| argument | type | meaning |
|---|---|---|
| `idFriend` | Integer | The friend id of the player who was updated. |

### `FriendshipUpdateOnline`

Fired whenever the player comes online or goes offline.

| argument | type | meaning |
|---|---|---|
| `idFriend` | Integer | The friend id of the player whose online/offline state changed. |

### `GMChatTellFailed`

### `GalacticArchiveArticleAdded`

Fires whenever the player unlocks the first entry of a particular Galactic Archive Article.

| argument | type | meaning |
|---|---|---|
| `artNewArticle` | GalacticArchiveArticle | The article that was just unlocked. |

### `GalacticArchiveEntryAdded`

Fires whenever a new entry is unlocked for an already known Galactic Archive Article.

| argument | type | meaning |
|---|---|---|
| `artParent` | GalacticArchiveArticle | The article that this entry belongs to. |
| `entUnlocked` | GalacticArchiveEntry | The newly unlocked entry. |

### `GalacticArchiveLinkClick`

Fired whenever a player clicks a link in a Galactic Archive article.

| argument | type | meaning |
|---|---|---|
| `artLinkTarget` | GalacticArchiveArticle | The target of the link that was clicked. |

> Carbine's own note: This isn't being referenced in Lua and is likely depricated.

### `GalacticArchiveRefresh`

Fires whenever the Galactic Archive refreshes.  This is generally when the player changes zones.

### `GameClickProp`

Fires whenever the player left clicks on a non-interactive object in the world.

| argument | type | meaning |
|---|---|---|
| `idProp` | Integer | The id number of the prop that the player selected. |

### `GameClickSky`

Fires when the player left clicks on the sky.

### `GameClickUnit`

Fires whenever the player left clicks on a unit in game.

| argument | type | meaning |
|---|---|---|
| `unitSelected` | Unit | The unit that was clicked on. |

### `GameClickWorld`

Fires whenever the player left clicks a location in the world.

| argument | type | meaning |
|---|---|---|
| `vec3Location` | Vector3 | The location where the player clicked in the world. |

### `GameEnd`

### `GameTimeHoursRemaining`

### `GenerateTooltip`

| argument | type | meaning |
|---|---|---|
| `eToolTipType` | EToolTipType |  |
| `x` | Integer |  |
| `y` | Integer |  |

### `GenericError`

Fires whenever the player causes a generic error that is flashed on the screen.

| argument | type | meaning |
|---|---|---|
| `eError` | GameLib.CodeEnumGenericError | The error that was fired. |
| `strMessage` | String | The string that should be shown when the error is thrown. |

### `GenericEvent_PlayerCampStart`

Fired whenever the player starts to log off.

> Carbine's own note: This does not appear to be fired from code.

### `GenericEvent_PlayerExitCancel`

Fires when the player cancels the log off timer.

### `GenericMapNodeChosen`

### `GenericMapNodeDisabled`

Fires whenever a GenericMapNode is disabled and hidden on the GenericMap.

| argument | type | meaning |
|---|---|---|
| `mapDisabled` | GenericMapNode | The GenericMapNode that was disabled. |

### `GenericMapNodeEnabled`

Fires whenever a GenericMapNode becomes active and is shown on the GenericMap.

| argument | type | meaning |
|---|---|---|
| `mapEnabled` | GenericMapNode | The GenericMapNode that was enabled. |

### `GenericMapShow`

Fires when the generic map should be shown to the player.

| argument | type | meaning |
|---|---|---|
| `idZoneMap` | Integer | The zone map id that should be shown. |
| `arGenericMapNodeInfo` | Table |  |

> Carbine's own note: Needs to be changed from oNode to mapNode

### `GridDoubleClick`

| argument | type | meaning |
|---|---|---|
| `iRow` | Integer |  |
| `iCol` | Integer |  |

### `GridSelChange`

| argument | type | meaning |
|---|---|---|
| `iRow` | Integer |  |
| `iCol` | Integer |  |

### `GridSelChanging`

| argument | type | meaning |
|---|---|---|
| `iRow` | Integer |  |
| `iCol` | Integer |  |
| `iCurrRow` | Integer |  |
| `iCurrCol` | Integer |  |
| `bAllowChange` | Boolean |  |

### `GridSort`

| argument | type | meaning |
|---|---|---|
| `iCol` | Integer |  |

### `GroupBag_Changed`

> Carbine's own note: GroupBag is no longer a thing.  There is one reference in code that needs to be cleaned up, but it is not firing the event.

### `GroupBag_ItemDistributed`

| argument | type | meaning |
|---|---|---|
| `idItem` | Integer |  |
| `idWinner` | Integer |  |

> Carbine's own note: GroupBag is no longer a thing.  There is one reference in code that needs to be cleaned up, but this event is not fired.

### `GroupLeaderPhaseChanged`

Fires whenever the group leader moves in another phase.

| argument | type | meaning |
|---|---|---|
| `bJoinAllowed` | Boolean | Whether or not the player is allowed to join the group leader's phase. |
| `nReferenceType` | Integer |  |
| `nReferenceId` | Integer |  |

> Carbine's own note: Too much unknown here.  There's no instance of us using this in Lua, so...?

### `Group_AcceptInvite`

### `Group_Add`

Fires whenever another player is added to a group that the current player is already part of.

| argument | type | meaning |
|---|---|---|
| `strName` | String | The name of the player that was added to the group. |

### `Group_Changed`

### `Group_DeclineInvite`

### `Group_Disbanded`

Handles the output of a group leave and if the group empties and disbands.

| argument | type | meaning |
|---|---|---|
| `nReason` | Integer | The reason for the group leave. This can be a kick or a leave. |
| `nGroupMemberIndex` | Integer | The affected group member's index in the group. |
| `nGroupActorIndex` | Integer | The kicker actor member's index in the group. |

### `Group_FlagsChanged`

### `Group_Invite_Declined`

Outputs the refused invitation to a group invite.

| argument | type | meaning |
|---|---|---|
| `tTableRef` | Table | Table reference to the invited player from the current context. |

### `Group_Invite_Result`

| argument | type | meaning |
|---|---|---|
| `nTableRef` | Lua Table |  |

### `Group_Invited`

| argument | type | meaning |
|---|---|---|
| `nTableRef` | Lua Table |  |

### `Group_Join`

Fires whenever the current player first joins a group.

### `Group_JoinRequest`

Fires whenever a player sends a request to join an existing party.

| argument | type | meaning |
|---|---|---|
| `strRequesterName` | String | The name of the player requesting to join the group. |

### `Group_Left`

Fires whenever the player is no longer in the group.  This only fires for the current player.

| argument | type | meaning |
|---|---|---|
| `eReason` | GroupLib.RemoveReason | The method used to remove the player from the group. |

### `Group_LootRulesChanged`

### `Group_MemberFlagsChanged`

| argument | type | meaning |
|---|---|---|
| `nMemberIdx` | Integer | The member index of the character whose permissions changed. |
| `bIsFromPromotion` | boolean | Whether or not the change in permissions is due to the character being promoted. |
| `tFlags` | Table |  |

> Carbine's own note: Not sure what Pending and HasSetReady are

### `Group_MemberOrderChanged`

Fires whenever the group's order has changed.

### `Group_MemberPromoted`

Fires whenever a group member is promoted to group leader

| argument | type | meaning |
|---|---|---|
| `strName` | String | The name of the player who was promoted to leader. |
| `bSelf` | Boolean | Whether the current player was promoted. |

### `Group_Mentor`

Fired whenever the player should be given the option to mentor another character and whenever they stop mentoring someone.

| argument | type | meaning |
|---|---|---|
| `arMentorTargets` | Table |  |

> Carbine's own note: PlayerPathLib.PlayerPathType needs to be made into an enum. Need to find out how certain flags are toggled.

### `Group_MentorLeftAOI`

Fired whenever a pair of players using mentoring get too far apart, when the players move within range again, and when the timer to move within range runs out.

| argument | type | meaning |
|---|---|---|
| `nTimeUntilCanceled` | Integer | How long the players have (in seconds) to return to eachother's Area of Interest before the Mentoring status is canceled. |
| `bTimerStop` | Boolean | Whether or not the countdown timer has stopped.  This can be because the players have moved within range of eachother or the timer has expired. |

### `Group_MentorRelationship`

Fires whenever a player begins mentoring another player.  This event is passed to every member in the group.

| argument | type | meaning |
|---|---|---|
| `unitMentor` | Unit | The unit that is mentoring the other member. |
| `unitMentee` | Unit | The unit being mentored. |

### `Group_Operation_Result`

Fires whenever an error occurs when attempting a group related action.

| argument | type | meaning |
|---|---|---|
| `strName` | String | The name of the player that the operation was attempted on. |
| `eResult` | GroupLib.ActionResult | The reason why the operation failed. |

### `Group_Other_Joined`

| argument | type | meaning |
|---|---|---|
| `nTableRef` | Lua Table |  |

### `Group_Other_Left`

| argument | type | meaning |
|---|---|---|
| `nTableRef` | Lua Table |  |

### `Group_Other_Promoted`

Outputs the promotion of a group member.

| argument | type | meaning |
|---|---|---|
| `tTableRef` | Table | Table reference to the player from the current context. |

### `Group_Player_Joined`

### `Group_Player_Left`

### `Group_Player_Promoted`

### `Group_QuestList`

| argument | type | meaning |
|---|---|---|
| `unitId` | Unit |  |
| `nTableRef` | Lua Table |  |

### `Group_ReadyCheck`

Fires whenever a ready check is started.

| argument | type | meaning |
|---|---|---|
| `nMemberIdx` | Integer | The group index of the player who started the ready check. |
| `strMessage` | String | The message sent out with the ready check. |

### `Group_ReadyCheckCooldownExpired`

### `Group_Referral`

Fires whenever a group member referrs another player for an invitation to the group.

| argument | type | meaning |
|---|---|---|
| `nMemberIdx` | Integer | The group index of the member who sent the referral. |
| `strTargetName` | String | The name of the player that was referred to the group. |

### `Group_Remove`

Fired whenever a player is removed from the group

| argument | type | meaning |
|---|---|---|
| `strMemberName` | String | The name of the player that was removed from the group. |
| `eReason` | GroupLib.RemoveReason | The method used to remove the player from the group. |

### `Group_Request_Result`

Fires whenever actions related to joining an existing group processed by the server.

| argument | type | meaning |
|---|---|---|
| `strPlayerName` | String | The name of the player whose group the player is attempting to join. |
| `eResult` | GroupLib.Result | The type of action that was processed. |
| `bIsJoin` | Boolean | Whether the message is an attempt to join the group or not. |

### `Group_SetMark`

Fires whenever a group member sets a target marker on a unit.

| argument | type | meaning |
|---|---|---|
| `idMarker` | Integer | The id number of the target marker that was placed on the unit. |
| `unitTarget` | Unit | The unit the marker was placed on. |

### `Group_UpdatePosition`

Fires at regular, 1 second intervals with updates to the player's positions in the world.

| argument | type | meaning |
|---|---|---|
| `arMemberPosInfo` | Table |  |

> Carbine's own note: There's some information being passed here that idk we want to expose, such as folders.

### `Group_Updated`

Fires whenever the the number of players in a group change, the instance difficulty is changed,

> Carbine's own note: Need more reasons why this fires.  It seems to fire every second.

### `GuildBankItem`

Fires whenever an item is added or removed from the guild bank, or moved to a different slot within the bank.

| argument | type | meaning |
|---|---|---|
| `guildOwner` | Guild | The guild that owns the bank. |
| `eGuildType` | Integer | The type of guild that owns the bank.  This should always be GuildLib.GuildType_Guild. |
| `nSlotIndex` | Integer | The bank slot where the item is placed. |
| `bRemoved` | Boolean | Whether the item was removed from the bank or not. |

### `GuildBankLog`

Returns the results from Guild:RequestBankLogs(), Guild:RequestMoneyLogs(), and Guild:RequestRepairLogs().

| argument | type | meaning |
|---|---|---|
| `guildOwner` | Guild | The guild that owns the bank that the logs belong to. |
| `arLogs` | Table | Each log entry contains the name of the player who performed the action and the time since the action occurred.  All other variables depend on the type of log entry.  The different combinations are:  uMoneyDeposit  uMoneyWithdraw  uRepairWithdraw  nTab uItemDeposit nStack  nTab uItemWithdraw nStack |

> Carbine's own note: Lots of coding standard fixes needed.

### `GuildBankTab`

Fires in response to Guild:OpenBankTab(), verifying that the tab was successfully opened.

| argument | type | meaning |
|---|---|---|
| `guildOwner` | Guild | The guild who owns the bank that the player is interacting with. |
| `nTab` | Integer | The index of the tab that was opened. |

### `GuildBankTabCount`

Fires whenever a Bank Tab perk is purchased for the guild.

| argument | type | meaning |
|---|---|---|
| `guildOwner` | Guild | The guild who owns the bank that the tab was added to. |

### `GuildBankTabRename`

Fires whenever the player successfully renames a guild bank tab.  To actually get the new tab names, Guild:GetBankTabName() will have to be called for each tab.

| argument | type | meaning |
|---|---|---|
| `guildOwner` | Guild | The guild who owns the bank that contains the renamed tab. |

### `GuildBankWithdraw`

Fires whenever a player successfully withdraws money or items from the guild bank.  This only fires for the player who performed the withdraw action.

| argument | type | meaning |
|---|---|---|
| `guildOwner` | Guild | The guild who owns the bank that the player withdrew from. |

### `GuildBankerClose`

Fires whenever the player interacts with another target or moves away from a guild bank while interacting with it.

### `GuildBankerOpen`

Fires whenever the player interacts with a guild bank.

| argument | type | meaning |
|---|---|---|
| `unitBank` | Unit | The unit that the player interacted with to open the guild bank. |

### `GuildChange`

Fired whenever the player is added to or removed from a guild, circle, arena team, or warparty.

### `GuildClassification`

### `GuildEmblem`

> Carbine's own note: No references to this in code so far as I can tell.

### `GuildEventLogChange`

Fires whenever a player joins the guild, a player leaves the guild, the guild unlocks a perk, activates a perk, or calls Guild:RequestEventLogList()

| argument | type | meaning |
|---|---|---|
| `guildSource` | Guild | The guild whose logs have changed. |

### `GuildFlags`

Fires whenever the guild turns taxes or recruitment on or off.

| argument | type | meaning |
|---|---|---|
| `guildUpdated` | Guild | The guild whose flags have been updated. |

### `GuildInfluenceAndMoney`

Fires whenever a guild's credits or influence are gained, withdrawn, or spent.

| argument | type | meaning |
|---|---|---|
| `guildUpdated` | Guild | The guild whose influence or credits were updated. |
| `nInfluence` | Integer | The amount of influence the guild has after the update. |
| `monUpdated` | Money | The amount of money the guild has after the update. |
| `nBonusInfluenceRemaining` | Integer | The amount of bonus influence remaining after the update. |

### `GuildInfoMessage`

Fires whenever a guild's Info Message is updated.

| argument | type | meaning |
|---|---|---|
| `guildOwner` | Guild | The guild whose Info Message has changed. |

### `GuildInvite`

Fired whenever the player receives an invitation to a guild.

| argument | type | meaning |
|---|---|---|
| `strGuildName` | String | The name of the guild that the player is invited to join. |
| `strInvitorName` | String | The player who sent the invite. |
| `eGuildType` | Integer | An integer representing the type of guild that the player is invited to join.  This lines up with the GuildLib.GuildType set of constants. |
| `tFlags` | Table |  |

> Carbine's own note: GuildLib.GuildType needs to be made an enum

### `GuildMemberChange`

Fires whenever information about a guild member has changed.  This includes coming online, going offline, leveling up, having their guild rank changed, joining or leaving the guild, or changing their guild note.

| argument | type | meaning |
|---|---|---|
| `guildUpdated` | Guild | The guild whose member's info changed. |

> Carbine's own note: Would it be better to mention which guild member changed?

### `GuildMessageOfTheDay`

Fires whenever the guild's Message of the Day has been updated and when the player logs in on a character.

| argument | type | meaning |
|---|---|---|
| `guildOwner` | Guild | The guild that the Message of the Day belongs to. |

### `GuildName`

Fires whenever the guild's name is changed.  This is only done when a player or GM sets up a new guild name after a forced name change.

| argument | type | meaning |
|---|---|---|
| `guildUpdated` | Guild | The guild whose name was updated. |

> Carbine's own note: No clue how to force this.  Probably needs testing.

### `GuildNameplateChange`

Fires whenever a player changes the guild name on their nameplate.  This event only fires for the character that changed the nameplate.

| argument | type | meaning |
|---|---|---|
| `guildShown` | Guild | The guild that the player selected to show on their nameplate. |

### `GuildPerkActivated`

Fires whenever a limited duration guild perk has been activated.

| argument | type | meaning |
|---|---|---|
| `guildActivated` | Guild | The guild that the perk was activated for. |
| `idGuildPerk` | Integer | The id number of the guild perk that was activated. |

### `GuildPerkDeactivated`

Fires whenever a guild perk is turned off or runs out of time.

| argument | type | meaning |
|---|---|---|
| `guildUpdated` | Guild | The guild whose perk was turned off. |

### `GuildPerkUnlocked`

### `GuildPvp`

Fires whenever an Arena Team's or Warparty's win/loss record or rating has updated.

| argument | type | meaning |
|---|---|---|
| `guildUpdated` | Guild |  |

### `GuildQueueStateChanged`

Fires whenever the arena team's or warparty's enters a queue, leaves a queue, enters a match, or leaves a match.

| argument | type | meaning |
|---|---|---|
| `guildUpdated` | Guild | The guild who's queue state has updated. |
| `eOldState` | Integer | The guild's previous queue state.  This lines up with the GuildLib.GuildQueueState set of constants. |
| `eNewState` | Integer | The guild's new queue state.  This lines up with the GuildLib.GuildQueueState set of constants. |

### `GuildRankChange`

Fires whenever a guild, circle, or warparty adds a rank, removes a rank, renames a rank, or changes a rank's permissions.

| argument | type | meaning |
|---|---|---|
| `guildUpdated` | Guild | The guild whose rank was updated. |

### `GuildRegistrarClose`

Fires whenever the player was interacting with a Guild Registrar and either interacts with another NPC or moves too far from the Registrar

### `GuildRegistrarOpen`

Fires whenever the player interacts with a Guild Registrar NPC.

### `GuildResult`

Fires the result of various guild operations.  These can be error messages, operation types, or success messages

| argument | type | meaning |
|---|---|---|
| `guildSource` | Guild | The guild that the operation was performed on. |
| `strTarget` | String | The name of the target of the operation.  This can be a character name or rank name. |
| `nRank` | Integer | If the operation was a rank update, then this value is the index of the rank that was updated.  Otherwise, this can be 1 or 0. |
| `eResult` | Integer | The result of the operation.  This value is pulled from the GuildLib.GuildResult set of constants. |

> Carbine's own note: GuildLib.GuildResult needs to be an enum.

### `GuildRoster`

Fires in response to Guild:RequestMembers().  This returns a list of the guild's members.

| argument | type | meaning |
|---|---|---|
| `arMembers` | Table |  |
| `guildSource` | Guild | The guild that is returning its member roster. |

### `GuildStandard`

Fires whenever the guild's holomark is updated.

| argument | type | meaning |
|---|---|---|
| `guildOwner` | Guild | The guild that owns the holomark. |

### `GuildWarCoinsChanged`

Fires whenever the Warparty gains or spends warcoins.

| argument | type | meaning |
|---|---|---|
| `guildUpdated` | Guild | The Warparty whose warcoins were updated. |
| `nWarcoinsDelta` | Integer | The change in the number of warcoins that the guild has. |

### `HarvestItemsSentToOwner`

Fires whenever the player harvests resources on a neighbor's housing plot while the plot's Resource Sharing returns more than 0% to the owner.

| argument | type | meaning |
|---|---|---|
| `arItemsSent` | Table |  |

### `HazardEnabled`

Fires whenever a hazard is activated for the player.  This can be triggered by entering a hazard area or by a quest/event starting a hazard for the player.

| argument | type | meaning |
|---|---|---|
| `idHazard` | Integer | The hazard's id number. |
| `strDisplayText` | String | The string associated with the hazard.  This is displayed next to the hazard bar in the base UI. |

### `HazardRemoveMinimapUnit`

Fires whenever a hazard that is currently shown on the Minimap should be removed.

| argument | type | meaning |
|---|---|---|
| `idHazard` | Integer | The id number for the hazard that should be removed. |
| `unitRemoved` | Unit | The unit used to represent the hazard on the minimap. |

### `HazardRemoved`

Fires whenever a the conditions for a hazard are removed from the player.

| argument | type | meaning |
|---|---|---|
| `idHazard` | Integer | The hazard's id number. |

### `HazardShowMinimapUnit`

Fires whenever a hazard should be displayed on the minimap.

| argument | type | meaning |
|---|---|---|
| `idHazard` | Integer | The hazard's id number. |
| `unitMarker` | Unit | The unit used to mark the hazard on the minimap. |
| `bBeneficial` | Boolean | Whether or not the hazard is helpful to the player. |

### `HazardUpdated`

Fires whenever information about the hazard has been updated.

### `HealthyGamingUpdate`

### `HideBank`

Fires whenever the player is interacting with a Bank NPC and either interacts with another unit or moves too far from the NPC.

### `HideCredits`

### `HideDye`

Fires whenever the player is interacting with a Stylist NPC and either interacts with another unit or moves too far from the NPC.

### `HideGachaUI`

### `HideInstanceGameModeDialog`

Fires whenever the the player moves away from an instance portal or teleporter after receiving a ShowInstanceGameModeDialog event.

| argument | type | meaning |
|---|---|---|
| `bNeedToNotifyServer` | Boolean | Whether or not the server needs to be notified of the window closing.  This should be passed into GameLib.OnClosedInstanceSettings(). |

### `HideQuestLog`

Fires in response to the Event_HideQuestLog() function that can be called from Lua.

### `HighlightProgressOption`

Fires whenever a button flashes during Memory CSIs.

| argument | type | meaning |
|---|---|---|
| `nButton` | Integer | The button that should be highlighted. |

### `HintArrowDistanceUpdate`

> Carbine's own note: Unable to get this to fire.

### `HousingBasicsUpdated`

Fires whenever the player changes the visitor rules for their housing plot.

### `HousingBuildComplete`

Fires whenever a housing plug starts building.

| argument | type | meaning |
|---|---|---|
| `nSocketUpdated` | Integer | The socket that was updated. |

> Carbine's own note: Event name seems different than when it fires.

### `HousingBuildStarted`

Fires whenever the player starts to build a plug on a housing plot.

| argument | type | meaning |
|---|---|---|
| `nSocket` | Integer | The socket number where the plug is being built. |

### `HousingButtonCrate`

### `HousingButtonLandscape`

### `HousingButtonList`

### `HousingButtonRemodel`

### `HousingButtonVendor`

### `HousingEditModeChanged`

### `HousingExitEditMode`

### `HousingMannequinClose`

Fires when the player is interacting with a mannequin and either interacts with another NPC or moves too far away from the mannequin.

### `HousingMannequinOpen`

Fires whenever the player interacts with a Mannequin.

### `HousingNamePropertyOpen`

Fires when a player enters their housing plot when it does not have a name.  It is meant to inform the UI that the player needs to name their home.

### `HousingNeighborInviteAccepted`

Fires whenever a player is added to the Neighbors list.

| argument | type | meaning |
|---|---|---|
| `strName` | String | The new neighbor's name. |

### `HousingNeighborInviteDeclined`

Fired whenever a player declines a neighbor invite that they received.  This event is sent to both the person who sent the invite and the person who declined the invite.

| argument | type | meaning |
|---|---|---|
| `strName` | String | The name of the player who declined the invite. |

### `HousingNeighborInviteRecieved`

Fires whenever a player is sent an invite from another player.

| argument | type | meaning |
|---|---|---|
| `strInvitorName` | String | The name of the player that sent the neighbor invite. |

### `HousingNeighborUpdate`

Fires whenever a player is added as a neighbor, a neighbor goes offline or comes online, or a player is set as a roommate.

| argument | type | meaning |
|---|---|---|
| `idNeighbor` | Integer | The neighbor id of the player that was updated. |

### `HousingNeighborsLoaded`

Fires whenever a player is removed from the Neighbors list.

### `HousingPrivacyUpdated`

Fires whenever a player changes their housing plot's visiter rules to or from Private.

| argument | type | meaning |
|---|---|---|
| `bIsPrivate` | Boolean | Determines whether or not the building is private. |

### `HousingRandomResidenceListRecieved`

Fires in response to HousingLib.RequestRandomResidenceList().

### `HousingRealtorOpen`

> Carbine's own note: This is no longer being used so far as I know.

### `HousingResult`

Fires whenever an error is thrown due to a housing operation.

| argument | type | meaning |
|---|---|---|
| `strName` | String | The name of the player who caused the error. |
| `eResult` | Integer | The error message sent.  These are found in the HousingLib.HousingResult set of constants. |

### `IconListBoxClicked`

| argument | type | meaning |
|---|---|---|
| `id` | Integer |  |

### `Inspect`

Fires whenever the server returns information from the Unit:Inspect() function.

| argument | type | meaning |
|---|---|---|
| `unitTarget` | Unit | The unit that the inspect function was called on. |
| `arItems` | Item | The items that unitTarget currently has equipped. |

### `InstanceSetBusy`

> Carbine's own note: Seems to be depricated, but more info is needed.

### `Interaction`

| argument | type | meaning |
|---|---|---|
| `title` | String |  |
| `type` | Integer |  |
| `speed` | Integer |  |
| `sweetspot` | Integer |  |
| `width1` | Integer |  |
| `width2` | Integer |  |

> Carbine's own note: Appears to be depricated.  Unable to get it to fire.

### `InteractiveUnitChanged`

This event is fired when the player targets an interactive unit, such as vendors, quest givers, and quest objective NPCs/props.

| argument | type | meaning |
|---|---|---|
| `unitNewTarget` | Unit | The interactive unit that the player is now targeting |
| `strContext` | String | A brief description of how the player can interact with the unit |

### `InterfaceMenu_ToggleLoreWindow`

Fires whenever the player presses the key bound to the Lore window.

> Carbine's own note: This should probably be renamed to something more generic like every other event.

### `InvokeCraftingWindow`

Fires whenever the player interacts with a crafting station.

### `InvokeEscapeMenu`

> Carbine's own note: This doesn't seem to be called anymore.

### `InvokeFriendsList`

> Carbine's own note: The keybinding that would have called this is removed.

### `InvokeOptionsDialog`

> Carbine's own note: This keybinding does not seem to exist anymore.

### `InvokeScientistExperimentation`

Fires whenever the player interacts with an object or NPC that starts a Scientist Experimentation minigame.

| argument | type | meaning |
|---|---|---|
| `pmMission` | PathMission | The mission that the experimentation minigame belongs to. |

### `InvokeSettlerBuild`

Fires whenever a settler interacts with a settler depot.

| argument | type | meaning |
|---|---|---|
| `unitHub` | Unit | The settler hub that the player is interacting with. |
| `arImprovements` | SettlerImprovement | An array of settler improvements that can be built at this hub. |

### `InvokeShuttlePrompt`

> Carbine's own note: Unable to get this to fire.  May need to do some research in case this is still a thing.

### `InvokeSoldierBuild`

> Carbine's own note: Soldier improvements are not currently in the game, but may be someday.

### `InvokeTaxiWindow`

Fires whenever the player interacts with a taxi vendor.

| argument | type | meaning |
|---|---|---|
| `unitTaxi` | Unit | The taxi station that the player interacted with. |
| `bIsSettlerTaxi` | Boolean | Whether or not this taxi station was created as a settler improvement. |

### `InvokeTradeskillTrainerWindow`

Fires whenever the player interacts with a tradeskill trainer.

| argument | type | meaning |
|---|---|---|
| `unitTrainer` | Unit | The tradeskill trainer NPC that the player interacted with. |

### `InvokeVendorWindow`

Fires whenever the player interacts with a vendor NPC.

| argument | type | meaning |
|---|---|---|
| `unitVendor` | Unit | The vendor that the player interacted with. |

### `ItemAdded`

Fires whenever an item is placed in a player's inventory by a method other than looting.

| argument | type | meaning |
|---|---|---|
| `itemBase` | Item | The base version of the item that was added, before random stats, glyphs, or microchips are factored in. |
| `nCount` | Integer | How many stacks of the item were added to the player's inventory. |
| `eUpdateReason` | Item.CodeEnumItemUpdateReason | A value that represents the method that was used to obtain the item. |
| `itemInstance` | Item | The specific instance of the item.  This is the version of the item that the player sees in their inventory. |

### `ItemAuctionBidPosted`

Fires whenever someone places a bid on an item that the player has posted on the Auction House.  This does not apply for items where the person who bought the item selected the "Buy Now" option

| argument | type | meaning |
|---|---|---|
| `auctBidOn` | ItemAuction | The auction that was bid on. |

### `ItemAuctionBidResult`

Fires whenever the player places a bid or selects the "Buy Now" option for an item on the auction house.

| argument | type | meaning |
|---|---|---|
| `eResult` | GameLib.CodeEnumGenericError | The result of the player's attempt to place a bid on the auction.  A result of Ok means the bid was successful. |
| `auctBidOn` | ItemAuction | The auction that the player bid on or bought. |

### `ItemAuctionBuyOrderSubmitted`

| argument | type | meaning |
|---|---|---|
| `bSuccess` | Boolean |  |

### `ItemAuctionExpired`

Fires whenever an auction's listing expires.

| argument | type | meaning |
|---|---|---|
| `auctExpired` | ItemAuction | The auction that expired. |

### `ItemAuctionOutbid`

Fires whenever someone else places a higher bid or buys an auction that the player had bid on.

| argument | type | meaning |
|---|---|---|
| `auctBidOn` | ItemAuction | The item that the player was outbid on. |

### `ItemAuctionSearchResults`

Returns results from the the MarketplaceLib.SearchAuctionableItems() function.

| argument | type | meaning |
|---|---|---|
| `nPage` | Integer | The page that the player is currently viewing. |
| `nTotalResults` | Integer | The total number of search results that the player has received. |
| `arAuctions` | ItemAuction | An array containing all of the auctions returned in the search results. |

### `ItemAuctionSellOrderSubmitted`

### `ItemAuctionWon`

Fires whenever the player wins an auction.

| argument | type | meaning |
|---|---|---|
| `auctWon` | ItemAuction | The auction that the player won. |

### `ItemAuctionsDisabled`

Fires if the Auction House is disabled or re-enabled by the server.

| argument | type | meaning |
|---|---|---|
| `bDisabled` | Boolean | Whether or not the Auction House is disabled. |

### `ItemCancelResult`

Fires whenever the player tries to cancel one of their auctions.

| argument | type | meaning |
|---|---|---|
| `eResult` | GameLib.CodeEnumGenericError | The result of the player's attempt to cancel the auction.  If it was successful, this value will be Ok. |
| `auctCanceled` | ItemAuction | The auction that the player attempted to cancel. |

### `ItemClick`

### `ItemConfirmClearRestockOnEquip`

### `ItemConfirmSoulboundOnEquip`

### `ItemDeprecationAlert`

### `ItemDurabilityUpdate`

Fires whenever one of the player's items loses some durability or gets repaired.

| argument | type | meaning |
|---|---|---|
| `itemUpdated` | Item | The item whose durability changed. |
| `nPreviousDurability` | Integer | The item's durability before the update. |

### `ItemLink`

Fires whenever the player attempts to add an item link to the chat window.

| argument | type | meaning |
|---|---|---|
| `itemLinked` | Item | The item that was linked in chat. |

### `ItemModified`

Fires whenever the player makes a change to an item.  These changes include adding runes, removing runes, and unlocking additional rune slots.

| argument | type | meaning |
|---|---|---|
| `itemModified` | Item | The item that the player modified. |

### `ItemRemoved`

Fires whenever an item is removed from the player's inventory.  This can be caused by destroying the item, turning in a quest that auto-removes the item, salvaging the item, or selling the item at a vendor.

| argument | type | meaning |
|---|---|---|
| `itemRemoved` | Item | The item that was removed from the player's inventory. |
| `nCount` | Integer | The stack size of the item that was deleted. |
| `eReason` | Item.CodeEnumItemUpdateReason | The reason the item was updated. |

### `ItemSentToCrate`

Fires whenever the player sends a decor item from their inventory to the crate.

| argument | type | meaning |
|---|---|---|
| `itemMoved` | Item | The decor item that the player placed in their crate. |
| `nCount` | Integer | The stack size of the item that was sent to the crate. |
| `eReason` | Item.CodeEnumItemUpdateReason | The method the player used to send the item to the crate. |

### `KeyBindingKeyChanged`

Fires whenever a player saves changes to their keybindings.  The event is fired once for each keybinding that was changed.

| argument | type | meaning |
|---|---|---|
| `strKeybinding` | String | The name of the keybinding that was changed. |

### `KeyBindingSaved`

Fired when when keybinding is saved after clicking the ActionConfirmButton

### `LogOut`

Fires whenever the player finishes logging out with their character.

### `LoginError`

Fires whenever an error is thrown while the player attempts to log in.

| argument | type | meaning |
|---|---|---|
| `strErrorMessage` | String | The error message that should be shown to the player. |
| `bHandled` | Boolean | Whether or not the error was handled before it affected the player. |

### `LootAssigned`

Fires whenever a master looter assigns loot to a party or raid member.  This event is seen by everyone in the party or raid.

| argument | type | meaning |
|---|---|---|
| `itemAssigned` | Item | The item that was assigned to the player. |
| `strWinnerName` | String | The name of the player that the item was assigned to. |

### `LootBindcheck`

Fires whenever the player attempts to loot an item that is Bind on Pickup while in a group.

| argument | type | meaning |
|---|---|---|
| `tLootInfo` | Table | A table that contains information about the Bind on Pickup items that the player is trying to loot. |

### `LootItemRequested`

### `LootRoll`

Fires whenever a playerrolls on an item in the Need vs. Greed looting system.  This only fires after every member has selected need, greed, or pass on the item and is sent to every member in the group.

| argument | type | meaning |
|---|---|---|
| `itemLoot` | Item | The item that the players are rolling for. |
| `strPlayerName` | String | The player that rolled for the item. |
| `bNeed` | Boolean | Whether or not the player chose "Need" for the item. |

### `LootRollAllPassed`

Fires when everyone in the group passes on an item under the Need vs. Greed system.

| argument | type | meaning |
|---|---|---|
| `itemPassed` | Item | The item that all of the players passed on. |

### `LootRollPassed`

Fires whenever a player passes on an item or does not select an option within the time limit under the Need vs. Greed system.

| argument | type | meaning |
|---|---|---|
| `itemPassed` | Item | The item that the player passed on. |
| `strPlayerName` | String | The name of the player that passed on the item. |

### `LootRollSelected`

Fires whenever a player selects Need or Greed under the Need vs. Greed loot system.

| argument | type | meaning |
|---|---|---|
| `itemRolling` | Item | The item that the player chose to roll for. |
| `strPlayerName` | String | The name of the player that chose to roll. |
| `bNeed` | Boolean | Whether or not the player chose to roll Need on the item. |

### `LootRollUpdate`

Fires whenever a new item is added or removed from the list of items that the player can roll for.

### `LootRollWon`

Fires whenever a player wins a piece of loot under the Need vs. Greed system.

| argument | type | meaning |
|---|---|---|
| `itemWon` | Item | The item that the player won. |
| `strWinnerName` | String | The name of the player who won the roll. |
| `bNeed` | Boolean | Whether or not the player chose "Need" on the item. |

### `LootTakenBy`

### `LootedItem`

This event is fired when the player loots an item that was dropped by an NPC

| argument | type | meaning |
|---|---|---|
| `itemLoot` | Item | The item that was looted |
| `nCount` | Integer | The number of items in the stack that was looted |

### `LootedMoney`

This event is fired when the player loots currency that was dropped by an NPC

| argument | type | meaning |
|---|---|---|
| `monLoot` | Money | The currency that the player looted |

### `LuaError`

Fires whenever an error is thrown in an addon's code.

| argument | type | meaning |
|---|---|---|
| `tAddonInfo` | Table | Information on the addon that threw the error. |
| `strError` | String | The error messages for the Lua error. |
| `bCanIgnore` | Boolean | Whether the player can ignore the error or not. |

### `MLNodeClick`

### `MailAddAttachment`

Fires whenever the player right clicks an item in their inventory to attach it to a mail message.

| argument | type | meaning |
|---|---|---|
| `nLocationId` | Integer | An id number that represents the item's location in the player's inventory. |

### `MailBoxActivate`

Fires whenever the player interacts with a mailbox.

### `MailBoxDeactivate`

Fires whenever the player is interacting with a mailbox and interacts with another targets or moves far enough away from the mailbox.

### `MailRead`

Fires whenever the player opens a piece of mail that was previously unread.

| argument | type | meaning |
|---|---|---|
| `strMailId` | String | The identifier for the mail that was read. |

### `MailResult`

Fires whenever an error is thrown when the player attempts to perform a mail action

| argument | type | meaning |
|---|---|---|
| `eResult` | GameLib.CodeEnumGenericError | The reason the operation failed. |

### `MannequinWindowClose`

> Carbine's own note: Depricated.  This has been replaced by HousingMannequinClose

### `MannequinWindowOpen`

> Carbine's own note: Depricated.  This has been replaced by HousingMannequinOpen

### `MapHexesRevealed`

> Carbine's own note: This appears to be depricated, as it isn't being called anywhere in code.

### `MapTrackedUnitDisable`

> Carbine's own note: Unsure of how to track units on the map, so unable to get this to fire.

### `MapTrackedUnitUpdate`

> Carbine's own note: Unable to figure out how to track units on the zone map, so unable to get this to fire.

### `MarketplaceCommoditiesSubmitted`

| argument | type | meaning |
|---|---|---|
| `bSuccess` | Boolean |  |

### `MarketplaceWindowClose`

Fires whenever the player is interacting with the Commodities Exchange NPC, then interacts with another NPC or moves too far from the Commodities Exchange NPC.

### `MasterCraftsmanClose`

### `MasterCraftsmanOpen`

### `MasterLootUpdate`

Fires whenever the items available to be assigned by the master looter change.  This is fired for everyone in the party or raid.

### `MatchEntered`

Fired whenever the player enters a PvP Match.

### `MatchExited`

Fires whenever the player leaves a PvP Match.

### `MatchFinished`

Fires when the PvP Match ends.

### `MatchJoined`

Fires when the player initially joins a match.

### `MatchLeft`

Fires whenever the player leaves the matching game.

### `MatchLookingForReplacements`

Fires when an existing group starts looking for replacements.  This event is the result of the MatchingGame:LookForReplacements() function successfully processing.

### `MatchStoppedLookingForReplacements`

Fires whenever a group that is looking for replacements fills or in response to MatchingGame:StopLookingForReplacements()

### `MatchVoteKickBegin`

Fires in response to someone in the group starting a vote to kick another player from the group using the MatchingGame:InitiateVoteToKick() function.

| argument | type | meaning |
|---|---|---|
| `unitMember` | Unit | The member that will be kicked if the vote is successful. |

### `MatchVoteKickEnd`

Fires when the server determines that a vote to kick a player has finished or was canceled.

### `MatchVoteSurrenderBegin`

Fires whenever a call to MatchingGame:InitiateVoteToSurrender() is successfully called by someone on the player's team during a PvP match.

### `MatchVoteSurrenderEnd`

Fires when the server determines that a vote to surrender a PvP match has finished or was canceled.

### `MatchingAverageWaitTimeUpdated`

Fires whenever the server recognizes a change in the average wait time for the Match the player is queued for.

> Carbine's own note: Need to find out how often this is fired.

### `MatchingCancelPendingGame`

Fires whenever a player fails to respond to a pending Match notification before it times out or a member of the group declines to join the pending game.

### `MatchingEligibilityChanged`

Fires whenever a group member's eligibility for the dungeon that the group is queued for changes.

### `MatchingGamePendingUpdate`

Fires whenever players that were sent the pending game notification accept or decline to join the match.

### `MatchingGameReady`

Fires whenever the player is able to join a matching game.

| argument | type | meaning |
|---|---|---|
| `bInProgress` | Boolean | Whether the match that the player has already started or not. |

### `MatchingGameRespondedToPending`

| argument | type | meaning |
|---|---|---|
| `bResponse` | Boolean | Was the matching game accepted or declined |

### `MatchingJoinQueue`

Fires whenever the player successfully joins a matching queue.

### `MatchingLeaveQueue`

Fires whenever the player successfully leaves a matching queue, declines to join a pending match, or allows a pending match notification to time out.

### `MatchingPvpInactivityAlert`

Fires at regular intervals if the player is AFK in a PvP match.  This is triggered when the player has 2 minutes, 1 minute, 30 seconds, and 5 second intervals before they are removed from a match.

| argument | type | meaning |
|---|---|---|
| `nRemainingTimeMs` | Integer | The amount of time before the player is removed from the match, in Milliseconds. |

### `MatchingRoleCheckCanceled`

### `MatchingRoleCheckHidden`

Fires if the player is the one who joined the queue for a dungeon or adventure.  If the player is part of a group that joined the queue together but is not the leader of that group, they will not receive this event.

### `MatchingRoleCheckStarted`

Fires when a group queues for a dungeon or adventure or when they look for new members from the queue.

### `MenuSelection`

| argument | type | meaning |
|---|---|---|
| `iOption` | Integer |  |

### `MessageFinished`

Fires whenever a floating text message is destroyed.

| argument | type | meaning |
|---|---|---|
| `uMessage` | Userdata | The floating text object that was destroyed. |

> Carbine's own note: This seems to be firing 3 times for each floating text.  Two are when the message is created and one when it is destroyed.  All of the floaters passed out have different memory addresses, so maybe we have invisible floaters? The value we're passing out is not recognized by apollo, so why are we passing it out?

### `MessageManager_DisplayStoryPanel`

### `MessageManager_HideStoryPanel`

### `ModelLoaded`

### `ModelLoaded`

### `ModuleLoaded`

Fires when every addon has finished loading.

### `ModuleRestore`

> Carbine's own note: This does not seem to be fired anywhere in code.

### `Mount`

An event that gets fired when the player mounts or dismounts

| argument | type | meaning |
|---|---|---|
| `bMounted` | Boolean | A boolean that states whether the player is mounting or dismounting |

### `MountUnlocked`

Fires whenever the player unlocks a new mount.

| argument | type | meaning |
|---|---|---|
| `nMountId` | Integer | The id number of the mount that was unlocked. |

### `MouseButtonDown`

| argument | type | meaning |
|---|---|---|
| `eMouseButton` | EMouseButton |  |
| `nLastRelativeMouseX` | Integer |  |
| `nLastRelativeMouseY` | Integer |  |
| `bDoubleClick` | Boolean |  |
| `bStopPropagation` | Boolean |  |

### `MouseButtonUp`

| argument | type | meaning |
|---|---|---|
| `eMouseButton` | EMouseButton |  |
| `nLastRelativeMouseX` | Integer |  |
| `nLastRelativeMouseY` | Integer |  |

### `MouseEnter`

| argument | type | meaning |
|---|---|---|
| `x` | Integer |  |
| `y` | Integer |  |

### `MouseExit`

| argument | type | meaning |
|---|---|---|
| `x` | Integer |  |
| `y` | Integer |  |

### `MouseMove`

| argument | type | meaning |
|---|---|---|
| `nLastRelativeMouseX` | Integer |  |
| `nLastRelativeMouseY` | Integer |  |

### `MouseOverUnitChanged`

Fires whenever the mouse is moved over a unit or off of a unit.

| argument | type | meaning |
|---|---|---|
| `unitMouseOver` | unit | The unit that the mouse is currently over.  This value is nil if the mouse moves off of a unit. |

### `MouseWheel`

| argument | type | meaning |
|---|---|---|
| `nLastRelativeMouseX` | Integer |  |
| `nLastRelativeMouseY` | Integer |  |
| `fScrollAmount` | Float |  |
| `bConsumeMouseWheel` | Boolean |  |

### `MovieFinished`

### `MovieFinished`

### `NavPointCleared`

### `NavPointSet`

### `NetworkStatus`

### `NewCustomerSurveyRequest`

Fires whenever the player is asked to fill out a customer survey.

| argument | type | meaning |
|---|---|---|
| `nSurveyCount` | Integer | The number of customer surveys the player has queued. |

### `NextFrame`

Fires once every frame.

> Carbine's own note: Really?  We're firing an event every frame that's just saying the frame updated?

### `OnInstanceResetResult`

Fires whenever the player attempts to reset an instance of a dungeon or adventure.

| argument | type | meaning |
|---|---|---|
| `bSuccessful` | Boolean | Whether or not the instance was able to reset. |

### `OpenAddons`

### `OpenOptions`

### `OpenSignature`

### `OpenStore`

### `OpenStoreLinkCategory`

### `OpenStoreLinkSingle`

### `OwnedCommodityOrders`

Fires in response to MarketplaceLib.RequestOwnedCommodityOrders().

| argument | type | meaning |
|---|---|---|
| `arOrders` | CommodityOrder | An array that contains the player's open buy and sell orders on the commodity exchange. |

### `OwnedItemAuctions`

Fires in response to the MarketplaceLib.RequestOwnedItemAuctions() function.

| argument | type | meaning |
|---|---|---|
| `arAuctions` | ItemAuction | An array of the player's open bids and listed items on the auction house. |

### `P2PCancelTrade`

### `P2PTradeChange`

### `P2PTradeCommit`

Fired whenever the player commits to a trade using a TradeCommitButton or an ActionConfirmButton whose data is set to GameLib.CodeEnumConfirmButtonType.CommitTrade.

### `P2PTradeInvite`

| argument | type | meaning |
|---|---|---|
| `idInvitor` | Unit |  |

### `P2PTradeResult`

nTradeResult: Integer

### `PTRCharacterCopyQueued`

### `PVPDeathmatchPoolUpdated`

Fires whenever the respawn pool is updated during a PvP match with the Deathmatch ruleset, such as Arenas.

| argument | type | meaning |
|---|---|---|
| `nLivesRemainingTeam1` | Integer | The number of respawns team 1 has left. |
| `nLivesRemainingTeam2` | Integer | The number of respawns team 2 has left. |

### `PVPMatchFinished`

Fires when a PvP match ends.

| argument | type | meaning |
|---|---|---|
| `eWinner` | MatchingGame.Winner | The team that won the match. |
| `eReason` | MatchingGame.MatchEndReason | The reason that the match ended. |
| `nRatingChangeTeam1` | Integer | The amount that Team 1's rating was changed by. |
| `nRatingChangeTeam2` | Integer | The amount that Team 2's rating was changed by. |

### `PVPMatchStateUpdated`

Fires whenever the PvP match's state is changed.

| argument | type | meaning |
|---|---|---|
| `eState` | MatchingGame.PVPGameState | The match's new state. |
| `fTimeRemaining` | Float | The amount of time remaining before the match automatically changes states, in seconds. |

### `PVPMatchTeamInfoUpdated`

Fires whenever the information for a team in a PvP match is updated during a match.  This includes when a team first joins a match.

### `PartyBagItemAdded`

| argument | type | meaning |
|---|---|---|
| `guid` | Integer |  |

> Carbine's own note: Still listed in LuaGameEvents, but party bag no longer exists.

### `PartyBagItemAwarded`

| argument | type | meaning |
|---|---|---|
| `guid` | Integer |  |

> Carbine's own note: Still listed in LuaGameDEvents, but event no longer exists.

### `PartyBagItemRemoved`

| argument | type | meaning |
|---|---|---|
| `guid` | Integer |  |

> Carbine's own note: Listed in LuaGameEvents, but never fired.

### `PartyBagItemTimerStarted`

| argument | type | meaning |
|---|---|---|
| `guid` | Integer |  |

> Carbine's own note: Listed in LuaGameEvents, but never called.

### `PartyBagItemTimerStopped`

| argument | type | meaning |
|---|---|---|
| `guid` | Integer |  |

> Carbine's own note: Listed in LuaGameEvents, but never called.

### `PartyBagItemTimerTick`

| argument | type | meaning |
|---|---|---|
| `msTimeRemaining` | Integer |  |

> Carbine's own note: Listed in LuaGameEvents, but never fired.

### `PartyBagItemUpdated`

| argument | type | meaning |
|---|---|---|
| `guid` | Integer |  |

> Carbine's own note: Listed in LuaGameEvents, but never fired.

### `PartyBagSharedItemsChanged`

> Carbine's own note: Listed in LuaGameEvents, but never fired.

### `PathLevelUp`

Fires whenever the player gains a path level.

| argument | type | meaning |
|---|---|---|
| `nLevel` | Integer | The player's new path level. |
| `strMessage` | String | The message that is shown in chat when the event is fired. |

### `PendingLootInteract`

> Carbine's own note: Unsure how to get this to fire.

### `PendingWorldRemovalCancel`

> Carbine's own note: Unsure how to get this to fire.

### `PendingWorldRemovalWarning`

> Carbine's own note: Unsure how to get this to fire.

### `PersonaUpdateCharacterStats`

Fires whenever the player moves an item from one inventory slot to another, the player gains a new item, or the player's stats change (via a buff, debuff, or new equipment).

### `PetCustomizationFailed`

Fires whenever the player attempts to customize their pet or scanbot and the attempt is not successful.

| argument | type | meaning |
|---|---|---|
| `tInfo` | Table |  |
| `eResult` | PetCustomizationLib.PetCustomizeResult | The reason why the customization attempt failed. |

### `PetCustomizationUpdated`

Fires whenever the player successfully update's a pet or scanbot's customization options.

| argument | type | meaning |
|---|---|---|
| `pcCustomization` | PetCustomization | The pet's new customization info. |

### `PetFlairCleared`

> Carbine's own note: Unsure how this is fired.

### `PetFlairUnlocked`

Fires whenever the player unlocks a new piece of flair for their pet or scanbot.

| argument | type | meaning |
|---|---|---|
| `idFlair` | Integer | The id number of the pet flair that was unlocked. |

### `PlayedTime`

Fires whenever the player types /played in chat.

| argument | type | meaning |
|---|---|---|
| `strCreationMessage` | String | A string describing when the character was created. |
| `strPlayedTotal` | String | A string describing the amount of time the player has played the game. |
| `strPlayedThisLevel` | String | A string describing how much time the player has spent in game since gaining a level. |
| `strPlayedThisSession` | String | A string describing how long the player has played since logging in this session. |
| `strCreationDate` | String | A string that contains the character's creation date and time. |
| `nTimePlayedTotal` | Integer | The amount of time that the player has played this character, in seconds. |
| `nTimePlayedLevel` | Integer | The amount of time that the player has played since the character last leveled up, in seconds. |
| `nTimePlayedSession` | Integer | The amount of time the player has played since logging in, in seconds. |

### `PlayerChanged`

Fires when the player first logs in, indicating that it has loaded.

### `PlayerCurrencyChanged`

Fires whenever the player earns or spends any form of currency.

### `PlayerEnteredWorld`

### `PlayerEquippedItemChanged`

Fires whenever the player equips or removes a piece of equipment.

| argument | type | meaning |
|---|---|---|
| `eSlot` | GameLib.CodeEnumEquippedItems | The equipment slot that was updated. |
| `itemNew` | Item | The item that was placed in the slot after the update.  If no item was added, then this value will be nil. |
| `itemOld` | Item | The item that was in the slot before the update.  If the slot was empty, this value will be nil. |

### `PlayerLevelChange`

Fires whenever the player gains a level.  This is not effected by changes in effective level caused by mentoring or rallying.

| argument | type | meaning |
|---|---|---|
| `nLevel` | Integer | The player's new level. |
| `nAttributePoints` | Integer | The number of attribute points that the player has available at the new level.  This should always be 0. |
| `nAbilityPoints` | Integer | The number of ability points granted to the character at the new level. |

> Carbine's own note: nAttribute points is 0 from lvl 1 - 50.  If we aren't using this, we shouldn't pass it out.  If we are, the data should be valid.

### `PlayerMovementSpeedUpdate`

### `PlayerPathAdd`

> Carbine's own note: Unsure how this is being used.  Cannot get it to fire.

### `PlayerPathExplorerPlaceBeacon`

| argument | type | meaning |
|---|---|---|
| `state` | Integer |  |
| `complete` | Boolean |  |

### `PlayerPathExplorerPowerMapEntered`

Fires whenever the player enters an area where a Tracking mission can be started

| argument | type | meaning |
|---|---|---|
| `pmMission` | PathMission | The Tracking mission that can be started at this location. |

### `PlayerPathExplorerPowerMapExited`

Fires whenever the player leaves a location where a power map mission can be started.

| argument | type | meaning |
|---|---|---|
| `pmMission` | PathMission | The mission that could have been started from the location that the player left. |

### `PlayerPathExplorerPowerMapFailed`

Fires whenever the player fails a Tracking mission.

| argument | type | meaning |
|---|---|---|
| `pmMission` | PathMission | The mission that the player failed. |

### `PlayerPathExplorerPowerMapStarted`

Fires whenever the player successfully starts a Tracking mission.

| argument | type | meaning |
|---|---|---|
| `pmMission` | PathMission | The Tracking mission that the player started. |
| `unitTarget` | Unit | The unit that the player is supposed to follow for the mission. |

### `PlayerPathExplorerPowerMapWaiting`

Fires when the unit that is being tracked in a Tracking mission reaches its destination before the player.

| argument | type | meaning |
|---|---|---|
| `pmMission` | PathMission | The Tracking mission that the player is on. |
| `nVictoryDelay` | Integer | The amount of time the player has to reach the destination before the mission fails. |

### `PlayerPathExplorerScavengerHuntStarted`

Fires whenever the player interacts with the NPC that starts a Scavenger Hunt mission.

| argument | type | meaning |
|---|---|---|
| `pmMission` | PathMission | The Scavenger Hunt mission that was started. |

### `PlayerPathExplorerZoneChange`

| argument | type | meaning |
|---|---|---|
| `enter` | Boolean |  |

### `PlayerPathMissionActivate`

| argument | type | meaning |
|---|---|---|
| `nTableRef` | Lua Table |  |

### `PlayerPathMissionAdvanced`

Fires whenever progress is made on a multi-step path mission.

| argument | type | meaning |
|---|---|---|
| `pmMission` | PathMission | The mission that was advanced. |

### `PlayerPathMissionComplete`

Fires whenever the player completes a path mission.

| argument | type | meaning |
|---|---|---|
| `pmMission` | PathMission | The mission that the player just completed. |

### `PlayerPathMissionCompleteSound`

> Carbine's own note: Does not seem to be referenced in Lua.  Unsure how this is actually fired.

### `PlayerPathMissionDeactivate`

| argument | type | meaning |
|---|---|---|
| `missionId` | Integer |  |

### `PlayerPathMissionUnlocked`

Fires whenever the player unlocks a new path mission.  If multiple missions are unlocked at once, an event will be fired for each of them.

| argument | type | meaning |
|---|---|---|
| `pmMission` | PathMission | The mission that was unlocked. |

### `PlayerPathMissionUnlockedSound`

Fires whenever a path mission is unlocked.

### `PlayerPathMissionUpdate`

Fires whenever a path mission is unlocked, advanced, completed, or failed.

| argument | type | meaning |
|---|---|---|
| `pmMission` | PathMission | The path mission that was updated. |

### `PlayerPathRefresh`

Fires whenever the player needs to redraw their path information, such as on reloadui or changing zones.

### `PlayerPathRewardAvailable`

Fires whenever the player completes all of the path missions in an episode.

| argument | type | meaning |
|---|---|---|
| `peCompleted` | PathEpisode | The path episode that the player completed. |

### `PlayerPathScientistScanBotCooldown`

Fires when the player's ability to summon their scanbot is on cooldown, such as after the player despawns their scanbot or their scanbot is destroyed.

| argument | type | meaning |
|---|---|---|
| `fCooldown` | Float | The number of seconds before the player can summon their scanbot. |

### `PlayerPathScientistScanBotDeployed`

Fires whenever the player summons their scanbot.

### `PlayerPathScientistScanBotDespawned`

Fires whenever the player manually despawns their scanbot or their scanbot runs out of HP.

### `PlayerPathScientistScanData`

| argument | type | meaning |
|---|---|---|
| `nTableRef` | Lua Table |  |

### `PlayerPathScientistScanEnd`

### `PlayerPathScientistScanStart`

### `PlayerPathShow`

### `PlayerPathSoldierNewWhackAMoleBurrows`

> Carbine's own note: Have not been able to find any of these missions in game.  Also, this is not referenced in lua.  Depricated?

### `PlayerPathUpdate`

### `PlayerPortraitMessage`

| argument | type | meaning |
|---|---|---|
| `text` | String |  |
| `crText` | Color |  |

> Carbine's own note: Does not appear to be called anywhere in code.

### `PlayerRealmName`

### `PlayerTitleChange`

Fires whenever the player changes their title.  This only fires to the current player. Other players should handle the UnitTitleChange event.

### `PlayerTitleUpdate`

Fires whenever the player gains a new title.

### `PostCommodityOrderResult`

Fires whenever the player attempts to post a buy or sell order on the commodities exchange.  Informs the player if the order was successfully placed or an error was thrown.

| argument | type | meaning |
|---|---|---|
| `eResult` | GameLib.CodeEnumGenericError | The result of the operation.  This will return the error that is received, or OK if the operation was successful. |
| `orderPosted` | CommodityOrder | The commodity order that the player attempted to post on the Commodities Exchange. |
| `monCost` | Money | The cost to post the order. |

### `PostItemAuctionResult`

Fires when the player attempts to post an auction on the Auction House.

| argument | type | meaning |
|---|---|---|
| `eResult` | GameLib.CodeEnumGenericError | If there was a problem posting the auction, this will contain the error explaining why it failed.  Otherwise, this value will be Ok. |
| `auctPosted` | ItemAuction | The auction that the player tried to post. |

### `PrereqFailureMessage`

> Carbine's own note: Unable to get this to fire.

### `PreviousActionBar`

> Carbine's own note: Unable to find any references to this event in code.

### `ProfessionAchievementUpdated`

Fires whenever the player crafts an item that advances a node in the Tradeskill tech tree.

| argument | type | meaning |
|---|---|---|
| `achUpdated` | Achievement | The achievement that go updated. |

### `ProfessionUpdated`

Fires whenever a profession gains XP, gains a talent point, chooses a talent, unlocks a schematic, or gets traded for another tradeskill.

### `ProfessionsLoaded`

Fires when the player's tradeskills are done loading.

### `ProgressClickHighlightTime`

Fires twice per frame while the Precision and Metronome CSIs are active.  This informs the UI of whether or not the target areas have been successfully hit by the player.

| argument | type | meaning |
|---|---|---|
| `nTargetIdx` | Integer | The target area being referenced.  0 is the first target, and 1 is the second.  If there is only one target, then events will still be fired for both, but only events with nTargetIdx of 0 will matter for that CSI. |
| `nPercentageHighlight` | Integer | Informs the UI of how much the color for the target area should be changed.  0 is the default color. |

> Carbine's own note: Does this really need to be fired so often?

### `ProgressClickWindowCompletionLevel`

Fires once per frame while the Click and Hold, Rapid Tap, Precision Tap, and Metronome CSIs are active.  For Click and Hold and Rapid Tap CSIs, this tells the UI the CSI's progress.

| argument | type | meaning |
|---|---|---|
| `nProgress` | Integer | The CSI's progress on the meter, with 0 being the beginning and 100 being the end. |
| `bIsReversed` | Boolean | Whether or not the CSI's progress is reversed.  This is primarily used in Metronome CSIs. |

### `ProgressClickWindowDisplay`

Fires whenever a CSI should be drawn or hidden.

| argument | type | meaning |
|---|---|---|
| `bIsActive` | Boolean | Whether or not the CSI should be shown. |

### `PublicEventBombDropped`

### `PublicEventBombStatus`

### `PublicEventCleared`

Fires whenever a PublicEvent is removed from the player's list of active events.

| argument | type | meaning |
|---|---|---|
| `peEnding` | PublicEvent | The PublicEvent that was cleared from the active list. |

> Carbine's own note: This doesn't seem to be called like I thought.  Might not ever be called. This might be depricated and replaced with PublicEventLeave.

### `PublicEventEnd`

Fires when a public event ends.

| argument | type | meaning |
|---|---|---|
| `peEvent` | PublicEvent | The public event that ended. |
| `eReason` | Integer | The reason the event ended.  This lines up with the PublicEvent.PublicEventParticipantRemoveReason set of int constants. |
| `tEventInfo` | Table |  |

> Carbine's own note: Lots of int constants that need to be converted to enums.  Lots of values that might not need to be passed.  Lots of values that don't seem consistent.

### `PublicEventInitiateVote`

Fires whenever the public event requires the group to vote on a decision before progressing.

### `PublicEventLeave`

Fires whenever the player leaves a public event area or zone.

| argument | type | meaning |
|---|---|---|
| `peEvent` | PublicEvent | The public event that the player left. |
| `eReason` | Integer | The reason the event was fired.  This lines up with the PublicEvent.PublicEventParticipantRemoveReason set of int constants. |

### `PublicEventLiveStatsUpdate`

Fires once per second during events with live stats, such as PvP matches.

| argument | type | meaning |
|---|---|---|
| `peUpdated` | PublicEvent | The public event whose stats were updated. |

### `PublicEventLocationAdded`

Fires whenever a new location is added to a public event.

| argument | type | meaning |
|---|---|---|
| `peUpdated` | PublicEvent | The public event that the location was added to. |

> Carbine's own note: Unsure of where to get this event to fire.  Needs further testing.

### `PublicEventLocationRemoved`

Fires whenever a location is removed from the public event.

| argument | type | meaning |
|---|---|---|
| `peUpdated` | PublicEvent | The public event that the location was removed from. |

> Carbine's own note: Unable to get this to fire.  Need a test case.

### `PublicEventObjectiveLocationAdded`

Fires whenever a location is added to a public event objective.

| argument | type | meaning |
|---|---|---|
| `peoUpdated` | PublicEventObjective | The objective that the location was added to. |

> Carbine's own note: Needs a test case.

### `PublicEventObjectiveLocationRemoved`

Fires whenever a location is removed from an objective.

| argument | type | meaning |
|---|---|---|
| `peoUpdated` | PublicEventObjective | The public event objective that the location was removed from. |

### `PublicEventObjectiveUpdate`

Fires whenever a player progresses a public event objective.

| argument | type | meaning |
|---|---|---|
| `peoUpdated` | PublicEventObjective | The public event objective that was updated. |

### `PublicEventStart`

Fires whenever a public event begins.

| argument | type | meaning |
|---|---|---|
| `peStarting` | PublicEvent | The public event that just started. |

### `PublicEventStatsUpdate`

Fires whenever players' public event stats update.

| argument | type | meaning |
|---|---|---|
| `peUpdated` | PublicEvent | The public event whose stats were updated. |

### `PublicEventUnitUpdate`

### `PublicEventUpdate`

Fires whenever a public event updates.

| argument | type | meaning |
|---|---|---|
| `peUpdated` | PublicEvent | The public event that was updated. |

> Carbine's own note: Need to find a test case for this

### `PublicEventVoteEnded`

Fires when every member of a group has voted when the public event requires it, or when the voting timer runs out.

| argument | type | meaning |
|---|---|---|
| `nWinner` | Integer | The voting option with the most votes. |

### `PublicEventVoteTallied`

Fires whenever a group member selections an option during a public event vote.

| argument | type | meaning |
|---|---|---|
| `nSelection` | Integer | The option that was selected by a player. |

### `PvpKillNotification`

Fires when a player is killed in PvP.

| argument | type | meaning |
|---|---|---|
| `strVictimName` | String | The name of the player that was killed. |
| `eReason` | MatchingGame.PvpDeathReason | The reason the victim died. |
| `strKillerName` | String | The name of the unit that killed the victim. |
| `eKillerClass` | GameLib.CodeEnumClass | The killer's class. |
| `eVictimTeam` | MatchingGame.Team | The team that the victim is on. |

### `PvpRatingUpdated`

Fires whenever a player's or PvP team's rating changes.

| argument | type | meaning |
|---|---|---|
| `eRatingType` | MatchingGame.RatingType | The type of rating that was changed. |

### `QueryBeginClickStick`

### `QueryBeginClickStick`

### `QueryBeginClickStick`

| argument | type | meaning |
|---|---|---|
| `x` | Integer |  |
| `y` | Integer |  |
| `bClickStickStarted` | Boolean |  |

### `QueryBeginDragDrop`

### `QueryBeginDragDrop`

### `QueryBeginDragDrop`

### `QueryBeginDragDrop`

| argument | type | meaning |
|---|---|---|
| `x` | Integer |  |
| `y` | Integer |  |
| `bDragDropStarted` | Boolean |  |

### `QueryCursor`

### `QueryDragDrop`

| argument | type | meaning |
|---|---|---|
| `x` | Integer |  |
| `y` | Integer |  |
| `wndSource` | Window |  |
| `strType` | String |  |
| `iData` | Integer |  |
| `eResult` | EDragDropQueryResult |  |

### `QuestCalloutToggle`

Fires in response to the GameLib.ToggleQuestUnitCallouts() function.  This event tells the UI that the gear / path interact icons on objects in the world were toggled on or off.

### `QuestFloater`

Fires whenever the quest is advanced, abandoned, failed, or completed.  This event is meant to give the UI the information it needs to show floating text related to the quest's state change.

| argument | type | meaning |
|---|---|---|
| `unitTarget` | Unit | The unit who the quest belonged to. |
| `strMessage` | String | The message that should be shown in the floating text. |
| `queUpdated` | Quest | The quest that was updated. |

### `QuestGetCurrentQuestId`

> Carbine's own note: This exists in code, but does not seem to be called anywhere.

### `QuestInit`

Fires when the quest system is initialized.

### `QuestObjectiveUpdated`

Fires whenever the player makes progress on a quest objective.

| argument | type | meaning |
|---|---|---|
| `queUpdated` | Quest | The quest that the objective belongs to. |
| `idObjective` | Integer | The id of the quest objective that was updated. |
| `bIsPathQuest` | Boolean | Whether or not the quest objective belongs to a path quest. |

> Carbine's own note: Are "Path Quests" actually a thing?

### `QuestPeriodicReset`

### `QuestStateChanged`

Fires whenever the quest's state is updated.

| argument | type | meaning |
|---|---|---|
| `queUpdated` | Quest | The quest whose state was changed. |
| `eState` | Integer | The quest's new state.  This value lines up with the Quest.QuestState set of int constants. |

> Carbine's own note: Quest.QuestState needs to be made an enum.

### `QuestTrackedChanged`

Fires whenever a quest becomes tracked or untracked.

| argument | type | meaning |
|---|---|---|
| `queUpdated` | Quest | The quest that was updated. |
| `bTracked` | Boolean | Whether the quest is now tracked or not. |
| `bIsPathQuest` | Boolean | Whether or not the quest is a path quest. |

> Carbine's own note: Are path quests really a thing?

### `QueueFinished`

### `QueueStatus`

### `RaidInfoResponse`

> Carbine's own note: Unsure how to get this to fire.  I don't think we're handling it atm.

### `RapidTransportResult`

### `RealmBack`

### `RealmBroadcast`

### `RealmBroadcast`

### `RealmBroadcastTierHigh`

Fires whenever a high priority message is broadcast to the entire realm.

| argument | type | meaning |
|---|---|---|
| `strMessage` | String | The message that was broadcast. |

### `RealmBroadcastTierMedium`

Fires whenever a medium priority message is broadcast to the entire realm.

| argument | type | meaning |
|---|---|---|
| `strMessage` | String | The message that was broadcast. |

### `RealmFirstAchievementAnnounce`

Fires whenever a player or guild is the first on the realm to earn an achievement.  This only applies to select achievements, such as hitting a certain level, reaching the highest tier of a tradeskill, and clearing certain dungeons and raids, etc.

| argument | type | meaning |
|---|---|---|
| `idAchievement` | Integer | The achievement that the player or guild earned. |
| `bGuildAchievement` | Boolean | Whether the achievement was a guild achievement or not. |
| `strName` | String | The name of the player or guild who earned the achievement. |
| `strMessage` | String | The message that is broadcast to the realm when the achievement is earned. |

### `RealmListChanged`

### `RealmTransferFlags`

### `RealmTransferResult`

### `RealmTrasnferResult`

### `RecallShardChanged`

> Carbine's own note: Does not seem to be called from code.  Probably depricated.

### `RecruitmentDemands`

### `RecruitmentDescription`

### `RecruitmentDetailedGuildInfo`

### `RecruitmentDetailedInfoRequestsUnblocked`

### `RecruitmentGuildsList`

### `RecruitmentGuildsUpdated`

### `RecruitmentMinLevel`

### `RecruitmentUnsubscribed`

### `RefreshHealthShieldBar`

Fires whenever the a unit's health or shields is updated.

> Carbine's own note: It would be awesome if we could get the unit whose health / shields updated and if it fired when absorb shields update.

### `RefreshInventoryBags`

Fires whenever the player right clicks to use an item or equip an item, or attempts to send a piece of decor to the crate.  This only fires if the item is in the player's inventory.

### `RefreshMail`

Fires whenever the player removes money or items attached to a piece of mail.

| argument | type | meaning |
|---|---|---|
| `strMailId` | String | The mail's unique id number....as a string.  Yeah, it's weird. |

> Carbine's own note: Why is the id a string?

### `RefreshOptionsDialog`

### `RemoveCCState`

Fires whenever a CC state is removed from a unit.

| argument | type | meaning |
|---|---|---|
| `eState` | Unit.CodeEnumCCState | The CC state that was removed from the unit. |
| `unitSource` | Unit | The unit that the CC state was removed from. |

### `RemoveCCStateStun`

Fires whenever the player leaves the Stun CC state.

### `RemoveSpellShortcut`

Fires whenever a spell that is part of a quest, challenge, public event, or path mission is removed from the character.

| argument | type | meaning |
|---|---|---|
| `spellData` | Spell | The spell that was removed from the character. |
| `eReason` | Integer | The reason the player had the spell. |
| `idSource` | Integer | The id number of the quest, quest objective, challenge, public event, public event objective, or path mission that the spell is tied to. |

> Carbine's own note: ESpellShortcutReason needs to be exposed to Lua for eReason.

### `RepairItemCompleted`

> Carbine's own note: Does not seem to be fired.

### `ReportPlayerComplete`

### `ReputationBoundryWarning`

Fires whenever a player has 75% of the reputation required to reach the next reputation level with a faction

| argument | type | meaning |
|---|---|---|
| `strReputationLevel` | String | The name of the reputation level that the player is approaching. |
| `strFactionName` | String | The name of the faction that the player gained reputation with. |

### `ReputationChanged`

Fires whenever the player gains or loses reputation with a faction.

| argument | type | meaning |
|---|---|---|
| `strFactionname` | String | The name of the faction that the player gained or lost reputation with. |
| `nReputation` | Integer | The amount of reputation the player has with the faction. |
| `fReputationDelta` | Float | The amount that the player's reputation was changed by. |

### `ReputationLevel`

Fires whenever the player reaches a new reputation level with a faction.

| argument | type | meaning |
|---|---|---|
| `strReputationLevel` | String | The name of the reputation level that the player reached. |
| `strFactionName` | String | The name of the faction that the player gained reputation with. |

### `ResolutionChanged`

Fires whenever the player logs into the game, reloads the UI, or changes their resolution.

| argument | type | meaning |
|---|---|---|
| `nWidth` | Integer | The resolution's width value. |
| `nHeight` | Integer | The resolution's height value. |

### `ResourceConversionClose`

Fires whenever the UI calls Event_CancelConverting(), the player interacts with another NPC while interacting with a Resource Conversion NPC, or when the player moves far enough away from the resource conversion NPC.

### `ResourceConversionOpen`

Fires whenever the player interacts with a Resource Conversion NPC.

| argument | type | meaning |
|---|---|---|
| `unitTarget` | Unit | The resource conversion NPC that the player interacted with. |

### `RewardTrackActive`

### `RewardTrackUpdated`

### `RewardTracksLoaded`

### `RuneSlotAdded`

### `RuneSlotCleared`

### `RuneSlotRerolled`

### `RuneTooltip`

### `SalvageItemRequested`

### `SaveModules`

Fires immediately before any addon calls its OnSave() function.

### `ScientistExperimentationResult`

Fires in response to a valid call to PathMission:AttemptScientistExperimentation().  This event returns the results of the player's attempt.

| argument | type | meaning |
|---|---|---|
| `arResults` | Integer | An array of all the results from the player's experimentation attempt.  These values line up with the PathMission.ScientistExperimentationResult set of int constants. |

> Carbine's own note: PathMission.ScientistExperimentationResult needs to be converted to an enum.

### `ScriptResurrect`

Fires when the player is forced to resurrect by a scripted event in game.

### `ServiceTokenCastResult`

### `SetNavPointFailed`

### `SetPlayerPath`

Fires whenever the player's path changes.  This should only be fired when the character is initially created.

### `SetProgressClickTimes`

Fires whenever the player starts a Press and Hold, Rapid Tap, Precision, or Metronome CSI.  Informs the UI of the areas the player is supposed to hit during the CSI.

| argument | type | meaning |
|---|---|---|
| `nWidth` | Integer | The width of the target area.  If this is 0, the target area is hidden. |
| `nLocation1Start` | Integer | The starting location of the first target area. |
| `nLocation2Start` | Integer | The starting area of the second target area. |
| `nPasses` | Integer | The number of times the progress meter is supposed to move back and forth over the CSI.  This value is nil for Press and Hold and Rapid Tap CSIs, 1 for Precision CSIs, and a number larger than 1 for Metronome CSIs. |

### `SettlerBuildResult`

Fires whenever the player build's a settler improvement.

| argument | type | meaning |
|---|---|---|
| `eResult` | Integer | The result of the player's build action. |
| `strName` | String | The name of the improvement that was built. |

> Carbine's own note: We really need an enum saying wtf eResult is.

### `SettlerBuildStatusUpdate`

Fires whenever the player builds or adds time to a settler improvement.

| argument | type | meaning |
|---|---|---|
| `idHub` | Integer | The id number of the hub that the player built the improvement at. |
| `unitHub` | Unit | The settler hub that the improvement was buit at. |

### `SettlerHubClose`

Fires whenever the UI calls Event_CancelSettlerHub() or the player moves too far from a settler hub that they are interacting with.

### `SettlerHubReward`

Fires whenever settlers unlock a reward for the players in the zone.

| argument | type | meaning |
|---|---|---|
| `strNotification` | String | The message that was broadcast, telling players about the reward that was unlocked. |

> Carbine's own note: Need to find out how these work.

### `SettlerHubUpdated`

Fires whenever a settler builds an improvement, the time on an improvement is updated, or a player adds time to an improvement.  This event is only sent to settlers.

### `SettlerInfrastructureAdvanced`

Fires whenever a the completion percentage of an infrastructure project is updated.  This event is only sent to settlers.

> Carbine's own note: Need to find out how this is called, because it doesn't seem to be

### `SettlerInfrastructureComplete`

Fires when a settler brings the last resource needed to finish an infrastructure project.

### `SettlerInfrastructureStarted`

Fires whenever a settler interacts with an infrastructure NPC while the project is not in progress.

### `SettlerInfrastructureUpdated`

Fires whenever a the completion percentage of an infrastructure project is updated.  This event is only sent to settlers.

### `SettlerNotifyUse`

> Carbine's own note: Unsure of how this is being used.  Not handled in Lua.

### `ShieldsOverloaded`

Fires whenever a unit's shields are overloaded or the overload effect ends.

| argument | type | meaning |
|---|---|---|
| `unitTarget` | Unit | The unit whose shields are overloaded or lost the overloaded state. |
| `bOverloaded` | Boolean | Whether the shields entered or left the overloaded state. |

> Carbine's own note: Need to figure out how shields get overloaded.

### `ShinyTooltip`

### `ShowActionBarShortcut`

Fires whenever an action bar shortcut is supposed to be shown or hidden.

| argument | type | meaning |
|---|---|---|
| `nBarIdx` | Integer | The bar whose visiblity state has updated. |
| `bShow` | Boolean | Whether the bar is supposed to be shown or not. |
| `nShortcuts` | Integer | The number of buttons to show from the bar. |

### `ShowBank`

Fires whenever the player interacts with a bank NPC.

### `ShowCredits`

Fired in response to PreGameLib.GetCredits().

> Carbine's own note: Not player facing. This is all in pregame.

### `ShowDye`

Fires whenever the player interacts with a stylist NPC.

### `ShowGachaUI`

### `ShowInstanceGameModeDialog`

Fires whenever a player should be shown the instance difficulty window.  This is primarily used when a player attempts to enter an adventure or dungeon via the entrance instead of via the group finder UI.

| argument | type | meaning |
|---|---|---|
| `tInfo` | Table |  |

### `ShowInstanceRestrictedDialog`

> Carbine's own note: Unsure of how to get this to fire.

### `ShowInstanceWaitingDialog`

> Carbine's own note: Unsure of what fires this.

### `ShowInventory`

Fires in response to the ShowInventory() function.

| argument | type | meaning |
|---|---|---|
| `bShow` | Boolean | Whether the inventory should be shown or not. |

### `ShowItemInDressingRoom`

Fires when the player presses Control + right click on a piece of equipment in a bag window.

| argument | type | meaning |
|---|---|---|
| `itemPreview` | Item | The item that the player wants to preview. |

### `ShowLocOnWorldMap`

Fires whenever a player clicks a location that was linked in an galactic archive article or quest.

| argument | type | meaning |
|---|---|---|
| `tLocationInfo` | Table |  |

### `ShowPurchaseReminder`

### `ShowQuestLog`

Fires when the UI calls the Event_ShowQuestLoc() function.

| argument | type | meaning |
|---|---|---|
| `idQuest` | Integer | The id number of the quest that the quest log should open to. |

### `ShowResurrectDialog`

Fires when the player shows up as a ghost after death and when the player's resurrect options update.

| argument | type | meaning |
|---|---|---|
| `bPlayerIsDead` | Boolean | Whether the player is dead or not. |
| `bWakeHere` | Boolean | Whether the player has the option to resurrect at their current location or not. |
| `bRezHolocrypt` | Boolean | Whether the player has the option to resurrect at the nearest holocrypt or not. |
| `bExitInstance` | Boolean | Whether the player has the option to exit the instance to resurrect or not.  This option is only available during dungeons, adventures, and shiphand missions. |
| `bRezAtCaster` | Boolean | Whether the player has the option to resurrect at the same location as a player who revived them or not. |
| `bHasRezFromPlayer` | Boolean | Whether another player has attempted to revive the player or not. |
| `nTimeBeforeRez` | Integer | How long the player must wait before they are able to select any resurrect options, in milliseconds. |
| `nTimeBeforeWakeHere` | Integer | The amount of time before the player is able to use the "Wake Here" option, in milliseconds. |
| `nForceRezTimer` | Integer | The amount of time before the player is forced to resurrect at the nearest holocrypt. |

### `ShowTutorial`

Fires whenever a tutorial should be shown or when the UI calls Event_ShowTutorial().  It informs the UI which tutorial to display and where to display it.

| argument | type | meaning |
|---|---|---|
| `idTutorial` | Integer | The tutorial's id number. |
| `bInstant` | Boolean | Whether the tutorial is shown immediately or is placed in a queue. |
| `strText` | String | The text for the tutorial. |
| `eAnchor` | GameLib.CodeEnumTutorialAnchor | The anchor that the tutorial should be attached to. |
| `wndContainer` | Window | The window where the tutorial is displayed. |
| `nOffsetX` | Integer | The amount the window is offset from the anchor along the X axis. |
| `nOffsetY` | Integer | The amount the window is offset from the anchor point along the Y axis. |

### `ShuttlePromptClose`

Fires whenever the player interacts with another unit or moves too far from a shuttle NPC while interacting with it.

### `SliderBarChanged`

| argument | type | meaning |
|---|---|---|
| `fNewValue` | Float |  |
| `fOldValue` | Float |  |

### `SliderBarChanging`

| argument | type | meaning |
|---|---|---|
| `fNewValue` | Float |  |
| `fOldValue` | Float |  |
| `bOkToChange` | Boolean |  |

### `SoldierHoldoutDeath`

Fires if a player that has either triggered the Holdout or damaged Holdout NPCs dies.

| argument | type | meaning |
|---|---|---|
| `solHoldout` | SoldierEvent | The holdout that the player was participating in. |

### `SoldierHoldoutEnd`

Fires whenever a soldier holdout ends, no matter if it was successful or unsuccessful.  This event fires for everyone who participated in the holdout.

| argument | type | meaning |
|---|---|---|
| `solHoldout` | SoldierEvent | The holdout that ended. |
| `eReason` | Integer | The reason the holdout ended.  This value lines up with the PathMission.PlayerPathSoldierResult set of int constants. |

### `SoldierHoldoutNextWave`

Fires whenever the next wave of a soldier holdout begins.  This event fires for everyone participating in the holdout.

| argument | type | meaning |
|---|---|---|
| `solHoldout` | SoldierEvent | The holdout that triggered the event. |

### `SoldierHoldoutStatus`

Fires whenever a holdout's state updates.  This is sent to every player involved in the holdout.

| argument | type | meaning |
|---|---|---|
| `solUpdated` | SoldierEvent | The soldier event whose state was updated. |

### `SpecChanged`

Fires whenever the player attempts to change their spec.  This event is only seen by the player that triggers the event.

| argument | type | meaning |
|---|---|---|
| `nSpecIndex` | Integer | The index of the spec that the player changed to. |
| `eResult` | AbilityBook.CodeEnumSpecError | The result of the player's attempt to change their spec.  This will show any errors caused by the attempt, or OK if successful. |

### `SpellCastFailed`

An event that fires whenever a spell is canceled by any means

| argument | type | meaning |
|---|---|---|
| `eMessageType` | Integer | An enum representing how long it will be before the unit can cast again.  This value is currently set to ECombatMessageType, which is not available to  the Lua API at the moment. |
| `eCastResult` | Integer | An enum representing why the cast failed.  This value uses the ESpell4CastResult enum, which is not available to players at the moment. |
| `unitTarget` | Unit | The target of the failed spell |
| `unitSource` | Unit | The caster of the failed spell |
| `strMessage` | String | A string describing why the spell failed |
| `strSpellName` | string | The name of the spell that failed |

> Carbine's own note: Need to give Lua access to ECombatMessageType and  ESpell4CastResul

### `SpellCastWithServiceToken`

### `SpinnerChanged`

| argument | type | meaning |
|---|---|---|
| `fNewValue` | Float |  |
| `fOldValue` | Float |  |

### `SpinnerChanging`

| argument | type | meaning |
|---|---|---|
| `fNewValue` | Float |  |
| `fOldValue` | Float |  |
| `bOkToChange` | Boolean |  |

### `SplineHintObjectEnd`

> Carbine's own note: No clue how to fire this.

### `SplitItemStack`

Fires whenever the player attempts to split a stack of items in their inventory.  The default keybind for this is Shift + Left Click on the item.  This event is only fired for the player who tried to split the stack.

| argument | type | meaning |
|---|---|---|
| `itemSplitting` | Item | The item stack that the player is trying to split. |

### `SprintEnergyUpdated`

### `SprintStateUpdated`

### `StalkerWoundsUpdate`

| argument | type | meaning |
|---|---|---|
| `percent` | Integer |  |
| `numWounds` | Integer |  |

> Carbine's own note: This does not appear to be fired and should be removed.

### `StanceChanged`

Fires whenever the player changes their character's innate ability.  This event is only sent to the player who triggered it.

### `StartSpellThreshold`

Fires whenever the player uses a spell that can be used multiple times within the same cooldown, such as the Warrior's Rampage or Esper's Telekinetic Strike.

| argument | type | meaning |
|---|---|---|
| `idSpell` | Integer | The id number of the spell that triggered this event. |
| `nMaxThresholds` | Integer | The maximum number of thresholds the spell has |
| `eCastMethod` | Spell.CodeEnumCastMethod | The method the player used to activate the spell. |

### `StoreCatalogReady`

### `StoreCatalogUpdated`

### `StoreClosed`

### `StoreError`

### `StoreLinksRefresh`

### `StorePurchaseHistoryReady`

### `StorePurchaseOfferResult`

### `StorePurchaseVirtualCurrencyPackageResult`

### `StoreRealCurrencyPurchaseHistoryReady`

### `StoryPanelDialog_Hide`

Fires whenever the UI is supposed to stop showing the currently displayed Story Panel.  This event is fired to individual players.

### `StoryPanelDialog_Show`

Fires whenever the UI is supposed to show a Story Panel window.

| argument | type | meaning |
|---|---|---|
| `ePanel` | GameLib.CodeEnumStoryPanel | The type of story panel that should be shown. |
| `arMessageLines` | String | An array of text to show in the story panel. |
| `fDisplayTime` | Float | The amount of time before the Story Panel stould stop being shown. |
| `eStyle` | GameLib.CodeEnumStoryPanelStyle | The style flag for the story panel window. |

### `StringCopiedToClipboard`

### `StunVGPressed`

Fired once every half second that the player is stunned.  This informs the UI of whether the player pressed the correct button to break out of the stun.  This event is only fired for the person who is stunned.

| argument | type | meaning |
|---|---|---|
| `bButtonPressed` | Boolean | Whether the player pressed the correct button or not. |

### `SubZoneChanged`

Fires whenever the player moves into a new subzone.

| argument | type | meaning |
|---|---|---|
| `idZone` | Integer | The id number for subzone. |
| `strSubZoneName` | String | The name of the subzone. |

### `SubscriptionExpired`

### `SupportTicketSubmitted`

### `SystemKeyDown`

Fires whenever the player presses a key.

| argument | type | meaning |
|---|---|---|
| `nKey` | Integer | The ASCII code for the key that was pressed. |

### `TalentRespecPointsChanged`

> Carbine's own note: Does not appear to be called anywhere in code.

### `TalentsChanged`

> Carbine's own note: Not called in code.

### `TargetThreatListUpdated`

Fires whenever the threat list for the targeted unit updates.  This is fired to any character that is targeting the unit whose threat table was updated.

| argument | type | meaning |
|---|---|---|
| `unitTarget1` | Unit | The player at the top of the threat list. |
| `nTarget1Threat` | Integer | unitTarget1's threat vs. the target unit. |
| `unitTarget2` | Unit | The unit with the second highest threat against the target unit. |
| `nTarget2Threat` | Integer | unitTarget2's threat vs. the target unit. |
| `unitTarget3` | Unit | The unit with the third highest threat against the target unit. |
| `nTarget3Threat` | Integer | unitTarget3's threat vs. the target unit. |
| `unitTarget4` | Unit | The player with the fourth highest threat against the target unit. |
| `nTarget4Threat` | Integer | unitTarget4's threat vs. the target unit. |
| `unitTarget5` | Unit | The unit with the fifth highest threat against the target unit. |
| `nTarget5Threat` | Integer | unitTarget5's threat vs. the target unit. |

> Carbine's own note: Why does this not pass out an array?

### `TargetUnitChanged`

An event that is fired whenever the player changes their target

| argument | type | meaning |
|---|---|---|
| `unitTarget` | Unit | The unit's new target |

### `TargetedByUnit`

Fires whenever the player's threat is increased with a hostile NPC to the point that it targets the player.  This only fires for the person being targeted.

| argument | type | meaning |
|---|---|---|
| `unitTargeting` | unit | The unit that is targeting the player. |

> Carbine's own note: The logic on when this is fired seems kinda really odd...

### `TaxiWindowClose`

Fires whenever the player interacts with another NPC, calls the Event_CancelTaxiVendor() function, or moves too far from a taxi NPC while interacting with it.  This is only sent to the person that triggered the event.

### `TextMessage`

| argument | type | meaning |
|---|---|---|
| `iType` | Integer |  |
| `strMessage` | String |  |

> Carbine's own note: The only place we were calling this has been commented out.  It is no longer in use.

### `TickClaimCount`

### `ToggleAbilitiesWindow`

Fires whenever the player presses the key bound to toggle the Limited Action Set Builder.  This is only fired for the player who pressed the keybind.

| argument | type | meaning |
|---|---|---|
| `bShow` | Boolean | Whether the Limited Action Set Builder should be shown or not. |

### `ToggleAccountInventoryWindow`

### `ToggleAchievementWindow`

Fires whenever the player presses the keybinding tied to the achievements window or the Event_ToggleAchievementWindow() function is called from the UI..  This is only fired for the player who clicked the keybinding.

### `ToggleAuctionList`

Fires whenever the player presses the keybinding tied to the Marketplace Listings.  This event is only fired for the player who presses the keybind.

### `ToggleAuctionWindow`

Fires when the player interacts with an auctioneer NPC.  This is only fired for the player who pressed the keybinding.

### `ToggleCREDDExchangeWindow`

Fires when the player interacts with a CREDD Exchange NPC.

### `ToggleChallengesWindow`

> Carbine's own note: This does not seem to be called.

### `ToggleCharacterWindow`

Fires whenever the player presses the keybinding tied to the character window.  This is only received by the player who pressed the button

### `ToggleCodex`

Fires whenever the player presses the keybind tied to the Codex menu or called Event_ToggleCodex() from the UI.  This event is only fired for the player who pressed the keybinding.

### `ToggleCollectiblesWindow`

### `ToggleContractsWindow`

### `ToggleErrorDialog`

Fires whenever a Lua error occurs.  This is only received by the client that the error occurred on.

### `ToggleFramerate`

Fires whenever the player toggles the framerate display (Ctrl + F by default).  This is only fired for the client where the key combination was pressed.

### `ToggleGhostModeMap`

Fired whenever the player presses the button to toggle the ghost mode.  This is only fired for the player.

> Carbine's own note: Could not get this to fire.

### `ToggleGroupFinder`

Fires whenever the player presses the key bound to the GroupFinder UI.  This event is only received by the player who pressed the keybinding.

### `ToggleGroupSharedBag`

> Carbine's own note: Group Shared Bag is depricated.

### `ToggleGroupsWindow`

> Carbine's own note: This doesn't appear to be called from anywhere in code.

### `ToggleGuild`

Fired whenever the player presses the keybinding tied to the Guild UI.  This event is only handled by the player who pressed the keybinding.

### `ToggleHoloWardrobeWindow`

### `ToggleInventory`

Fires whenever the player presses the key bound to the Inventory.  This is only received by the player who pressed the key.

### `ToggleItemContextMenu`

### `ToggleLevelUpUnlockWindow`

### `ToggleMacrosWindow`

### `ToggleMailWindow`

Fires whenever the player presses the key bound to Mail.  This event is only handled by the player who pressed the key.

### `ToggleMarketplaceWindow`

Fires whenever the player interacts with a Commodities Marketplace NPC.  This is only handled by the player who triggered the event.

### `ToggleNonCombatAbilitiesWindow`

### `TogglePlayerTicketWindow`

Fires whenever the player types the slash command to open the Player Ticket Window.  It is only handled by the player who used the command.

### `ToggleQuestLog`

Fires whenever the UI calls the Event_ToggleQuestLog() function or the player presses the key bound to the quest log.  This is only sent to the player that fired it.

### `ToggleReputationInterface`

Fires whenever the UI calls Event_ToggleReputationWindow().  This is only fired to the player with the addon that called the function.

### `ToggleSocialWindow`

Fires whenever the player presses the key bound to the Social window.  It is only sent to the player that pressed the button.

### `ToggleStuckWindow`

Fires whenever the player types /stuck while in game or the UI calls ShowStuckUI().  This event will only fire for the player who used the command or whose UI called the function.

### `ToggleTradeSkillsInventory`

Fires whenever the ToggleTradeSkillsInventory() function is called from the UI.  This is only sent to the player whose UI called the function.

### `ToggleTradeskills`

Fires whenever the player presses the key bound to Tradeskills.  This only fires for the player that pressed the key.

### `ToggleWhoWindow`

### `ToggleZoneMap`

Fires whenever the player presses the key bound to the Map.  This event only fires for the player that pressed the key.

### `TopLevelWindowMove`

### `TradeSkillSigilResult`

Fires whenever the player attempts to add a rune to a rune slot on a piece of equipment.

| argument | type | meaning |
|---|---|---|
| `eResult` | CraftingLib.CodeEnumTradeskillResult | The result of the player's attempt to add a rune to a piece of equipment. |

### `TradeSkillsBreakdown_Show`

| argument | type | meaning |
|---|---|---|
| `bShow` | Boolean |  |

> Carbine's own note: Does not appear to be called in code.

### `TradeSkillsItemBreakdown_BreakCompleted`

| argument | type | meaning |
|---|---|---|
| `success` | Boolean |  |

> Carbine's own note: This does not appear to be called in code.

### `TradeSkills_Crafting`

| argument | type | meaning |
|---|---|---|
| `text` | String |  |
| `percentComplete` | Integer |  |

> Carbine's own note: Does not seem to be called anywhere in code

### `TradeSkills_Learned`

Fires whenever the player learns a new crafting tradeskill.  This does not get fired for learning Runecrafting or harvesting (Mining, Survivalist, Relic Hunter) tradeskills.

| argument | type | meaning |
|---|---|---|
| `eTradeskill` | CraftingLib.CodeEnumTradeskill | The tradeskill that was learned. |

### `TradeSkills_Show`

| argument | type | meaning |
|---|---|---|
| `schematicId` | Integer |  |

> Carbine's own note: Does not seem to be called in code.

### `TradeSkills_UpdateQuantities`

> Carbine's own note: Does not seem to be called in code.

### `TradeskillAchievementComplete`

Fires whenever the player finishes an entry on a tradeskill's tech tree.

| argument | type | meaning |
|---|---|---|
| `idAchievement` | Integer | The id number for the achievement that the player earned. |

### `TradeskillAchievementUpdate`

Fires whenever progress is made on an entry in the player's tech tree.

| argument | type | meaning |
|---|---|---|
| `achUpdated` | Achievement | The tech tree entry that was updated. |
| `nCurrentProgress` | Integer | The progress the player has made towards completing the achievement. |
| `nProgressNeeded` | Integer | The total amount of progress needed to complete the achievement. |

### `TradeskillEngravingStationClose`

Fires whenever the player interacts with another NPC or moves away from the Engraving Station while they are interacting with it.

### `TradeskillEngravingStationOpen`

Fires whenever the player interacts with an Engraving Station NPC.

### `TransferDestinationRealmList`

### `TreeDoubleClick`

| argument | type | meaning |
|---|---|---|
| `hNode` | Handle |  |

### `TreeNodeCollapse`

| argument | type | meaning |
|---|---|---|
| `hNode` | Handle |  |

### `TreeNodeExpand`

| argument | type | meaning |
|---|---|---|
| `hNode` | Handle |  |

### `TreeSelectionChanged`

| argument | type | meaning |
|---|---|---|
| `hSelected` | Handle |  |
| `hPrevSelected` | Handle |  |

### `TreeSelectionChanging`

| argument | type | meaning |
|---|---|---|
| `hNode` | Handle |  |
| `hSelected` | Handle |  |
| `bAllowed` | Boolean |  |

### `TriggerDemoOptions`

### `TutorialPlaybackEnded`

Fires whenever the VO for a tutorial ends.

### `UDE`

### `UI_EffectiveLevelChanged`

Fires whenever the player's effective level changes due to rallying or mentoring.

| argument | type | meaning |
|---|---|---|
| `nNewEffectiveLevel` | Integer | The player's current effective level. |

### `UI_EnergyChanged`

Fires whenever the amount of energy that the player has for sprinting changes.

| argument | type | meaning |
|---|---|---|
| `nCurrentEnergy` | Integer | The amount of energy the player currently has. |
| `nMaxEnergy` | Integer | The maximum amount of energy the player can have. |

### `UI_HealthChanged`

Fires whenever the player's HP changes

| argument | type | meaning |
|---|---|---|
| `nHP` | Integer | The player's current HP. |
| `nMaxHP` | Integer | The character's maximum HP. |

### `UI_LevelChanged`

Fires whenever the player's level changes.

| argument | type | meaning |
|---|---|---|
| `nLevel` | Integer | The player's current level. |

> Carbine's own note: Isn't this covered by PlayerLevelChange?

### `UI_XPBonusAwarded`

Queues an XP award bonus to various RewardQueues and updates the RewardBar's progress.

| argument | type | meaning |
|---|---|---|
| `awardType` | CharacterStat | The corresponding queue to award towards. Calculated as: awardType - CharacterStat_KillingSpreeBonus + 1 |
| `newValue` | Float | The amount to reward. |

> Carbine's own note: This does not appear to be called from code.

### `UI_XPBonusUpdated`

| argument | type | meaning |
|---|---|---|
| `who` | Integer |  |
| `preview` | Boolean |  |
| `earnsXP` | Boolean |  |

> Carbine's own note: This does not appear to be called from code.

### `UI_XPChanged`

Fires whenever the player's XP, Elder Points, or rested bonus changes.

| argument | type | meaning |
|---|---|---|
| `nXP` | Integer | The player's current XP.  Note, this will not list the player's current EP once they have hit level 50. |
| `nMinXPForLevel` | Integer | The amount of XP the player had to earn before becoming their current level. |
| `nXPToLevel` | Integer | The amount of XP the player needs to reach the next level.  This is -1 if the player is at the maximum level. |
| `nRestedBonus` | Integer | The amount of XP or EP the player can get from their rested bonus. |

### `UnTargetedByUnit`

Fires whenever a unit stops targeting the current player.

| argument | type | meaning |
|---|---|---|
| `unitAttacking` | Unit | The unit who changed their target. |

### `UnavailableMail`

Fires whenever a piece of mail is deleted or the player reports a piece of mail as spam.

| argument | type | meaning |
|---|---|---|
| `strMailId` | String | An array of strings that contain the mail's Id |

> Carbine's own note: Why does this return an array with one element???

### `UnitActivationTypeChanged`

An event that gets fired whenever the effect that happens when you interact with the object changes.

| argument | type | meaning |
|---|---|---|
| `unitChanged` | Unit | The unit who has a new activation type |

### `UnitCreated`

An event that is fired whenever a unit is spawned or a player enters the world

| argument | type | meaning |
|---|---|---|
| `unitSpawned` | Unit | The newly created unit |

### `UnitDestroyed`

An event that gets fired whenever a unit is despawned or a player leaves the game world

| argument | type | meaning |
|---|---|---|
| `unitDestroyed` | Unit | The unit that has left this world |

### `UnitEnteredCombat`

An event that gets fired whenever a unit enters or leaves combat

| argument | type | meaning |
|---|---|---|
| `unitInCombat` | Unit | The unit that just entered combat |
| `bInCombat` | Boolean | A boolean stating whether or not the unit has entered or left combat |

### `UnitEvaded`

Fires if an NPC evades or resets due to the player being in stealth for too long.

| argument | type | meaning |
|---|---|---|
| `unitEvading` | Unit | The unit that evaded. |
| `unitTarget` | Unit | The unit that the NPC was targeting before it evaded. |
| `eReason` | Integer | The reason that the NPC evaded.  This should be either 2 (Timeout), 5 (FailedToPath) or 6 (StealthWanderTimeout) |
| `strText` | String | The floating text that should be shown when the unit evades. |

> Carbine's own note: We need an enum for eReason.

### `UnitGibbed`

### `UnitGroupChanged`

Fires whenever a player is added or removed from the group.  This is sent to every member of the group.

| argument | type | meaning |
|---|---|---|
| `unitUpdated` | Unit | The unit that was added or removed from the group. |

### `UnitGuildNameplateChanged`

Fires whenever a nearby player updates their guild tag on their nameplate.

| argument | type | meaning |
|---|---|---|
| `unitUpdated` | Unit | The unit whose guild tag was updated. |

### `UnitLevelChanged`

Fires whenever a nearby player's level or effective level changes.

| argument | type | meaning |
|---|---|---|
| `unitUpdated` | Unit | The unit whose level or effective level changed. |

> Carbine's own note: Firing multiple times for the same level change. Only seems to fire once for each effective level change.

### `UnitMemberOfGuildChange`

Fires whenever a nearby player is added or removed from a guild.

| argument | type | meaning |
|---|---|---|
| `unitUpdated` | Unit | The player that was added to or removed from a guild. |

### `UnitMiniMapMarkerChanged`

An event that is fired whenever a player whose location shows on the map/minimap moves

| argument | type | meaning |
|---|---|---|
| `unitMoving` | Unit | The unit who has changed position |

### `UnitNameChanged`

An event that gets fired whenever the unit's name gets changed

| argument | type | meaning |
|---|---|---|
| `unitChanged` | Unit | The unit whose name was changed |
| `strNewName` | String | The unit's new name |

### `UnitOcclusionChanged`

### `UnitPvpFlagsChanged`

Fires whenever a nearby player changes their PvP flag state.

| argument | type | meaning |
|---|---|---|
| `unitUpdated` | Unit | The unit who toggled their PvP flag state. |

### `UnitTextBubbleCreate`

Fires whenever an unit should display a text bubble over their head.

| argument | type | meaning |
|---|---|---|
| `unitSpeaker` | Unit | The unit that the text bubble is attached to. |
| `strText` | String | The text in the text bubble. |
| `bImmediate` | Boolean | Whether the text bubble should be shown immediately or fade in. |
| `fRange` | Boolean | The maximum range that people can see the text bubble from. |

### `UnitTextBubblesDestroyed`

Fires whenever a text bubble's internal timer has expired.

### `UnitTitleChanged`

Fires whenever a nearby unit changes their title.

| argument | type | meaning |
|---|---|---|
| `unitUpdated` | Unit | The unit who changed their title. |

### `UnlockCostumeItem`

### `UpdateCCStateStun`

Fires every 0.2 seconds while the player is stunned.  This event informs the UI how much progress the player has made towards breaking out of the stun.

| argument | type | meaning |
|---|---|---|
| `fProgress` | Float | The progress the player has made towards breaking out of the stun.  This value is percentage based, with the player breaking out on 100 or higher. |

### `UpdateGearScore`

Fires whenever an item is added or removed from the player that changes their Gear Score.

### `UpdateInventory`

Fires whenever an item is added to, removed from, or moved within the player's inventory.

### `UpdatePathXp`

Fires whenever the player gains Path XP.

| argument | type | meaning |
|---|---|---|
| `nXPDelta` | Integer | The amount of Path XP the player gained. |
| `strFloaterMessage` | String | The message that should be displayed on a combat floater when this event is fired. |

### `UpdateResurrectDialog`

### `UpdateRewardProperties`

### `UpdateSoldierBuild`

> Carbine's own note: Are soldier buildings still a thing?

### `UpdateSpellThreshold`

Fires whenever the player uses a spell with a threshold timer, while the timer is running.

| argument | type | meaning |
|---|---|---|
| `idSpell` | Integer | The spell's id number. |
| `nCurrentThreshold` | Integer | The number of times the player has used the ability since the threshold timer was started. |

### `Vacuum`

Fires whenever the player press the key bound to vacuum looting.

### `VendorItemsUpdated`

Fires whenever the player opens the Vendor UI, any player purchases a limited supply item while the player is interacting with the vendor, or the vendor restocks a limited supply item while the player is interacting with it.

### `WakeHereServiceTokenCompleted`

### `WalletUpdate`

Fires whenever the wallet tied to a player's account updates.  The wallet is used to purchase microtransaction items.

| argument | type | meaning |
|---|---|---|
| `nAmount` | Integer | The amount of currency that was added to the player's wallet. |

### `WarPartyBankerClose`

Fires whenever the player interacts with another NPC or moves too far away while interacting with the warparty bank, or whenever the UI calls Event_CancelWarpartyBank()..

### `WarPartyBankerOpen`

Fires whenever the player interacts with the Warparty Bank.

### `WarPartyBattleClose`

Fires whenever the player's UI reloads and they are not on a warplot or in a warplot match.

### `WarPartyBattleOpen`

Fires whenever the player presses the Warparty Crate button in the Warplot UI.

| argument | type | meaning |
|---|---|---|
| `guildWarparty` | Guild | The warparty that the plot belongs to. |

### `WarPartyBossTokensUpdated`

Fires whenever a player uses a boss token during a Warplot match or the player adds a boss token to the Warparty Bank.

| argument | type | meaning |
|---|---|---|
| `guildWarparty` | Guild | The warparty whose boss tokens were updated. |

### `WarPartyMatchResults`

Fires when a Warplot match ends.  This event is sent to every player involved in the match.

| argument | type | meaning |
|---|---|---|
| `arTeamResults` | Table |  |

### `WarPartyRegistrarClose`

> Carbine's own note: Depricated since this only happened when Warparty Registrars were NPCs

### `WarPartyRegistrarOpen`

> Carbine's own note: Depricated since this only happened when Warparty Registrars were NPCs

### `WarplotBattleStateChanged`

Fires when the player enters the warplot or when one of the warparty's plugs is destroyed.

### `WhoResponse`

The response the player gets when they use the /who slash command.

| argument | type | meaning |
|---|---|---|
| `tResults` | Table |  |

> Carbine's own note: Need an enum for Paths

### `WindowClosed`

### `WindowGainedFocus`

### `WindowGainedFocus`

Fires when a window gains focus

### `WindowHide`

### `WindowKeyDown`

| argument | type | meaning |
|---|---|---|
| `strKeyName` | String |  |
| `nScanCode` | Integer |  |
| `nMetakeys` | Integer |  |

### `WindowKeyEscape`

### `WindowKeyReturn`

### `WindowKeyTab`

### `WindowLoad`

### `WindowLostFocus`

### `WindowLostFocus`

Fires when a window lost focus

### `WindowMove`

When a window is moved

| argument | type | meaning |
|---|---|---|
| `nOldLeft` | Integer | The left x position before the move |
| `nOldTop` | Integer | The top y position before the move |
| `nOldRight` | Integer | The right x position before the move |
| `nOldBottom` | Integer | The bottome y position before the move |

### `WindowShow`

### `WindowSizeChanged`

### `WindowToFront`

| argument | type | meaning |
|---|---|---|
| `bOkToBringToFront` | Boolean |  |

### `WindowTransitionComplete`

### `WorkOrderLocate`

Fires whenever the player clicks a work order quest in the Quest Tracker.

| argument | type | meaning |
|---|---|---|
| `idSchematic` | Integer | The id number of the schematic required for the work order. |

### `WorldLocationOnScreen`

### `WrangleCreature`

| argument | type | meaning |
|---|---|---|
| `uTarget` | Unit | A UnitId of the targetted creature |
| `fMeter` | Float | The current progress of the action, the player wants this to remain within the success and failure thresholds |
| `fSuccessThreshold` | Float | The maximum cieling for the capture meter |
| `fFailureThreshold` | Float | The minimum floor for the capture meter |
| `nRangeBand` | Integer | Converted to text for the distance indicator |
| `fRate` | Float | Currently unused |

> Carbine's own note: Wrangling is no longer in the game.

### `ZoneCompletionUpdated`

Fires whenever the player enters a zone, explores a new part of the zone, or completes a challenge, task, datacube, or path mission

| argument | type | meaning |
|---|---|---|
| `idZone` | Integer | The id number for the zone whose completion percentage was updated. |

### `ZoneMapPing`

Fires whenever the player or a group member clicks the minimap.

| argument | type | meaning |
|---|---|---|
| `idUnit` | Integer | The id number of the unit that pinged the map. |
| `tPos` | Vector3 | The coordinates that were pinged. |

> Carbine's own note: idUnit should be changed to a Unit

### `ZoneMapPlayerIndicatorUpdated`

Fires whenever a player is added or removed from the Zone Map.

| argument | type | meaning |
|---|---|---|
| `bVisible` | Boolean | Whether the player is visible on the map or not. |

### `ZoneMapUpdateHexGroup`

Fires when a hex group is added or removed from the zone map.

| argument | type | meaning |
|---|---|---|
| `hexUpdated` | HexGroups | The hex group that was shown or hidden. |

### `ZoneMapWindowChange`

### `ZoneMapWindowModeChange`

