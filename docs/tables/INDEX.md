# Every game table, dumped

**376 tables · 2,096,496 rows · build 16042.** The complete client database as TSV in
`docs/client-data/tables/`.

Produced by `dotnet run --project Tools/NexusUnleashed.TableDump -c Release -- <tbl> --all <out>`.

## Why this was not available before

The dumper hand-listed seven tables. The other 370 were unreachable not because they were hard
to read, but because **235 of the 377 `GameTable<>` properties carry no `[GameData]` attribute**,
and the filename resolver returned `null` without one — surfacing as
`Value cannot be null (Parameter 'path2')`, a path-join error several frames from the cause.

The derivation it needed (property name + `.tbl`) was already in that method, gated behind the
attribute. Ungating it does not change what the server loads at boot: the parameterless
`Initialise()` filters to attributed properties *before* that point, so `ModelMesh`, `SoundBank`
and friends stay out of the world server exactly as before.

| table | rows | cols | first columns |
|---|---|---|---|
| `localizedText` | 539,251 | 7 | `Id`, `SoundEventId`, `SoundEventIdFemale`, `Version`, `UnitVoiceTypeId` |
| `spline2Node` | 380,576 | 14 | `Id`, `SplineId`, `Ordinal`, `Position0`, `Position1` |
| `spell4effects` | 131,010 | 36 | `Id`, `SpellId`, `TargetFlags`, `EffectType`, `DamageType` |
| `mapZoneHex` | 117,452 | 5 | `Id`, `MapZoneId`, `Pos0`, `Pos1`, `Flags` |
| `item` | 71,918 | 45 | `Id`, `ItemBudgetId`, `ItemStatId`, `ItemRuneInstanceId`, `ItemQualityId` |
| `spell4` | 66,383 | 95 | `Id`, `Description`, `Spell4BaseIdBaseSpell`, `TierIndex`, `RavelInstanceId` |
| `creature2` | 53,137 | 119 | `Id`, `CreationTypeEnum`, `Description`, `LocalizedTextIdName`, `Creature2AoiSizeEnum` |
| `spell4Visual` | 47,283 | 34 | `Id`, `TargetTypeFlags`, `StageType`, `StageFlags`, `VisualEffectId` |
| `mapZoneHexGroupEntry` | 46,168 | 4 | `Id`, `MapZoneHexGroupId`, `HexX`, `HexY` |
| `spell4Base` | 44,838 | 42 | `Id`, `LocalizedTextIdName`, `Spell4HitResultId`, `Spell4TargetMechanicId`, `Spell4TargetAngleId` |
| `soundEvent` | 43,659 | 14 | `Id`, `Name`, `Hash`, `Radius`, `SoundBankId00` |
| `visualEffect` | 43,433 | 38 | `Id`, `VisualType`, `StartDelay`, `Duration`, `ModelItemSlot` |
| `worldLocation2` | 33,396 | 13 | `Id`, `Radius`, `MaxVerticalDistance`, `Position0`, `Position1` |
| `prerequisite` | 32,131 | 7 | `Id`, `Flags`, `PrerequisiteTypeId`, `PrerequisiteComparisonId`, `ObjectId` |
| `randomTextLine` | 25,190 | 3 | `Id`, `LocalizedTextId`, `RandomTextLineSetId` |
| `spell4Telegraph` | 24,343 | 3 | `Id`, `Spell4Id`, `TelegraphDamageId` |
| `spellPhase` | 23,099 | 5 | `Id`, `PhaseDelay`, `PhaseFlags`, `OrderIndex`, `Spell4IdOwner` |
| `quest2RandomTextLineJoin` | 20,684 | 4 | `Id`, `Quest2Id`, `QuestVOTextType`, `RandomTextLineId` |
| `randomTextLineSet` | 18,479 | 46 | `Id`, `GeneralVOSetEnumFirst00`, `GeneralVOSetEnumFirst01`, `GeneralVOSetEnumFirst02`, `GeneralVOSetEnumFirst03` |
| `spell4VisualGroup` | 18,148 | 3 | `Id`, `Spell4VisualIdVisuals`, `VisualEffectIdPrimaryCaster` |
| `creature2DisplayGroupEntry` | 18,028 | 4 | `Id`, `Creature2DisplayGroupId`, `Creature2DisplayInfoId`, `Weight` |
| `creature2OverrideProperties` | 15,365 | 4 | `Id`, `Creature2Id`, `UnitPropertyIndex`, `UnitPropertyValue` |
| `creature2DisplayInfo` | 13,868 | 78 | `Id`, `StatusFlags`, `AssetPath`, `AssetTexture00`, `AssetTexture01` |
| `spline2` | 13,304 | 3 | `Id`, `WorldId`, `SplineType` |
| `telegraphDamage` | 12,085 | 25 | `Id`, `TelegraphSubtypeEnum`, `DamageShapeEnum`, `Param00`, `Param01` |
| `gossipEntry` | 10,799 | 5 | `Id`, `GossipSetId`, `IndexOrder`, `LocalizedTextId`, `PrerequisiteId` |
| `localizedEnum` | 10,551 | 3 | `Id`, `EnumName`, `LocalizedTextId` |
| `questObjective` | 10,031 | 14 | `Id`, `Type`, `Flags`, `Data`, `Count` |
| `targetGroup` | 9,644 | 4 | `Id`, `LocalizedTextIdDisplayString`, `Type`, `DataEntries` |
| `itemDisplay` | 8,737 | 44 | `Id`, `Description`, `Item2TypeId`, `ObjectModel`, `ObjectModelL` |
| `spell4ClientMissile` | 7,617 | 53 | `Id`, `MissileType`, `CastStage`, `OriginUnitEnum`, `TargetFlags` |
| `creature2Action` | 7,311 | 12 | `Id`, `Description`, `CreatureActionSetId`, `State`, `Event` |
| `modelSequence` | 7,287 | 4 | `Id`, `Description`, `FallBackID`, `Flag` |
| `achievementChecklist` | 6,568 | 7 | `Id`, `AchievementId`, `Bit`, `ObjectId`, `ObjectIdAlt` |
| `itemSpecial` | 6,035 | 5 | `Id`, `PrerequisiteIdGeneric00`, `LocalizedTextIdName`, `Spell4IdOnEquip`, `Spell4IdOnActivate` |
| `quest2Reward` | 5,415 | 6 | `Id`, `Quest2Id`, `Quest2RewardTypeId`, `ObjectId`, `ObjectAmount` |
| `quest2` | 5,194 | 95 | `Id`, `LocalizedTextIdTitle`, `LocalizedTextIdText`, `Flags`, `ConLevel` |
| `achievement` | 4,943 | 23 | `Id`, `AchievementTypeId`, `AchievementCategoryId`, `Flags`, `WorldZoneId` |
| `characterCustomization` | 4,784 | 8 | `Id`, `RaceId`, `Gender`, `ItemSlotId`, `ItemDisplayId` |
| `modelEventVisualJoin` | 4,620 | 8 | `Id`, `UnitVisualTypeId`, `ItemVisualTypeId`, `MaterialTypeId`, `ModelEventId` |
| `creature2ModelInfo` | 4,328 | 59 | `Id`, `AssetPath`, `AssetTexture0`, `AssetTexture1`, `ModelTextureId0` |
| `wordFilter` | 4,165 | 6 | `Id`, `Filter`, `UserTextFilterClassEnum`, `DeploymentRegionEnum`, `LanguageId` |
| `communicatorMessages` | 4,105 | 24 | `Id`, `LocalizedTextIdMessage`, `Delay`, `Flags`, `CreatureId` |
| `creature2OutfitGroupEntry` | 3,986 | 4 | `Id`, `Creature2OutfitGroupId`, `Creature2OutfitInfoId`, `Weight` |
| `publicEventObjective` | 3,703 | 23 | `Id`, `PublicEventId`, `PublicEventObjectiveFlags`, `PublicEventObjectiveTypeSpecificFlags`, `WorldLocation2Id` |
| `creature2ActionSet` | 3,688 | 3 | `Id`, `Description`, `PrerequisiteId` |
| `worldzone` | 3,436 | 10 | `Id`, `LocalizedTextIdName`, `ParentZoneId`, `AllowAccess`, `Color` |
| `housingDecorInfo` | 3,248 | 16 | `Id`, `HousingDecorTypeId`, `HookTypeId`, `LocalizedTextIdName`, `Flags` |
| `creature2OutfitInfo` | 3,109 | 13 | `Id`, `ItemDisplayId00`, `ItemDisplayId01`, `ItemDisplayId02`, `ItemDisplayId03` |
| `hookAsset` | 2,916 | 9 | `Id`, `Asset`, `Scale`, `OffsetX`, `OffsetY` |
| `tradeskillSchematic2` | 2,867 | 32 | `Id`, `LocalizedTextIdName`, `TradeSkillId`, `Item2IdOutput`, `Item2IdOutputFail` |
| `world` | 2,729 | 19 | `Id`, `AssetPath`, `Flags`, `Type`, `ScreenPath` |
| `questDirectionEntry` | 2,520 | 6 | `Id`, `WorldLocation2Id`, `WorldLocation2IdInactive`, `WorldZoneId`, `QuestDirectionEntryFlags` |
| `itemDisplaySourceEntry` | 2,509 | 7 | `Id`, `ItemSourceId`, `Item2TypeId`, `ItemMinLevel`, `ItemMaxLevel` |
| `pathSettlerImprovement` | 2,475 | 8 | `Id`, `CountResource00`, `CountResource01`, `CountResource02`, `CountRecontributionResource00` |
| `storyPanel` | 2,413 | 7 | `Id`, `LocalizedTextIdBody`, `SoundEventId`, `WindowTypeId`, `DurationMS` |
| `spell4StackGroup` | 2,348 | 3 | `Id`, `StackCap`, `StackTypeEnum` |
| `salvage` | 2,335 | 3 | `Id`, `Item2TypeId`, `Level` |
| `accountItem` | 2,219 | 17 | `Id`, `Flags`, `Item2Id`, `EntitlementId`, `EntitlementCount` |
| `gossipSet` | 1,978 | 4 | `Id`, `Flags`, `GossipProximityEnum`, `Cooldown` |
| `worldSocket` | 1,971 | 4 | `Id`, `WorldId`, `BoundIds`, `AverageHeight` |
| `faction2Relationship` | 1,964 | 4 | `Id`, `FactionId0`, `FactionId1`, `FactionLevel` |
| `randomPlayerName` | 1,846 | 7 | `Id`, `NameFragment`, `NameFragmentTypeEnum`, `RaceId`, `Gender` |
| `challengeTier` | 1,684 | 2 | `Id`, `Count` |
| `tradeskillAchievementLayout` | 1,609 | 9 | `Id`, `AchievementId`, `AchievementIdParent00`, `AchievementIdParent01`, `AchievementIdParent02` |
| `mapZoneHexGroup` | 1,542 | 2 | `Id`, `MapZoneId` |
| `episodeQuest` | 1,497 | 5 | `Id`, `EpisodeId`, `QuestId`, `OrderIdx`, `Flags` |
| `pathSettlerImprovementGroup` | 1,438 | 16 | `Id`, `PathSettlerHubId`, `PathSettlerImprovementGroupFlags`, `Creature2IdDepot`, `LocalizedTextIdName` |
| `spell4GroupList` | 1,431 | 2 | `Id`, `SpellGroupIds` |
| `soundZoneKit` | 1,427 | 19 | `Id`, `SoundZoneKitIdParent`, `WorldZoneId`, `InheritFlags`, `PropertyFlags` |
| `pathSoldierEventWave` | 1,411 | 4 | `Id`, `PathSoldierEventId`, `WaveIndex`, `SoundZoneKitId` |
| `storeKeyword` | 1,299 | 3 | `Id`, `StoreDisplayInfoId`, `Keyword` |
| `questDirection` | 1,255 | 19 | `Id`, `QuestDirectionFlags`, `QuestDirectionEntryId00`, `QuestDirectionEntryId01`, `QuestDirectionEntryId02` |
| `gameFormula` | 1,217 | 11 | `Id`, `Dataint0`, `Dataint01`, `Dataint02`, `Dataint03` |
| `faction2` | 1,189 | 7 | `Id`, `Faction2IdParent`, `Flags`, `LocalizedTextIdName`, `LocalizedTextIdToolTip` |
| `salvageException` | 1,169 | 3 | `Id`, `Item2Id`, `Flags` |
| `worldLayer` | 1,117 | 20 | `Id`, `Description`, `HeightScale`, `HeightOffset`, `ParallaxScale` |
| `pathMission` | 1,064 | 21 | `Id`, `Creature2IdUnlock`, `PathTypeEnum`, `PathMissionTypeEnum`, `PathMissionDisplayTypeEnum` |
| `clientSideInteraction` | 1,057 | 25 | `Id`, `InteractionType`, `Threshold`, `Duration`, `IncrementValue` |
| `virtualItem` | 1,046 | 6 | `Id`, `ButtonIcon`, `Item2TypeId`, `LocalizedTextIdName`, `LocalizedTextIdFlavor` |
| `storeDisplayInfo` | 1,023 | 5 | `Id`, `DisplayType`, `DisplayValue`, `ModelCameraId`, `LocalizedTextIdName` |
| `modelSequenceByMode` | 1,013 | 5 | `Id`, `ModelSequenceId`, `ModelSequenceIdSwim`, `ModelSequenceIdHover`, `ModelSequenceIdFly` |
| `creature2ActionText` | 1,012 | 16 | `Id`, `LocalizedTextIdOnEnterCombat00`, `LocalizedTextIdOnEnterCombat01`, `LocalizedTextIdOnEnterCombat02`, `LocalizedTextIdOnEnterCombat03` |
| `eldanAugmentation` | 910 | 12 | `Id`, `DisplayRow`, `DisplayColumn`, `ClassId`, `PowerCost` |
| `worldSky` | 886 | 4 | `Id`, `AssetPath`, `AssetPathInFlux`, `Color` |
| `archiveEntryUnlockRule` | 867 | 10 | `Id`, `ArchiveEntryId`, `ArchiveEntryUnlockRuleEnum`, `ArchiveEntryUnlockRuleFlags`, `Object00` |
| `archiveEntry` | 796 | 21 | `Id`, `LocalizedTextIdHeading`, `LocalizedTextIdText00`, `LocalizedTextIdText01`, `LocalizedTextIdText02` |
| `datacube` | 765 | 16 | `Id`, `DatacubeTypeEnum`, `LocalizedTextIdTitle`, `LocalizedTextIdText00`, `LocalizedTextIdText01` |
| `tradeskillAchievementReward` | 761 | 13 | `Id`, `AchievementId`, `Faction2Id`, `FactionIdAmount`, `TalentPoints` |
| `itemSetBonus` | 749 | 6 | `Id`, `RequiredPower`, `UnitProperty2Id`, `Scalar`, `Offset` |
| `materialRemap` | 698 | 4 | `Id`, `MaterialDataRow`, `MaterialSetId`, `MaterialDataRowRemap` |
| `spell4AoeTargetConstraints` | 690 | 6 | `Id`, `Angle`, `TargetCount`, `MinRange`, `MaxRange` |
| `mapZonePOI` | 670 | 7 | `Id`, `MapZoneId`, `Pos0`, `Pos1`, `Pos2` |
| `challenge` | 643 | 22 | `Id`, `ChallengeTypeEnum`, `Target`, `ChallengeFlags`, `WorldZoneIdRestriction` |
| `publicEvent` | 642 | 13 | `Id`, `WorldId`, `WorldZoneId`, `LocalizedTextIdName`, `FailureTimeMs` |
| `spell4Thresholds` | 622 | 12 | `Id`, `Spell4IdParent`, `Spell4IdToCast`, `OrderIndex`, `ThresholdDuration` |
| `pathExplorerNode` | 576 | 7 | `Id`, `PathExplorerAreaId`, `WorldLocation2Id`, `Spline2Id`, `LocalizedTextIdSettlerButton` |
| `creature2Affiliation` | 569 | 4 | `Id`, `LocalizedTextIdTitle`, `MiniMapMarkerId`, `OverheadIconAssetPath` |
| `propAdditionalDetail` | 553 | 2 | `Id`, `LocalizedTextId` |
| `item2Type` | 542 | 12 | `Id`, `LocalizedTextId`, `ItemSlotId`, `SoundEventIdLoot`, `SoundEventIdEquip` |
| `actionBarShortcutSet` | 541 | 25 | `Id`, `ShortcutType00`, `ShortcutType01`, `ShortcutType02`, `ShortcutType03` |
| `lootSpell` | 533 | 10 | `Id`, `LootSpellTypeEnum`, `LootSpellPickupEnumFlags`, `Creature2Id`, `ButtonIcon` |
| `worldClutter` | 528 | 46 | `Id`, `Description`, `Density`, `ClutterFlags`, `AssetPath0` |
| `housingPlugItem` | 514 | 48 | `Id`, `LocalizedTextIdName`, `HousingPlotTypeId`, `LocalizedTextIdTooltip`, `WorldIdPlug00` |
| `mapzone` | 490 | 14 | `Id`, `LocalizedTextIdName`, `MapContinentId`, `Folder`, `HexMinX` |
| `mapZoneWorldJoin` | 489 | 3 | `Id`, `MapZoneId`, `WorldId` |
| `unitVehicle` | 466 | 30 | `Id`, `VehicleTypeEnum`, `NumberPilots`, `PilotPosture00`, `PilotPosture01` |
| `itemStat` | 454 | 3 | `Id`, `ItemStatTypeEnum`, `ItemStatData` |
| `rewardTrackRewards` | 446 | 16 | `Id`, `RewardTrackId`, `RewardPointFlags`, `PrerequisiteId`, `Flags` |
| `customizationParameterMap` | 443 | 7 | `Id`, `RaceId`, `GenderEnum`, `ModelBoneId`, `CustomizationParameterId` |
| `characterTitle` | 427 | 8 | `Id`, `CharacterTitleCategoryId`, `LocalizedTextIdName`, `LocalizedTextIdTitle`, `Spell4IdActivate` |
| `dyeColorRamp` | 422 | 7 | `Id`, `Flags`, `LocalizedTextIdName`, `RampIndex`, `CostMultiplier` |
| `housingPlotInfo` | 420 | 6 | `Id`, `WorldSocketId`, `PlotType`, `HousingPropertyInfoId`, `HousingPropertyPlotIndex` |
| `spell4EffectModification` | 417 | 10 | `Id`, `Spell4EffectsId`, `EffectTypeEnum`, `ModificationParameterEnum`, `Priority` |
| `pathScientistCreatureInfo` | 402 | 14 | `Id`, `ScientistCreatureFlags`, `DisplayIcon`, `PrerequisiteIdScan`, `PrerequisiteIdRawScan` |
| `datacubeVolume` | 401 | 19 | `Id`, `LocalizedTextIdName`, `AssetPath`, `DatacubeId00`, `DatacubeId01` |
| `itemImbuement` | 399 | 31 | `Id`, `Quest2Id00`, `Quest2Id01`, `Quest2Id02`, `Quest2Id03` |
| `emotes` | 397 | 26 | `Id`, `LocalizedTextIdNoArgToAll`, `LocalizedTextIdNoArgToSelf`, `NoArgAnim`, `LocalizedTextIdArgToAll` |
| `soundMusicSet` | 396 | 6 | `Id`, `SoundEventIdStart`, `SoundEventIdStop`, `RestartDelayMin`, `RestartDelayMax` |
| `dailyLoginReward` | 365 | 5 | `Id`, `LoginDay`, `DailyLoginRewardTypeEnum`, `RewardObjectValue`, `DailyLoginRewardTierEnum` |
| `pathSoldierEvent` | 356 | 7 | `Id`, `PathSoldierEventType`, `MaxTimeBetweenWaves`, `MaxEventTime`, `TowerDefenseAllowance` |
| `characterCreation` | 350 | 13 | `Id`, `ClassId`, `RaceId`, `Sex`, `FactionId` |
| `itemColorSet` | 341 | 4 | `Id`, `DyeColorRampId00`, `DyeColorRampId01`, `DyeColorRampId02` |
| `petFlair` | 336 | 7 | `Id`, `UnlockBitIndex`, `Type`, `Spell4Id`, `LocalizedTextIdTooltip` |
| `spell4Modification` | 331 | 9 | `Id`, `Spell4EffectsId`, `ModificationParameterEnum`, `Priority`, `ModificationTypeEnum` |
| `spell4CastResult` | 327 | 5 | `Id`, `EnumName`, `CombatMessageTypeEnum`, `LocalizedTextIdDisplayText`, `SoundEventId` |
| `housingContributionInfo` | 326 | 13 | `Id`, `HousingContributionTypeId`, `ContributionPointRequirement`, `Item2IdTier00`, `Item2IdTier01` |
| `pathReward` | 302 | 11 | `Id`, `PathRewardTypeEnum`, `ObjectId`, `Spell4Id`, `Item2Id` |
| `episode` | 300 | 9 | `Id`, `LocalizedTextIdName`, `LocalizedTextIdBriefing`, `LocalizedTextIdEndSummary`, `Flags` |
| `tradeskillMaterial` | 300 | 5 | `Id`, `Item2IdStatRevolution`, `Item2Id`, `DisplayIndex`, `TradeskillMaterialCategoryId` |
| `tutorial` | 298 | 7 | `Id`, `Flags`, `TutorialCategoryEnum`, `LocalizedTextIdContextualPopup`, `TutorialAnchorId` |
| `spellLevel` | 288 | 6 | `Id`, `ClassId`, `CharacterLevel`, `PrerequisiteId`, `Spell4Id` |
| `cCStateAdditionalData` | 283 | 12 | `Id`, `CcStatesId`, `DataInt00`, `DataInt01`, `DataInt02` |
| `housingWallpaperInfo` | 280 | 16 | `Id`, `LocalizedTextId`, `Cost`, `CostCurrencyTypeId`, `ReplaceableMaterialInfoId` |
| `tutorialPage` | 276 | 12 | `Id`, `TutorialId`, `Page`, `TutorialLayoutId`, `LocalizedTextIdTitle` |
| `achievementCategory` | 273 | 4 | `Id`, `LocalizedTextId`, `LocalizedTextIdFullName`, `AchievementCategoryIdParent` |
| `prerequisiteType` | 273 | 2 | `Id`, `LocalizedTextIdError` |
| `soundUIContext` | 271 | 3 | `Id`, `LuaVariableName`, `SoundEventId` |
| `taxiNode` | 261 | 11 | `Id`, `LocalizedTextId`, `TaxiNodeTypeEnum`, `Flags`, `FlightPathTypeEnum` |
| `archiveArticle` | 251 | 34 | `Id`, `Creature2IdPortrait`, `IconAssetPath`, `LocalizedTextIdTitle`, `LocalizedTextIdText00` |
| `genericStringGroups` | 251 | 2 | `Id`, `LocalizedTextId` |
| `genericUnlockEntry` | 251 | 6 | `Id`, `LocalizedTextIdDescription`, `SpriteIcon`, `SpritePreview`, `GenericUnlockTypeEnum` |
| `genericUnlockSet` | 251 | 8 | `Id`, `GenericUnlockScopeEnum`, `GenericUnlockEntryId00`, `GenericUnlockEntryId01`, `GenericUnlockEntryId02` |
| `characterCustomizationSelection` | 248 | 4 | `Id`, `CharacterCustomizationLabelId`, `Value`, `Cost` |
| `tradeskillBonus` | 248 | 24 | `Id`, `TradeSkillTierId`, `AchievementId`, `IconPath`, `LocalizedTextIdName` |
| `instancePortal` | 241 | 6 | `Id`, `LocalizedTextIdName`, `MinLevel`, `MaxLevel`, `ExpectedCompletionTime` |
| `soundImpactEvents` | 239 | 5 | `Id`, `Origin`, `Target`, `Qualifier`, `Event` |
| `taxiRoute` | 238 | 4 | `Id`, `TaxiNodeIdSource`, `TaxiNodeIdDestination`, `Price` |
| `clientEvent` | 228 | 9 | `Id`, `Description`, `WorldId`, `EventTypeEnum`, `EventData` |
| `hazard` | 228 | 15 | `Id`, `LocalizedTextIdName`, `LocalizedTextIdTooltip`, `MeterChangeRate`, `MeterMaxValue` |
| `itemRuneInstance` | 222 | 13 | `Id`, `DefinedSocketCount`, `DefinedSocketType00`, `DefinedSocketType01`, `DefinedSocketType02` |
| `unitRace` | 221 | 8 | `Id`, `SoundImpactDescriptionIdOrigin`, `SoundImpactDescriptionIdTarget`, `UnitVisualTypeId`, `SoundEventIdAggro` |
| `loadingScreenTip` | 217 | 2 | `Id`, `LocalizedTextId` |
| `inputAction` | 210 | 6 | `Id`, `EnumName`, `LocalizedTextId`, `InputActionCategoryId`, `CanHaveUpDownState` |
| `questHub` | 209 | 3 | `Id`, `WorldLocation2Id`, `LocalizedTextIdName` |
| `modelAttachment` | 202 | 2 | `Id`, `EnumName` |
| `spellCoolDown` | 202 | 2 | `Id`, `CooldownTime` |
| `modelMesh` | 201 | 2 | `Id`, `EnumName` |
| `modelPose` | 201 | 5 | `Id`, `SequenceId`, `Description`, `ModelPoseIdBase`, `ModelPoseTypeEnum` |
| `xpPerLevel` | 201 | 6 | `Id`, `MinXpForLevel`, `BaseQuestXpPerLevel`, `AbilityPointsPerLevel`, `AttributePointsPerLevel` |
| `tradeskillHarvestingInfo` | 200 | 4 | `Id`, `TradeSkillTierId`, `PrerequisiteId`, `MiniMapMarkerId` |
| `unitProperty2` | 200 | 11 | `Id`, `Description`, `EnumName`, `DefaultValue`, `LocalizedTextId` |
| `pathExplorerScavengerClue` | 197 | 7 | `Id`, `LocalizedTextIdClue`, `ExplorerScavengerClueTypeEnum`, `Creature2Id`, `TargetGroupId` |
| `trackingSlot` | 175 | 4 | `Id`, `LocalizedTextIdLabel`, `IconPath`, `PublicEventObjectiveId` |
| `pathExplorerArea` | 172 | 2 | `Id`, `PathSettlerHubId` |
| `guildStandardPart` | 167 | 4 | `Id`, `GuildStandardPartTypeEnum`, `LocalizedTextIdName`, `ItemDisplayIdStandard` |
| `tradeskillCatalyst` | 164 | 13 | `Id`, `TradeSkillId`, `Tier`, `TradeskillCatalystEnum00`, `TradeskillCatalystEnum01` |
| `lootPinataInfo` | 163 | 10 | `Id`, `Item2Id`, `Item2TypeId`, `Item2CategoryId`, `Item2FamilyId` |
| `modelBonePriority` | 158 | 4 | `Id`, `BoneID`, `BoneSetID`, `Priority` |
| `item2Category` | 155 | 13 | `Id`, `LocalizedTextId`, `ItemProficiencyId`, `Flags`, `TradeSkillId` |
| `spellEffectType` | 150 | 12 | `Id`, `Flags`, `DataType00`, `DataType01`, `DataType02` |
| `modelSequenceByWeapon` | 146 | 12 | `Id`, `ModelSequenceId`, `ModelSequenceId1H`, `ModelSequenceId2H`, `ModelSequenceId2HL` |
| `soundBank` | 140 | 2 | `Id`, `Name` |
| `clientEventAction` | 138 | 5 | `Id`, `ActionTypeEnum`, `ActionData00`, `ActionData01`, `LocalizedTextIdSubZoneName` |
| `primalMatrixNode` | 136 | 16 | `Id`, `PositionX`, `PositionY`, `PrimalMatrixNodeTypeEnum`, `Flags` |
| `soundContext` | 133 | 3 | `Id`, `EventId`, `Type` |
| `mapZoneSprite` | 130 | 2 | `Id`, `SpriteName` |
| `tradeskillAdditive` | 129 | 6 | `Id`, `TradeSkillId`, `Tier`, `VectorX`, `VectorY` |
| `rewardPropertyPremiumModifier` | 125 | 9 | `Id`, `PremiumSystemEnum`, `Tier`, `RewardPropertyId`, `RewardPropertyData` |
| `itemImbuementReward` | 124 | 5 | `Id`, `ItemImbuementRewardTypeEnum`, `RewardObjectId`, `RewardValue`, `RewardValueFloat` |
| `pathLevel` | 120 | 4 | `Id`, `PathTypeEnum`, `PathLevel`, `PathXP` |
| `veteranTier` | 116 | 4 | `Id`, `PrimeLevel`, `VeteranTierScalingType`, `UnitPropertyOverrideMenace` |
| `pathEpisode` | 115 | 6 | `Id`, `LocalizedTextIdName`, `LocalizedTextIdSummary`, `WorldId`, `WorldZoneId` |
| `soundSwitch` | 113 | 3 | `Id`, `NameHash`, `GroupHash` |
| `housingWarplotPlugInfo` | 112 | 18 | `Id`, `HousingPlugItemId`, `MaintenanceCost`, `UpgradeCost00`, `UpgradeCost01` |
| `levelUpUnlock` | 106 | 8 | `Id`, `LevelUpUnlockSystemEnum`, `Level`, `LevelUpUnlockTypeId`, `LocalizedTextIdDescription` |
| `cinematic` | 104 | 1 | `Id` |
| `spell4SpellTypes` | 104 | 3 | `Id`, `TypeName`, `EnumName` |
| `cityDirection` | 103 | 8 | `Id`, `CityDirectionTypeEnum`, `LocalizedTextIdName`, `WorldZoneId`, `WorldLocation2Id00` |
| `creatureLevel` | 101 | 2 | `Id`, `UnitPropertyValue` |
| `luaEvent` | 99 | 3 | `Id`, `EventName`, `Parameters` |
| `matchingGameMap` | 99 | 9 | `Id`, `MatchingGameMapEnumFlags`, `LocalizedTextIdName`, `LocalizedTextIdDescription`, `MatchingGameTypeId` |
| `pathSettlerHub` | 96 | 29 | `Id`, `MaxAvenueEconomy`, `MaxAvenueSecurity`, `MaxAvenueQualityOfLife`, `LocalizedTextIdEconomy` |
| `liveEvent` | 95 | 16 | `Id`, `LiveEventTypeEnum`, `MaxValue`, `Flags`, `LiveEventCategoryEnum` |
| `miniMapMarker` | 95 | 2 | `Id`, `LuaName` |
| `replaceableMaterialInfo` | 94 | 100 | `Id`, `Type`, `Flags`, `Op`, `Blend` |
| `tradeskillTalentTier` | 92 | 9 | `Id`, `TradeSkillId`, `PointsToUnlock`, `RespecCost`, `TradeSkillBonusId00` |
| `itemSet` | 91 | 14 | `Id`, `LocalizedTextId`, `ItemSetBonusId00`, `ItemSetBonusId01`, `ItemSetBonusId02` |
| `resourceConversion` | 90 | 9 | `Id`, `ResourceConversionTypeEnum`, `SourceId`, `SourceCount`, `TargetId` |
| `componentRegionRect` | 87 | 7 | `Id`, `RegionId`, `RectMinX`, `RectMinY`, `RectLimX` |
| `mapContinent` | 85 | 13 | `Id`, `LocalizedTextIdName`, `AssetPath`, `ImagePath`, `ImageWidth` |
| `periodicQuestGroup` | 85 | 7 | `Id`, `PeriodicQuestSetId`, `PeriodicQuestsOffered`, `MaxPeriodicQuestsAllowed`, `Weight` |
| `worldWaterLayer` | 84 | 15 | `Id`, `Description`, `RippleColorTex`, `RippleNormalTex`, `Scale` |
| `modelEvent` | 81 | 2 | `Id`, `EnumName` |
| `soundStates` | 80 | 3 | `Id`, `NameHash`, `SoundGroupHash` |
| `pathSoldierAssassinate` | 77 | 4 | `Id`, `Creature2Id`, `TargetGroupId`, `Count` |
| `pathSoldierActivate` | 76 | 5 | `Id`, `Creature2Id`, `TargetGroupId`, `Count`, `SoldierActivateModeEnum` |
| `binkMovieSubtitle` | 74 | 4 | `Id`, `BinkMovieId`, `DelayMs`, `LocalizedTextIdDisplayText` |
| `primalMatrixReward` | 74 | 17 | `Id`, `PrimalMatrixRewardTypeEnum0`, `PrimalMatrixRewardTypeEnum1`, `PrimalMatrixRewardTypeEnum2`, `PrimalMatrixRewardTypeEnum3` |
| `tutorialAnchor` | 71 | 5 | `Id`, `TutorialAnchorOrientationEnum`, `HOffset`, `VOffset`, `Flags` |
| `matchingGameType` | 69 | 14 | `Id`, `LocalizedTextIdName`, `LocalizedTextIdDescription`, `MatchTypeEnum`, `MatchingGameTypeEnumFlags` |
| `materialData` | 69 | 3 | `Id`, `Row`, `MaterialTypeId` |
| `itemBudget` | 67 | 2 | `Id`, `Budgets` |
| `periodicQuestSet` | 67 | 4 | `Id`, `PeriodicQuestSetCategoryId`, `PeriodicGroupsOffered`, `Weight` |
| `housingPropertyInfo` | 65 | 13 | `Id`, `LocalizedTextIdName`, `WorldId`, `HousingMapInfoId`, `Cost` |
| `housingDecorType` | 64 | 3 | `Id`, `LocalizedTextId`, `LuaString` |
| `publicEventVote` | 64 | 7 | `Id`, `LocalizedTextIdTitle`, `LocalizedTextIdDescription`, `LocalizedTextIdOption`, `LocalizedTextIdLabel` |
| `resourceConversionGroup` | 64 | 8 | `Id`, `Flags`, `ResourceConversionId00`, `ResourceConversionId01`, `ResourceConversionId02` |
| `bindPoint` | 62 | 3 | `Id`, `BindPointFactionEnum`, `LocalizedTextId` |
| `modelBone` | 62 | 2 | `Id`, `XSIName` |
| `hookType` | 61 | 1 | `Id` |
| `modelCluster` | 61 | 2 | `Id`, `EnumName` |
| `spell4TargetMechanics` | 61 | 3 | `Id`, `TargetType`, `Flags` |
| `entitlement` | 60 | 8 | `Id`, `MaxCount`, `Flags`, `Spell4IdPersistentBuff`, `CharacterTitleId` |
| `missileRevolverTrack` | 60 | 6 | `Id`, `Radius`, `Speed`, `SpeedMultiplier`, `ScaleMultiplier` |
| `modelCamera` | 60 | 2 | `Id`, `EnumName` |
| `pathExplorerScavengerHunt` | 58 | 12 | `Id`, `Creature2IdStart`, `PathExplorerScavengerClueId00`, `PathExplorerScavengerClueId01`, `PathExplorerScavengerClueId02` |
| `tradeskillTier` | 56 | 13 | `Id`, `TradeSkillId`, `Tier`, `RequiredXp`, `LearnXp` |
| `achievementText` | 55 | 2 | `Id`, `LocalizedTextId` |
| `pathSoldierSWAT` | 55 | 5 | `Id`, `Creature2Id`, `TargetGroupId`, `Count`, `VirtualItemIdDisplay` |
| `finishingMoveDeathVisual` | 54 | 12 | `Id`, `Priority`, `DamageTypeFlags`, `Creature2MinSize`, `Creature2MaxSize` |
| `genericMapNode` | 54 | 8 | `Id`, `GenericMapId`, `WorldLocation2Id`, `LocalizedTextIdName`, `LocalizedTextIdDescription` |
| `pathExplorerDoorEntrance` | 53 | 7 | `Id`, `PathExplorerDoorTypeEnumSurface`, `PathExplorerDoorTypeEnumMicro`, `Creature2IdSurface`, `Creature2IdMicro` |
| `questCategory` | 53 | 4 | `Id`, `Description`, `LocalizedTextIdTitle`, `QuestCategoryTypeEnum` |
| `itemRandomStat` | 52 | 5 | `Id`, `ItemRandomStatGroupId`, `Weight`, `ItemStatTypeEnum`, `ItemStatData` |
| `pathScientistExperimentationPattern` | 52 | 6 | `Id`, `LocalizedTextIdName`, `LocalizedTextIdDescription`, `PathMissionId`, `PathScientistExperimentationId` |
| `positionalRequirement` | 52 | 4 | `Id`, `AngleCenter`, `AngleRange`, `Flags` |
| `spell4Reagent` | 51 | 5 | `Id`, `ReagentType`, `ReagentTypeObjectId`, `ReagentCount`, `ConsumeReagent` |
| `itemSlot` | 50 | 8 | `Id`, `EnumName`, `EquippedSlotFlags`, `ArmorModifier`, `ItemLevelModifier` |
| `spell4Conditions` | 48 | 3 | `Id`, `ConditionMask`, `ConditionValue` |
| `mapZoneNemesisRegion` | 47 | 4 | `Id`, `MapZoneHexGroupId`, `LocalizedTextIdDescription`, `Faction2Id` |
| `pathSettlerMayor` | 47 | 26 | `Id`, `LocalizedTextId00`, `LocalizedTextId01`, `LocalizedTextId02`, `LocalizedTextId03` |
| `periodicQuestSetCategory` | 47 | 2 | `Id`, `PeriodicSetsOffered` |
| `modelBoneSet` | 46 | 1 | `Id` |
| `pathSettlerSheriff` | 44 | 18 | `Id`, `Quest2IdSheriff00`, `Quest2IdSheriff01`, `Quest2IdSheriff02`, `Quest2IdSheriff03` |
| `pathSettlerInfrastructure` | 43 | 18 | `Id`, `PathSettlerHubId00`, `PathSettlerHubId01`, `LocalizedTextIdObjective`, `MissionCount` |
| `liveEventDisplayItem` | 41 | 4 | `Id`, `LiveEventId`, `Item2Id`, `StoreLinkId` |
| `chatChannel` | 39 | 10 | `Id`, `EnumName`, `UniversalCommand00`, `UniversalCommand01`, `LocalizedTextIdName` |
| `bugSubcategory` | 38 | 3 | `Id`, `BugCategoryId`, `LocalizedTextId` |
| `pathExplorerDoor` | 38 | 4 | `Id`, `WorldZoneIdInsideMicro`, `TargetGroupIdActivate`, `TargetGroupIdKill` |
| `attributeMilestoneGroup` | 36 | 11 | `Id`, `RequiredAttributeAmount00`, `RequiredAttributeAmount01`, `RequiredAttributeAmount02`, `RequiredAttributeAmount03` |
| `attributeMiniMilestoneGroup` | 36 | 136 | `Id`, `RequiredAttributeAmount00`, `RequiredAttributeAmount01`, `RequiredAttributeAmount02`, `RequiredAttributeAmount03` |
| `classSecondaryStatBonus` | 36 | 7 | `Id`, `UnitProperty2IdSecondaryStat00`, `UnitProperty2IdSecondaryStat01`, `UnitProperty2IdSecondaryStat02`, `Modifier00` |
| `item2Family` | 36 | 6 | `Id`, `LocalizedTextId`, `Flags`, `SoundEventIdEquip`, `VendorMultiplier` |
| `publicEventDepot` | 36 | 3 | `Id`, `Creature2Id`, `Item2Id` |
| `rewardRotationContent` | 35 | 2 | `Id`, `ContentTypeEnum` |
| `rewardProperty` | 34 | 3 | `Id`, `LocalizedTextId`, `RewardModifierValueTypeEnum` |
| `componentRegion` | 32 | 3 | `Id`, `EnumName`, `ComponentMap` |
| `rewardTrack` | 32 | 19 | `Id`, `RewardTrackTypeEnum`, `PrerequisiteId`, `LocalizedTextId`, `LocalizedTextIdSummary` |
| `creature2ArcheType` | 31 | 3 | `Id`, `Icon`, `UnitPropertyMultiplier` |
| `characterCreationPreset` | 30 | 5 | `Id`, `RaceId`, `Faction2Id`, `Gender`, `StringPreset` |
| `guildPermission` | 30 | 7 | `Id`, `LocalizedTextIdName`, `LocalizedTextIdDescription`, `LuaVariable`, `LocalizedTextIdCommand` |
| `modelSequenceBySeatPosture` | 30 | 9 | `Id`, `ModelSequenceId`, `ModelSequenceIdNarrow`, `ModelSequenceIdMedium`, `ModelSequenceIdWide` |
| `vital` | 29 | 2 | `Id`, `LocalizedTextIdDisplayText` |
| `cCStates` | 28 | 9 | `Id`, `Flags`, `DefaultBreakProbability`, `LocalizedTextIdName`, `SpellIcon` |
| `zoneCompletion` | 28 | 10 | `Id`, `MapZoneId`, `ZoneCompletionFactionEnum`, `EpisodeQuestCount`, `TaskQuestCount` |
| `characterCustomizationLabel` | 27 | 4 | `Id`, `LocalizedTextId`, `Faction2Id`, `DisplayIndex` |
| `creature2Tier` | 27 | 2 | `Id`, `UnitPropertyMultiplier` |
| `housingPlotType` | 27 | 2 | `Id`, `MaxPlacedDecor` |
| `pathExplorerPowerMap` | 27 | 7 | `Id`, `DistanceThreshold`, `CollectQuantity`, `VictoryPauseMS`, `WorldLocation2IdVisual` |
| `guildPerk` | 25 | 12 | `Id`, `LocalizedTextIdTitle`, `LocalizedTextIdDescription`, `LuaSprite`, `LuaName` |
| `levelUpUnlockType` | 25 | 2 | `Id`, `LocalizedTextId` |
| `modelSequenceTransition` | 25 | 4 | `Id`, `ModelSequenceIdFrom`, `ModelSequenceIdTo`, `ModelSequenceIdTransition` |
| `creature2Difficulty` | 24 | 7 | `Id`, `LocalizedTextIdTitle`, `PathScientistScanMultiplier`, `ClusterContributionValueDifficulty`, `RankValue` |
| `customizationParameter` | 24 | 11 | `Id`, `LocalizedTextId`, `SclX`, `SclY`, `SclZ` |
| `publicEventCustomStat` | 24 | 6 | `Id`, `PublicEventTypeEnum`, `PublicEventId`, `StatIndex`, `LocalizedTextIdStatName` |
| `soundParameter` | 24 | 2 | `Id`, `Hash` |
| `housingResidenceInfo` | 23 | 13 | `Id`, `HousingDecorInfoIdDefaultRoof`, `HousingDecorInfoIdDefaultEntryway`, `HousingDecorInfoIdDefaultDoor`, `HousingWallpaperInfoIdDefault` |
| `itemProficiency` | 23 | 3 | `Id`, `BitMask`, `LocalizedTextIdString` |
| `questGroup` | 23 | 2 | `Id`, `LocalizedTextId` |
| `materialType` | 22 | 2 | `Id`, `MaterialFlags` |
| `pathExplorerActivate` | 22 | 4 | `Id`, `Creature2Id`, `TargetGroupId`, `Count` |
| `skyTrackCloudSet` | 22 | 38 | `Id`, `Count`, `MinSize00`, `MinSize01`, `MinSize02` |
| `cinematicRace` | 21 | 5 | `Id`, `CinematicId`, `RaceId`, `MaleAssetPath`, `FemaleAssetPath` |
| `spell4EffectGroupList` | 21 | 33 | `Id`, `Spell4EffectGroupId00`, `Spell4EffectGroupId01`, `Spell4EffectGroupId02`, `Spell4EffectGroupId03` |
| `ticketSubCategory` | 21 | 3 | `Id`, `TicketCategoryId`, `LocalizedTextId` |
| `characterTitleCategory` | 20 | 2 | `Id`, `LocalizedTextId` |
| `rewardRotationEssence` | 20 | 4 | `Id`, `AccountCurrencyTypeId`, `MinPlayerLevel`, `WorldDifficultyFlags` |
| `storeLink` | 20 | 5 | `Id`, `EnumName`, `CategoryData`, `CategoryDataPTR`, `AccountItemId` |
| `combatReward` | 19 | 6 | `Id`, `CombatRewardTypeEnum`, `LocalizedTextIdCombatFloater`, `LocalizedTextIdCombatLogMessage`, `VisualEffectIdVisual00` |
| `characterCreationArmorSet` | 18 | 15 | `Id`, `CreationGearSetEnum`, `ClassId`, `ItemDisplayId00`, `ItemDisplayId01` |
| `spell4ValidTargets` | 18 | 2 | `Id`, `TargetBitmask` |
| `accountCurrencyType` | 17 | 4 | `Id`, `LocalizedTextId`, `IconName`, `AccountItemId` |
| `pathScientistDatacubeDiscovery` | 17 | 2 | `Id`, `WorldZoneId` |
| `pathScientistSpecimenSurvey` | 17 | 41 | `Id`, `LocalizedTextIdObjective00`, `LocalizedTextIdObjective01`, `LocalizedTextIdObjective02`, `LocalizedTextIdObjective03` |
| `tradeskillMaterialCategory` | 17 | 2 | `Id`, `LocalizedTextIdName` |
| `worldWaterType` | 17 | 5 | `Id`, `WorldWaterFogId`, `SurfaceType`, `ParticleFile`, `SoundDirectionalAmbienceId` |
| `cCStateDiminishingReturns` | 16 | 2 | `Id`, `LocalizedTextIdName` |
| `colorShift` | 16 | 4 | `Id`, `TexturePath`, `LocalizedTextId`, `PreviewSwatchIcon` |
| `fullScreenEffect` | 16 | 14 | `Id`, `Description`, `TexturePath`, `ModelPath`, `Priority` |
| `rewardRotationModifier` | 16 | 6 | `Id`, `RewardPropertyId`, `RewardPropertyData`, `Value`, `MinPlayerLevel` |
| `waterSurfaceEffect` | 16 | 8 | `Id`, `EmissionDelay`, `WorldWaterWakeIdStillWater0`, `WorldWaterWakeIdStillWater1`, `VisualEffectIdParticle0` |
| `matchingRandomReward` | 15 | 13 | `Id`, `MatchTypeEnum`, `Item2Id`, `ItemCount`, `CurrencyTypeId` |
| `itemRandomStatGroup` | 14 | 2 | `Id`, `LocalizedTextIdName` |
| `currencyType` | 13 | 5 | `Id`, `Description`, `LocalizedTextId`, `IconName`, `CapAmount` |
| `pathScientistExperimentation` | 13 | 2 | `Id`, `NumAttempts` |
| `publicEventTeam` | 13 | 2 | `Id`, `LocalizedTextIdName` |
| `tradeskill` | 13 | 11 | `Id`, `LocalizedTextIdName`, `LocalizedTextIdDescription`, `Flags`, `TutorialId` |
| `tradeskillProficiency` | 13 | 2 | `Id`, `ProficiencyFlagEnum` |
| `wind` | 13 | 15 | `Id`, `Type`, `Duration`, `RadiusEnd`, `Direction` |
| `actionSlotPrereq` | 12 | 3 | `Id`, `SlotIndex`, `PrerequisiteIdUnlock` |
| `archiveCategory` | 12 | 2 | `Id`, `LocalizedTextId` |
| `customerSurvey` | 12 | 6 | `Id`, `CustomerSurveyTypeEnum`, `LocalizedTextIdOverrideTitle`, `LocalizedTextIdQuestion00`, `LocalizedTextIdQuestion01` |
| `materialSet` | 12 | 1 | `Id` |
| `spell4CCConditions` | 12 | 3 | `Id`, `CcStateMask`, `CcStateFlagsRequired` |
| `spell4HitResults` | 12 | 2 | `Id`, `Flags` |
| `worldWaterFog` | 12 | 10 | `Id`, `FogStart`, `FogEnd`, `FogStartUW`, `FogEndUW` |
| `pathScientistFieldStudy` | 11 | 28 | `Id`, `Creature2Id`, `TargetGroupId`, `PathScientistFieldStudyFlags`, `LocalizedTextIdChecklist00` |
| `publicEventVirtualItemDepot` | 11 | 8 | `Id`, `Creature2Id`, `VirtualItemId00`, `VirtualItemId01`, `VirtualItemId02` |
| `spell4Prerequisites` | 11 | 2 | `Id`, `Flags` |
| `spell4Tag` | 11 | 3 | `Id`, `Flags`, `LocalizedTextIdName` |
| `spell4TargetAngle` | 11 | 2 | `Id`, `TargetAngle` |
| `windSpawn` | 11 | 5 | `Id`, `IntervalMin`, `IntervalMax`, `DirectionMin`, `DirectionMax` |
| `archiveLink` | 10 | 4 | `Id`, `ArchiveArticleIdParent`, `ArchiveArticleIdChild`, `ArchiveLinkFlags` |
| `bugCategory` | 10 | 2 | `Id`, `LocalizedTextId` |
| `housingBuild` | 10 | 22 | `Id`, `Description`, `AssetPath`, `ConstructionEffectsId`, `BuildPreDelayTimeMS` |
| `housingWarplotBossToken` | 10 | 4 | `Id`, `Spell4IdSummon`, `MinimumUpgradeTierEnum`, `HousingPlugItemIdLinked` |
| `publicEventStatDisplay` | 10 | 4 | `Id`, `PublicEventTypeEnum`, `PublicEventId`, `Flags` |
| `pvPRatingFloor` | 10 | 5 | `Id`, `Flags`, `PvpRatingTypeEnum`, `FloorValue`, `LocalizedTextIdLabel` |
| `realmDataCenter` | 10 | 14 | `Id`, `Flags`, `DeploymentRegionEnum`, `DeploymentTypeEnum`, `LocalizedTextId` |
| `worldWaterWake` | 10 | 18 | `Id`, `Flags`, `ColorTexture`, `NormalTexture`, `DistortionTexture` |
| `achievementGroup` | 9 | 3 | `Id`, `LocalizedTextId`, `TradeSkillId` |
| `inputActionCategory` | 9 | 2 | `Id`, `LocalizedTextId` |
| `levelDifferentialAttribute` | 9 | 4 | `Id`, `LocalizedTextIdDescription`, `LevelDifferentialValue`, `QuestXpMultiplier` |
| `spell4TierRequirements` | 9 | 3 | `Id`, `TierIndex`, `LevelRequirement` |
| `achievementSubGroup` | 8 | 3 | `Id`, `LocalizedTextId`, `Tier` |
| `pathScientistScanBotProfile` | 8 | 17 | `Id`, `LocalizedTextId`, `Creature2Id`, `ScanTimeMS`, `ProcessingTimeMS` |
| `race` | 8 | 31 | `Id`, `EnumName`, `LocalizedTextId`, `LocalizedTextIdNameFemale`, `MaleAssetPath` |
| `targetMarker` | 8 | 3 | `Id`, `VisualEffectId`, `IconPath` |
| `distanceDamageModifier` | 7 | 11 | `Id`, `DistancePercent00`, `DistancePercent01`, `DistancePercent02`, `DistancePercent03` |
| `housingMapInfo` | 7 | 4 | `Id`, `WorldId`, `PrivatePropertyCount`, `PublicPropertyCount` |
| `itemQuality` | 7 | 13 | `Id`, `SalvageCritChance`, `TurninMultiplier`, `RuneCostMultiplier`, `DyeCostMultiplier` |
| `skyCloudSet` | 7 | 8 | `Id`, `Density`, `SkyTrackCloudSetId00`, `SkyTrackCloudSetId01`, `SkyTrackCloudSetId02` |
| `tutorialLayout` | 7 | 3 | `Id`, `Form`, `Flags` |
| `class` | 6 | 55 | `Id`, `EnumName`, `LocalizedTextId`, `LocalizedTextIdNameFemale`, `Mechanic` |
| `eldanAugmentationCategory` | 6 | 8 | `Id`, `EldanAugmentationCategoryIdTier2Category00`, `EldanAugmentationCategoryIdTier2Category01`, `Tier2CostAmount00`, `Tier2CostAmount01` |
| `emoteSequenceTransition` | 6 | 5 | `Id`, `EmotesIdTo`, `StandStateFrom`, `EmotesIdFrom`, `ModelSequenceId` |
| `housingResource` | 6 | 2 | `Id`, `LocalizedTextIdName` |
| `pathSoldierTowerDefense` | 6 | 9 | `Id`, `PathSoldierEventId`, `BuildCost`, `LocalizedTextIdName`, `WorldLocation2IdDisplay` |
| `publicEventObjectiveBombDeployment` | 6 | 3 | `Id`, `Creature2IdBomb`, `Spell4IdCarrying` |
| `publicEventRewardModifier` | 6 | 5 | `Id`, `PublicEventId`, `RewardPropertyId`, `Data`, `Offset` |
| `quest2Difficulty` | 6 | 4 | `Id`, `XpMultiplier`, `CashRewardMultiplier`, `RepRewardMultiplier` |
| `rewardRotationItem` | 6 | 7 | `Id`, `RewardItemTypeEnum`, `RewardItemObject`, `Count`, `IconPath` |
| `spell4Runner` | 6 | 7 | `Id`, `SpriteName`, `RedTint`, `GreenTint`, `BlueTint` |
| `spell4ServiceTokenCost` | 6 | 3 | `Id`, `Spell4Id`, `ServiceTokenCost` |
| `binkMovie` | 5 | 3 | `Id`, `BinkMovieAssetPath`, `Flags` |
| `ticketCategory` | 5 | 2 | `Id`, `LocalizedTextId` |
| `creature2Resist` | 4 | 4 | `Id`, `ResistPhysicalMultiplier`, `ResistTechMultiplier`, `ResistMagicMultiplier` |
| `housingContributionType` | 4 | 3 | `Id`, `Description`, `EnumName` |
| `housingDecorLimitCategory` | 4 | 2 | `Id`, `DecorLimit` |
| `language` | 4 | 4 | `Id`, `LanguageTag`, `ClientLanguageTag`, `SoundAvailabilityIndexFemale` |
| `playerNotificationType` | 4 | 3 | `Id`, `Priority`, `LifetimeMs` |
| `publicEventObjectiveGatherResource` | 4 | 8 | `Id`, `PublicEventObjectiveGatherResourceEnumFlag`, `Creature2IdContainer`, `Creature2IdResource`, `Spell4IdResource` |
| `redacted` | 4 | 4 | `Id`, `IdString`, `LocalizedTextIdName`, `MtxCategoryIdParent` |
| `accountItemCooldownGroup` | 3 | 1 | `Id` |
| `housingMannequinPose` | 3 | 4 | `Id`, `EnumName`, `LocalizedTextId`, `ModelSequenceId` |
| `modelSkinFX` | 3 | 2 | `Id`, `Suffix` |
| `soundDirectionalAmbience` | 3 | 3 | `Id`, `SoundEventIdOutsideStart`, `SoundEventIdOutsideStop` |
| `genericMap` | 2 | 2 | `Id`, `MapZoneId` |
| `soundEnvironment` | 2 | 2 | `Id`, `Hash` |
| `tradeskillCatalystOrdering` | 2 | 6 | `Id`, `UnlockLevel00`, `UnlockLevel01`, `UnlockLevel02`, `UnlockLevel03` |
| `costumeSpecies` | 1 | 3 | `Id`, `ComponentLayoutId`, `EnumName` |
| `matchTypeRewardRotationContent` | 1 | 4 | `Id`, `MatchTypeEnum`, `RewardRotationContentIdRandomNormal`, `RewardRotationContentIdRandomVeteran` |
| `publicEventObjectiveState` | 1 | 17 | `Id`, `LocalizedTextIdState00`, `LocalizedTextIdState01`, `LocalizedTextIdState02`, `LocalizedTextIdState03` |
| `soundCombatLoop` | 1 | 4 | `Id`, `SoundEventIdStart`, `SoundEventIdStop`, `SoundParameterIdUnitsInCombat` |
| `worldWaterEnvironment` | 1 | 2 | `Id`, `LandMapPath` |
