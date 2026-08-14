# Enums, from the client's own documentation

**234 sets.** These are the values every API argument expects. Where a set has
explicit numbers they are given; where the client documents only names, the order is
shown but **no numeric value is invented** — declaration order is not a guarantee of
value, and guessing one produces an off-by-one that reads like data.

## ActionResult

| name | order | meaning |
|---|---|---|
| `LeaveSuccess` | 0 |  |
| `LeaveFailed` | 1 |  |
| `DisbandSuccess` | 2 |  |
| `DisbandFailed` | 3 |  |
| `KickSuccess` | 4 |  |
| `KickFailed` | 5 |  |
| `PromoteSuccess` | 6 |  |
| `PromoteFailed` | 7 |  |
| `FlagsSuccess` | 8 |  |
| `FlagsFailed` | 9 |  |
| `MemberFlagsSuccess` | 10 |  |
| `MemberFlagsFailed` | 11 |  |
| `NotInGroup` | 12 |  |
| `ChangeSettingsFailed` | 13 |  |
| `ChangeSettingsSuccess` | 14 |  |
| `MentoringInvalidMentor` | 15 |  |
| `MentoringInvalidMentee` | 16 |  |
| `InvalidGroup` | 17 |  |
| `MentoringSelf` | 18 |  |
| `ReadyCheckFailed` | 19 |  |
| `MentoringNotAllowed` | 20 |  |
| `MarkingNotPermitted` | 21 |  |
| `InvalidMarkIndex` | 22 |  |
| `InvalidMarkTarget` | 23 |  |
| `MentoringInCombat` | 24 |  |
| `MentoringLowestLevel` | 25 |  |
| `MentoringNoAction` | 26 |  |
| `OrderInvalidMember` | 27 |  |
| `OrderFailedLeader` | 28 |  |
| `AlreadyInGroupInstance` | 29 |  |
| `OrderFailedInUse` | 30 |  |

## AddonLoadStatus

An enum that describes the load state of an addon.  This is primarily used alongside the depricated GetAsyncLoad functionality.

| name | order | meaning |
|---|---|---|
| `Loading` | 0 |  |
| `Loaded` | 1 |  |
| `LoadingError` | 2 |  |

## AuctionEventType

| name | order | meaning |
|---|---|---|
| `Post` | 0 |  |
| `Bid` | 1 |  |
| `Fill` | 2 |  |
| `Expire` | 3 |  |
| `Cancel` | 4 |  |

## AuctionPostResult

| name | order | meaning |
|---|---|---|
| `Ok` | 0 |  |
| `DbFailure` | 1 |  |
| `Item_BadId` | 2 |  |
| `NotReady` | 3 |  |
| `CannotFillOrder` | 4 |  |
| `TooManyOrders` | 5 |  |
| `OrderTooBig` | 6 |  |
| `NotFound` | 7 |  |
| `BidTooLow` | 8 |  |
| `OwnItem` | 9 |  |
| `BidTooHigh` | 10 |  |
| `AlreadyHasBid` | 11 |  |
| `NotEnoughToFillQuantity` | 12 |  |
| `NotEnoughCash` | 13 |  |
| `ItemAuctionDisabled` | 14 |  |
| `CommodityDisabled` | 15 |  |
| `TooManyBids` | 16 |  |

## AuctionSort

| name | order | meaning |
|---|---|---|
| `MinBid` | 0 |  |
| `Buyout` | 1 |  |
| `TimeLeft` | 2 |  |
| `Property` | 3 |  |

## BannerLocation

| name | order | meaning |
|---|---|---|
| `RotatingBanner` | 0 |  |
| `UpperRightBanner` | 1 |  |
| `LowerRightBanner` | 2 |  |

## BannerPageType

| name | order | meaning |
|---|---|---|
| `Product` | 0 |  |
| `SearchTerm` | 1 |  |
| `Category` | 2 |  |
| `BrowserLink` | 3 |  |
| `OfferGroup` | 4 |  |
| `Signature` | 5 |  |

## ChallengeTier

| name | order | meaning |
|---|---|---|
| `Bronze` | 0 |  |
| `Silver` | 1 |  |
| `Gold` | 2 |  |

## ChannelUpdateCraftingType

| name | order | meaning |
|---|---|---|
| `Item` | 0 |  |

## ChannelUpdateLootType

| name | order | meaning |
|---|---|---|
| `Item` | 0 |  |
| `Currency` | 1 |  |
| `ItemDestroy` | 2 |  |

## ChannelUpdateProgressType

| name | order | meaning |
|---|---|---|
| `RewardPoints` | 0 |  |
| `Experience` | 1 |  |
| `RestExperience` | 2 |  |
| `ElderPoints` | 3 |  |
| `RestElderPoints` | 4 |  |
| `SignatureExperience` | 5 |  |
| `SignatureElderPoints` | 6 |  |

## CharacterRecustomizationResultCharacterRecustomizationResult

| name | order | meaning |
|---|---|---|
| `Success` | 0 |  |
| `UnknownError` | 1 |  |
| `NoChanges` | 2 |  |
| `InsufficientFunds` | 3 |  |
| `OutOfRange` | 4 |  |

## CityDirectionType

| name | order | meaning |
|---|---|---|
| `Mailbox` | 0 |  |
| `Bank` | 1 |  |
| `AuctionHouse` | 2 |  |
| `CommodityMarket` | 3 |  |
| `AbilityVendor` | 4 |  |
| `Tradeskill` | 5 |  |
| `General` | 6 |  |
| `HousingNpc` | 7 |  |
| `Transport` | 8 |  |
| `Fortune` | 9 |  |

## CodeEnumAMPRespecType

| name | order | meaning |
|---|---|---|
| `Full` | 0 |  |
| `Section` | 1 |  |
| `Single` | 2 |  |

## CodeEnumAOESelectionType

| name | order | meaning |
|---|---|---|
| `None` | 0 |  |
| `Closest` | 1 |  |
| `Furthest` | 2 |  |
| `Random` | 3 |  |
| `LowestAbsoluteHealth` | 4 |  |
| `MissingMostHealth` | 5 |  |

## CodeEnumAccountCurrency

| name | order | meaning |
|---|---|---|
| `None` | 0 |  |
| `CREDD` | 1 |  |
| `RealmTransfer` | 2 |  |
| `NameChange` | 3 |  |
| `Essence` | 4 |  |
| `MysticShiny` | 5 |  |
| `Omnibits` | 6 |  |
| `NCoins` | 7 |  |
| `Loyalty` | 8 |  |
| `ServiceToken` | 9 |  |

## CodeEnumAccountCurrency

| name | order | meaning |
|---|---|---|
| `None` | 0 |  |
| `CREDD` | 1 |  |
| `RealmTransfer` | 2 |  |
| `NameChange` | 3 |  |
| `Essence` | 4 |  |
| `MysticShiny` | 5 |  |
| `Omnibits` | 6 |  |
| `NCoins` | 7 |  |
| `Loyalty` | 8 |  |
| `ServiceToken` | 9 |  |

## CodeEnumAccountOperation

| name | order | meaning |
|---|---|---|
| `MTXPurchase` | 0 |  |
| `ClaimPending` | 1 |  |
| `ReturnPending` | 2 |  |
| `TakeItem` | 3 |  |
| `GiftItem` | 4 |  |
| `RedeemCoupon` | 5 |  |
| `GetCREDDExchangeInfo` | 6 |  |
| `SellCREDD` | 7 |  |
| `BuyCREDD` | 8 |  |
| `CancelCREDDOrder` | 9 |  |
| `ExpireCREDDOrder` | 10 |  |
| `SellCREDDComplete` | 11 |  |
| `BuyCREDDComplete` | 12 |  |
| `CREDDRedeem` | 13 |  |
| `RequestDailyLoginRewards` | 14 |  |

## CodeEnumAccountOperation

The different types of account operations that the player can perform.

| name | order | meaning |
|---|---|---|
| `MTXPurchase` | 0 |  |
| `ClaimPending` | 1 |  |
| `ReturnPending` | 2 |  |
| `TakeItem` | 3 |  |
| `GiftItem` | 4 |  |
| `RedeemCoupon` | 5 |  |
| `GetCREDDExchangeInfo` | 6 |  |
| `SellCREDD` | 7 |  |
| `BuyCREDD` | 8 |  |
| `CancelCREDDOrder` | 9 |  |
| `ExpireCREDDOrder` | 10 |  |
| `SellCREDDComplete` | 11 |  |
| `BuyCREDDComplete` | 12 |  |
| `CREDDRedeem` | 13 |  |
| `RequestDailyLoginRewards` | 14 |  |

## CodeEnumAccountOperation

| name | order | meaning |
|---|---|---|
| `MTXPurchase` | 0 |  |
| `ClaimPending` | 1 |  |
| `ReturnPending` | 2 |  |
| `TakeItem` | 3 |  |
| `GiftItem` | 4 |  |
| `RedeemCoupon` | 5 |  |
| `GetCREDDExchangeInfo` | 6 |  |
| `SellCREDD` | 7 |  |
| `BuyCREDD` | 8 |  |
| `CancelCREDDOrder` | 9 |  |
| `ExpireCREDDOrder` | 10 |  |
| `SellCREDDComplete` | 11 |  |
| `BuyCREDDComplete` | 12 |  |
| `CREDDRedeem` | 13 |  |
| `RequestDailyLoginRewards` | 14 |  |

## CodeEnumAccountOperationResult

| name | order | meaning |
|---|---|---|
| `Ok` | 0 |  |
| `GenericFail` | 1 |  |
| `DBError` | 2 |  |
| `MTXError` | 3 |  |
| `InvalidOffer` | 4 |  |
| `InvalidPrice` | 5 |  |
| `NotEnoughCurrency` | 6 |  |
| `NeedTransaction` | 7 |  |
| `InvalidAccountItem` | 8 |  |
| `InvalidPendingItem` | 9 |  |
| `InvalidInventoryItem` | 10 |  |
| `NoConnection` | 11 |  |
| `NoCharacter` | 12 |  |
| `AlreadyClaimed` | 13 |  |
| `MaxEntitlementCount` | 14 |  |
| `NoRegift` | 15 |  |
| `NoGifting` | 16 |  |
| `InvalidFriend` | 17 |  |
| `InvalidCoupon` | 18 |  |
| `CannotReturn` | 19 |  |
| `Prereq` | 20 |  |
| `CREDDExchangeNotLoaded` | 21 |  |
| `NoCREDD` | 22 |  |
| `NoMatchingOrder` | 23 |  |
| `InvalidCREDDOrder` | 24 |  |
| `Cooldown` | 25 |  |
| `MissingEntitlement` | 26 |  |
| `AlreadyClaimedMultiRedeem` | 27 |  |

## CodeEnumAccountOperationResult

Results of various account operations.  This includes reasons the operation might have failed, as well as "Ok" for successful operations.

| name | order | meaning |
|---|---|---|
| `Ok` | 0 |  |
| `GenericFail` | 1 |  |
| `DBError` | 2 |  |
| `MTXError` | 3 |  |
| `InvalidOffer` | 4 |  |
| `InvalidPrice` | 5 |  |
| `NotEnoughCurrency` | 6 |  |
| `NeedTransaction` | 7 |  |
| `InvalidAccountItem` | 8 |  |
| `InvalidPendingItem` | 9 |  |
| `InvalidInventoryItem` | 10 |  |
| `NoConnection` | 11 |  |
| `NoCharacter` | 12 |  |
| `AlreadyClaimed` | 13 |  |
| `MaxEntitlementCount` | 14 |  |
| `NoRegift` | 15 |  |
| `NoGifting` | 16 |  |
| `InvalidFriend` | 17 |  |
| `InvalidCoupon` | 18 |  |
| `CannotReturn` | 19 |  |
| `Prereq` | 20 |  |
| `CREDDExchangeNotLoaded` | 21 |  |
| `NoCREDD` | 22 |  |
| `NoMatchingOrder` | 23 |  |
| `InvalidCREDDOrder` | 24 |  |
| `Cooldown` | 25 |  |
| `MissingEntitlement` | 26 |  |
| `AlreadyClaimedMultiRedeem` | 27 |  |

## CodeEnumAccountOperationResult

| name | order | meaning |
|---|---|---|
| `Ok` | 0 |  |
| `GenericFail` | 1 |  |
| `DBError` | 2 |  |
| `MTXError` | 3 |  |
| `InvalidOffer` | 4 |  |
| `InvalidPrice` | 5 |  |
| `NotEnoughCurrency` | 6 |  |
| `NeedTransaction` | 7 |  |
| `InvalidAccountItem` | 8 |  |
| `InvalidPendingItem` | 9 |  |
| `InvalidInventoryItem` | 10 |  |
| `NoConnection` | 11 |  |
| `NoCharacter` | 12 |  |
| `AlreadyClaimed` | 13 |  |
| `MaxEntitlementCount` | 14 |  |
| `NoRegift` | 15 |  |
| `NoGifting` | 16 |  |
| `InvalidFriend` | 17 |  |
| `InvalidCoupon` | 18 |  |
| `CannotReturn` | 19 |  |
| `Prereq` | 20 |  |
| `CREDDExchangeNotLoaded` | 21 |  |
| `NoCREDD` | 22 |  |
| `NoMatchingOrder` | 23 |  |
| `InvalidCREDDOrder` | 24 |  |
| `Cooldown` | 25 |  |
| `MissingEntitlement` | 26 |  |
| `AlreadyClaimedMultiRedeem` | 27 |  |

## CodeEnumAccountPrivilegeRestriction

| name | order | meaning |
|---|---|---|
| `Chat` | 0 |  |
| `Invite` | 1 |  |
| `PvpMatch` | 2 |  |
| `Trade` | 3 |  |

## CodeEnumAddonSaveLevel

| name | order | meaning |
|---|---|---|
| `General` | 0 |  |
| `Account` | 1 |  |
| `Realm` | 2 |  |
| `Character` | 3 |  |

## CodeEnumAddonStatus

| name | order | meaning |
|---|---|---|
| `Invalid` | 0 |  |
| `NotLoaded` | 1 |  |
| `ParsingError` | 2 |  |
| `Loaded` | 3 |  |
| `Suspended` | 4 |  |
| `RunningWithError` | 5 |  |
| `RunningOk` | 6 |  |

## CodeEnumArchetype

| name | order | meaning |
|---|---|---|
| `EliteShields` | 0 |  |
| `Iconic` | 1 |  |
| `Townie` | 2 |  |
| `EliteNoShields` | 3 |  |
| `Guard` | 4 |  |

## CodeEnumArrangeOrigin

| name | order | meaning |
|---|---|---|
| `LeftOrTop` | 0 |  |
| `Middle` | 1 |  |
| `RightOrBottom` | 2 |  |

## CodeEnumAttributeMilestoneResult

The possible results when attempting to get an Attribute Milestone's info.

| name | order | meaning |
|---|---|---|
| `Ok` | 0 |  |
| `InvalidUnit` | 1 |  |
| `UnknownClassId` | 2 |  |

## CodeEnumAuctionRemaining

| name | order | meaning |
|---|---|---|
| `Expiring` | 0 |  |
| `LessThanHour` | 1 |  |
| `Short` | 2 |  |
| `Long` | 3 |  |
| `Very_Long` | 4 |  |

## CodeEnumCCState

An enum representing the various crowd control effects, including Taunt

| name | order | meaning |
|---|---|---|
| `Stun` | 0 |  |
| `Sleep` | 1 |  |
| `Root` | 2 |  |
| `Disarm` | 3 |  |
| `Silence` | 4 |  |
| `Polymorph` | 5 |  |
| `Fear` | 6 |  |
| `Hold` | 7 |  |
| `Knockdown` | 8 |  |
| `Vulnerability` | 9 |  |
| `VulnerabilityWithAct` | 10 |  |
| `Disorient` | 11 |  |
| `Disable` | 12 |  |
| `Taunt` | 13 |  |
| `Detaunt` | 14 |  |
| `Blind` | 15 |  |
| `Knockback` | 16 |  |
| `Pushback` | 17 |  |
| `Pull` | 18 |  |
| `PositionSwitch` | 19 |  |
| `Tether` | 20 |  |
| `Snare` | 21 |  |
| `Interrupt` | 22 |  |
| `Daze` | 23 |  |
| `Subdue` | 24 |  |
| `Grounded` | 25 |  |
| `DisableCinematic` | 26 |  |
| `AbilityRestriction` | 27 |  |

## CodeEnumCCStateApplyRulesResult

The possible results when something attempts to apply a Crowd Control state to a unit.

| name | order | meaning |
|---|---|---|
| `Ok` | 0 |  |
| `InvalidCCState` | 1 |  |
| `NoTargetSpecified` | 2 |  |
| `Target_Immune` | 3 |  |
| `Target_InfiniteInterruptArmor` | 4 |  |
| `Stacking_DoesNotStack` | 5 |  |
| `Stacking_ShorterDuration` | 6 |  |
| `Target_InterruptArmorReduced` | 7 |  |
| `Target_InterruptArmorBlocked` | 8 |  |
| `DiminishingReturns_TriggerCap` | 9 |  |

## CodeEnumCCStateStunVictimGameplay

| name | order | meaning |
|---|---|---|
| `Forward` | 0 |  |
| `Backward` | 1 |  |
| `Left` | 2 |  |
| `Right` | 3 |  |

## CodeEnumCastBarType

Represents the type of cast bar being shown

| name | order | meaning |
|---|---|---|
| `None` | 0 |  |
| `Normal` | 1 |  |
| `Telegraph_Backlash` | 2 |  |
| `Telegraph_Evade` | 3 |  |

## CodeEnumCastMethod

| name | order | meaning |
|---|---|---|
| `Normal` | 0 |  |
| `Channeled` | 1 |  |
| `ChanneledField` | 2 |  |
| `ClientSideInteraction` | 3 |  |
| `PressHold` | 4 |  |
| `RapidTap` | 5 |  |
| `ChargeRelease` | 6 |  |
| `Multiphase` | 7 |  |
| `Transactional` | 8 |  |
| `UNUSED04` | 9 |  |
| `Aura` | 10 |  |

## CodeEnumCastResult

| name | order | meaning |
|---|---|---|
| `Ok` | 0 |  |
| `UnableToCreateSpell` | 1 |  |
| `MovingToCast` | 2 |  |
| `PendingSpellCast` | 3 |  |
| `SpellBad` | 4 |  |
| `SpellCancelled` | 5 |  |
| `SpellMaxChannel` | 6 |  |
| `SpellRemoved` | 7 |  |
| `SpellCountered` | 8 |  |
| `SpellCastingInterrupts` | 9 |  |
| `SpellInterrupted` | 10 |  |
| `SpellCombatModeActiveCount` | 11 |  |
| `SpellAlreadyCasting` | 12 |  |
| `SpellGlobalCooldown` | 13 |  |
| `SpellCooldown` | 14 |  |
| `SpellGroupCooldown` | 15 |  |
| `SpellPreRequisites` | 16 |  |
| `ActionBarSetDisallows` | 17 |  |
| `DamageInterrupts` | 18 |  |
| `InvalidInventoryIndex` | 19 |  |
| `ItemUnknown` | 20 |  |
| `ItemBad` | 21 |  |
| `ItemNoSpellId` | 22 |  |
| `ItemUnEquipped` | 23 |  |
| `ItemCharges` | 24 |  |
| `ItemTooHighLevel` | 25 |  |
| `ItemQuestRequirementsNotMet` | 26 |  |
| `ItemObjectiveComplete` | 27 |  |
| `CasterUnknown` | 28 |  |
| `CasterMustHaveTarget` | 29 |  |
| `CasterCannotBePrimaryTarget` | 30 |  |
| `CasterNotIncontrolOfSelf` | 31 |  |
| `CasterMovement` | 32 |  |
| `CasterMaxCast` | 33 |  |
| `CCStun` | 34 |  |
| `CCSleep` | 35 |  |
| `CCRoot` | 36 |  |
| `CCDisarm` | 37 |  |
| `CCSilence` | 38 |  |
| `CCPolymorph` | 39 |  |
| `CCFear` | 40 |  |
| `CCHold` | 41 |  |
| `CasterVitalCostHealth` | 42 |  |
| `CasterVitalCostXp` | 43 |  |
| `CasterVitalCostMoney` | 44 |  |
| `CasterVitalCostCurrency1` | 45 |  |
| `CasterVitalCostCurrency2` | 46 |  |
| `CasterVitalCostCurrency3` | 47 |  |
| `CasterVitalCostResource0` | 48 |  |
| `CasterVitalCostResource1` | 49 |  |
| `CasterVitalCostResource2` | 50 |  |
| `CasterVitalCostResource3` | 51 |  |
| `CasterVitalCostResource4` | 52 |  |
| `CasterVitalCostResource5` | 53 |  |
| `CasterVitalCostResource6` | 54 |  |
| `Caster_CannotBeDead` | 55 |  |
| `Caster_MustBeDead` | 56 |  |
| `Caster_CannotBe_Moving` | 57 |  |
| `Caster_MustBe_Moving` | 58 |  |
| `Caster_CannotBe_Stealth` | 59 |  |
| `Caster_MustBe_Stealth` | 60 |  |
| `Caster_CannotBe_Piloting` | 61 |  |
| `Caster_MustBe_Piloting` | 62 |  |
| `Caster_CannotBe_Embarked` | 63 |  |
| `Caster_MustBe_Embarked` | 64 |  |
| `Caster_CannotBe_Taxi` | 65 |  |
| `Caster_MustBe_Taxi` | 66 |  |
| `Caster_CannotBe_Stun` | 67 |  |
| `Caster_MustBe_Stun` | 68 |  |
| `Caster_CannotBe_Sleep` | 69 |  |
| `Caster_MustBe_Sleep` | 70 |  |
| `Caster_CannotBe_Root` | 71 |  |
| `Caster_MustBe_Root` | 72 |  |
| `Caster_CannotBe_Disarm` | 73 |  |
| `Caster_MustBe_Disarm` | 74 |  |
| `Caster_CannotBe_Silence` | 75 |  |
| `Caster_MustBe_Silence` | 76 |  |
| `Caster_CannotBe_Pacify` | 77 |  |
| `Caster_MustBe_Pacify` | 78 |  |
| `Caster_CannotBe_Fear` | 79 |  |
| `Caster_MustBe_Fear` | 80 |  |
| `Caster_CannotBe_Confuse` | 81 |  |
| `Caster_MustBe_Confuse` | 82 |  |
| `TargetGroup` | 83 |  |
| `TargetUnknown` | 84 |  |
| `NoTarget` | 85 |  |
| `Target_ImmuneToSpellType` | 86 |  |
| `Target_ImmuneToSpell` | 87 |  |
| `Target_ImmuneToSpellGroupList` | 88 |  |
| `Target_ImmuneToSpellGroup` | 89 |  |
| `Target_Invulnerable` | 90 |  |
| `TargetMaxTarget` | 91 |  |
| `TargetVital` | 92 |  |
| `TargetFaction` | 93 |  |
| `TargetIsNotUseable` | 94 |  |
| `TargetOrientation` | 95 |  |
| `TargetCannotBePlayer` | 96 |  |
| `TargetCannotBeNpc` | 97 |  |
| `TargetRangeMin` | 98 |  |
| `TargetRangeMax` | 99 |  |
| `Target_CannotBeDead` | 100 |  |
| `Target_MustBeDead` | 101 |  |
| `Target_CannotBe_Moving` | 102 |  |
| `Target_MustBe_Moving` | 103 |  |
| `Target_CannotBe_Stealth` | 104 |  |
| `Target_MustBe_Stealth` | 105 |  |
| `Target_CannotBe_Piloting` | 106 |  |
| `Target_MustBe_Piloting` | 107 |  |
| `Target_CannotBe_Embarked` | 108 |  |
| `Target_MustBe_Embarked` | 109 |  |
| `Target_CannotBe_Taxi` | 110 |  |
| `Target_MustBe_Taxi` | 111 |  |
| `Target_CannotBe_Stun` | 112 |  |
| `Target_MustBe_Stun` | 113 |  |
| `Target_CannotBe_Sleep` | 114 |  |
| `Target_MustBe_Sleep` | 115 |  |
| `Target_CannotBe_Root` | 116 |  |
| `Target_MustBe_Root` | 117 |  |
| `Target_CannotBe_Disarm` | 118 |  |
| `Target_MustBe_Disarm` | 119 |  |
| `Target_CannotBe_Silence` | 120 |  |
| `Target_MustBe_Silence` | 121 |  |
| `Target_CannotBe_Pacify` | 122 |  |
| `Target_MustBe_Pacify` | 123 |  |
| `Target_CannotBe_Fear` | 124 |  |
| `Target_MustBe_Fear` | 125 |  |
| `Target_CannotBe_Confuse` | 126 |  |
| `Target_MustBe_Confuse` | 127 |  |
| `Target_CannotBe_Swimming` | 128 |  |
| `Target_MustBe_Swimming` | 129 |  |
| `InWrongWorldZone` | 130 |  |
| `DuelOver` | 131 |  |
| `UNUSED142` | 132 |  |
| `UNUSED143` | 133 |  |
| `MissingResult` | 134 |  |
| `IsP2PTrading` | 135 |  |
| `ClientSideInteractionFail` | 136 |  |
| `StackingRefreshExistingSpell` | 137 |  |
| `StackingTargetHasMorePowerfulSpells` | 138 |  |
| `StackingCasterHasMorePowerfulSpells` | 139 |  |
| `StackingError` | 140 |  |
| `Prereq_CasterCast` | 141 |  |
| `CCKnockdown` | 142 |  |
| `CCVulnerability` | 143 |  |
| `Target_MustBe_Knockdown` | 144 |  |
| `Target_MustBe_Vulnerability` | 145 |  |
| `Caster_MustBe_Vulnerability` | 146 |  |
| `Caster_MustBe_Knockdown` | 147 |  |
| `Caster_CannotBe_Knockdown` | 148 |  |
| `Caster_CannotBe_Vulnerability` | 149 |  |
| `Target_CannotBe_Vulnerability` | 150 |  |
| `Target_CannotBe_Knockdown` | 151 |  |
| `MissingReagent_Item` | 152 |  |
| `MissingReagent_ItemFamily` | 153 |  |
| `MissingReagent_ItemCategory` | 154 |  |
| `MissingReagent_ItemType` | 155 |  |
| `Caster_Needs_LoS` | 156 |  |
| `CasterVitalCostMana` | 157 |  |
| `TargetImmuneToSpellEffect` | 158 |  |
| `WeaponSlot` | 159 |  |
| `Caster_MustBe_Jumping` | 160 |  |
| `Caster_CannotBe_Jumping` | 161 |  |
| `Target_CannotBe_Jumping` | 162 |  |
| `Target_MustBe_Jumping` | 163 |  |
| `InvalidPosition` | 164 |  |
| `CasterVitalCost` | 165 |  |
| `CasterVitalCostShieldCapacity` | 166 |  |
| `CasterVitalCostResource7` | 167 |  |
| `FailSpecialRestrictions` | 168 |  |
| `NoValidActivateSpell` | 169 |  |
| `SchematicAlreadyKnown` | 170 |  |
| `TradeskillTier` | 171 |  |
| `SpellNoCharges` | 172 |  |
| `TargetRangeVertical` | 173 |  |
| `StackingDuplicateDurationalSpell` | 174 |  |
| `SpellMaxPhaseReached` | 175 |  |
| `CCVulnerabilityWithAct` | 176 |  |
| `CCDisorient` | 177 |  |
| `CCDisable` | 178 |  |
| `CCTaunt` | 179 |  |
| `CCDeTaunt` | 180 |  |
| `CCBlind` | 181 |  |
| `CCKnockback` | 182 |  |
| `CCPushback` | 183 |  |
| `CCPull` | 184 |  |
| `CCPositionSwitch` | 185 |  |
| `CCTether` | 186 |  |
| `CCSnare` | 187 |  |
| `Caster_MustBe_Polymorph` | 188 |  |
| `Target_MustBe_Polymorph` | 189 |  |
| `Caster_CannotBe_Polymorph` | 190 |  |
| `Target_CannotBe_Polymorph` | 191 |  |
| `Caster_MustBe_Hold` | 192 |  |
| `Target_MustBe_Hold` | 193 |  |
| `Caster_CannotBe_Hold` | 194 |  |
| `Target_CannotBe_Hold` | 195 |  |
| `Caster_MustBe_Disorient` | 196 |  |
| `Target_MustBe_Disorient` | 197 |  |
| `Caster_CannotBe_Disorient` | 198 |  |
| `Target_CannotBe_Disorient` | 199 |  |
| `Caster_MustBe_Disable` | 200 |  |
| `Target_MustBe_Disable` | 201 |  |
| `Caster_CannotBe_Disable` | 202 |  |
| `Target_CannotBe_Disable` | 203 |  |
| `Caster_MustBe_Taunt` | 204 |  |
| `Target_MustBe_Taunt` | 205 |  |
| `Caster_CannotBe_Taunt` | 206 |  |
| `Target_CannotBe_Taunt` | 207 |  |
| `Caster_MustBe_DeTaunt` | 208 |  |
| `Target_MustBe_DeTaunt` | 209 |  |
| `Caster_CannotBe_DeTaunt` | 210 |  |
| `Target_CannotBe_DeTaunt` | 211 |  |
| `Caster_MustBe_Blind` | 212 |  |
| `Target_MustBe_Blind` | 213 |  |
| `Caster_CannotBe_Blind` | 214 |  |
| `Target_CannotBe_Blind` | 215 |  |
| `Caster_MustBe_Knockback` | 216 |  |
| `Target_MustBe_Knockback` | 217 |  |
| `Caster_CannotBe_Knockback` | 218 |  |
| `Target_CannotBe_Knockback` | 219 |  |
| `Caster_MustBe_Pushback` | 220 |  |
| `Target_MustBe_Pushback` | 221 |  |
| `Caster_CannotBe_Pushback` | 222 |  |
| `Target_CannotBe_Pushback` | 223 |  |
| `Caster_MustBe_Pull` | 224 |  |
| `Target_MustBe_Pull` | 225 |  |
| `Caster_CannotBe_Pull` | 226 |  |
| `Target_CannotBe_Pull` | 227 |  |
| `Caster_MustBe_PositionSwitch` | 228 |  |
| `Target_MustBe_PositionSwitch` | 229 |  |
| `Caster_CannotBe_PositionSwitch` | 230 |  |
| `Target_CannotBe_PositionSwitch` | 231 |  |
| `Caster_MustBe_Tether` | 232 |  |
| `Target_MustBe_Tether` | 233 |  |
| `Caster_CannotBe_Tether` | 234 |  |
| `Target_CannotBe_Tether` | 235 |  |
| `Caster_MustBe_Snare` | 236 |  |
| `Target_MustBe_Snare` | 237 |  |
| `Caster_CannotBe_Snare` | 238 |  |
| `Target_CannotBe_Snare` | 239 |  |
| `CasterVitalCostInterruptArmor` | 240 |  |
| `CCNoAbilities` | 241 |  |
| `Blacklisted` | 242 |  |
| `TargetCannotBePickup` | 243 |  |
| `CasterVitalCostAbsorption` | 244 |  |
| `Target_MustBe_CastersPet` | 245 |  |
| `Target_MustBe_CastersMaster` | 246 |  |
| `CCInterrupt` | 247 |  |
| `Caster_MustBe_Interrupt` | 248 |  |
| `Target_MustBe_Interrupt` | 249 |  |
| `Caster_CannotBe_Interrupt` | 250 |  |
| `Target_CannotBe_Interrupt` | 251 |  |
| `CSICooldown` | 252 |  |
| `CCDaze` | 253 |  |
| `Caster_MustBe_Daze` | 254 |  |
| `Target_MustBe_Daze` | 255 |  |
| `Caster_CannotBe_Daze` | 256 |  |
| `Target_CannotBe_Daze` | 257 |  |
| `CCSubdue` | 258 |  |
| `Caster_MustBe_Subdue` | 259 |  |
| `Target_MustBe_Subdue` | 260 |  |
| `Caster_CannotBe_Subdue` | 261 |  |
| `Target_CannotBe_Subdue` | 262 |  |
| `Target_CannotBe_Evading` | 263 |  |
| `Target_StructuredPlugBenefitRestricted` | 264 |  |
| `CasterVitalCostPublicResource0` | 265 |  |
| `CasterVitalCostPublicResource1` | 266 |  |
| `CasterVitalCostPublicResource2` | 267 |  |
| `InactiveInnateAbilitySpell` | 268 |  |
| `Caster_CannotBe_Swimming` | 269 |  |
| `Caster_MustBe_Swimming` | 270 |  |
| `Prereq_TargetCast` | 271 |  |
| `Prereq_CasterPersistence` | 272 |  |
| `Prereq_TargetPersistence` | 273 |  |
| `Prereq_Trap` | 274 |  |
| `IllegalSpellCast` | 275 |  |
| `TargetNotInSameGroup` | 276 |  |
| `BossToken_Permission` | 277 |  |
| `BossToken_NotReady` | 278 |  |
| `CCGrounded` | 279 |  |
| `Caster_MustBe_Grounded` | 280 |  |
| `Target_MustBe_Grounded` | 281 |  |
| `Caster_CannotBe_Grounded` | 282 |  |
| `Target_CannotBe_Grounded` | 283 |  |
| `SpellUnknown` | 284 |  |
| `ItemAchievementComplete` | 285 |  |
| `Caster_CannotBeInCombat` | 286 |  |
| `Caster_MustBeInCombat` | 287 |  |
| `Target_CannotBeInCombat` | 288 |  |
| `Target_MustBeInCombat` | 289 |  |
| `CCDisableCinematic` | 290 |  |
| `Caster_MustBe_DisableCinematic` | 291 |  |
| `Target_MustBe_DisableCinematic` | 292 |  |
| `Caster_CannotBe_DisableCinematic` | 293 |  |
| `Target_CannotBe_DisableCinematic` | 294 |  |
| `CCAbilityRestriction` | 295 |  |
| `Caster_MustBe_AbilityRestriction` | 296 |  |
| `Target_MustBe_AbilityRestriction` | 297 |  |
| `Caster_CannotBe_AbilityRestriction` | 298 |  |
| `Target_CannotBe_AbilityRestriction` | 299 |  |
| `Target_VehicleBenefitRestricted` | 300 |  |
| `TargetCannotBePet` | 301 |  |
| `Target_HostileInvulnerability` | 302 |  |
| `Target_InvulnerableToOther` | 303 |  |
| `Target_BeneficialInvulnerability` | 304 |  |
| `Caster_MustBe_Falling` | 305 |  |
| `Caster_CannotBe_Falling` | 306 |  |
| `Target_CannotBe_Falling` | 307 |  |
| `Target_MustBe_Falling` | 308 |  |
| `Caster_MustBe_Sprinting` | 309 |  |
| `Caster_CannotBe_Sprinting` | 310 |  |
| `Target_CannotBe_Sprinting` | 311 |  |
| `Target_MustBe_Sprinting` | 312 |  |
| `Queued` | 313 |  |
| `ItemWrongRace` | 314 |  |
| `ItemWrongClass` | 315 |  |
| `ItemAlreadyUnlocked` | 316 |  |
| `PlayerSpellPending` | 317 |  |
| `Target_MustBe_PvpFlagged` | 318 |  |
| `Caster_MustBe_PvpFlagged` | 319 |  |
| `Target_OutsideTelegraph` | 320 |  |
| `ShieldsOverloaded` | 321 |  |
| `CasterVitalCostResource8` | 322 |  |
| `CasterVitalCostResource9` | 323 |  |
| `CasterVitalCostResource10` | 324 |  |
| `RapidTransport_Invalid` | 325 |  |
| `CasterVitalCostFocus` | 326 |  |
| `ServiceTokens_InsufficentFunds` | 327 |  |

## CodeEnumCharacterCreationStart

| name | order | meaning |
|---|---|---|
| `Arkship` | 0 |  |
| `Demo01` | 1 |  |
| `Demo02` | 2 |  |
| `Nexus` | 3 |  |
| `PreTutorial` | 4 |  |
| `CostumeOnly` | 5 |  |

## CodeEnumCharacterModifyResults

| name | order | meaning |
|---|---|---|
| `DeleteOk` | 0 |  |
| `DeleteFailed` | 1 |  |
| `DeleteFailed_GuildMaster` | 2 |  |
| `CreateOk` | 3 |  |
| `CreateFailed` | 4 |  |
| `CreateFailed_Items` | 5 |  |
| `CreateFailed_UniqueName` | 6 |  |
| `CreateFailed_ActionBar` | 7 |  |
| `CreateFailed_Quests` | 8 |  |
| `CreateFailed_AccountFull` | 9 |  |
| `CreateFailed_InvalidName` | 10 |  |
| `CreateFailed_Faction` | 11 |  |
| `CreateFailed_Internal` | 12 |  |
| `RenameFailed` | 13 |  |
| `RenameFailed_Internal` | 14 |  |
| `RenameFailed_InvalidName` | 15 |  |
| `RenameFailed_UniqueName` | 16 |  |
| `RenameFailed_NoRename` | 17 |  |
| `RenameOk` | 18 |  |
| `RenameFailed_NoCurrency` | 19 |  |
| `RealmTransferFailed_InvalidRealm` | 20 |  |
| `RealmTransferOk` | 21 |  |
| `RealmTransferFailed_ServerDown` | 22 |  |
| `RealmTransferFailed_CharacterOnline` | 23 |  |
| `RealmTransferFailed_InvalidCharacter` | 24 |  |
| `RealmTransferFailed_CharacterLocked` | 25 |  |
| `RealmTransferFailed_NoCurrency` | 26 |  |
| `RealmTransferFailed_DbError` | 27 |  |
| `RealmTransferFailed_HasAuction` | 28 |  |
| `RealmTransferFailed_InGuild` | 29 |  |
| `RealmTransferFailed_HasCREDDExchange` | 30 |  |
| `RealmTransferFailed_CharacterBusy` | 31 |  |
| `RealmTransferFailed_HasMail` | 32 |  |
| `RealmTransferFailed_ServerFull` | 33 |  |
| `RedeemCREDDFailed_NoCREDD` | 34 |  |
| `RedeemCREDDFailed_NoEntitlement` | 35 |  |
| `RedeemCREDDFailed_Internal` | 36 |  |
| `RedeemCREDDOk` | 37 |  |
| `RedeemCREDDFailed_InvalidCREDD` | 38 |  |
| `RedeemCREDDFailed_PlatformError` | 39 |  |
| `RedeemCREDDFailed_PlatformPermaFail` | 40 |  |
| `RedeemCREDDFailed_PlatformTempFail` | 41 |  |
| `DeleteFailed_CharacterOnline` | 42 |  |
| `RenameFailed_CharacterOnline` | 43 |  |
| `CreateFailed_CharacterOnline` | 44 |  |
| `RealmTransferFailed_NoSubscription` | 45 |  |
| `RealmTransferFailed_Internal` | 46 |  |
| `RealmTransferFailed_Money` | 47 |  |
| `RealmTransferFailed_CharacterCooldown` | 48 |  |
| `RenameFailed_GameSessionMissing` | 49 |  |
| `RealmTransferFailed_HasSavedInstance` | 50 |  |
| `UndeleteOk` | 51 |  |
| `UndeleteFailed` | 52 |  |

## CodeEnumCharacterSelectResults

| name | order | meaning |
|---|---|---|
| `FailedRename` | 0 |  |
| `Failed` | 1 |  |
| `FailedDisabled` | 2 |  |
| `FailedCharacterInWorld` | 3 |  |

## CodeEnumClaimItemState

| name | order | meaning |
|---|---|---|
| `CanClaim` | 0 |  |
| `CharacterMaxed` | 1 |  |
| `AccountMaxed` | 2 |  |

## CodeEnumClass

| name | order | meaning |
|---|---|---|
| `Warrior` | 0 |  |
| `Engineer` | 1 |  |
| `Esper` | 2 |  |
| `Medic` | 3 |  |
| `Stalker` | 4 |  |
| `Spellslinger` | 5 |  |

## CodeEnumClass

| name | order | meaning |
|---|---|---|
| `Warrior` | 0 |  |
| `Engineer` | 1 |  |
| `Esper` | 2 |  |
| `Medic` | 3 |  |
| `Stalker` | 4 |  |
| `Spellslinger` | 5 |  |

## CodeEnumCombatMomentum

The different types of Combat Momentum bonuses that a player can earn.

| name | order | meaning |
|---|---|---|
| `Impulse` | 0 |  |
| `KillingPerformance` | 1 |  |
| `KillChain` | 2 |  |
| `Evade` | 3 |  |
| `Interrupt` | 4 |  |
| `CCBreak` | 5 |  |

## CodeEnumCombatResult

| name | order | meaning |
|---|---|---|
| `Avoid` | 0 |  |
| `Critical` | 1 |  |
| `Hit` | 2 |  |
| `NeedsTelegraphEvaluation` | 3 |  |
| `OutsideTelegraph` | 4 |  |
| `OutsideTelegraphInvalid` | 5 |  |
| `InsideTelegraph` | 6 |  |
| `NeedsHitResultCalc` | 7 |  |

## CodeEnumComparison

| name | order | meaning |
|---|---|---|
| `Equals` | 0 |  |
| `Greater` | 1 |  |
| `GreaterThanEqualTo` | 2 |  |
| `Less` | 3 |  |
| `LessThanEqualTo` | 4 |  |
| `Percent_Equals` | 5 |  |
| `Percent_Greater` | 6 |  |
| `Percent_GreaterThanEqualTo` | 7 |  |
| `Percent_Less` | 8 |  |
| `Percent_LessThanEqualTo` | 9 |  |

## CodeEnumConfirmButtonType

The different types of Action Confirm Buttons available

| name | order | meaning |
|---|---|---|
| `SendMail` | 0 |  |
| `CommitTrade` | 1 |  |
| `DeleteItem` | 2 |  |
| `SalvageItem` | 3 |  |
| `EquipItem` | 4 |  |
| `CraftingAbandon` | 5 |  |
| `MarketplaceAuctionSellSubmit` | 6 |  |
| `MarketplaceAuctionBuySubmit` | 7 |  |
| `MarketplaceCommoditiesSubmit` | 8 |  |
| `AccountClaimItem` | 9 |  |
| `AccountTakeItem` | 10 |  |
| `AccountGiftItem` | 11 |  |
| `AccountGiftItemReturn` | 12 |  |
| `CREDDExchangeSubmit` | 13 |  |
| `AccountCreddRedeem` | 14 |  |
| `CopyToClipboard` | 15 |  |
| `MatchingGameRespondToPending` | 16 |  |
| `ReportPlayer` | 17 |  |
| `GenericMapNodeChoose` | 18 |  |
| `SubmitSupportTicket` | 19 |  |
| `LootItem` | 20 |  |
| `RuneSlotReroll` | 21 | Used when setting up an ActionConfirmButton for use with a rune slot reroll.  Two additional parameters to SetActionData should be provided.  The first is the item containing the rune slot.  The second is the index of the rune slot. |
| `EldanForge` | 22 |  |
| `UnlockCostumeItem` | 23 |  |
| `ForgetCostumeItem` | 24 |  |
| `SaveCostumeChanges` | 25 |  |
| `RuneSlotClear` | 26 |  |
| `RuneSlotAdd` | 27 |  |
| `CommitCustomizationChanges` | 28 |  |
| `WakeHereService` | 29 |  |
| `CastSpellService` | 30 |  |
| `RapidTransport` | 31 |  |
| `SaveKeyBinding` | 32 | For saving the whole set of keybindings |

## CodeEnumConfirmButtonType

| name | order | meaning |
|---|---|---|
| `CopyToClipboard` | 0 |  |

## CodeEnumCraftingDirection

A list of directions used when performing non-equipment based tradeskills.

| name | order | meaning |
|---|---|---|
| `None` | 0 |  |
| `N` | 1 |  |
| `NE` | 2 |  |
| `E` | 3 |  |
| `SE` | 4 |  |
| `S` | 5 |  |
| `SW` | 6 |  |
| `W` | 7 |  |
| `NW` | 8 |  |

## CodeEnumCraftingDiscoveryHotCold

A set of enums representing how close a player was to discovering a schematic while performing non-equipment based tradeskills.

| name | order | meaning |
|---|---|---|
| `Cold` | 0 |  |
| `Warm` | 1 |  |
| `Hot` | 2 |  |
| `Success` | 3 |  |

## CodeEnumCreationGearSet

| name | order | meaning |
|---|---|---|
| `Low` | 0 |  |
| `Mid` | 1 |  |
| `High` | 2 |  |

## CodeEnumCurrencyType

| name | order | meaning |
|---|---|---|
| `Credits` | 0 |  |
| `Renown` | 1 |  |
| `ElderGems` | 2 |  |
| `CraftingVouchers` | 3 |  |
| `Prestige` | 4 |  |
| `GroupCurrency` | 5 |  |
| `ShadeSilver` | 6 |  |
| `Glory` | 7 |  |
| `ProtoCoins` | 8 |  |

## CodeEnumDailyLoginRewardTier

| name | order | meaning |
|---|---|---|
| `Normal` | 0 |  |
| `Milestone` | 1 |  |

## CodeEnumDailyLoginRewardType

| name | order | meaning |
|---|---|---|
| `AccountItem` | 0 |  |

## CodeEnumDamageType

| name | order | meaning |
|---|---|---|
| `Heal` | 0 |  |
| `Fall` | 1 |  |
| `Suffocate` | 2 |  |
| `Physical` | 3 |  |
| `Tech` | 4 |  |
| `Magic` | 5 |  |
| `HealShields` | 6 |  |

## CodeEnumDecorHookType

| name | order | meaning |
|---|---|---|
| `Roof` | 0 |  |
| `Entryway` | 1 |  |
| `Door` | 2 |  |
| `Wallpaper` | 3 |  |
| `FreePlace` | 4 |  |
| `DefaultHook` | 5 |  |
| `Crate` | 6 |  |
| `Landscape` | 7 |  |
| `WarplotFreePlace` | 8 |  |
| `Mannequin` | 9 |  |

## CodeEnumDiminishingReturnState

| name | order | meaning |
|---|---|---|
| `Linear` | 0 |  |
| `SoftCap` | 1 |  |
| `HardCap` | 2 |  |

## CodeEnumDisplayMode

| name | order | meaning |
|---|---|---|
| `SuperPanning` | 0 |  |
| `Panning` | 1 |  |
| `Scaled` | 2 |  |
| `Continent` | 3 |  |
| `World` | 4 |  |
| `SolarSystem` | 5 |  |

## CodeEnumDisposition

An NPC's disposition towards the player. Hostile: Attacks when their target is within agro range Neutral: Will only attack if they are attacked first     Friendly: The unit cannot attack or be attacked by the target

| name | order | meaning |
|---|---|---|
| `Hostile` | 0 |  |
| `Neutral` | 1 |  |
| `Friendly` | 2 |  |
| `Unknown` | 3 |  |

## CodeEnumDuelState

| name | order | meaning |
|---|---|---|
| `None` | 0 |  |
| `Pending` | 1 |  |
| `WaitingToAccept` | 2 |  |
| `Dueling` | 3 |  |

## CodeEnumEUnitStatType

| name | order | meaning |
|---|---|---|
| `Resources0` | 0 |  |
| `Resources1` | 1 |  |
| `Resources2` | 2 |  |
| `Resources3` | 3 |  |
| `Resources4` | 4 |  |
| `Resources5` | 5 |  |
| `Resources6` | 6 |  |
| `Resources7` | 7 |  |
| `Resources8` | 8 |  |
| `Resources9` | 9 |  |
| `Resources10` | 10 |  |

## CodeEnumEldanAvailability

This enum rempresents the AMP's current state.  Unavailable - The player has not unlocked the AMP Inaccessible - The player has not unlocked that AMP's tier Inactivated - The player has not spent points to activate this AMP Activated - The player has spent points to activate this AMP

| name | order | meaning |
|---|---|---|
| `Unavailable` | 0 |  |
| `Inaccessible` | 1 |  |
| `Inactivated` | 2 |  |
| `Activated` | 3 |  |

## CodeEnumEliteness

An enum representing the estimated group size needed to kill the NPC.

| name | order | meaning |
|---|---|---|
| `Solo` | 0 |  |
| `Group` | 1 |  |
| `SmallRaid` | 2 |  |
| `LargeRaid` | 3 |  |

## CodeEnumEntitlement

| name | order | meaning |
|---|---|---|
| `BaseCharacterProgressionCaps` | 0 |  |
| `BaseCharacterSlots` | 1 |  |
| `BaseCurrencyCaps` | 2 |  |
| `EconomyParticipation` | 3 |  |
| `GuildsAccess` | 4 |  |
| `FullSocialParticipation` | 5 |  |
| `CREDDUsage` | 6 |  |
| `InGameCSAccess` | 7 |  |
| `CostumeSlots` | 8 |  |
| `Signature` | 9 |  |
| `Free` | 10 |  |
| `ExtraAuctions` | 11 |  |
| `ExtraCommodity` | 12 |  |
| `ExtraBankSlots` | 13 |  |
| `FullGuildsAccess` | 14 |  |
| `WakeHereCooldownReduction` | 15 |  |
| `TwoStepVerification` | 16 |  |
| `LoyaltyBonusCoordinateCraftingRadius` | 17 |  |
| `ExtraCommodityOrders` | 18 |  |
| `ExtraDecorSlots` | 19 |  |
| `AdditionalCostumeUnlocks` | 20 |  |
| `LoyaltyExtraCommodityOrders` | 21 |  |
| `LoyaltyExtraAuctions` | 22 |  |
| `LoyaltyChallengeBonus` | 23 |  |
| `LoyaltyRestXpBonus` | 24 |  |

## CodeEnumEquipItemResult

| name | order | meaning |
|---|---|---|
| `Ok` | 0 |  |
| `Cooldown` | 1 |  |
| `Invalid` | 2 |  |
| `LevelTooLow` | 3 |  |
| `WrongClass` | 4 |  |
| `WrongRace` | 5 |  |

## CodeEnumEquippedItems

| name | order | meaning |
|---|---|---|
| `Chest` | 0 |  |
| `Legs` | 1 |  |
| `Head` | 2 |  |
| `Shoulder` | 3 |  |
| `Feet` | 4 |  |
| `Hands` | 5 |  |
| `WeaponTool` | 6 |  |
| `WeaponAttachment` | 7 |  |
| `System` | 8 |  |
| `Augment` | 9 |  |
| `Implant` | 10 |  |
| `Gadget` | 11 |  |
| `Shields` | 12 |  |
| `WeaponPrimary` | 13 |  |
| `Bag0` | 14 |  |
| `Bag1` | 15 |  |
| `Bag2` | 16 |  |
| `Bag3` | 17 |  |
| `BankBag0` | 18 |  |
| `BankBag1` | 19 |  |
| `BankBag2` | 20 |  |
| `BankBag3` | 21 |  |
| `BankBag4` | 22 |  |
| `DEPRECATED3` | 23 |  |
| `DEPRECATED2` | 24 |  |
| `DEPRECATED1` | 25 |  |
| `BankBag5` | 26 |  |
| `BankBag6` | 27 |  |
| `BankBag7` | 28 |  |
| `BankBag8` | 29 |  |
| `BankBag9` | 30 |  |

## CodeEnumExitEvent

| name | order | meaning |
|---|---|---|
| `None` | 0 |  |
| `Camp` | 1 |  |
| `Quit` | 2 |  |

## CodeEnumExpReason

The possible sources that a player can gain experience from.

| name | order | meaning |
|---|---|---|
| `Invalid` | 0 |  |
| `Load` | 1 |  |
| `Cheat` | 2 |  |
| `KillCreature` | 3 |  |
| `Quest` | 4 |  |
| `ClusterBonus` | 5 |  |
| `Spell` | 6 |  |
| `Exploration` | 7 |  |
| `QuestEpisodeCompletion` | 8 |  |
| `PathMission` | 9 |  |
| `PathEpisode` | 10 |  |
| `KillPerformance` | 11 |  |
| `MultiKill` | 12 |  |
| `KillingSpree` | 13 |  |
| `TelegraphInterrupt` | 14 |  |
| `TelegraphEvade` | 15 |  |
| `Momentum` | 16 |  |
| `Rested` | 17 |  |
| `PublicEvent` | 18 |  |
| `DailyQuest` | 19 |  |
| `PeriodicQuest` | 20 |  |

## CodeEnumFaction

An enum representing the different player factions

| name | order | meaning |
|---|---|---|
| `DominionPlayer` | 0 |  |
| `ExilesPlayer` | 1 |  |

## CodeEnumFaction

| name | order | meaning |
|---|---|---|
| `Dominion` | 0 |  |
| `Exile` | 1 |  |

## CodeEnumFlightPathType

An enum representing different types of flight paths Local: Traveling from one place to another within the same worldId Transfer: Traveling from one worldId to another

| name | order | meaning |
|---|---|---|
| `Local` | 0 |  |
| `Transfer` | 1 |  |

## CodeEnumFloaterCollisionMode

The collision modes that floating combat text can be set to.

| name | order | meaning |
|---|---|---|
| `IgnoreCollision` | 0 |  |
| `Horizontal` | 1 |  |
| `Vertical` | 2 |  |

## CodeEnumFloaterEffect

A list of particle effects that can be added to floating combat text

| name | order | meaning |
|---|---|---|
| `Flames` | 0 |  |
| `BluishWhite` | 1 |  |
| `Sparks` | 2 |  |
| `Spiral` | 3 |  |
| `Cloud` | 4 |  |
| `Splotches` | 5 |  |
| `SlashBlood` | 6 |  |
| `Impact` | 7 |  |
| `SplatBlood` | 8 |  |
| `Helix` | 9 |  |
| `ShadowFire` | 10 |  |
| `Cold` | 11 |  |
| `Stars` | 12 |  |

## CodeEnumFloaterLocation

The location on a unit that the floating text would spawn from.

| name | order | meaning |
|---|---|---|
| `Top` | 0 |  |
| `Head` | 1 |  |
| `Chest` | 2 |  |
| `Back` | 3 |  |
| `Bottom` | 4 |  |

## CodeEnumGameCommandType

| name | order | meaning |
|---|---|---|
| `GadgetAbility` | 0 |  |
| `DefaultAttack` | 1 |  |
| `ClassInnateAbility` | 2 |  |
| `ActivateTarget` | 3 |  |
| `FollowTarget` | 4 |  |
| `Sprint` | 5 |  |
| `ToggleWalk` | 6 |  |
| `Dismount` | 7 |  |
| `Vacuum` | 8 |  |
| `PathAction` | 9 |  |
| `ToggleScannerBot` | 10 |  |
| `DashForward` | 11 |  |
| `DashBackward` | 12 |  |
| `DashLeft` | 13 |  |
| `DashRight` | 14 |  |
| `PathAction2` | 15 |  |
| `Interact` | 16 |  |
| `GoToBind` | 17 |  |
| `GoToHouse` | 18 |  |
| `EscapeHouse` | 19 |  |
| `GoToWarplot` | 20 |  |
| `WarplotBossTokenUI` | 21 |  |
| `SummonMount` | 22 |  |
| `UsePotion` | 23 |  |
| `GoToIllium` | 24 |  |
| `GoToThayd` | 25 |  |
| `HousingLandscape` | 26 |  |
| `HousingRemodel` | 27 |  |
| `HousingCrate` | 28 |  |
| `HousingVendor` | 29 |  |
| `HousingList` | 30 |  |
| `HousingEditMode` | 31 |  |

## CodeEnumGameMode

| name | order | meaning |
|---|---|---|
| `West` | 0 |  |
| `China` | 1 |  |

## CodeEnumGameMode

| name | order | meaning |
|---|---|---|
| `West` | 0 |  |
| `China` | 1 |  |

## CodeEnumGameMode

| name | order | meaning |
|---|---|---|
| `West` | 0 |  |
| `China` | 1 |  |

## CodeEnumGender

An enum representing a unit's gender.  For the sake of this enum, Chua are male.

| name | order | meaning |
|---|---|---|
| `Male` | 0 |  |
| `Female` | 1 |  |
| `Uni` | 2 |  |

## CodeEnumGender

| name | order | meaning |
|---|---|---|
| `Male` | 0 |  |
| `Female` | 1 |  |
| `Unisex` | 2 |  |

## CodeEnumGenericError

| name | order | meaning |
|---|---|---|
| `Ok` | 0 |  |
| `Params` | 1 |  |
| `PlayerBusy` | 2 |  |
| `UnknownTargetUnit` | 3 |  |
| `TargetFaction` | 4 |  |
| `DbFailure` | 5 |  |
| `Item_BadId` | 6 |  |
| `Vendor_StackSize` | 7 |  |
| `Vendor_SoldOut` | 8 |  |
| `Vendor_UnknownItem` | 9 |  |
| `Vendor_FailedPreReq` | 10 |  |
| `Vendor_NotAVendor` | 11 |  |
| `Vendor_TooFar` | 12 |  |
| `Vendor_BadItemRec` | 13 |  |
| `Vendor_NotEnoughToFillQuantity` | 14 |  |
| `Vendor_NotEnoughCash` | 15 |  |
| `Vendor_UniqueConstraint` | 16 |  |
| `Vendor_ItemLocked` | 17 |  |
| `Vendor_IWontBuyThat` | 18 |  |
| `Vendor_NoQuantity` | 19 |  |
| `Vendor_BagIsNotEmpty` | 20 |  |
| `Item_OverFlowChestCreated` | 21 |  |
| `Item_InventoryFull` | 22 |  |
| `Item_UnknownItem` | 23 |  |
| `Item_QuestViolation` | 24 |  |
| `Item_Unique` | 25 |  |
| `Item_NotValidforSlot` | 26 |  |
| `Item_Locked` | 27 |  |
| `Item_AlreadyEquipped` | 28 |  |
| `Item_NotEquipped` | 29 |  |
| `Item_BagMustBeEmpty` | 30 |  |
| `Item_CannotFindBag` | 31 |  |
| `Item_BagToSmall` | 32 |  |
| `Item_CantPutBagInItself` | 33 |  |
| `Item_WrongRace` | 34 |  |
| `Item_WrongClass` | 35 |  |
| `Item_FailedProficiency` | 36 |  |
| `Item_LevelToLow` | 37 |  |
| `Embark_PlayerAlreadyinSeat` | 38 |  |
| `Embark_PlayerUnableToEmbark` | 39 |  |
| `Embark_InvalidVehicleUnit` | 40 |  |
| `Embark_NoSplineForTaxi` | 41 |  |
| `Embark_VehicleIsBroken` | 42 |  |
| `Embark_InvalidSeat` | 43 |  |
| `Embark_SeatTaken` | 44 |  |
| `Embark_SeatEmpty` | 45 |  |
| `Embark_NotInRange` | 46 |  |
| `Embark_CannotDoWhileOnTaxi` | 47 |  |
| `Mail_CannotFindPlayer` | 48 |  |
| `Mail_FailedToCreate` | 49 |  |
| `Vendor_CuratorOnlyBuysRelics` | 50 |  |
| `Vendor_CannotBuyRelics` | 51 |  |
| `Player_CantDoWhileDead` | 52 |  |
| `Vendor_NoBuyer` | 53 |  |
| `Vendor_NoVendor` | 54 |  |
| `Vendor_Buyer_NoActionCC` | 55 |  |
| `Vendor_Vendor_NoActionCC` | 56 |  |
| `Vendor_Vendor_Disposition` | 57 |  |
| `Player_CannotWhileInCombat` | 58 |  |
| `Mail_Busy` | 59 |  |
| `Mail_MailBoxOutOfRange` | 60 |  |
| `Mail_NoAttachment` | 61 |  |
| `Mail_InsufficientFunds` | 62 |  |
| `Mail_InvalidInventorySlot` | 63 |  |
| `Mail_UniqueExists` | 64 |  |
| `Mail_CannotDelete` | 65 |  |
| `Mail_DoesNotExist` | 66 |  |
| `Item_CannotBeSalvaged` | 67 |  |
| `Conversion_BadConversionRec` | 68 |  |
| `Conversion_CannotRemoveSource` | 69 |  |
| `Conversion_CannotAddTarget` | 70 |  |
| `Faction_NotEnoughRep` | 71 |  |
| `Item_NoItems` | 72 |  |
| `Craft_TierTooLow` | 73 |  |
| `Craft_MissingMaterials` | 74 |  |
| `Craft_IncompleteCircuit` | 75 |  |
| `Craft_SocketNotModdable` | 76 |  |
| `Craft_DuplicateChip` | 77 |  |
| `DisEmbark_PlayerNotInWorld` | 78 |  |
| `Item_NeedsRepair` | 79 |  |
| `Craft_TooManyAdditives` | 80 |  |
| `Item_SlotDisabled` | 81 |  |
| `Matching_NoRoleSelected` | 82 |  |
| `Instance_NotFound` | 83 |  |
| `Mail_CannotTransferItem` | 84 |  |
| `Mail_InvalidText` | 85 |  |
| `Mail_CanNotHaveCoDAndGift` | 86 |  |
| `Reserved02` | 87 |  |
| `Reserved03` | 88 |  |
| `Reserved04` | 89 |  |
| `Auction_NotReady` | 90 |  |
| `Auction_CannotFillOrder` | 91 |  |
| `Auction_TooManyOrders` | 92 |  |
| `Auction_OrderTooBig` | 93 |  |
| `Auction_NotFound` | 94 |  |
| `Auction_BidTooLow` | 95 |  |
| `Auction_OwnItem` | 96 |  |
| `Auction_BidTooHigh` | 97 |  |
| `Auction_AlreadyHasBid` | 98 |  |
| `Mail_InvalidDeliverySpeed` | 99 |  |
| `Housing_InvalidDecorPlacement` | 100 |  |
| `Instance_LimitExceeded` | 101 |  |
| `Craft_UnknownSchematic` | 102 |  |
| `Craft_MicrochipInvalidSocket` | 103 |  |
| `Craft_MicrochipInvalidSlot` | 104 |  |
| `Craft_FailChanceTooHigh` | 105 |  |
| `Instance_EncounterInProgress` | 106 |  |
| `Instance_Full` | 107 |  |
| `Housing_CrateFull` | 108 |  |
| `TargetBusy` | 109 |  |
| `Mail_CannotReturn` | 110 |  |
| `Mail_CannotMailSelf` | 111 |  |
| `Faction_AtMax` | 112 |  |
| `Housing_MaxDecor` | 113 |  |
| `Auction_ItemAuctionDisabled` | 114 |  |
| `Auction_CommodityDisabled` | 115 |  |
| `Mail_CannotMailTrialAccount` | 116 |  |
| `MissingEntitlement` | 117 |  |
| `Instance_TransferPending` | 118 |  |
| `Instance_InvalidDestination` | 119 |  |
| `Instance_NotInGroup` | 120 |  |
| `Instance_DifferentSavedInstance` | 121 |  |
| `Instance_InstanceInUse` | 122 |  |
| `Item_WrongFaction` | 123 |  |
| `Instance_WrongLevel` | 124 |  |
| `Mail_Squelched` | 125 |  |
| `LootForge_QualityMismatch` | 126 |  |
| `LootForge_InvalidItem` | 127 |  |
| `LootForge_CountMismatch` | 128 |  |
| `LootForge_Invalid` | 129 |  |
| `RewardTrack_CannotClaim` | 130 |  |
| `RewardTrack_InvalidRewardChoice` | 131 |  |
| `RewardTrack_InvalidTrackChoice` | 132 |  |
| `RewardTrack_TrackNotActive` | 133 |  |
| `RewardTrack_TrackAlreadyActive` | 134 |  |
| `Item_EquipPrereqFailed` | 135 |  |
| `Instance_PenaltyMap` | 136 |  |
| `Item_CannotBeDeleted` | 137 |  |
| `UNUSED81` | 138 |  |
| `UNUSED113` | 139 |  |
| `Auction_TooManyBids` | 140 |  |
| `AccountItem_MaxEntitlementCount` | 141 |  |
| `Item_BadParams` | 142 |  |
| `Item_BadStaticData` | 143 |  |
| `Craft_TooFar` | 144 |  |
| `Craft_InvalidTier` | 145 |  |
| `Craft_BadId` | 146 |  |
| `Craft_BadParams` | 147 |  |
| `Craft_InvalidPowerCore` | 148 |  |
| `RewardTrack_Locked` | 149 |  |
| `MTXChest_AlreadyOpened` | 150 |  |

## CodeEnumGroupCurrencyType

| name | order | meaning |
|---|---|---|
| `None` | 0 |  |
| `WarCoins` | 1 |  |

## CodeEnumGuildEventType

| name | order | meaning |
|---|---|---|
| `Achievement` | 0 |  |
| `PerkUnlock` | 1 |  |
| `PerkActivate` | 2 |  |
| `MemberAdded` | 3 |  |
| `MemberRemoved` | 4 |  |
| `MemberRankChanged` | 5 |  |
| `MessageOfTheDay` | 6 |  |
| `BankMoney` | 7 |  |
| `ItemRepair` | 8 |  |
| `BankTab` | 9 |  |

## CodeEnumHintType

| name | order | meaning |
|---|---|---|
| `None` | 0 |  |
| `PathMission` | 1 |  |
| `Quest` | 2 |  |
| `PublicEvent` | 3 |  |
| `PublicEventObjective` | 4 |  |
| `Unit` | 5 |  |
| `Challenge` | 6 |  |
| `NavPoint` | 7 |  |

## CodeEnumInputAction

| name | order | meaning |
|---|---|---|
| `Nothing` | 0 |  |
| `Options` | 1 |  |
| `CharacterPanel` | 2 |  |
| `Inventory` | 3 |  |
| `QuestLog` | 4 |  |
| `Communicator` | 5 |  |
| `Escape` | 6 |  |
| `Shift` | 7 |  |
| `Control` | 8 |  |
| `Select` | 9 |  |
| `MouseInteract` | 10 |  |
| `Interact` | 11 |  |
| `HostileInteract` | 12 |  |
| `TargetSelf` | 13 |  |
| `TargetParty1` | 14 |  |
| `TargetParty2` | 15 |  |
| `TargetParty3` | 16 |  |
| `TargetParty4` | 17 |  |
| `TargetNextEnemy` | 18 |  |
| `TargetPreviousEnemy` | 19 |  |
| `TargetNextFriend` | 20 |  |
| `TargetPreviousFriend` | 21 |  |
| `AssistTarget` | 22 |  |
| `MoveForward` | 23 |  |
| `MoveBackward` | 24 |  |
| `StrafeLeft` | 25 |  |
| `StrafeRight` | 26 |  |
| `TurnLeft` | 27 |  |
| `TurnRight` | 28 |  |
| `PitchUp` | 29 |  |
| `PitchDown` | 30 |  |
| `MouseTurn` | 31 |  |
| `SprintModifier` | 32 |  |
| `VacuumLoot` | 33 |  |
| `PathAction` | 34 |  |
| `Jump` | 35 |  |
| `Dismount` | 36 |  |
| `ToggleSit` | 37 |  |
| `ToggleWalk` | 38 |  |
| `ToggleAutoRun` | 39 |  |
| `CameraUp` | 40 |  |
| `CameraDown` | 41 |  |
| `CameraLeft` | 42 |  |
| `CameraRight` | 43 |  |
| `CameraIn` | 44 |  |
| `CameraOut` | 45 |  |
| `MouseLook` | 46 |  |
| `CastObjectiveAbility` | 47 |  |
| `LimitedActionSet1` | 48 |  |
| `LimitedActionSet2` | 49 |  |
| `LimitedActionSet3` | 50 |  |
| `LimitedActionSet4` | 51 |  |
| `LimitedActionSet5` | 52 |  |
| `LimitedActionSet6` | 53 |  |
| `LimitedActionSet7` | 54 |  |
| `LimitedActionSet8` | 55 |  |
| `CastGadgetAbility` | 56 |  |
| `CastPathAbility` | 57 |  |
| `ActionBar0_Unused1` | 58 |  |
| `ActionBar0_Unused2` | 59 |  |
| `ActionBar1_Slot1` | 60 |  |
| `ActionBar1_Slot2` | 61 |  |
| `ActionBar1_Slot3` | 62 |  |
| `ActionBar1_Slot4` | 63 |  |
| `ActionBar1_Slot5` | 64 |  |
| `ActionBar1_Slot6` | 65 |  |
| `ActionBar1_Slot7` | 66 |  |
| `ActionBar1_Slot8` | 67 |  |
| `ActionBar1_Slot9` | 68 |  |
| `ActionBar1_Slot10` | 69 |  |
| `ActionBar1_Slot11` | 70 |  |
| `ActionBar1_Slot12` | 71 |  |
| `ActionBar2_Slot1` | 72 |  |
| `ActionBar2_Slot2` | 73 |  |
| `ActionBar2_Slot3` | 74 |  |
| `ActionBar2_Slot4` | 75 |  |
| `ActionBar2_Slot5` | 76 |  |
| `ActionBar2_Slot6` | 77 |  |
| `ActionBar2_Slot7` | 78 |  |
| `ActionBar2_Slot8` | 79 |  |
| `ActionBar2_Slot9` | 80 |  |
| `ActionBar2_Slot10` | 81 |  |
| `ActionBar2_Slot11` | 82 |  |
| `ActionBar2_Slot12` | 83 |  |
| `ActionBar3_Slot1` | 84 |  |
| `ActionBar3_Slot2` | 85 |  |
| `ActionBar3_Slot3` | 86 |  |
| `ActionBar3_Slot4` | 87 |  |
| `ActionBar3_Slot5` | 88 |  |
| `ActionBar3_Slot6` | 89 |  |
| `ActionBar3_Slot7` | 90 |  |
| `ActionBar3_Slot8` | 91 |  |
| `ActionBar3_Slot9` | 92 |  |
| `ActionBar3_Slot10` | 93 |  |
| `ActionBar3_Slot11` | 94 |  |
| `ActionBar3_Slot12` | 95 |  |
| `Unused1` | 96 |  |
| `Unused2` | 97 |  |
| `Unused3` | 98 |  |
| `Unused4` | 99 |  |
| `Unused5` | 100 |  |
| `Unused6` | 101 |  |
| `SetStance1` | 102 |  |
| `SetStance2` | 103 |  |
| `SetStance3` | 104 |  |
| `Unused7` | 105 |  |
| `Unused20` | 106 |  |
| `Unused11` | 107 |  |
| `ToggleInterface` | 108 |  |
| `ToggleFramerate` | 109 |  |
| `Unused21` | 110 |  |
| `Unused23` | 111 |  |
| `Unused22` | 112 |  |
| `WorldMap` | 113 |  |
| `LimitedActionSetBuilder` | 114 |  |
| `Unused8` | 115 |  |
| `Unused9` | 116 |  |
| `ExplicitMouseLook` | 117 |  |
| `ToggleWeapons` | 118 |  |
| `LeftMouseHold` | 119 |  |
| `RightMouseHold` | 120 |  |
| `CenterMouseHold` | 121 |  |
| `CastInnateAbility` | 122 |  |
| `MarkingMenuLeftClick` | 123 |  |
| `MarkingMenuLeftHold` | 124 |  |
| `MarkingMenuRightClick` | 125 |  |
| `MarkingMenuRightHold` | 126 |  |
| `HUDShowQuests` | 127 |  |
| `ToggleCameraAngle` | 128 |  |
| `ToggleScannerBot` | 129 |  |
| `Codex` | 130 |  |
| `PathAction2` | 131 |  |
| `FloatingActionBar_Slot1` | 132 |  |
| `FloatingActionBar_Slot2` | 133 |  |
| `FloatingActionBar_Slot3` | 134 |  |
| `FloatingActionBar_Slot4` | 135 |  |
| `FloatingActionBar_Slot5` | 136 |  |
| `FloatingActionBar_Slot6` | 137 |  |
| `ScaleRampedMotion` | 138 |  |
| `ScaleRampedRotation` | 139 |  |
| `BrakeRampedMotion` | 140 |  |
| `BrakeRampedRotation` | 141 |  |
| `MoveDown` | 142 |  |
| `GroupFinder` | 143 |  |
| `CastMiscSpell` | 144 |  |
| `SetTargetMark1` | 145 |  |
| `SetTargetMark2` | 146 |  |
| `SetTargetMark3` | 147 |  |
| `SetTargetMark4` | 148 |  |
| `SetTargetMark5` | 149 |  |
| `SetTargetMark6` | 150 |  |
| `SetTargetMark7` | 151 |  |
| `SetTargetMark8` | 152 |  |
| `DashForward` | 153 |  |
| `DashBackward` | 154 |  |
| `DashLeft` | 155 |  |
| `DashRight` | 156 |  |
| `Unused12` | 157 |  |
| `Unused13` | 158 |  |
| `ChatReply` | 159 |  |
| `ChatReWhisper` | 160 |  |
| `Unused14` | 161 |  |
| `Unused15` | 162 |  |
| `Unused16` | 163 |  |
| `Unused17` | 164 |  |
| `Unused18` | 165 |  |
| `Unused19` | 166 |  |
| `TargetNearestEnemy` | 167 |  |
| `TargetNearestFriend` | 168 |  |
| `Achievements` | 169 |  |
| `AuctionListings` | 170 |  |
| `Challenges` | 171 |  |
| `Unused10` | 172 |  |
| `FriendsList` | 173 |  |
| `Lore` | 174 |  |
| `Mail` | 175 |  |
| `Path` | 176 |  |
| `Reputation` | 177 |  |
| `Social` | 178 |  |
| `Tradeskills` | 179 |  |
| `DirectionalDash` | 180 |  |
| `PrimaryPetActionBar_Slot1` | 181 |  |
| `PrimaryPetActionBar_Slot2` | 182 |  |
| `PrimaryPetActionBar_Slot3` | 183 |  |
| `PrimaryPetActionBar_Slot4` | 184 |  |
| `PrimaryPetActionBar_Slot5` | 185 |  |
| `PrimaryPetActionBar_Slot6` | 186 |  |
| `GhostModeMap` | 187 |  |
| `Mount` | 188 |  |
| `UsePotion` | 189 |  |
| `Guild` | 190 |  |
| `StunBreakoutUp` | 191 |  |
| `StunBreakoutDown` | 192 |  |
| `StunBreakoutLeft` | 193 |  |
| `StunBreakoutRight` | 194 |  |
| `ExplicitMouseLookHold` | 195 |  |
| `Store` | 196 |  |
| `AccountInventory` | 197 |  |
| `CreddExchange` | 198 |  |
| `Collectibles` | 199 |  |
| `Contracts` | 200 |  |
| `HoloWardrobe` | 201 |  |
| `LevelUpUnlocks` | 202 |  |
| `Who` | 203 |  |
| `NonCombatAbilities` | 204 |  |
| `Macros` | 205 |  |

## CodeEnumInputAction

| name | order | meaning |
|---|---|---|
| `Nothing` | 0 |  |
| `Options` | 1 |  |
| `CharacterPanel` | 2 |  |
| `Inventory` | 3 |  |
| `QuestLog` | 4 |  |
| `Communicator` | 5 |  |
| `Escape` | 6 |  |
| `Shift` | 7 |  |
| `Control` | 8 |  |
| `Select` | 9 |  |
| `MouseInteract` | 10 |  |
| `Interact` | 11 |  |
| `HostileInteract` | 12 |  |
| `TargetSelf` | 13 |  |
| `TargetParty1` | 14 |  |
| `TargetParty2` | 15 |  |
| `TargetParty3` | 16 |  |
| `TargetParty4` | 17 |  |
| `TargetNextEnemy` | 18 |  |
| `TargetPreviousEnemy` | 19 |  |
| `TargetNextFriend` | 20 |  |
| `TargetPreviousFriend` | 21 |  |
| `AssistTarget` | 22 |  |
| `MoveForward` | 23 |  |
| `MoveBackward` | 24 |  |
| `StrafeLeft` | 25 |  |
| `StrafeRight` | 26 |  |
| `TurnLeft` | 27 |  |
| `TurnRight` | 28 |  |
| `PitchUp` | 29 |  |
| `PitchDown` | 30 |  |
| `MouseTurn` | 31 |  |
| `SprintModifier` | 32 |  |
| `VacuumLoot` | 33 |  |
| `PathAction` | 34 |  |
| `Jump` | 35 |  |
| `Dismount` | 36 |  |
| `ToggleSit` | 37 |  |
| `ToggleWalk` | 38 |  |
| `ToggleAutoRun` | 39 |  |
| `CameraUp` | 40 |  |
| `CameraDown` | 41 |  |
| `CameraLeft` | 42 |  |
| `CameraRight` | 43 |  |
| `CameraIn` | 44 |  |
| `CameraOut` | 45 |  |
| `MouseLook` | 46 |  |
| `CastObjectiveAbility` | 47 |  |
| `LimitedActionSet1` | 48 |  |
| `LimitedActionSet2` | 49 |  |
| `LimitedActionSet3` | 50 |  |
| `LimitedActionSet4` | 51 |  |
| `LimitedActionSet5` | 52 |  |
| `LimitedActionSet6` | 53 |  |
| `LimitedActionSet7` | 54 |  |
| `LimitedActionSet8` | 55 |  |
| `CastGadgetAbility` | 56 |  |
| `CastPathAbility` | 57 |  |
| `ActionBar0_Unused1` | 58 |  |
| `ActionBar0_Unused2` | 59 |  |
| `ActionBar1_Slot1` | 60 |  |
| `ActionBar1_Slot2` | 61 |  |
| `ActionBar1_Slot3` | 62 |  |
| `ActionBar1_Slot4` | 63 |  |
| `ActionBar1_Slot5` | 64 |  |
| `ActionBar1_Slot6` | 65 |  |
| `ActionBar1_Slot7` | 66 |  |
| `ActionBar1_Slot8` | 67 |  |
| `ActionBar1_Slot9` | 68 |  |
| `ActionBar1_Slot10` | 69 |  |
| `ActionBar1_Slot11` | 70 |  |
| `ActionBar1_Slot12` | 71 |  |
| `ActionBar2_Slot1` | 72 |  |
| `ActionBar2_Slot2` | 73 |  |
| `ActionBar2_Slot3` | 74 |  |
| `ActionBar2_Slot4` | 75 |  |
| `ActionBar2_Slot5` | 76 |  |
| `ActionBar2_Slot6` | 77 |  |
| `ActionBar2_Slot7` | 78 |  |
| `ActionBar2_Slot8` | 79 |  |
| `ActionBar2_Slot9` | 80 |  |
| `ActionBar2_Slot10` | 81 |  |
| `ActionBar2_Slot11` | 82 |  |
| `ActionBar2_Slot12` | 83 |  |
| `ActionBar3_Slot1` | 84 |  |
| `ActionBar3_Slot2` | 85 |  |
| `ActionBar3_Slot3` | 86 |  |
| `ActionBar3_Slot4` | 87 |  |
| `ActionBar3_Slot5` | 88 |  |
| `ActionBar3_Slot6` | 89 |  |
| `ActionBar3_Slot7` | 90 |  |
| `ActionBar3_Slot8` | 91 |  |
| `ActionBar3_Slot9` | 92 |  |
| `ActionBar3_Slot10` | 93 |  |
| `ActionBar3_Slot11` | 94 |  |
| `ActionBar3_Slot12` | 95 |  |
| `Unused1` | 96 |  |
| `Unused2` | 97 |  |
| `Unused3` | 98 |  |
| `Unused4` | 99 |  |
| `Unused5` | 100 |  |
| `Unused6` | 101 |  |
| `SetStance1` | 102 |  |
| `SetStance2` | 103 |  |
| `SetStance3` | 104 |  |
| `Unused7` | 105 |  |
| `Unused20` | 106 |  |
| `Unused11` | 107 |  |
| `ToggleInterface` | 108 |  |
| `ToggleFramerate` | 109 |  |
| `Unused21` | 110 |  |
| `Unused23` | 111 |  |
| `Unused22` | 112 |  |
| `WorldMap` | 113 |  |
| `LimitedActionSetBuilder` | 114 |  |
| `Unused8` | 115 |  |
| `Unused9` | 116 |  |
| `ExplicitMouseLook` | 117 |  |
| `ToggleWeapons` | 118 |  |
| `LeftMouseHold` | 119 |  |
| `RightMouseHold` | 120 |  |
| `CenterMouseHold` | 121 |  |
| `CastInnateAbility` | 122 |  |
| `MarkingMenuLeftClick` | 123 |  |
| `MarkingMenuLeftHold` | 124 |  |
| `MarkingMenuRightClick` | 125 |  |
| `MarkingMenuRightHold` | 126 |  |
| `HUDShowQuests` | 127 |  |
| `ToggleCameraAngle` | 128 |  |
| `ToggleScannerBot` | 129 |  |
| `Codex` | 130 |  |
| `PathAction2` | 131 |  |
| `FloatingActionBar_Slot1` | 132 |  |
| `FloatingActionBar_Slot2` | 133 |  |
| `FloatingActionBar_Slot3` | 134 |  |
| `FloatingActionBar_Slot4` | 135 |  |
| `FloatingActionBar_Slot5` | 136 |  |
| `FloatingActionBar_Slot6` | 137 |  |
| `ScaleRampedMotion` | 138 |  |
| `ScaleRampedRotation` | 139 |  |
| `BrakeRampedMotion` | 140 |  |
| `BrakeRampedRotation` | 141 |  |
| `MoveDown` | 142 |  |
| `GroupFinder` | 143 |  |
| `CastMiscSpell` | 144 |  |
| `SetTargetMark1` | 145 |  |
| `SetTargetMark2` | 146 |  |
| `SetTargetMark3` | 147 |  |
| `SetTargetMark4` | 148 |  |
| `SetTargetMark5` | 149 |  |
| `SetTargetMark6` | 150 |  |
| `SetTargetMark7` | 151 |  |
| `SetTargetMark8` | 152 |  |
| `DashForward` | 153 |  |
| `DashBackward` | 154 |  |
| `DashLeft` | 155 |  |
| `DashRight` | 156 |  |
| `Unused12` | 157 |  |
| `Unused13` | 158 |  |
| `ChatReply` | 159 |  |
| `ChatReWhisper` | 160 |  |
| `Unused14` | 161 |  |
| `Unused15` | 162 |  |
| `Unused16` | 163 |  |
| `Unused17` | 164 |  |
| `Unused18` | 165 |  |
| `Unused19` | 166 |  |
| `TargetNearestEnemy` | 167 |  |
| `TargetNearestFriend` | 168 |  |
| `Achievements` | 169 |  |
| `AuctionListings` | 170 |  |
| `Challenges` | 171 |  |
| `Unused10` | 172 |  |
| `FriendsList` | 173 |  |
| `Lore` | 174 |  |
| `Mail` | 175 |  |
| `Path` | 176 |  |
| `Social` | 177 |  |
| `Tradeskills` | 178 |  |
| `DirectionalDash` | 179 |  |
| `PrimaryPetActionBar_Slot1` | 180 |  |
| `PrimaryPetActionBar_Slot2` | 181 |  |
| `PrimaryPetActionBar_Slot3` | 182 |  |
| `PrimaryPetActionBar_Slot4` | 183 |  |
| `PrimaryPetActionBar_Slot5` | 184 |  |
| `PrimaryPetActionBar_Slot6` | 185 |  |
| `GhostModeMap` | 186 |  |
| `Mount` | 187 |  |
| `UsePotion` | 188 |  |
| `Guild` | 189 |  |
| `StunBreakoutUp` | 190 |  |
| `StunBreakoutDown` | 191 |  |
| `StunBreakoutLeft` | 192 |  |
| `StunBreakoutRight` | 193 |  |
| `ExplicitMouseLookHold` | 194 |  |
| `Store` | 195 |  |
| `AccountInventory` | 196 |  |
| `CreddExchange` | 197 |  |
| `Collectibles` | 198 |  |
| `Contracts` | 199 |  |
| `HoloWardrobe` | 200 |  |
| `LevelUpUnlocks` | 201 |  |
| `Who` | 202 |  |
| `NonCombatAbilities` | 203 |  |
| `Macros` | 204 |  |
| `Reputation` | 205 |  |

## CodeEnumInputDevice

| name | order | meaning |
|---|---|---|
| `None` | 0 |  |
| `Keyboard` | 1 |  |
| `Mouse` | 2 |  |

## CodeEnumInputEventType

| name | order | meaning |
|---|---|---|
| `Raw` | 0 |  |
| `Click` | 1 |  |
| `Hold` | 2 |  |
| `DoubleClick` | 3 |  |
| `DoubleHold` | 4 |  |
| `Rapid` | 5 |  |

## CodeEnumInputKeyLookupGroup

| name | order | meaning |
|---|---|---|
| `Main` | 0 |  |
| `StunBreakoutGameplay` | 1 |  |
| `Count` | 2 |  |
| `First` | 3 |  |
| `Last` | 4 |  |

## CodeEnumInputModifier

| name | order | meaning |
|---|---|---|
| `Shift` | 0 |  |
| `Control` | 1 |  |
| `Alt` | 2 |  |

## CodeEnumInputModifierScancode

| name | order | meaning |
|---|---|---|
| `LeftShift` | 0 |  |
| `LeftCtrl` | 1 |  |
| `LeftAlt` | 2 |  |
| `RightShift` | 3 |  |
| `RightCtrl` | 4 |  |
| `RightAlt` | 5 |  |

## CodeEnumInputMouse

| name | order | meaning |
|---|---|---|
| `Left` | 0 |  |
| `Right` | 1 |  |
| `Middle` | 2 |  |
| `X1` | 3 |  |
| `X2` | 4 |  |
| `WheelUp` | 5 |  |
| `WheelDown` | 6 |  |

## CodeEnumInputSets

| name | order | meaning |
|---|---|---|
| `Default1` | 0 |  |
| `Default2` | 1 |  |
| `Default3` | 2 |  |
| `Account` | 3 |  |
| `Character` | 4 |  |
| `Count` | 5 |  |

## CodeEnumItem2Category

| name | order | meaning |
|---|---|---|
| `Weapon_Sword2H` | 0 |  |
| `Weapon_Paddles` | 1 |  |
| `Weapon_Pistols1H` | 2 |  |
| `Weapon_Psyblade` | 3 |  |
| `Weapon_Claws` | 4 |  |
| `Weapon_HeavyGun` | 5 |  |
| `FireRune` | 6 |  |
| `WaterRune` | 7 |  |
| `EarthRune` | 8 |  |
| `AirRune` | 9 |  |
| `LifeRune` | 10 |  |
| `LogicRune` | 11 |  |
| `FusionRune` | 12 |  |
| `PowerCore` | 13 |  |

## CodeEnumItem2Family

| name | order | meaning |
|---|---|---|
| `Armor` | 0 |  |
| `Weapon` | 1 |  |
| `Container` | 2 |  |
| `Key` | 3 |  |
| `Furniture` | 4 |  |
| `Mount` | 5 |  |
| `Body` | 6 |  |
| `General` | 7 |  |
| `BrokenItem` | 8 |  |
| `Ornamental` | 9 |  |
| `Consumable` | 10 |  |
| `ChargedItem` | 11 |  |
| `Reagent` | 12 |  |
| `Schematic` | 13 |  |
| `HousingInterior` | 14 |  |
| `HousingExterior` | 15 |  |
| `HousingPlug` | 16 |  |
| `Special` | 17 |  |
| `Quest` | 18 |  |
| `Item` | 19 |  |
| `Costume` | 20 |  |
| `Crafting` | 21 |  |
| `Tool` | 22 |  |
| `Rune` | 23 |  |

## CodeEnumItemCraftingGroupFlag

| name | order | meaning |
|---|---|---|
| `Air` | 0 |  |
| `Water` | 1 |  |
| `Earth` | 2 |  |
| `Fire` | 3 |  |
| `Logic` | 4 |  |
| `Life` | 5 |  |
| `Fusion` | 6 |  |

## CodeEnumItemDetailedTooltip

| name | order | meaning |
|---|---|---|
| `Basic` | 0 |  |
| `Spells` | 1 |  |
| `Economics` | 2 |  |
| `Sigils` | 3 |  |
| `Imbuements` | 4 |  |
| `Stats` | 5 |  |
| `Restrictions` | 6 |  |
| `Specifics` | 7 |  |
| `Runes` | 8 |  |

## CodeEnumItemQuality

| name | order | meaning |
|---|---|---|
| `Average` | 0 |  |
| `Good` | 1 |  |
| `Excellent` | 2 |  |
| `Superb` | 3 |  |
| `Legendary` | 4 |  |
| `Inferior` | 5 |  |
| `Artifact` | 6 |  |

## CodeEnumItemSlots

| name | order | meaning |
|---|---|---|
| `Chest` | 0 |  |
| `Legs` | 1 |  |
| `Head` | 2 |  |
| `Shoulder` | 3 |  |
| `Feet` | 4 |  |
| `Hands` | 5 |  |
| `Tool` | 6 |  |
| `Weapon` | 7 |  |
| `Shields` | 8 |  |
| `Gadget` | 9 |  |
| `Attachment` | 10 |  |
| `System` | 11 |  |
| `Augment` | 12 |  |
| `Implant` | 13 |  |

## CodeEnumItemStatType

| name | order | meaning |
|---|---|---|
| `None` | 0 |  |
| `UnitProperty` | 1 |  |
| `Random` | 2 |  |
| `Set` | 3 |  |
| `UnlockedGroup` | 4 |  |
| `UNUSED03` | 5 |  |

## CodeEnumItemType

| name | order | meaning |
|---|---|---|
| `ArmorArcaneChest` | 0 |  |
| `ArmorArcaneLegs` | 1 |  |
| `ArmorArcaneHead` | 2 |  |
| `ArmorArcaneShoulder` | 3 |  |
| `ArmorArcaneFeet` | 4 |  |
| `ArmorArcaneHands` | 5 |  |
| `ArmorArcaneBuckle` | 6 |  |
| `ArmorReflexChest` | 7 |  |
| `ArmorReflexLegs` | 8 |  |
| `ArmorReflexHead` | 9 |  |
| `ArmorReflexShoulder` | 10 |  |
| `ArmorReflexFeet` | 11 |  |
| `ArmorReflexHands` | 12 |  |
| `ArmorReflexBuckle` | 13 |  |
| `ArmorFocalChest` | 14 |  |
| `ArmorFocalLegs` | 15 |  |
| `ArmorFocalHead` | 16 |  |
| `ArmorFocalShoulder` | 17 |  |
| `ArmorFocalFeet` | 18 |  |
| `ArmorFocalHands` | 19 |  |
| `ArmorFocalBuckle` | 20 |  |
| `ArmorBattleChest` | 21 |  |
| `ArmorBattleLegs` | 22 |  |
| `ArmorBattleHead` | 23 |  |
| `ArmorBattleShoulder` | 24 |  |
| `ArmorBattleFeet` | 25 |  |
| `ArmorBattleHands` | 26 |  |
| `ArmorBattleBuckle` | 27 |  |
| `ArmorJewelryRing` | 28 |  |
| `ArmorJewelryFace` | 29 |  |
| `ArmorJewelryNeck` | 30 |  |
| `ArmorJewelryTrinket` | 31 |  |
| `ArmorMiscChest` | 32 |  |
| `ArmorMiscLegs` | 33 |  |
| `ArmorMiscHead` | 34 |  |
| `ArmorMiscShoulder` | 35 |  |
| `ArmorMiscFeet` | 36 |  |
| `ArmorMiscHands` | 37 |  |
| `ArmorMiscBuckle` | 38 |  |
| `ArmorMiscRing` | 39 |  |
| `ArmorMiscFace` | 40 |  |
| `ArmorMiscNeck` | 41 |  |
| `ArmorMiscTrinket` | 42 |  |
| `WeaponMHAxe` | 43 |  |
| `WeaponMHPistols` | 44 |  |
| `WeaponMHEnergy` | 45 |  |
| `WeaponMHCrook` | 46 |  |
| `WeaponMHFist` | 47 |  |
| `WeaponMHPlasmaGun` | 48 |  |
| `WeaponMHStave` | 49 |  |
| `WeaponMHSword` | 50 |  |
| `WeaponMHMace` | 51 |  |
| `WeaponOHShadowCrystal` | 52 |  |
| `WeaponOHBatteryPack` | 53 |  |
| `WeaponOHInstrument` | 54 |  |
| `WeaponOHBook` | 55 |  |
| `WeaponOHMindGem` | 56 |  |
| `WeaponOHWrench` | 57 |  |
| `WeaponOHSword` | 58 |  |
| `WeaponOHShotgun` | 59 |  |
| `WeaponOHRelic` | 60 |  |
| `BodySkin` | 61 |  |
| `BodyFace` | 62 |  |
| `BodyEye` | 63 |  |
| `BodyEar` | 64 |  |
| `BodyHair` | 65 |  |
| `BodyTatoo` | 66 |  |
| `BodyTail` | 67 |  |
| `BodyHand` | 68 |  |
| `BodyUnderwear` | 69 |  |
| `BodyFacialHair` | 70 |  |
| `Bag` | 71 |  |
| `Spellbook` | 72 |  |
| `ItemFood` | 73 |  |
| `ItemPotion` | 74 |  |
| `Spell` | 75 |  |
| `QuestItem` | 76 |  |
| `WeaponMHScythe` | 77 |  |
| `Spell_Temporary` | 78 |  |
| `WeaponOHMagicthingy` | 79 |  |
| `ItemBandage` | 80 |  |
| `BrokenWeapon` | 81 |  |
| `BrokenRanged` | 82 |  |
| `BrokenMagic` | 83 |  |
| `Seeds` | 84 |  |
| `CookingStaple` | 85 |  |
| `CookingMeat` | 86 |  |
| `CookingHerb` | 87 |  |
| `CookingVeggie` | 88 |  |
| `CookingSeasoning` | 89 |  |
| `MiningMineral` | 90 |  |
| `WildGrowth` | 91 |  |
| `HarvestingPlant` | 92 |  |
| `RelicAndLore` | 93 |  |
| `Power` | 94 |  |
| `MineralComponent` | 95 |  |
| `WildComponent` | 96 |  |
| `PowerComponent` | 97 |  |
| `RelicComponent` | 98 |  |
| `ArmsmasterSchematic` | 99 |  |
| `TechsmithSchematic` | 100 |  |
| `WeaponchanterSchematic` | 101 |  |
| `ArcaneWeaverSchematic` | 102 |  |
| `ApothecarySchematic` | 103 |  |
| `TinkererSchematic` | 104 |  |
| `CookingSchematic` | 105 |  |
| `ArtisanSchematic` | 106 |  |
| `AssayConsumable` | 107 |  |
| `RefiningConsumable` | 108 |  |
| `ClubSoldiers` | 109 |  |
| `DiamondMerchants` | 110 |  |
| `SpadeCraftspeople` | 111 |  |
| `HeartArtists` | 112 |  |
| `StarPoliticans` | 113 |  |
| `OmniWild` | 114 |  |
| `OmniMining` | 115 |  |
| `OmniRelics` | 116 |  |
| `OmniPower` | 117 |  |
| `AssayMinigame` | 118 |  |
| `RefiningMinigame` | 119 |  |
| `HousingAddon` | 120 |  |
| `ArmorEnchantment` | 121 |  |
| `WeaponEnchantment` | 122 |  |
| `TempBag` | 123 |  |
| `TaxiRoute` | 124 |  |
| `TempMount` | 125 |  |
| `RepItem` | 126 |  |
| `WeaponMHShockPaddles` | 127 |  |
| `WeaponMHClawsAttached` | 128 |  |
| `MountRight` | 129 |  |
| `HoverboardFront` | 130 |  |
| `HoverboardBack` | 131 |  |
| `HoverboardSides` | 132 |  |
| `HoverboardBottom` | 133 |  |
| `MountFront` | 134 |  |
| `MountBack` | 135 |  |
| `MountLeft` | 136 |  |

## CodeEnumItemUpdateReason

| name | order | meaning |
|---|---|---|
| `StackSplit` | 0 |  |
| `ConsumeCharge` | 1 |  |
| `SpellReagent` | 2 |  |
| `Transform` | 3 |  |
| `Cheat` | 4 |  |
| `Salvage` | 5 |  |
| `Extract` | 6 |  |
| `Vendor` | 7 |  |
| `Quest` | 8 |  |
| `SpellEffect` | 9 |  |
| `Script` | 10 |  |
| `PathReward` | 11 |  |
| `ResourceConversion` | 12 |  |
| `Auction` | 13 |  |
| `MaterialBagConversion` | 14 |  |
| `Loot` | 15 |  |
| `Buyback` | 16 |  |
| `Crafting` | 17 |  |
| `NewCharacter` | 18 |  |
| `PublicEvent` | 19 |  |
| `Mail` | 20 |  |
| `PlayerRequested` | 21 |  |
| `GuildBank` | 22 |  |
| `Trade` | 23 |  |
| `HousingCrate` | 24 |  |
| `None` | 25 |  |
| `GM` | 26 |  |
| `Expired` | 27 |  |
| `Gadget` | 28 |  |
| `AltSpell` | 29 |  |
| `Challenge` | 30 |  |
| `SettlerImprovementConsumeResource` | 31 |  |
| `HousingContribution` | 32 |  |
| `HousingUpkeep` | 33 |  |
| `TradeskillAdditiveCost` | 34 |  |
| `TradeskillGlyph` | 35 |  |
| `UniqueCleanup` | 36 |  |
| `PathExplorerReward` | 37 |  |
| `CharacterRecustomization` | 38 |  |
| `LootForge` | 39 |  |
| `RewardTrack` | 40 |  |
| `MatchingReward` | 41 |  |
| `DyeCostume` | 42 |  |
| `PublicEventObjective` | 43 |  |
| `ItemDeprecation` | 44 |  |
| `MTXChest` | 45 |  |

## CodeEnumLevelDifferentialAttribute

An enum that contains the different colors used to show level difference between a unit and the player.  These are listed in ascending order.

| name | order | meaning |
|---|---|---|
| `Grey` | 0 |  |
| `Green` | 1 |  |
| `Cyan` | 2 |  |
| `Blue` | 3 |  |
| `White` | 4 |  |
| `Yellow` | 5 |  |
| `Orange` | 6 |  |
| `Red` | 7 |  |
| `Magenta` | 8 |  |

## CodeEnumLimitedActionSetResult

The possible results that the UI can receive when trying to save an Action Set or AMP loadout.

| name | order | meaning |
|---|---|---|
| `Ok` | 0 |  |
| `SlotUnlockPrereqFalse` | 1 |  |
| `UnknownSpellId` | 2 |  |
| `UnknownClassId` | 3 |  |
| `UnknownSpellActionSetCategoryGroupPlacement` | 4 |  |
| `UnknownSlotActionSetCategoryGroupAllowed` | 5 |  |
| `InvalidSpellActionSetCategoryGroupPlacement` | 6 |  |
| `InvalidSlotActionSetCategoryGroupAllowed` | 7 |  |
| `SlotSpellAnyMatchFail` | 8 |  |
| `SlotSpellAllMatchFail` | 9 |  |
| `SlotSpellNoneMatchFail` | 10 |  |
| `UnknownSpellActionSetGroupMatchType` | 11 |  |
| `DuplicateSpell` | 12 |  |
| `SpellActionSetPrereqFalse` | 13 |  |
| `SpellDependencyAnyMatchFail` | 14 |  |
| `SpellDependencyAllMatchFail` | 15 |  |
| `SpellDependencyNoneMatchFail` | 16 |  |
| `BadSpellInActionSet` | 17 |  |
| `ActionSetRequirementAnyMatchFail` | 18 |  |
| `ActionSetRequirementAllMatchFail` | 19 |  |
| `ActionSetRequirementNoneMatchFail` | 20 |  |
| `InvalidActionSetSize` | 21 |  |
| `InvalidUnit` | 22 |  |
| `InvalidSlot` | 23 |  |
| `InvalidActionSetTable` | 24 |  |
| `SpellDependencyMaxMatchFail` | 25 |  |
| `RestrictedInPVP` | 26 |  |
| `PlayerIsDead` | 27 |  |
| `MissingTag` | 28 |  |
| `InCombat` | 29 |  |
| `EldanAugmentation_NotEnoughPower` | 30 |  |
| `EldanAugmentation_LockedInlaid` | 31 |  |
| `EldanAugmentation_LockedCategoryTier` | 32 |  |
| `EldanAugmentation_InvalidSeries` | 33 |  |
| `EldanAugmentation_InvalidId` | 34 |  |
| `EldanAugmentation_InvalidCategoryId` | 35 |  |
| `EldanAugmentation_InvalidCategoryTier` | 36 |  |
| `UpdateSpellInProgress` | 37 |  |
| `InVoid` | 38 |  |
| `InvalidSpecIndex` | 39 |  |
| `InvalidSpellTier` | 40 |  |
| `InsufficientAbilityPoints` | 41 |  |
| `EldanAugmentation_VersionMismatch` | 42 |  |
| `EldanAugmentation_SpecNotFound` | 43 |  |
| `LASChangeSpellFailed` | 44 |  |
| `SpecUnlockPrereqFalse` | 45 |  |

## CodeEnumLoadLevel

| name | order | meaning |
|---|---|---|
| `Machine` | 0 |  |
| `Account` | 1 |  |
| `Realm` | 2 |  |
| `Character` | 3 |  |

## CodeEnumLoadType

| name | order | meaning |
|---|---|---|
| `Default` | 0 |  |
| `Yes` | 1 |  |
| `No` | 2 |  |

## CodeEnumLootItemType

| name | order | meaning |
|---|---|---|
| `StaticItem` | 0 |  |
| `AltTable` | 1 |  |
| `Cash` | 2 |  |
| `Spell` | 3 |  |
| `CurrencyExchange` | 4 |  |
| `VirtualItem` | 5 |  |
| `AdventureSpell` | 6 |  |
| `AccountItem` | 7 |  |
| `AccountCurrency` | 8 |  |

## CodeEnumLootItemType

An enum representing the different types of loot that can drop off an NPC.  StaticItem: Your typical item loot.  Cash: Make money money...    Virtual Item: Virtual items used for specific quests / challenges / dungeons / adventures AdventureSpell: Drops that have an immediate effect on the player that picks them up

| name | order | meaning |
|---|---|---|
| `StaticItem` | 0 |  |
| `Cash` | 1 |  |
| `VirtualItem` | 2 |  |
| `AdventureSpell` | 3 |  |
| `AccountItem` | 4 |  |

## CodeEnumMapOverlayType

| name | order | meaning |
|---|---|---|
| `Unit` | 0 |  |
| `Object` | 1 |  |
| `PathObjective` | 2 |  |
| `QuestObjective` | 3 |  |

## CodeEnumMicrochipType

| name | order | meaning |
|---|---|---|
| `PowerSource` | 0 |  |
| `Stat` | 1 |  |
| `PowerUp` | 2 |  |
| `Special` | 3 |  |
| `Set` | 4 |  |
| `Omni` | 5 |  |
| `Resistor` | 6 |  |
| `Inductor` | 7 |  |
| `Capacitor` | 8 |  |

## CodeEnumMissType

| name | order | meaning |
|---|---|---|
| `Dodge` | 0 |  |

## CodeEnumModelAttachment

| name | order | meaning |
|---|---|---|
| `SpellMisc01` | 0 |  |
| `PropMisc01` | 1 |  |
| `FXMisc01` | 2 |  |
| `FXMisc02` | 3 |  |
| `FXMisc03` | 4 |  |
| `FXMisc04` | 5 |  |
| `FXMisc05` | 6 |  |
| `FXMisc06` | 7 |  |
| `FXMisc07` | 8 |  |
| `Passenger01` | 9 |  |
| `Passenger02` | 10 |  |
| `Passenger03` | 11 |  |
| `Passenger04` | 12 |  |
| `Passenger05` | 13 |  |
| `Passenger06` | 14 |  |
| `Passenger07` | 15 |  |
| `Passenger08` | 16 |  |
| `Passenger09` | 17 |  |
| `Passenger10` | 18 |  |
| `Head` | 19 |  |

## CodeEnumModelAttachment

| name | order | meaning |
|---|---|---|
| `FXMisc01` | 0 |  |
| `FXMisc02` | 1 |  |
| `FXMisc03` | 2 |  |
| `FXMisc04` | 3 |  |
| `FXMisc05` | 4 |  |
| `FXMisc06` | 5 |  |
| `FXMisc07` | 6 |  |
| `FXMisc08` | 7 |  |
| `FXMisc09` | 8 |  |

## CodeEnumModelSequence

| name | order | meaning |
|---|---|---|
| `APState0Idle` | 0 |  |
| `APState1Idle` | 1 |  |
| `APState2Idle` | 2 |  |
| `PistolsReady` | 3 |  |
| `ClawsReady` | 4 |  |
| `HeavyGunReady` | 5 |  |
| `TwoHReady` | 6 |  |
| `EsperReady` | 7 |  |
| `ShockPaddlesReady` | 8 |  |
| `PistolsStand` | 9 |  |
| `ClawsStand` | 10 |  |
| `TwoHGunStand` | 11 |  |
| `TwoHStand` | 12 |  |
| `DefaultStand` | 13 |  |
| `ShockPaddlesStand` | 14 |  |
| `DefaultStartScreenLoop01` | 15 |  |
| `DefaultExileStartScreenLoop01` | 16 |  |
| `DefaultDominionStartScreenLoop01` | 17 |  |

## CodeEnumMoveSpeed

| name | order | meaning |
|---|---|---|
| `Walk` | 0 |  |
| `Run` | 1 |  |
| `Sprint` | 2 |  |

## CodeEnumMusic

| name | order | meaning |
|---|---|---|
| `Auth` | 0 |  |
| `CharacterCreate` | 1 |  |
| `CharacterDelete` | 2 |  |
| `CharacterSelect` | 3 |  |
| `Login` | 4 |  |
| `Realm` | 5 |  |
| `Default` | 6 |  |

## CodeEnumPetStance

| name | order | meaning |
|---|---|---|
| `Assist` | 0 |  |
| `Stay` | 1 |  |
| `Passive` | 2 |  |
| `Defensive` | 3 |  |
| `Aggressive` | 4 |  |

## CodeEnumPlayerPathType

| name | order | meaning |
|---|---|---|
| `Explorer` | 0 |  |
| `Scientist` | 1 |  |
| `Settler` | 2 |  |
| `Soldier` | 3 |  |

## CodeEnumProperties

An enum representing various unit properties.  These properties are generally seen on the Character and Inspect screens in the default UI

| name | order | meaning |
|---|---|---|
| `Strength` | 0 |  |
| `Dexterity` | 1 |  |
| `Technology` | 2 |  |
| `Magic` | 3 |  |
| `Wisdom` | 4 |  |
| `BaseHealth` | 5 |  |
| `ManaPerFiveSeconds` | 6 |  |
| `HealthRegenMultiplier` | 7 |  |
| `ResourceMax_0` | 8 |  |
| `ResourceMax_1` | 9 |  |
| `ResourceMax_2` | 10 |  |
| `ResourceMax_3` | 11 |  |
| `ResourceMax_4` | 12 |  |
| `ResourceMax_5` | 13 |  |
| `ResourceMax_6` | 14 |  |
| `ResourceRegenMultiplier_0` | 15 |  |
| `ResourceRegenMultiplier_1` | 16 |  |
| `ResourceRegenMultiplier_2` | 17 |  |
| `ResourceRegenMultiplier_3` | 18 |  |
| `ResourceRegenMultiplier_4` | 19 |  |
| `ResourceRegenMultiplier_5` | 20 |  |
| `ResourceRegenMultiplier_6` | 21 |  |
| `ResistPhysical` | 22 |  |
| `ResistTech` | 23 |  |
| `ResistMagic` | 24 |  |
| `StalkerWoundMultiplier` | 25 |  |
| `KillingSpreeOutOfCombatGracePeriodMS` | 26 |  |
| `Rating_AvoidReduce` | 27 |  |
| `Rating_AvoidIncrease` | 28 |  |
| `MoveSpeedMultiplier` | 29 |  |
| `Rating_CritChanceIncrease` | 30 |  |
| `AssaultPower` | 31 |  |
| `SupportPower` | 32 |  |
| `ResourceMax_7` | 33 |  |
| `ResourceRegenMultiplier_7` | 34 |  |
| `Stamina` | 35 |  |
| `ShieldCapacityMax` | 36 |  |
| `Armor` | 37 |  |
| `Rating_CritChanceDecrease` | 38 |  |
| `InterruptArmor_Threshold` | 39 |  |
| `InterruptArmor_RechargeTime` | 40 |  |
| `InterruptArmor_RechargeCount` | 41 |  |
| `RatingCritSeverityIncrease` | 42 |  |
| `BaseAvoidChance` | 43 |  |
| `BaseCritChance` | 44 |  |
| `PvPPrestigeMultiplier` | 45 |  |
| `PvPXPMultiplier` | 46 |  |
| `BreathDecay` | 47 |  |
| `CCPower` | 48 |  |
| `CriticalHitSeverityMultiplier` | 49 |  |
| `Health_Total_Multiplier` | 50 |  |
| `JumpHeight` | 51 |  |
| `GravityMultiplier` | 52 |  |
| `XpMultiplier` | 53 |  |
| `ThreatMultiplier` | 54 |  |
| `AutoAttackDelayMultiplier` | 55 |  |
| `FallingDamageMultiplier` | 56 |  |
| `DamageDealtMultiplierMelee` | 57 |  |
| `DamageDealtMultiplierRanged` | 58 |  |
| `DamageDealtMultiplierSpell` | 59 |  |
| `DamageDealtMultiplierPhysical` | 60 |  |
| `DamageDealtMultiplierTech` | 61 |  |
| `DamageDealtMultiplierMagic` | 62 |  |
| `DamageTakenOffsetPhysical` | 63 |  |
| `DamageTakenOffsetTech` | 64 |  |
| `DamageTakenOffsetMagic` | 65 |  |
| `DamageTakenMultiplierPhysical` | 66 |  |
| `DamageTakenMultiplierTech` | 67 |  |
| `DamageTakenMultiplierMagic` | 68 |  |
| `HealingMultiplierOutgoing` | 69 |  |
| `HealingMultiplierIncoming` | 70 |  |
| `ExecutingEnergyRateMultiplier` | 71 |  |
| `CCDurationModifier` | 72 |  |
| `ResistPhysicalMitigationMultiplier` | 73 |  |
| `ResistTechMitigationMultiplier` | 74 |  |
| `ResistMagicMitigationMultiplier` | 75 |  |
| `KillSpreeCCVMulitplier` | 76 |  |
| `ManaFinalMultiplier` | 77 |  |
| `ReputationMultiplier` | 78 |  |
| `ShieldMitigationMin` | 79 |  |
| `ShieldMitigationMax` | 80 |  |
| `ShieldRegenPct` | 81 |  |
| `ShieldDamageTypes` | 82 |  |
| `SlowFallMultiplier` | 83 |  |
| `PathXpMultiplier` | 84 |  |
| `ScientistScanBotThoroughnessMultiplier` | 85 |  |
| `ScientistScanBotScanTimeMultiplier` | 86 |  |
| `ScientistScanBotRangeMultiplier` | 87 |  |
| `ScientistScanBotHealthMultiplier` | 88 |  |
| `ScientistScanBotSpeedMultiplier` | 89 |  |
| `SettlerImprovementTimeMultiplier` | 90 |  |
| `CreatureScientistScanMultiplier` | 91 |  |
| `ManaBase` | 92 |  |
| `InterruptArmor_AfterCCRechargeTime` | 93 |  |
| `InterruptArmor_AfterCCRechargeCount` | 94 |  |
| `PvPOffensiveRating` | 95 |  |
| `PvPDefensiveRating` | 96 |  |
| `DamageMitigationPctOffset` | 97 |  |
| `BaseAvoidReduceChance` | 98 |  |
| `BaseAvoidCritChance` | 99 |  |
| `StealthDetectionModifier` | 100 |  |
| `ManaRegenInCombat` | 101 |  |
| `ManaRegenOutOfCombat` | 102 |  |
| `SeeThroughStealth` | 103 |  |
| `FrictionMax` | 104 |  |
| `Deprecated1` | 105 |  |
| `Deprecated2` | 106 |  |
| `RenownGainMultiplier` | 107 |  |
| `MoneyDropMultiplier` | 108 |  |
| `SpellMechanicEnergyRegenOrDecayMultiplier` | 109 |  |
| `SpellMechanicEnergyDecayOverdriveMultiplier` | 110 |  |
| `ItemArmor` | 111 |  |
| `ItemAssaultPower` | 112 |  |
| `ItemSupportPower` | 113 |  |
| `IgnoreArmorBase` | 114 |  |
| `IgnoreShieldBase` | 115 |  |
| `MaxThreatVsCreature` | 116 |  |
| `ManaCostModifier` | 117 |  |
| `CooldownReductionModifier` | 118 |  |
| `BaseLifesteal` | 119 |  |
| `DamageMitigationPctOffsetPhysical` | 120 |  |
| `DamageMitigationPctOffsetTech` | 121 |  |
| `DamageMitigationPctOffsetMagic` | 122 |  |
| `PvPOffensePctOffset` | 123 |  |
| `PvPDefensePctOffset` | 124 |  |
| `ShieldTickTime` | 125 |  |
| `ShieldRebootTime` | 126 |  |
| `ScientistScanBotHealthRegenMultiplier` | 127 |  |
| `ScientistScanBotCooldownMultiplier` | 128 |  |
| `MountSpeedMultiplier` | 129 |  |
| `MoneyQuestMultiplier` | 130 |  |
| `XpQuestMultiplier` | 131 |  |
| `ReputationQuestMultiplier` | 132 |  |
| `PrestigeQuestMultiplier` | 133 |  |
| `NPCSpellExecutionFreqMultiplier` | 134 |  |
| `ResourceMax_8` | 135 |  |
| `ResourceRegenMultiplier_8` | 136 |  |
| `ResourceMax_9` | 137 |  |
| `ResourceRegenMultiplier_9` | 138 |  |
| `ResourceMax_10` | 139 |  |
| `ResourceRegenMultiplier_10` | 140 |  |
| `HealToShieldConversion` | 141 |  |
| `BaseGlanceAmount` | 142 |  |
| `BaseFocusPool` | 143 |  |
| `RatingFocusRecovery` | 144 |  |
| `RatingLifesteal` | 145 |  |
| `RatingMultiHitChance` | 146 |  |
| `AssaultRating` | 147 |  |
| `SupportRating` | 148 |  |
| `RatingCriticalMitigation` | 149 |  |
| `RatingIntensity` | 150 |  |
| `RatingVigor` | 151 |  |
| `RatingGlanceChance` | 152 |  |
| `RatingArmorPierce` | 153 |  |
| `RatingMultiHitAmount` | 154 |  |
| `RatingGlanceAmount` | 155 |  |
| `RatingDamageReflectAmount` | 156 |  |
| `RatingDamageReflectChance` | 157 |  |
| `RatingCCResilience` | 158 |  |
| `BaseFocusRecoveryInCombat` | 159 |  |
| `BaseFocusRecoveryOutofCombat` | 160 |  |
| `BaseMultiHitAmount` | 161 |  |
| `FocusCostModifier` | 162 |  |
| `BaseMultiHitChance` | 163 |  |
| `BaseDamageReflectAmount` | 164 |  |
| `BaseDamageReflectChance` | 165 |  |
| `BaseCriticalMitigation` | 166 |  |
| `BaseIntensity` | 167 |  |
| `BaseGlanceChance` | 168 |  |
| `FocusFinalMultiplier` | 169 |  |
| `BaseVigor` | 170 |  |

## CodeEnumRace

| name | order | meaning |
|---|---|---|
| `Human` | 0 |  |
| `Granok` | 1 |  |
| `Aurin` | 2 |  |
| `Draken` | 3 |  |
| `Mechari` | 4 |  |
| `Mordesh` | 5 |  |
| `Chua` | 6 |  |

## CodeEnumRace

| name | order | meaning |
|---|---|---|
| `Human` | 0 |  |
| `Granok` | 1 |  |
| `Aurin` | 2 |  |
| `Draken` | 3 |  |
| `Mechari` | 4 |  |
| `Mordesh` | 5 |  |
| `Chua` | 6 |  |

## CodeEnumRank

An enum representing the difficulty of an NPC in relation to other NPCs of the same level

| name | order | meaning |
|---|---|---|
| `Fodder` | 0 |  |
| `Minion` | 1 |  |
| `Standard` | 2 |  |
| `Champion` | 3 |  |
| `Superior` | 4 |  |
| `Elite` | 5 |  |

## CodeEnumReagentType

| name | order | meaning |
|---|---|---|
| `Item` | 0 |  |
| `ItemFamily` | 1 |  |
| `ItemCategory` | 2 |  |

## CodeEnumRealCurrency

| name | order | meaning |
|---|---|---|
| `USD` | 0 |  |
| `GBP` | 1 |  |
| `EUR` | 2 |  |

## CodeEnumRealmPVPType

| name | order | meaning |
|---|---|---|
| `PVE` | 0 |  |
| `PVP` | 1 |  |

## CodeEnumRealmPopulation

| name | order | meaning |
|---|---|---|
| `Low` | 0 |  |
| `Medium` | 1 |  |
| `High` | 2 |  |
| `Full` | 3 |  |

## CodeEnumRealmStatus

| name | order | meaning |
|---|---|---|
| `Unknown` | 0 |  |
| `Offline` | 1 |  |
| `Down` | 2 |  |
| `Standby` | 3 |  |
| `Up` | 4 |  |

## CodeEnumRecallCommand

| name | order | meaning |
|---|---|---|
| `BindPoint` | 0 |  |
| `House` | 1 |  |
| `Warplot` | 2 |  |
| `Illium` | 3 |  |
| `Thayd` | 4 |  |

## CodeEnumReportPlayerReason

| name | order | meaning |
|---|---|---|
| `Spam` | 0 |  |
| `Bot` | 1 |  |
| `Cheat` | 2 |  |
| `AFK` | 3 |  |

## CodeEnumReportPlayerSource

| name | order | meaning |
|---|---|---|
| `Default` | 0 |  |
| `Mail` | 1 |  |
| `FriendRequest` | 2 |  |
| `PartyRequest` | 3 |  |
| `InWorld` | 4 |  |
| `Chat` | 5 |  |
| `GuildRequest` | 6 |  |
| `PvpMatch` | 7 |  |
| `TradeRequest` | 8 |  |
| `AccountFriendRequest` | 9 |  |
| `NeighborRequest` | 10 |  |
| `Overturn` | 11 |  |

## CodeEnumResourceConversionType

An enum representing the various types of resource conversion.  Item2Item: One type of item for another type Item2Rep: One type of item for reputation with a faction Prereq2Rep: ???

| name | order | meaning |
|---|---|---|
| `Item2Item` | 0 |  |
| `Item2Rep` | 1 |  |
| `Prereq2Rep` | 2 |  |

## CodeEnumRewardInfoType

| name | order | meaning |
|---|---|---|
| `Quest` | 0 |  |
| `Challenge` | 1 |  |
| `Explorer` | 2 |  |
| `Scientist` | 3 |  |
| `Soldier` | 4 |  |
| `Settler` | 5 |  |
| `PublicEvent` | 6 |  |
| `Rival` | 7 |  |
| `Friend` | 8 |  |
| `ScientistSpell` | 9 |  |
| `TSpell` | 10 |  |
| `Contract` | 11 |  |

## CodeEnumRewardTrackType

| name | order | meaning |
|---|---|---|
| `ContractPvP` | 0 |  |
| `ContractPvE` | 1 |  |
| `Loyalty` | 2 |  |
| `Challenge` | 3 |  |

## CodeEnumRuneType

| name | order | meaning |
|---|---|---|
| `Air` | 0 |  |
| `Fire` | 1 |  |
| `Water` | 2 |  |
| `Earth` | 3 |  |
| `Logic` | 4 |  |
| `Life` | 5 |  |
| `Fusion` | 6 |  |
| `Omni` | 7 |  |

## CodeEnumSchool

| name | order | meaning |
|---|---|---|
| `Spell` | 0 |  |
| `Melee` | 1 |  |
| `Ranged` | 2 |  |
| `Unarmed` | 3 |  |

## CodeEnumSetNavPointFailed

| name | order | meaning |
|---|---|---|
| `Unknown` | 0 |  |
| `InMicro` | 1 |  |

## CodeEnumShortcutSet

These values represent what each Action Bar Shortcut is used for.

| name | order | meaning |
|---|---|---|
| `VehicleBar` | 0 |  |
| `PrimaryPetBar` | 1 |  |
| `PetMiniBar0` | 2 |  |
| `PetMiniBar1` | 3 |  |
| `PetMiniBar2` | 4 |  |
| `PetMiniBar3` | 5 |  |
| `PetMiniBar4` | 6 |  |
| `FloatingSpellBar` | 7 |  |
| `FloatingDynamicSpellBar` | 8 |  |
| `Count` | 9 |  |

## CodeEnumSigilType

| name | order | meaning |
|---|---|---|
| `Air` | 0 |  |
| `Fire` | 1 |  |
| `Water` | 2 |  |
| `Earth` | 3 |  |
| `Logic` | 4 |  |
| `Life` | 5 |  |
| `Fusion` | 6 |  |
| `Omni` | 7 |  |

## CodeEnumSpecConstant

This is a single value representing the maximum number of specs the player can have.

| name | order | meaning |
|---|---|---|
| `MaxNumSpecs` | 0 |  |

## CodeEnumSpecError

Error messages that the player can receive when attempting to save their spec.  Ok is the success case.

| name | order | meaning |
|---|---|---|
| `Ok` | 0 |  |
| `InvalidIndex` | 1 |  |
| `NoChange` | 2 |  |
| `InCombat` | 3 |  |
| `InvalidPlayer` | 4 |  |
| `IndexLocked` | 5 |  |
| `PvPRestricted` | 6 |  |
| `InVoid` | 7 |  |

## CodeEnumSpellClass

| name | order | meaning |
|---|---|---|
| `BuffDispellable` | 0 |  |
| `BuffNonDispellable` | 1 |  |
| `DebuffDispellable` | 2 |  |
| `DebuffNonDispellable` | 3 |  |
| `BuffNonDispelRightClickOk` | 4 |  |

## CodeEnumSpellEffectType

| name | order | meaning |
|---|---|---|
| `UnitPropertyModifier` | 0 |  |
| `VitalModifier` | 1 |  |
| `SpellCounter` | 2 |  |
| `ForcedMove` | 3 |  |
| `CCStateSet` | 4 |  |
| `Transference` | 5 |  |
| `SummonVehicle` | 6 |  |
| `Activate` | 7 |  |
| `Damage` | 8 |  |
| `FactionSet` | 9 |  |
| `Heal` | 10 |  |
| `Harvest` | 11 |  |
| `DistanceDependentDamage` | 12 |  |
| `Script` | 13 |  |
| `Proc` | 14 |  |
| `UnitStateSet` | 15 |  |
| `Resurrect` | 16 |  |
| `Fluff` | 17 |  |
| `Scale` | 18 |  |
| `ProxyLinearAE` | 19 |  |
| `SummonCreature` | 20 |  |
| `HousingTeleport` | 21 |  |
| `ActionBarSet` | 22 |  |
| `ForcedAction` | 23 |  |
| `ProxyChannel` | 24 |  |
| `Proxy` | 25 |  |
| `CCStateBreak` | 26 |  |
| `ForceFacing` | 27 |  |
| `Absorption` | 28 |  |
| `SapVital` | 29 |  |
| `Disguise` | 30 |  |
| `SpellImmunity` | 31 |  |
| `DistributedDamage` | 32 |  |
| `ChangePhase` | 33 |  |
| `NpcExecutionDelay` | 34 |  |
| `SummonMount` | 35 |  |
| `ReputationModify` | 36 |  |
| `GiveSchematic` | 37 |  |
| `ModifySchematic` | 38 |  |
| `TradeSkillProfession` | 39 |  |
| `QuestAdvanceObjective` | 40 |  |
| `GiveItemToPlayer` | 41 |  |
| `GiveLootTableToPlayer` | 42 |  |
| `NpcLootTableModify` | 43 |  |
| `ThreatModification` | 44 |  |
| `ThreatTransfer` | 45 |  |
| `WarplotTeleport` | 46 |  |
| `CraftItem` | 47 |  |
| `ItemBreakdown` | 48 |  |
| `SpellForceRemoveChanneled` | 49 |  |
| `ModifyInterruptArmor` | 50 |  |
| `SpellDispel` | 51 |  |
| `TradeSkillProfessionXp` | 52 |  |
| `ModifySpell` | 53 |  |
| `ModifySpellEffect` | 54 |  |
| `AddSpell` | 55 |  |
| `AddSpellEffect` | 56 |  |
| `SuppressSpellEffect` | 57 |  |
| `VacuumLoot` | 58 |  |
| `ShieldOverload` | 59 |  |
| `Teleport` | 60 |  |
| `TitleGrant` | 61 |  |
| `TitleRevoke` | 62 |  |
| `VendorPriceModifier` | 63 |  |
| `RechargeItemBatteries` | 64 |  |
| `FacilityModification` | 65 |  |
| `PetAIStanceSet` | 66 |  |
| `ModifySpellCooldown` | 67 |  |
| `FinishingMove` | 68 |  |
| `ChangeIcon` | 69 |  |
| `ItemVisualSwap` | 70 |  |
| `AggroImmune` | 71 |  |
| `SpellEffectImmunity` | 72 |  |
| `SpellForceRemove` | 73 |  |
| `RavelSignal` | 74 |  |
| `ChangeDisplayName` | 75 |  |
| `Stealth` | 76 |  |
| `RemoveStealth` | 77 |  |
| `PathActionExplorerDig` | 78 |  |
| `HazardEnable` | 79 |  |
| `HazardModify` | 80 |  |
| `HazardSuspend` | 81 |  |
| `NpcForceFacing` | 82 |  |
| `AchievementAdvance` | 83 |  |
| `PathXpModify` | 84 |  |
| `ProxyChannelVariableTime` | 85 |  |
| `FullScreenEffect` | 86 |  |
| `ProxyRandomExclusive` | 87 |  |
| `DespawnUnit` | 88 |  |
| `SummonPet` | 89 |  |
| `MimicDisplayName` | 90 |  |
| `MimicDisguise` | 91 |  |
| `GrantXP` | 92 |  |
| `DatacubeUpdate` | 93 |  |
| `DatacubeVolumeUpdate` | 94 |  |
| `SettlerCampfire` | 95 |  |
| `SummonTrap` | 96 |  |
| `SetBusy` | 97 |  |
| `CooldownReset` | 98 |  |
| `RestedXpDecorBonus` | 99 |  |
| `LearnDyeColor` | 100 |  |
| `PetCastSpell` | 101 |  |
| `DisguiseOutfit` | 102 |  |
| `RewardBuffModifier` | 103 |  |
| `HousingEscape` | 104 |  |
| `NPCForceAIMovement` | 105 |  |
| `HealShields` | 106 |  |
| `PathMissionIncrement` | 107 |  |
| `GrantLevelScaledXP` | 108 |  |
| `DelayDeath` | 109 |  |
| `GrantLevelScaledPrestige` | 110 |  |
| `UnlockPetFlair` | 111 |  |
| `WarplotPlugUpgrade` | 112 |  |
| `SetMatchingEligibility` | 113 |  |
| `UnlockActionBar` | 114 |  |
| `UNUSED040` | 115 |  |
| `ModifyCreatureFlags` | 116 |  |
| `UNUSED061` | 117 |  |
| `UNUSED063` | 118 |  |
| `ApplyLASChanges` | 119 |  |
| `GiveAbilityPointsToPlayer` | 120 |  |
| `ModifyAbilityCharges` | 121 |  |
| `UNUSED091` | 122 |  |
| `UNUSED104` | 123 |  |
| `UnlockMount` | 124 |  |
| `UnlockInlaidAugment` | 125 |  |
| `GiveAugmentPowerToPlayer` | 126 |  |
| `TemporarilyUnflagPvp` | 127 |  |
| `SupportStuck` | 128 |  |
| `MiniMapIcon` | 129 |  |
| `Disembark` | 130 |  |
| `ChangePlane` | 131 |  |
| `ModifyRestedXP` | 132 |  |
| `UNUSED011` | 133 |  |
| `UNUSED039` | 134 |  |
| `UNUSED050` | 135 |  |
| `UNUSED054` | 136 |  |
| `UNUSED070` | 137 |  |
| `UNUSED072` | 138 |  |
| `UNUSED074` | 139 |  |
| `UNUSED102` | 140 |  |
| `UNUSED103` | 141 |  |
| `UNUSED114` | 142 |  |
| `UNUSED115` | 143 |  |
| `HousingPlantSeed` | 144 |  |
| `UnlockVanityPet` | 145 |  |
| `SummonVanityPet` | 146 |  |
| `DamageShields` | 147 |  |
| `RewardPropertyModifier` | 148 |  |
| `RapidTransport` | 149 |  |
| `DisallowPvP` | 150 |  |

## CodeEnumSpellMechanic

An enum representing the spell mechanics of each class

| name | order | meaning |
|---|---|---|
| `None` | 0 |  |
| `Focus` | 1 |  |
| `MedicCore` | 2 |  |
| `Empathy` | 3 |  |
| `SpellSurge` | 4 |  |
| `Kinetic` | 5 |  |
| `Volatility` | 6 |  |
| `Unused03` | 7 |  |

## CodeEnumSpellTag

| name | order | meaning |
|---|---|---|
| `Assault` | 0 |  |
| `Support` | 1 |  |
| `Path` | 2 |  |
| `Misc` | 3 |  |
| `Mount` | 4 |  |
| `DoesNotUseSpecIndex` | 5 |  |
| `Utility` | 6 |  |
| `NotAutoActivated` | 7 |  |
| `Conditional` | 8 |  |
| `VanityPet` | 9 |  |
| `MTX` | 10 |  |

## CodeEnumStoreDisplayFlag

| name | order | meaning |
|---|---|---|
| `New` | 0 |  |
| `Recommended` | 1 |  |
| `Popular` | 2 |  |
| `LimitedTime` | 3 |  |

## CodeEnumStoreDisplayInfoDisplayType

| name | order | meaning |
|---|---|---|
| `None` | 0 |  |
| `Creature` | 1 |  |
| `Decor` | 2 |  |
| `Mannequin` | 3 |  |
| `Mount` | 4 |  |

## CodeEnumStoreError

| name | order | meaning |
|---|---|---|
| `CatalogUnavailable` | 0 |  |
| `StoreDisabled` | 1 |  |
| `InvalidOffer` | 2 |  |
| `InvalidPrice` | 3 |  |
| `GenericFail` | 4 |  |
| `PurchasePending` | 5 |  |

## CodeEnumStoreLink

| name | order | meaning |
|---|---|---|
| `Signature` | 0 |  |

## CodeEnumStoryPanel

| name | order | meaning |
|---|---|---|
| `Default` | 0 |  |
| `Low` | 1 |  |
| `Center` | 2 |  |
| `FullScreen` | 3 |  |
| `Whiteout` | 4 |  |
| `Urgent` | 5 |  |
| `FullScreenBlackNoFlash` | 6 |  |
| `Informational` | 7 |  |

## CodeEnumStoryPanelStyle

| name | order | meaning |
|---|---|---|
| `Default` | 0 |  |
| `Paper` | 1 |  |
| `Electronic` | 2 |  |
| `Eldan` | 3 |  |
| `Arcane` | 4 |  |
| `Natural` | 5 |  |
| `Exile` | 6 |  |
| `Dominion` | 7 |  |

## CodeEnumSurveyType

The different types of surveys that the player can receive.

| name | order | meaning |
|---|---|---|
| `General` | 0 |  |
| `Quest` | 1 |  |
| `PathMission` | 2 |  |
| `Challenge` | 3 |  |

## CodeEnumTradeskill

A list of the different tradeskills available to the player.  Augmentor, Farmer, and Fishing are not currently used.

| name | order | meaning |
|---|---|---|
| `Weaponsmith` | 0 |  |
| `Cooking` | 1 |  |
| `Armorer` | 2 |  |
| `Mining` | 3 |  |
| `Outfitter` | 4 |  |
| `Survivalist` | 5 |  |
| `Augmentor` | 6 |  |
| `Architect` | 7 |  |
| `Relic_Hunter` | 8 |  |
| `Fishing` | 9 |  |
| `Farmer` | 10 |  |
| `Tailor` | 11 |  |
| `Runecrafting` | 12 |  |

## CodeEnumTradeskillResult

A list of possible outcomes for several tradeskill actions.

| name | order | meaning |
|---|---|---|
| `Success` | 0 |  |
| `InsufficentFund` | 1 |  |
| `InvalidItem` | 2 |  |
| `InvalidSlot` | 3 |  |
| `MissingEngravingStation` | 4 |  |
| `Unlocked` | 5 |  |
| `UnknownError` | 6 |  |
| `GlyphExists` | 7 |  |
| `MissingGlyph` | 8 |  |
| `DuplicateGlyph` | 9 |  |
| `AttemptFailed` | 10 |  |
| `GlyphSlotLimit` | 11 |  |
| `RuneExists` | 12 |  |
| `MissingRune` | 13 |  |
| `DuplicateRune` | 14 |  |
| `RuneSlotLimit` | 15 |  |

## CodeEnumTradeskillTier

These values represent the various tradeskill tiers.

| name | order | meaning |
|---|---|---|
| `Novice` | 0 |  |
| `Apprentice` | 1 |  |
| `Journeyman` | 2 |  |
| `Expert` | 3 |  |
| `Artisan` | 4 |  |
| `Zero` | 5 |  |
| `Master` | 6 |  |
| `GrandMaster` | 7 |  |

## CodeEnumTutorial

| name | order | meaning |
|---|---|---|
| `Codex` | 0 |  |
| `CharacterPanel` | 1 |  |
| `AbilityWindow` | 2 |  |
| `Crafting_UI_Tutorial` | 3 |  |
| `Special_Ability_Chips` | 4 |  |
| `Tradeskill_Codex_Tutorial` | 5 |  |
| `Crafting_Components_Tutorial` | 6 |  |
| `Crafting_Station_Tutorial` | 7 |  |
| `Basic_Salvaging_Tutorial` | 8 |  |
| `QuestCommunicatorGiven` | 9 |  |
| `QuestAccepted` | 10 |  |
| `QuestAchieved` | 11 |  |
| `QuestBotched` | 12 |  |
| `QuestCommunicatorReceived` | 13 |  |
| `ChallengeUnlocked` | 14 |  |
| `ChallengeCompleted` | 15 |  |
| `ChallengeRewardPanel` | 16 |  |
| `AchievementCompleted` | 17 |  |
| `Telegraphs` | 18 |  |
| `NewBindpoint` | 19 |  |
| `Path_MissionComplete` | 20 |  |
| `Path_EpisodeComplete` | 21 |  |
| `Soldier_MissionUnlock` | 22 |  |
| `Soldier_TowerDefense` | 23 |  |
| `Soldier_Assassinate` | 24 |  |
| `Soldier_SWAT` | 25 |  |
| `Soldier_Demolition` | 26 |  |
| `Soldier_Rescue` | 27 |  |
| `Explorer_MissionUnlock` | 28 |  |
| `Explorer_Vista` | 29 |  |
| `Explorer_ClaimTerritory` | 30 |  |
| `Explorer_Door` | 31 |  |
| `Explorer_ScavengerHunt` | 32 |  |
| `Explorer_PowerMap` | 33 |  |
| `Scientist_FieldStudy` | 34 |  |
| `Settler_MissionUnlock` | 35 |  |
| `Settler_Infrastructure` | 36 |  |
| `Settler_DepotActivate` | 37 |  |
| `Death` | 38 |  |
| `Hazards` | 39 |  |
| `PublicEventStart` | 40 |  |
| `GalacticArchive_NewEntry` | 41 |  |
| `Soldier_StopTheThieves` | 42 |  |
| `Soldier_WhackAMole` | 43 |  |
| `Farmer_Powershrooms` | 44 |  |
| `General_Quest_SpellShortcut` | 45 |  |
| `CoordinateCrafting` | 46 |  |
| `CombatBuff` | 47 |  |
| `General_Social` | 48 |  |
| `QuestCommunicatorMissed` | 49 |  |
| `MailMenu` | 50 |  |
| `CSI_PressAndHold` | 51 |  |
| `CSI_RapidTapping` | 52 |  |
| `CSI_PrecisionTapping` | 53 |  |
| `CSI_Memory` | 54 |  |
| `CSI_KeyPad` | 55 |  |
| `CSI_Metronome` | 56 |  |
| `QuestCommunicatorDeclined` | 57 |  |
| `General_Lore` | 58 |  |
| `GroupFinderMenu` | 59 |  |
| `Renown` | 60 |  |
| `AMPs` | 61 |  |
| `Reputation` | 62 |  |
| `Housing_Landscape` | 63 |  |
| `Housing_House` | 64 |  |
| `Housing_Crate` | 65 |  |
| `Housing_Vendor` | 66 |  |
| `Housing_Room` | 67 |  |
| `General_CREDD` | 68 |  |
| `General_AccountServices` | 69 |  |
| `Contracts` | 70 |  |
| `Path_AbilityUnlock` | 71 |  |
| `LootDropped` | 72 |  |
| `AMPTab` | 73 |  |
| `InventoryBag` | 74 |  |
| `TradeskillsInventory` | 75 |  |
| `Discoveries` | 76 |  |
| `QuestGivingItem` | 77 |  |
| `QuestIntroduction` | 78 |  |
| `QuestCanAccept` | 79 |  |
| `AMPSave` | 80 |  |
| `LASSave` | 81 |  |
| `LASBuilder` | 82 |  |
| `CharacterWindow` | 83 |  |
| `MultipleQuests` | 84 |  |
| `CraftingPowerCore` | 85 |  |
| `CraftingSlotColor` | 86 |  |
| `CraftingSlotCharge` | 87 |  |
| `CraftingApSp` | 88 |  |
| `CraftingFailChance` | 89 |  |
| `AbandonCraft` | 90 |  |
| `Daze` | 91 |  |

## CodeEnumTutorialAnchor

| name | order | meaning |
|---|---|---|
| `Codex` | 0 |  |
| `Inventory` | 1 |  |
| `None` | 2 |  |
| `Abilities` | 3 |  |
| `Character` | 4 |  |
| `Mail` | 5 |  |
| `GalacticArchive` | 6 |  |
| `Social` | 7 |  |
| `GroupFinder` | 8 |  |
| `Challenge` | 9 |  |
| `Datachron` | 10 |  |
| `AbilityBar` | 11 |  |
| `MiniMap` | 12 |  |
| `QuestTracker` | 13 |  |
| `HUDAlert` | 14 |  |
| `PressAndHold` | 15 |  |
| `RapidTapping` | 16 |  |
| `PrecisionTapping` | 17 |  |
| `Memory` | 18 |  |
| `Keypad` | 19 |  |
| `Metronome` | 20 |  |
| `ShieldBar` | 21 |  |
| `InnateAbility` | 22 |  |
| `DashMeter` | 23 |  |
| `SprintMeter` | 24 |  |
| `HealthBar` | 25 |  |
| `BuffFrame` | 26 |  |
| `ClassResource` | 27 |  |
| `QuestCommunicatorReceived` | 28 |  |
| `DatachronBody` | 29 |  |
| `Recall` | 30 |  |
| `InterruptArmor` | 31 |  |
| `Contracts` | 32 |  |
| `CraftingApSp` | 33 |  |
| `InterfaceMenuListCharacter` | 34 |  |
| `EquippedBags` | 35 |  |
| `TradeskillInventory` | 36 |  |
| `SalvageIcon` | 37 |  |
| `NPCInteraction` | 38 |  |
| `QuestIntroduction` | 39 |  |
| `QuestAccept` | 40 |  |
| `InterfaceMenuListInventory` | 41 |  |
| `InventoryItem` | 42 |  |
| `LASBuilderButton` | 43 |  |
| `LASSaveActionSetButton` | 44 |  |
| `LASAmpTabButton` | 45 |  |
| `LASAbilityTypeTab` | 46 |  |
| `LASAbilityTier` | 47 |  |
| `AbandonCraft` | 48 |  |
| `CraftingSlotColor` | 49 |  |
| `CraftingSlotCharge` | 50 |  |
| `CraftingPowerCore` | 51 |  |
| `CraftingFailChance` | 52 |  |
| `FloatingActionBar` | 53 |  |
| `FloatingActionBarBase` | 54 |  |
| `FloatingActionBarHorz` | 55 |  |
| `FloatingActionBarVert` | 56 |  |
| `PathAbility` | 57 |  |

## CodeEnumTutorialAnchorOrientation

| name | order | meaning |
|---|---|---|
| `North` | 0 |  |
| `Northeast` | 1 |  |
| `East` | 2 |  |
| `Southeast` | 3 |  |
| `South` | 4 |  |
| `Southwest` | 5 |  |
| `West` | 6 |  |
| `Northwest` | 7 |  |

## CodeEnumTutorialCategory

| name | order | meaning |
|---|---|---|
| `General` | 0 |  |
| `Beginner` | 1 |  |
| `Combat` | 2 |  |
| `PVP` | 3 |  |
| `Housing` | 4 |  |
| `Challenges` | 5 |  |
| `PublicEvents` | 6 |  |
| `Adventures` | 7 |  |
| `Path_Soldier` | 8 |  |
| `Path_Settler` | 9 |  |
| `Path_Scientist` | 10 |  |
| `Path_Explorer` | 11 |  |
| `Class_Warrior` | 12 |  |
| `Class_Esper` | 13 |  |
| `Class_Spellslinger` | 14 |  |
| `Class_Stalker` | 15 |  |
| `Class_Medic` | 16 |  |
| `Class_Engineer` | 17 |  |
| `Class_Charmer` | 18 |  |
| `Tradeskill_Outfitter` | 19 |  |
| `Tradeskill_Tailor` | 20 |  |
| `Tradeskill_Architect` | 21 |  |
| `Tradeskill_Miner` | 22 |  |
| `Tradeskill_Augmentor` | 23 |  |
| `Tradeskill_Survivalist` | 24 |  |
| `Tradeskill_Farmer` | 25 |  |
| `Tradeskill_Weaponsmith` | 26 |  |
| `Tradeskill_Armorer` | 27 |  |
| `UNUSED12` | 28 |  |
| `UNUSED13` | 29 |  |
| `UNUSED14` | 30 |  |
| `UNUSED15` | 31 |  |
| `UNUSED16` | 32 |  |
| `UNUSED17` | 33 |  |
| `UNUSED18` | 34 |  |
| `UNUSED19` | 35 |  |
| `UNUSED20` | 36 |  |
| `UNUSED21` | 37 |  |
| `UNUSED22` | 38 |  |
| `UNUSED23` | 39 |  |
| `UNUSED24` | 40 |  |
| `UNUSED25` | 41 |  |
| `UNUSED26` | 42 |  |
| `UNUSED27` | 43 |  |
| `Tradeskills` | 44 |  |
| `Zones` | 45 |  |
| `Classes` | 46 |  |

## CodeEnumUserText

| name | order | meaning |
|---|---|---|
| `CharacterName` | 0 |  |
| `ScientistScanbotName` | 1 |  |
| `GuildName` | 2 |  |
| `GuildRankName` | 3 |  |
| `GuildBankTabName` | 4 |  |
| `HousingResidenceName` | 5 |  |
| `Chat` | 6 |  |
| `MailSubject` | 7 |  |
| `MailBody` | 8 |  |
| `ChatCustomChannelName` | 9 |  |
| `FriendshipNote` | 10 |  |
| `ReadyCheck` | 11 |  |
| `ChatCustomChannelPassword` | 12 |  |
| `GuildMessageOfTheDay` | 13 |  |
| `GuildMemberNote` | 14 |  |
| `GuildRercuitDescription` | 15 |  |
| `GuildInfoMessage` | 16 |  |
| `FriendshipAccountName` | 17 |  |
| `FriendshipAccountPrivateNote` | 18 |  |
| `FriendshipAccountPublicNote` | 19 |  |
| `FriendshipAccountEmail` | 20 |  |
| `FriendshipInviteNote` | 21 |  |
| `PlayerTicketText` | 22 |  |
| `GuildRecruitDescription` | 23 |  |
| `PlayerTicketSubject` | 24 |  |

## CodeEnumUserTextFilterClass

| name | order | meaning |
|---|---|---|
| `Strict` | 0 |  |
| `Standard` | 1 |  |
| `Low` | 2 |  |

## CodeEnumVital

| name | order | meaning |
|---|---|---|
| `Invalid` | 0 |  |
| `Health` | 1 |  |
| `Breath` | 2 |  |
| `ShieldCapacity` | 3 |  |
| `KineticCell` | 4 |  |
| `Resource0` | 5 |  |
| `Resource1` | 6 |  |
| `Resource2` | 7 |  |
| `Resource3` | 8 |  |
| `Resource4` | 9 |  |
| `Resource5` | 10 |  |
| `Resource6` | 11 |  |
| `StalkerA` | 12 |  |
| `StalkerB` | 13 |  |
| `StalkerC` | 14 |  |
| `Mana` | 15 |  |
| `Resource7` | 16 |  |
| `MedicCore` | 17 |  |
| `SpellSurge` | 18 |  |
| `InterruptArmor` | 19 |  |
| `Absorption` | 20 |  |
| `PublicResource0` | 21 |  |
| `PublicResource1` | 22 |  |
| `PublicResource2` | 23 |  |
| `Volatility` | 24 |  |
| `Resource8` | 25 |  |
| `Resource9` | 26 |  |
| `Resource10` | 27 |  |
| `Focus` | 28 |  |

## CodeEnumWhoResult

| name | order | meaning |
|---|---|---|
| `OK` | 0 |  |
| `Partial` | 1 |  |
| `UnderCooldown` | 2 |  |

## CodeEnumZoneCompletionType

| name | order | meaning |
|---|---|---|
| `EpisodeQuest` | 0 |  |
| `TaskQuest` | 1 |  |
| `Challenge` | 2 |  |
| `TaxiNode` | 3 |  |
| `Datacube` | 4 |  |
| `Tale` | 5 |  |
| `Journal` | 6 |  |

## CodeEnumZonePvpRules

| name | order | meaning |
|---|---|---|
| `None` | 0 |  |
| `ExileStronghold` | 1 |  |
| `DominionStronghold` | 2 |  |
| `Sanctuary` | 3 |  |
| `Pvp` | 4 |  |
| `ExilePVPStronghold` | 5 |  |
| `DominionPVPStronghold` | 6 |  |

## CombatMessageType

| name | order | meaning |
|---|---|---|
| `General` | 0 |  |
| `Experience` | 1 |  |
| `QuestUpdate` | 2 |  |
| `LocationChange` | 3 |  |
| `Combat_Damage_Done` | 4 |  |
| `Combat_Damage_Done_Critical` | 5 |  |
| `Combat_Damage_Taken` | 6 |  |
| `Combat_Damage_Taken_Critical` | 7 |  |
| `Combat_Healing_Done` | 8 |  |
| `Combat_Healing_Done_Critical` | 9 |  |
| `Combat_Healing_Taken` | 10 |  |
| `Combat_Healing_Taken_Critical` | 11 |  |
| `Combat_Block_Taken` | 12 |  |
| `Combat_Block_Done` | 13 |  |
| `Combat_Parry_Taken` | 14 |  |
| `Combat_Parry_Done` | 15 |  |
| `Combat_Dodge_Taken` | 16 |  |
| `Combat_Dodge_Done` | 17 |  |
| `Combat_NoEffect_Taken` | 18 |  |
| `Combat_NoEffect_Done` | 19 |  |
| `Combat_Shallow_Taken` | 20 |  |
| `Combat_Shallow_Done` | 21 |  |
| `Combat_Falling_Damage_Done` | 22 |  |
| `Combat_Death` | 23 |  |
| `Error` | 24 |  |
| `SpellFailure` | 25 |  |
| `UNUSED00` | 26 |  |
| `UNUSED01` | 27 |  |
| `Faction` | 28 |  |
| `LootBase` | 29 |  |
| `LootAverage` | 30 |  |
| `LootGood` | 31 |  |
| `LootExcellent` | 32 |  |
| `LootSuperb` | 33 |  |
| `LootLegendary` | 34 |  |
| `LootQuestActivation` | 35 |  |
| `Achievement` | 36 |  |
| `Experience_KillCreature` | 37 |  |
| `Experience_ClusterBonus` | 38 |  |
| `Experience_Quest` | 39 |  |
| `Absorption_Taken` | 40 |  |
| `Absorption_Done` | 41 |  |
| `Transference_Taken` | 42 |  |
| `Transference_Done` | 43 |  |
| `SpellFailure_Long` | 44 |  |
| `SpellFailure_Medium` | 45 |  |
| `SpellFailure_Short` | 46 |  |
| `SpellFailure_Target_Head` | 47 |  |
| `SpellFailure_Target_Feet` | 48 |  |
| `Special_Done` | 49 |  |
| `Special_Taken` | 50 |  |
| `UNUSED02` | 51 |  |
| `PlayerPath` | 52 |  |
| `KillPerformanceReward` | 53 |  |
| `MultiKillReward` | 54 |  |
| `KillingSpreeReward` | 55 |  |
| `LootInferior` | 56 |  |
| `TelegraphEvadeReward` | 57 |  |
| `TelegraphInterruptReward` | 58 |  |
| `RestedReward` | 59 |  |
| `UNUSED04` | 60 |  |
| `UNUSED03` | 61 |  |
| `LootArtifact` | 62 |  |

## ContractQuality

| name | order | meaning |
|---|---|---|
| `None` | 0 |  |
| `Good` | 1 |  |
| `Excellent` | 2 |  |
| `Superb` | 3 |  |
| `Legendary` | 4 |  |

## ContractType

| name | order | meaning |
|---|---|---|
| `None` | 0 |  |
| `Pvp` | 1 |  |
| `Pve` | 2 |  |

## CostumeSaveResult

| name | order | meaning |
|---|---|---|
| `Saved` | 0 |  |
| `InvalidCostumeIndex` | 1 |  |
| `CostumeIndexNotUnlocked` | 2 |  |
| `InvalidMannequinIndex` | 3 |  |
| `UnknownMannequinError` | 4 |  |
| `ItemNotUnlocked` | 5 |  |
| `InvalidItem` | 6 |  |
| `UnusableItem` | 7 |  |
| `InvalidDye` | 8 |  |
| `DyeNotUnlocked` | 9 |  |
| `NotEnoughTokens` | 10 |  |
| `InsufficientFunds` | 11 |  |
| `UnknownError` | 12 |  |
| `Saving` | 13 |  |

## CostumeUnlockResult

| name | order | meaning |
|---|---|---|
| `UnlockSuccess` | 0 |  |
| `AlreadyKnown` | 1 |  |
| `OutOfSpace` | 2 |  |
| `UnknownFailure` | 3 |  |
| `ForgetItemSuccess` | 4 |  |
| `ForgetItemFailed` | 5 |  |
| `FailedPrerequisites` | 6 |  |
| `InsufficientCredits` | 7 |  |
| `ItemInUse` | 8 |  |
| `ItemNotKnown` | 9 |  |
| `UnlockRequested` | 10 |  |
| `ForgetRequested` | 11 |  |
| `InvalidItem` | 12 |  |

## CreatureRisk

| name | order | meaning |
|---|---|---|
| `Minor` | 0 |  |
| `Average` | 1 |  |
| `Major` | 2 |  |

## DecorCategoryLimit

| name | order | meaning |
|---|---|---|
| `Mannequin` | 0 |  |
| `Light` | 1 |  |
| `Special` | 2 |  |

## DecorControlMode

| name | order | meaning |
|---|---|---|
| `Local` | 0 |  |
| `Global` | 1 |  |

## Difficulty

| name | order | meaning |
|---|---|---|
| `Normal` | 0 |  |
| `Veteran` | 1 |  |
| `Count` | 2 |  |

## DisabledGameplaySystem

| name | order | meaning |
|---|---|---|
| `Mail` | 0 |  |
| `Store` | 1 |  |
| `Omnibits` | 2 |  |

## DragDropCancelReason

An enum that describes why a player's attempt to drag and drop something with their mouse was canceled.

| name | order | meaning |
|---|---|---|
| `EscapeKey` | 0 |  |
| `DroppedOnNothing` | 1 |  |
| `ClickedOnNothing` | 2 |  |
| `ClickedOnWorld` | 3 |  |
| `WindowMove` | 4 |  |

## DragDropQueryResult

The set of results that the player can get when attempting to drag and drop something using the mouse.

| name | order | meaning |
|---|---|---|
| `PassOn` | 0 |  |
| `Ignore` | 1 |  |
| `Accept` | 2 |  |
| `Invalid` | 3 |  |

## DuelStateDuelState

| name | order | meaning |
|---|---|---|
| `None` | 0 |  |
| `WaitingToAccept` | 1 |  |
| `Pending` | 2 |  |
| `Dueling` | 3 |  |

## EnumDeviceTypes

| name | order | meaning |
|---|---|---|
| `Unknown` | 0 |  |
| `Notebook` | 1 |  |
| `Desktop` | 2 |  |
| `Server` | 3 |  |
| `Display` | 4 |  |
| `Mouse` | 5 |  |
| `Keyboard` | 6 |  |
| `Gamepad` | 7 |  |
| `Speaker` | 8 |  |
| `Other` | 9 |  |

## GenericMapNodeType

| name | order | meaning |
|---|---|---|
| `Default` | 0 |  |
| `Back` | 1 |  |
| `Confirm` | 2 |  |

## GuildClassification

| name | order | meaning |
|---|---|---|
| `Leveling` | 0 |  |
| `Raiding` | 1 |  |
| `PvP` | 2 |  |
| `Social` | 3 |  |
| `Tradeskill` | 4 |  |
| `Roleplay` | 5 |  |

## GuildHolomark

| name | order | meaning |
|---|---|---|
| `Left` | 0 |  |
| `Right` | 1 |  |
| `Back` | 2 |  |

## HarvestLootRule

| name | order | meaning |
|---|---|---|
| `RoundRobin` | 0 |  |
| `FirstTagger` | 1 |  |

## HealthyGamingStatus

| name | order | meaning |
|---|---|---|
| `Normal` | 0 |  |
| `Fatigue` | 1 |  |
| `Unhealthy` | 2 |  |

## HousingPlugFacing

| name | order | meaning |
|---|---|---|
| `North` | 0 |  |
| `South` | 1 |  |
| `East` | 2 |  |
| `West` | 3 |  |
| `Default` | 4 |  |

## HousingUpkeepType

| name | order | meaning |
|---|---|---|
| `Permanent` | 0 |  |
| `Timed` | 1 |  |
| `Charged` | 2 |  |
| `TimedCharged` | 3 |  |
| `Decay` | 4 |  |
| `StructurePoints` | 5 |  |

## HoverboardSlot

| name | order | meaning |
|---|---|---|
| `Front` | 0 |  |
| `Back` | 1 |  |
| `Sides` | 2 |  |

## ICCommJoinResult

| name | order | meaning |
|---|---|---|
| `NoGuild` | 0 |  |
| `BadName` | 1 |  |
| `Join` | 2 |  |
| `TooManyChannels` | 3 |  |
| `Left` | 4 |  |
| `NoGroup` | 5 |  |
| `MissingEntitlement` | 6 |  |

## InvitationMethod

| name | order | meaning |
|---|---|---|
| `Open` | 0 |  |
| `Neutral` | 1 |  |
| `Closed` | 2 |  |

## ItemAuctionFilterData

| name | order | meaning |
|---|---|---|
| `ItemAuctionFilterPropertyMin` | 0 |  |
| `ItemAuctionFilterPropertyMax` | 1 |  |
| `ItemAuctionFilterLevel` | 2 |  |
| `ItemAuctionFilterQuality` | 3 |  |
| `ItemAuctionFilterGlyphSlot` | 4 |  |
| `ItemAuctionFilterBuyoutMax` | 5 |  |
| `ItemAuctionFilterEquippableBy` | 6 |  |
| `ItemAuctionFilterRuneSlot` | 7 |  |

## LevelUpUnlock

| name | order | meaning |
|---|---|---|
| `Builder_NewTierPoint` | 0 |  |
| `Builder_LASSlot2` | 1 |  |
| `Character_GearSlot_Shield` | 2 |  |
| `WorldMapNewZone_Deradune` | 3 |  |
| `WorldMapAdventure_Astrovoid` | 4 |  |
| `Character_GearSlot_Implants` | 5 |  |
| `GroupFinder_Dungeons` | 6 |  |
| `Character_CostumeSlot6` | 7 |  |
| `Builder_AMPPoint` | 8 |  |
| `Customization_Mount` | 9 |  |
| `WorldMapNewZone_Ellevar` | 10 |  |
| `Inventory_Salvage` | 11 |  |
| `Character_GearSlot_Gloves` | 12 |  |
| `GroupFinder_Warplots` | 13 |  |
| `WorldMapNewZone_Malgrave` | 14 |  |
| `Builder_LASSlot8` | 15 |  |
| `Builder_LASSlot7` | 16 |  |
| `Builder_LASSlot4` | 17 |  |
| `Builder_AbilityTier2` | 18 |  |
| `WorldMapDungeon_Stormtalon` | 19 |  |
| `WorldMapAdventure_Galeras` | 20 |  |
| `Character_GearSlot_Shoulders` | 21 |  |
| `WorldMapDungeon_KelVoreth` | 22 |  |
| `GroupFinder_Arenas` | 23 |  |
| `Character_GearSlot_Gadgets` | 24 |  |
| `Customization_Scanbot` | 25 |  |
| `WorldMapNewZone_Grimvault` | 26 |  |
| `Character_CostumeSlot2` | 27 |  |
| `WorldMapNewZone_Wilderrun` | 28 |  |
| `Character_CostumeSlot4` | 29 |  |
| `WorldMapAdventure_Whitevale` | 30 |  |
| `Character_GearSlot_Helm` | 31 |  |
| `WorldMapNewZone_Farside` | 32 |  |
| `WorldMapNewZone_Algoroc` | 33 |  |
| `Builder_LASSlot6` | 34 |  |
| `WorldMapNewZone_NorthernWilds` | 35 |  |
| `Builder_AbilityTier8` | 36 |  |
| `WorldMapNewZone_EverstarGrove` | 37 |  |
| `WorldMapNewZone_Whitevale` | 38 |  |
| `Character_GearSlot_WeaponAttachment` | 39 |  |
| `GroupFinder_General` | 40 |  |
| `WorldMapDungeon_Skullcano` | 41 |  |
| `WorldMapNewZone_CrimsonIsle` | 42 |  |
| `WorldMapCapital_Illium` | 43 |  |
| `Builder_LASSlot5` | 44 |  |
| `Builder_AbilityTier5` | 45 |  |
| `Character_GearSlot_SupportSystem` | 46 |  |
| `WorldMapAdventure_Hycrest` | 47 |  |
| `Character_CostumeSlot3` | 48 |  |
| `WorldMapNewZone_LevianBay` | 49 |  |
| `Builder_AbilityTier6` | 50 |  |
| `WorldMapNewZone_Celestion` | 51 |  |
| `WorldMapNewZone_Auroria` | 52 |  |
| `WorldMapAdventure_NorthernWilds` | 53 |  |
| `Builder_AbilityTier4` | 54 |  |
| `WorldMapNewZone_Galeras` | 55 |  |
| `Builder_AbilityTier3` | 56 |  |
| `Character_CostumeSystem` | 57 |  |
| `WorldMapCapital_Thayd` | 58 |  |
| `Builder_LASSlot3` | 59 |  |
| `WorldMapAdventure_Malgrave` | 60 |  |
| `Builder_AMPSystem` | 61 |  |
| `Character_CostumeSlot5` | 62 |  |
| `Builder_TierPointSystem` | 63 |  |
| `Builder_AbilityTier7` | 64 |  |
| `WorldMapDungeon_SwordMaiden` | 65 |  |
| `GroupFinder_Adventures` | 66 |  |
| `Character_GearSlot_RaidKey` | 67 |  |
| `Tradeskills` | 68 |  |
| `Runecrafting` | 69 |  |
| `WorldMapDungeon_UltimateProtogames` | 70 |  |
| `WorldMapDungeon_ProtogamesAcademyExile` | 71 |  |
| `WorldMapDungeon_ProtogamesAcademyDominion` | 72 |  |
| `GroupFinder_Expeditions` | 73 |  |
| `Expedition_FragmentZero` | 74 |  |
| `Expedition_OutpostM13` | 75 |  |
| `Expedition_Infestation` | 76 |  |
| `Expedition_RageLogic` | 77 |  |
| `Expedition_SpaceMadness` | 78 |  |
| `Expedition_DeepSpaceExploration` | 79 |  |
| `Expedition_Gauntlet` | 80 |  |
| `Contracts` | 81 |  |
| `ActionSetBuilder` | 82 |  |
| `HoloWardrobe` | 83 |  |
| `Inventory` | 84 |  |
| `LevelUpUnlocks` | 85 |  |

## LevelUpUnlockSystem

| name | order | meaning |
|---|---|---|
| `Path` | 0 |  |
| `Level` | 1 |  |

## LevelUpUnlockType

| name | order | meaning |
|---|---|---|
| `Dungeon_New` | 0 |  |
| `Raid_40` | 1 |  |
| `Adventure_New` | 2 |  |
| `Content_Capital` | 3 |  |
| `Content_Feature` | 4 |  |
| `Class_LAS_Slot` | 5 |  |
| `General_Expanded_Feature` | 6 |  |
| `Class_Feature` | 7 |  |
| `Class_Attribute` | 8 |  |
| `Path_ScanBot` | 9 |  |
| `Path_Spell` | 10 |  |
| `Path_Title` | 11 |  |
| `Gear_Slot` | 12 |  |
| `Path_Quest` | 13 |  |
| `Social_Feature` | 14 |  |
| `Class_Improvement` | 15 |  |
| `Raid_20` | 16 |  |
| `Path_Item` | 17 |  |
| `Class_Tier` | 18 |  |
| `Class_Ability` | 19 |  |
| `PvP_Battleground` | 20 |  |
| `General_Feature` | 21 |  |
| `Content_Zone` | 22 |  |
| `PvP_Feature` | 23 |  |
| `Shiphand_New` | 24 |  |

## LiveEventCategory

| name | order | meaning |
|---|---|---|
| `RealmFlag` | 0 |  |
| `Generic` | 1 |  |
| `WorldStory` | 2 |  |
| `Holiday` | 3 |  |
| `OneTime` | 4 |  |
| `Bonus` | 5 |  |

## LiveEventFlags

| name | order | meaning |
|---|---|---|
| `ShowCompletedObjectives` | 0 |  |
| `Hidden` | 1 |  |
| `CompleteOnMaxCountReached` | 2 |  |
| `SuccessOnExpire` | 3 |  |
| `CompleteOnExpire` | 4 |  |
| `BonusEvent` | 5 |  |
| `AllowCrossRealm` | 6 |  |

## LiveEventType

| name | order | meaning |
|---|---|---|
| `Count` | 0 |  |
| `Bitfield` | 1 |  |

## LootRule

| name | order | meaning |
|---|---|---|
| `FreeForAll` | 0 |  |
| `RoundRobin` | 1 |  |
| `NeedBeforeGreed` | 2 |  |
| `Master` | 3 |  |

## LootThreshold

| name | order | meaning |
|---|---|---|
| `Average` | 0 |  |
| `Good` | 1 |  |
| `Excellent` | 2 |  |
| `Superb` | 3 |  |
| `Legendary` | 4 |  |
| `Inferior` | 5 |  |
| `Artifact` | 6 |  |

## MapZone

| name | order | meaning |
|---|---|---|
| `PublicEventIslandStage2` | 0 |  |
| `LevianBay` | 1 |  |
| `Thayd` | 2 |  |
| `Ellevar` | 3 |  |
| `halonring` | 4 |  |
| `Grimvault` | 5 |  |
| `Galeras` | 6 |  |
| `LevianBayStarComm1` | 7 |  |
| `EasternGrimvault` | 8 |  |
| `HalonRingIsland2` | 9 |  |
| `Malgrave` | 10 |  |
| `LevianBayStarComm3` | 11 |  |
| `WesternGrimvault` | 12 |  |
| `NorthernGrimvault` | 13 |  |
| `EverstarGrove` | 14 |  |
| `EternityIslands` | 15 |  |
| `Celestion` | 16 |  |
| `CrimsonIsle` | 17 |  |
| `Auroria` | 18 |  |
| `Illium` | 19 |  |
| `NorthernWilds` | 20 |  |
| `Wilderrun` | 21 |  |
| `LevianBayStarComm2` | 22 |  |
| `HalonRingIsland3` | 23 |  |
| `Whitevale` | 24 |  |
| `Algoroc` | 25 |  |
| `Deradune` | 26 |  |
| `TheDefileScreamingSword` | 27 |  |
| `HalonRingBCChamberofNurielDom` | 28 |  |
| `HalonRingBCChamberoftheEntityDom` | 29 |  |
| `BlighthavenChamberEarth` | 30 |  |
| `NorthernWildsExoLab729` | 31 |  |
| `HalonRingBCChamberofMadocExile` | 32 |  |
| `BlighthavenQueensDen` | 33 |  |
| `HalonRingBCCrystalCavernsExile` | 34 |  |
| `TheDefileResonanceTowerControlRoomDominion` | 35 |  |
| `TheDefileResonanceTowerControlRoomExile` | 36 |  |
| `HalonRingBCCrystalCavernsDominion` | 37 |  |
| `BlighthavenDecrepitExoLab` | 38 |  |
| `HalonRingBCDoomfarer` | 39 |  |
| `SouthernGrimvaultCreepingCaverns` | 40 |  |
| `HalonRingBCTerminiteMound` | 41 |  |
| `BlighthavenTransfusionChamber` | 42 |  |
| `BlighthavenChamberAir` | 43 |  |
| `BlighthavenRecontaminationRoom` | 44 |  |
| `HalonRingBCChamberofAradelExile` | 45 |  |
| `BlighthavenEmpyrealCaverns` | 46 |  |
| `HalonRingBCCaptainKrull` | 47 |  |
| `HalonRingBloodCrater` | 48 |  |
| `HalonRingBCChamberofAradelDom` | 49 |  |
| `SouthernGrimvaultEtherealCavity` | 50 |  |
| `HalonRingBCChamberofEnochDom` | 51 |  |
| `HalonRingBCChamberofEnochExile` | 52 |  |
| `TheDefileEmperorsDaughter` | 53 |  |
| `HalonRingBCRoughrockUnderground` | 54 |  |
| `HalonRingBCChamberofEshiaDom` | 55 |  |
| `BlighthavenDecontaminationRoom` | 56 |  |
| `TheDefileStrainMaw` | 57 |  |
| `SouthernGrimvaultStrainTunnels` | 58 |  |
| `SouthernGrimvaultEtherealHollow` | 59 |  |
| `BlighthavenGenesisChamber` | 60 |  |
| `BlighthavenChamberLife` | 61 |  |
| `HalonRingBCChamberoftheEntityExile` | 62 |  |
| `HalongRingBCCraterofCarnage` | 63 |  |
| `BlighthavenChamberWater` | 64 |  |
| `BlighthavenChamberLogic` | 65 |  |
| `BlighthavenChamberFire` | 66 |  |
| `HalonRingBCChamberofMadocDom` | 67 |  |
| `BlighthavenNurseryObservationRoom` | 68 |  |
| `HalonRingBCBlightmuckAbscess` | 69 |  |
| `BlighthavenNurseryChecpoint` | 70 |  |
| `BlighthavenMindoftheGlobellum` | 71 |  |
| `HalonRingBCChamberofEshiaExile` | 72 |  |
| `BlighthavenEtherealCaverns` | 73 |  |
| `BlighthavenAbandonedExoLab` | 74 |  |
| `HalonRingBCGoldenhandsReach` | 75 |  |
| `HalonRingBCChamberofNurielExile` | 76 |  |
| `HalonRingBCGrimvoidDreadvault` | 77 |  |
| `TheDefileBlackFocusEvacuationHub` | 78 |  |
| `HalonRingBCChamberofYuriaExile` | 79 |  |
| `NorthernWildsColdburrowCavern` | 80 |  |
| `HalonRingBCChamberofYuriaDom` | 81 |  |

## MatchEndReason

| name | order | meaning |
|---|---|---|
| `Completed` | 0 |  |
| `Forfeit` | 1 |  |
| `TimeExpired` | 2 |  |

## MatchType

| name | order | meaning |
|---|---|---|
| `Battleground` | 0 |  |
| `Dungeon` | 1 |  |
| `Adventure` | 2 |  |
| `Arena` | 3 |  |
| `Warplot` | 4 |  |
| `RatedBattleground` | 5 |  |
| `OpenArena` | 6 |  |
| `Event` | 7 |  |
| `Shiphand` | 8 |  |

## MountSlot

| name | order | meaning |
|---|---|---|
| `Front` | 0 |  |
| `Back` | 1 |  |
| `Left` | 2 |  |
| `Right` | 3 |  |

## MoveMethod

| name | order | meaning |
|---|---|---|
| `Nothing` | 0 |  |
| `Simple` | 1 |  |
| `EaseInSine` | 2 |  |
| `EaseOutSine` | 3 |  |
| `EaseInOutSine` | 4 |  |
| `EaseInQuad` | 5 |  |
| `EaseOutQuad` | 6 |  |
| `EaseInOutQuad` | 7 |  |
| `EaseInCubic` | 8 |  |
| `EaseOutCubic` | 9 |  |
| `EaseInOutCubic` | 10 |  |
| `EaseInQuart` | 11 |  |
| `EaseOutQuart` | 12 |  |
| `EaseInOutQuart` | 13 |  |
| `EaseInQuint` | 14 |  |
| `EaseOutQuint` | 15 |  |
| `EaseInOutQuint` | 16 |  |
| `EaseInExpo` | 17 |  |
| `EaseOutExpo` | 18 |  |
| `EaseInOutExpo` | 19 |  |
| `EaseInCirc` | 20 |  |
| `EaseOutCirc` | 21 |  |
| `EaseInOutCirc` | 22 |  |
| `EaseInBack` | 23 |  |
| `EaseOutBack` | 24 |  |
| `EaseInOutBack` | 25 |  |

## NeighborPermissionLevel

| name | order | meaning |
|---|---|---|
| `Normal` | 0 |  |
| `Roommate` | 1 |  |
| `Account` | 2 |  |

## PVPGameState

| name | order | meaning |
|---|---|---|
| `Preparation` | 0 |  |
| `InProgress` | 1 |  |
| `Finished` | 2 |  |

## PathMissionDisplayType

| name | order | meaning |
|---|---|---|
| `Soldier_Assassination` | 0 |  |
| `Soldier_Defend` | 1 |  |
| `Soldier_Demolition` | 2 |  |
| `Soldier_FirstStrike` | 3 |  |
| `Soldier_Holdout` | 4 |  |
| `Soldier_RescueOp` | 5 |  |
| `Soldier_Security` | 6 |  |
| `Soldier_Swat` | 7 |  |
| `Settler_Cache` | 8 |  |
| `Settler_CivilService` | 9 |  |
| `Settler_Expansion` | 10 |  |
| `Settler_Project` | 11 |  |
| `Settler_PublicSafety` | 12 |  |
| `Scientist_Analysis` | 13 |  |
| `Scientist_Archaeology` | 14 |  |
| `Scientist_Biology` | 15 |  |
| `Scientist_Botany` | 16 |  |
| `Scientist_Chemistry` | 17 |  |
| `Scientist_DatacubeDecryption` | 18 |  |
| `Scientist_Diagnostics` | 19 |  |
| `Scientist_Experimentation` | 20 |  |
| `Scientist_FieldStudy` | 21 |  |
| `Scientist_SpecimenSurvey` | 22 |  |
| `Explorer_Cartography` | 23 |  |
| `Explorer_Exploration` | 24 |  |
| `Explorer_Operations` | 25 |  |
| `Explorer_ScavengerHunt` | 26 |  |
| `Explorer_StakingClaim` | 27 |  |
| `Explorer_Surveillance` | 28 |  |
| `Explorer_Tracking` | 29 |  |
| `Explorer_Vista` | 30 |  |

## Perk

| name | order | meaning |
|---|---|---|
| `BankTab5` | 0 |  |
| `BankTab2` | 1 |  |
| `BankTab3` | 2 |  |
| `BankTab4` | 3 |  |
| `BankTab1` | 4 |  |
| `Tier6Unlock` | 5 |  |
| `Tier2Unlock` | 6 |  |
| `Tier5Unlock` | 7 |  |
| `Tier3Unlock` | 8 |  |
| `Tier4Unlock` | 9 |  |

## PetCustomizeResult

| name | order | meaning |
|---|---|---|
| `PetTypeNotSupported` | 0 |  |
| `InvalidName` | 1 |  |
| `InvalidSlot` | 2 |  |
| `UnknownFlairType` | 3 |  |
| `InvalidFlair` | 4 |  |
| `NotUnlocked` | 5 |  |
| `InvalidObject` | 6 |  |

## PetType

| name | order | meaning |
|---|---|---|
| `Scanbot` | 0 |  |
| `GroundMount` | 1 |  |
| `HoverBoard` | 2 |  |

## PublicEventStatType

| name | order | meaning |
|---|---|---|
| `Damage` | 0 |  |
| `Hits` | 1 |  |
| `Haters` | 2 |  |
| `Kills` | 3 |  |
| `Deaths` | 4 |  |
| `Healed` | 5 |  |
| `Contributions` | 6 |  |
| `DamageReceived` | 7 |  |
| `HealingReceived` | 8 |  |
| `Assists` | 9 |  |
| `Saves` | 10 |  |
| `Overhealed` | 11 |  |
| `OverhealingReceived` | 12 |  |
| `MedalPoints` | 13 |  |
| `MaxMultiKill` | 14 |  |
| `LongestImpulse` | 15 |  |
| `LongestLife` | 16 |  |
| `KillStreak` | 17 |  |
| `CustomStat00` | 18 |  |
| `CustomStat01` | 19 |  |
| `CustomStat02` | 20 |  |
| `CustomStat03` | 21 |  |
| `CustomStat04` | 22 |  |
| `CustomStat05` | 23 |  |

## PvpDeathReason

| name | order | meaning |
|---|---|---|
| `KilledByPlayer` | 0 |  |
| `KilledByCreature` | 1 |  |
| `Falling` | 2 |  |
| `Drowning` | 3 |  |

## QuestCategoryType

| name | order | meaning |
|---|---|---|
| `None` | 0 |  |
| `WorldStory` | 1 |  |
| `Adventures` | 2 |  |
| `Dungeons` | 3 |  |
| `Shiphands` | 4 |  |
| `Zones` | 5 |  |
| `Events` | 6 |  |
| `Housing` | 7 |  |
| `ItemImbuements` | 8 |  |
| `Tradeskills` | 9 |  |

## QuestRepeatPeriod

| name | order | meaning |
|---|---|---|
| `None` | 0 |  |
| `Daily` | 1 |  |
| `Weekly` | 2 |  |
| `Monthly` | 3 |  |
| `Yearly` | 4 |  |

## RatingType

| name | order | meaning |
|---|---|---|
| `Arena2v2` | 0 |  |
| `Arena3v3` | 1 |  |
| `Arena5v5` | 2 |  |
| `RatedBattleground` | 3 |  |
| `Warplot` | 4 |  |

## RecruitmentDemand

| name | order | meaning |
|---|---|---|
| `Full` | 0 |  |
| `Low` | 1 |  |
| `Medium` | 2 |  |
| `High` | 3 |  |

## RemodelOptionTypeCommunity

| name | order | meaning |
|---|---|---|
| `Sky` | 0 |  |
| `Music` | 1 |  |
| `Ground` | 2 |  |

## RemodelOptionTypeExterior

| name | order | meaning |
|---|---|---|
| `Roof` | 0 |  |
| `Wallpaper` | 1 |  |
| `Entry` | 2 |  |
| `Door` | 3 |  |
| `Sky` | 4 |  |
| `Music` | 5 |  |
| `Ground` | 6 |  |

## RemodelOptionTypeInterior

| name | order | meaning |
|---|---|---|
| `Wallpaper` | 0 |  |
| `Floor` | 1 |  |
| `Ceiling` | 2 |  |
| `Trim` | 3 |  |
| `Lighting` | 4 |  |
| `Music` | 5 |  |

## RemoveReason

| name | order | meaning |
|---|---|---|
| `Left` | 0 |  |
| `Kicked` | 1 |  |
| `Disconnected` | 2 |  |
| `Disband` | 3 |  |
| `RemovedByServer` | 4 |  |
| `VoteKicked` | 5 |  |

## ResidenceCustomizationMode

| name | order | meaning |
|---|---|---|
| `Advanced` | 0 |  |
| `Simple` | 1 |  |

## ResidencePrivacyLevel

| name | order | meaning |
|---|---|---|
| `Public` | 0 |  |
| `NeighborsOnly` | 1 |  |
| `RoommatesOnly` | 2 |  |
| `Private` | 3 |  |

## ResidencePrivileges

| name | order | meaning |
|---|---|---|
| `None` | 0 |  |
| `Owner` | 1 |  |
| `Roommate` | 2 |  |

## Result

| name | order | meaning |
|---|---|---|
| `PlayerNotFound` | 0 |  |
| `RealmNotFound` | 1 |  |
| `Sent` | 2 |  |
| `Accepted` | 3 |  |
| `Declined` | 4 |  |
| `NoPermissions` | 5 |  |
| `Grouped` | 6 |  |
| `Pending` | 7 |  |
| `ExpiredInviter` | 8 |  |
| `IsInvited` | 9 |  |
| `InvitedYou` | 10 |  |
| `Full` | 11 |  |
| `RoleFull` | 12 |  |
| `NoInvitingSelf` | 13 |  |
| `ExpiredInvitee` | 14 |  |
| `ServerControlled` | 15 |  |
| `GroupNotFound` | 16 |  |
| `NotAcceptingRequests` | 17 |  |
| `Busy` | 18 |  |
| `SentToLeader` | 19 |  |
| `LeaderOffline` | 20 |  |
| `WrongFaction` | 21 |  |
| `PrivilegeRestricted` | 22 |  |

## RewardModifierOwner

| name | order | meaning |
|---|---|---|
| `None` | 0 |  |
| `Spell` | 1 |  |
| `System` | 2 |  |
| `PublicEvent` | 3 |  |
| `HybridTier` | 4 |  |
| `Entitlement` | 5 |  |

## RewardProperty

| name | order | meaning |
|---|---|---|
| `XP` | 0 |  |
| `CurrencyType` | 1 |  |
| `RewardTrackId` | 2 |  |
| `RewardTrackType` | 3 |  |
| `OmniBits` | 4 |  |
| `Reputation` | 5 |  |
| `OmnibitDropChance` | 6 |  |

## RewardTrackRewardType

| name | order | meaning |
|---|---|---|
| `Item` | 0 |  |
| `AccountItem` | 1 |  |

## RewardTrackType

| name | order | meaning |
|---|---|---|
| `Contract_Pvp` | 0 |  |
| `Contract_Pve` | 1 |  |
| `Loyalty` | 2 |  |
| `Challenge` | 3 |  |

## RezType

| name | order | meaning |
|---|---|---|
| `WakeHere` | 0 |  |
| `Holocrypt` | 1 |  |
| `ExitInstance` | 2 |  |
| `SpellCasterLocation` | 3 |  |
| `WakeHereServiceToken` | 4 |  |

## Roles

| name | order | meaning |
|---|---|---|
| `Tank` | 0 |  |
| `Healer` | 1 |  |
| `DPS` | 2 |  |

## Rules

| name | order | meaning |
|---|---|---|
| `Default` | 0 |  |
| `DeathmatchPool` | 1 |  |
| `WaveRespawn` | 2 |  |

## SetCostumeResult

| name | order | meaning |
|---|---|---|
| `Success` | 0 |  |
| `AlreadySet` | 1 |  |
| `InvalidIndex` | 2 |  |
| `InCombat` | 3 |  |
| `NotUnlocked` | 4 |  |
| `TooSoon` | 5 |  |

## SharedChallengePreference

| name | order | meaning |
|---|---|---|
| `AutoAccept` | 0 |  |
| `Prompt` | 1 |  |
| `AutoReject` | 2 |  |

## SupportStuckAction

| name | order | meaning |
|---|---|---|
| `RecallBind` | 0 |  |
| `RecallDeath` | 1 |  |
| `RecallHouse` | 2 |  |

## Team

| name | order | meaning |
|---|---|---|
| `Team1` | 0 |  |
| `Team2` | 1 |  |

## TelegraphColorSet

| name | order | meaning |
|---|---|---|
| `Default` | 0 |  |
| `Deuteranopia` | 1 |  |
| `Protanopia` | 2 |  |
| `Tritanopia` | 3 |  |
| `Custom1` | 4 |  |
| `Custom2` | 5 |  |

## Winner

| name | order | meaning |
|---|---|---|
| `Team1` | 0 |  |
| `Team2` | 1 |  |
| `Draw` | 2 |  |

