# The client's UI source, indexed

191 Lua scripts recovered from the CDN mirror (`docs/client-extract/lua/`). Names come from
each file's own header comment — the store has no filenames.

`requires` is the client's own dependency declaration; `events` are the Apollo events each
script listens for. Both are read from the source, not inferred.

| script | chars | requires | events |
|---|---|---|---|
| [Abilities](../client-extract/lua/ee71e6143602-Client-Lua-Script-for-Abilities.lua) | 44538 | AbilityBook, ActionSetLib, Spell, Tooltip, Window | 39 |
| [AbilityAMPs](../client-extract/lua/14da7e1d5f05-Client-Lua-Script-for-AbilityAMPs.lua) | 34768 | AbilityBook, Window | 9 |
| [AbilityVendor](../client-extract/lua/5c281cb1a475-Client-Lua-Script-for-AbilityVendor.lua) | 8772 | AbilityBook, GameLib, Item, Money, Sound, Spell, Tooltip, Window | 5 |
| [AccountInventory](../client-extract/lua/1f68bda0a7f1-Client-Lua-Script-for-AccountInventory.lua) | 9288 | AccountItemLib, CREDDExchangeLib, FriendshipLib, Window | 10 |
| [AccountInventory](../client-extract/lua/fb1981881224-Client-Lua-Script-for-AccountInventory.lua) | 57149 | AccountItemLib, CREDDExchangeLib, FriendshipLib, Item, Window | 9 |
| [AccountServices](../client-extract/lua/0d3708bd06b4-Client-Lua-Script-for-AccountServices.lua) | 45167 | AccountItemLib, Apollo, CharacterScreenLib, Money, PreGameLib, Window | 14 |
| [Achievements](../client-extract/lua/3cf713cfb868-Client-Lua-Script-for-Achievements.lua) | 44292 | Achievement, AchievementsLib, Apollo, PlayerPathLib, Window | 5 |
| [ActionBarFrame](../client-extract/lua/73a99d171fe4-Client-Lua-Script-for-ActionBarFrame.lua) | 24733 | AbilityBook, ActionSetLib, Apollo, CollectiblesLib, GameLib, Item, Spell, Tooltip | 16 |
| [ActionBarShortcut](../client-extract/lua/acca14b8b739-Client-Lua-Script-for-ActionBarShortcut.lua) | 17497 | ActionSetLib, Unit, Window | 2 |
| [AdventureLevianBay](../client-extract/lua/eaeb6afcb83e-Client-Lua-Script-for-AdventureLevianBay.lua) | 7687 | Window | 5 |
| [AdventureWhitevale](../client-extract/lua/0cc1662cb3f7-Client-Lua-Script-for-AdventureWhitevale.lua) | 7678 | Window | 4 |
| [AlienFx](../client-extract/lua/32899bcea07b-Client-Lua-Script-for-AlienFx.lua) | 1236 | AlienFxLib | 0 |
| [Arena-Team](../client-extract/lua/d9929b1a309d-Client-Lua-Script-for-Arena-Team.lua) | 21228 | GameLib, GroupLib, GuildLib, GuildTypeLib, Window | 9 |
| [Arena-Team-Registr](../client-extract/lua/92630b6ac297-Client-Lua-Script-for-Arena-Team-Registr.lua) | 9499 | GameLib, GuildLib, Unit, Window | 5 |
| [BankViewer](../client-extract/lua/d9d819b34ee0-Client-Lua-Script-for-BankViewer.lua) | 11437 | AccountItemLib, Apollo, Money, StorefrontLib, Window | 9 |
| [BuildMap](../client-extract/lua/80f3cdd9e4aa-Client-Lua-Script-for-BuildMap.lua) | 21191 | Apollo, DialogSys, GameLib, MailSystemLib, PlayerPathLib, Quest, SettlerImprovement, SoldierImprovement | 10 |
| [CSI](../client-extract/lua/12eb0cfc86db-Client-Lua-Script-for-CSI.lua) | 34469 | CSIsLib, GameLib, Unit, Window | 8 |
| [Carbind.lua](../client-extract/lua/d38c58616f43-Client-Lua-Script-for-Carbind.lua.lua) | 8242 | ApolloTimer | 0 |
| [CastBar](../client-extract/lua/d852bcf0c4a5-Client-Lua-Script-for-CastBar.lua) | 12627 | GameLib, Sound, Spell, Window | 3 |
| [ChallengeDisplay](../client-extract/lua/f3c8012daff6-Client-Lua-Script-for-ChallengeDisplay.lua) | 21762 | Challenges, ChallengesLib, GameLib, PlayerPathLib, Window | 12 |
| [ChallengeLog](../client-extract/lua/1b3a033140f9-Client-Lua-Script-for-ChallengeLog.lua) | 75912 | AccountItemLib, ChallengesLib, GameLib, RewardTrackLib, Window | 18 |
| [ChallengeLog](../client-extract/lua/262960445afa-Client-Lua-Script-for-ChallengeLog.lua) | 38900 | CommDialog, DialogResponse, DialogSys, Quest, Window | 6 |
| [ChallengeLog](../client-extract/lua/5f79b3544e75-Client-Lua-Script-for-ChallengeLog.lua) | 49099 | GameLib, PathMission, PlayerPathLib, Tooltip, Window, XmlDoc | 12 |
| [ChallengeLog](../client-extract/lua/70a706dbc3ef-Client-Lua-Script-for-ChallengeLog.lua) | 18135 | AbilityBook, Apollo, DialogSys, GameLib, MailSystemLib, PathMission, PlayerPathLib, Quest | 6 |
| [ChallengeLog](../client-extract/lua/d8f9a1346a4e-Client-Lua-Script-for-ChallengeLog.lua) | 23229 | AbilityBook, Apollo, DialogSys, GameLib, MailSystemLib, PathMission, PlayerPathLib, Quest | 13 |
| [ChallengeLog](../client-extract/lua/e735569c3b12-Client-Lua-Script-for-ChallengeLog.lua) | 7645 | DialogResponse, DialogSys, GameLib, Quest, Window | 3 |
| [ChallengeLog](../client-extract/lua/ed541b61bd7b-Client-Lua-Script-for-ChallengeLog.lua) | 79574 | AbilityBook, Apollo, DialogSys, GameLib, MailSystemLib, PathMission, PlayerPathLib, Quest | 29 |
| [ChallengeTracker](../client-extract/lua/ace5d42fe544-Client-Lua-Script-for-ChallengeTracker.lua) | 31849 | Challenges, ChallengesLib, GameLib, Window | 20 |
| [Character](../client-extract/lua/1fdd7b949083-Client-Lua-Script-for-Character.lua) | 82675 | AccountItemLib, Apollo, CharacterTitle, CostumesLib, GameLib, GuildLib, Item, PlayerPathLib | 42 |
| [CharacterCustomiza](../client-extract/lua/df3ab5dad79d-Client-Lua-Script-for-CharacterCustomiza.lua) | 39187 | GameLib, StorefrontLib, Window | 6 |
| [CharacterSelect](../client-extract/lua/621a09e33742-Client-Lua-Script-for-CharacterSelect.lua) | 50440 | AccountItemLib, AlienFxLib, Apollo, CharacterScreenLib, PreGameLib, StorefrontLib, Window | 13 |
| [ChatLog](../client-extract/lua/9ede5030ec14-Client-Lua-Script-for-ChatLog.lua) | 112845 | AccountItemLib, Apollo, ChatChannelLib, ChatSystemLib, CombatFloater, DatacubeLib, FriendshipLib, GameLib | 36 |
| [CircleRegistration](../client-extract/lua/99a0112beeb6-Client-Lua-Script-for-CircleRegistration.lua) | 13427 | Window | 2 |
| [Circles](../client-extract/lua/a6746919ed22-Client-Lua-Script-for-Circles.lua) | 39890 | Apollo, ChatChannelLib, ChatSystemLib, GuildLib, GuildTypeLib, Window | 10 |
| [ClassResources](../client-extract/lua/e4399f90286b-Client-Lua-Script-for-ClassResources.lua) | 42405 | Window | 8 |
| [Client-Lua-Script](../client-extract/lua/9988653bbdd1-Client-Lua-Script.lua) | 61343 | AccountItemLib, GameLib, Item, Money, Sound, Window, math, string | 14 |
| [Client-Lua-Script-for](../client-extract/lua/b71fb2f6472a-Client-Lua-Script-for.lua) | 7066 | Window | 1 |
| [Client-lua-script](../client-extract/lua/04e2218a1a75-Client-lua-script.lua) | 21937 | Apollo, CommunicatorLib, DialogSys, GameLib, MailSystemLib, PlayerPathLib, Quest, Sound | 15 |
| [Client-lua-script](../client-extract/lua/15498df0222e-Client-lua-script.lua) | 14680 | QuestLib, Window | 8 |
| [Client-lua-script](../client-extract/lua/2d781c40cf57-Client-lua-script.lua) | 1218 | DialogSys, Quest, Unit, Window | 0 |
| [Client-lua-script](../client-extract/lua/86ab7d68053c-Client-lua-script.lua) | 12200 | FriendshipLib, Window | 5 |
| [Client-lua-script](../client-extract/lua/acd7f1723292-Client-lua-script.lua) | 8407 | Apollo, Window | 1 |
| [Client-lua-script](../client-extract/lua/f3e60f3cf52a-Client-lua-script.lua) | 22145 | Apollo, CommDialog, CommunicatorLib, DialogSys, GameLib, MailSystemLib, PlayerPathLib, Quest | 7 |
| [ClueTracker](../client-extract/lua/6db764aa8eb1-Client-Lua-Script-for-ClueTracker.lua) | 3821 | GameLib, Window | 4 |
| [Collectables](../client-extract/lua/957239cfbb8c-Client-Lua-Script-for-Collectables.lua) | 7183 | Window | 9 |
| [CombatFloaterConfig.lua](../client-extract/lua/558b635346b8-CombatFloaterConfig.lua.lua) | 88097 | CombatFloaters, GenericDialog, Window | 1 |
| [CombatLog](../client-extract/lua/e68c21799ebe-Client-Lua-Script-for-CombatLog.lua) | 79376 | Apollo, ChatChannelLib, ChatSystemLib, CombatFloater, GameLib, GroupLib, Spell, Unit | 41 |
| [Communities](../client-extract/lua/2dc9b0a92658-Client-Lua-Script-for-Communities.lua) | 38056 | Apollo, ChatChannelLib, ChatSystemLib, GuildLib, GuildTypeLib, Window | 10 |
| [CommunityRegistrat](../client-extract/lua/54627d29f8d1-Client-Lua-Script-for-CommunityRegistrat.lua) | 13327 | StorefrontLib, Window | 6 |
| [ContextMenuItem](../client-extract/lua/9ead20c693d6-Client-Lua-Script-for-ContextMenuItem.lua) | 5935 | ChatSystemLib, FriendshipLib, GameLib, GroupLib, Window | 6 |
| [ContextMenuPlayer](../client-extract/lua/a2844aaf2848-Client-Lua-Script-for-ContextMenuPlayer.lua) | 44072 | AccountItemLib, ChatSystemLib, FriendshipLib, GameLib, GroupLib, HousingLib, MatchingGameLib, Window | 10 |
| [Contracts](../client-extract/lua/4b708561e510-Client-Lua-Script-for-Contracts.lua) | 58839 | Contract, ContractsLib, GameLib, Quest, RewardTrack, RewardTrackLib, Window | 11 |
| [Costumes](../client-extract/lua/598cc3894697-Client-Lua-Script-for-Costumes.lua) | 72923 | Apollo, Costume, CostumesLib, GameLib, HousingLib, Item, StorefrontLib | 24 |
| [Crafting](../client-extract/lua/861728c0ecd4-Client-Lua-Script-for-Crafting.lua) | 45111 | CraftingLib, Window | 15 |
| [CraftingGrid](../client-extract/lua/1b2bd36c961e-Client-Lua-Script-for-CraftingGrid.lua) | 51777 | AccountItemLib, CraftingLib, Window | 15 |
| [CraftingResume](../client-extract/lua/e5088cd07bb1-Client-Lua-Script-for-CraftingResume.lua) | 7361 | Window | 5 |
| [CraftingSummaryScr](../client-extract/lua/6a6456a49fe5-Client-Lua-Script-for-CraftingSummaryScr.lua) | 14659 | CraftingLib, Window | 9 |
| [Credits](../client-extract/lua/79efa04c30b8-Client-Lua-Script-for-Credits.lua) | 8181 | Window | 3 |
| [CrowdControlGamepl](../client-extract/lua/3b2df54ac6de-Client-Lua-Script-for-CrowdControlGamepl.lua) | 6188 | GameLib, Unit, Window | 4 |
| [CustomerSurvey](../client-extract/lua/08a462de63e5-Client-Lua-Script-for-CustomerSurvey.lua) | 6962 | CustomerSurveyLib, CustomerSurveyTypeLib, Window | 2 |
| [Death](../client-extract/lua/da8ecc498f70-Client-Lua-Script-for-Death.lua) | 19472 | AccountItemLib, GameLib, MatchingGameLib, Tooltip, Window, XmlDoc | 12 |
| [DecorPreview](../client-extract/lua/7b0356e0f331-Client-Lua-Script-for-DecorPreview.lua) | 3695 | HousingLib, Window | 2 |
| [ExitWindow](../client-extract/lua/dee225626d36-Client-Lua-Script-for-ExitWindow.lua) | 14495 | GameLib, Window | 5 |
| [FloatTextPanel](../client-extract/lua/19fec399661c-Client-Lua-Script-for-FloatTextPanel.lua) | 51159 | CombatFloater, GameLib, Spell, Unit, Window | 26 |
| [FloatTextPanel](../client-extract/lua/46a9a517dbb3-Client-Lua-Script-for-FloatTextPanel.lua) | 36083 | Apollo, Challenges, ChallengesLib, CombatFloater, CommunicatorLib, DialogSys, GameLib, MailSystemLib | 20 |
| [FriendsList](../client-extract/lua/34d47ec0f86d-Client-Lua-Script-for-FriendsList.lua) | 95899 | ChatSystemLib, FriendshipLib, GameLib, PlayerPathLib, Unit, Window, math, string | 25 |
| [FriendsList](../client-extract/lua/e383642afe9e-Client-Lua-Script-for-FriendsList.lua) | 22202 | ChatSystemLib, FriendshipLib, HousingLib, PlayerPathLib, Unit, Window, math, string | 10 |
| [Gacha](../client-extract/lua/5a12c8ca3d8a-Client-Lua-Script-for-Gacha.lua) | 13319 | AccountItemLib, Apollo, FortunesLib, Item, StorefrontLib, Tooltip, Window | 14 |
| [GalacticArchive](../client-extract/lua/8a66c701588c-Client-Lua-Script-for-GalacticArchive.lua) | 29663 | ApolloTimer, GalacticArchiveArticle, GalacticArchiveEntry, Window | 6 |
| [GroupDisplayOption](../client-extract/lua/206730bf9426-Client-Lua-Script-for-GroupDisplayOption.lua) | 69132 | ChatSystemLib, GameLib, GroupLib, PlayerPathLib, Tooltip, Unit, Window | 26 |
| [GroupDisplayOption](../client-extract/lua/f1135fafb764-Client-Lua-Script-for-GroupDisplayOption.lua) | 14710 | GroupLib, Window | 3 |
| [GuildAlerts](../client-extract/lua/3bdfc01b7e71-Client-Lua-Script-for-GuildAlerts.lua) | 26251 | ChatChannelLib, ChatSystemLib, GuildLib, GuildTypeLib, Window | 3 |
| [GuildBank](../client-extract/lua/7492f977526a-Client-Lua-Script-for-GuildBank.lua) | 56895 | AccountItemLib, Money, Window | 15 |
| [GuildDesigner](../client-extract/lua/53f3add660ea-Client-Lua-Script-for-GuildDesigner.lua) | 17606 | Apollo, ChallengesLib, CommunicatorLib, DialogSys, Episode, GameLib, GroupLib, Money | 6 |
| [GuildInfo](../client-extract/lua/ddca5df923ed-Client-Lua-Script-for-GuildInfo.lua) | 19212 | Apollo, ChatChannelLib, ChatSystemLib, GuildLib, GuildTypeLib, Window | 10 |
| [GuildMain](../client-extract/lua/8c69a291380b-Client-Lua-Script-for-GuildMain.lua) | 8282 | GameLib, Window | 6 |
| [GuildPerks](../client-extract/lua/dca790145c1a-Client-Lua-Script-for-GuildPerks.lua) | 39280 | AchievementsLib, Apollo, ChatChannelLib, ChatSystemLib, GameLib, GuildLib, GuildTypeLib, Window | 6 |
| [GuildRegistration](../client-extract/lua/7af6ba1f0e7c-Client-Lua-Script-for-GuildRegistration.lua) | 25133 | Apollo, ChallengesLib, CommunicatorLib, DialogSys, Episode, GameLib, GroupLib, GuildLib | 6 |
| [GuildRoster](../client-extract/lua/379c8213a780-Client-Lua-Script-for-GuildRoster.lua) | 35151 | Apollo, ChatChannelLib, ChatSystemLib, GameLib, GuildLib, GuildTypeLib, Window | 7 |
| [HUDAlerts](../client-extract/lua/86de675a322c-Client-Lua-Script-for-HUDAlerts.lua) | 20656 | Apollo, CommunicatorLib, DatacubeLib, GameLib, PathEpisode, QuestLib, Window | 17 |
| [HUDInteract](../client-extract/lua/291027e48c27-Client-Lua-Script-for-HUDInteract.lua) | 8838 | Window | 14 |
| [HousingAlerts](../client-extract/lua/24019a713a30-Client-Lua-Script-for-HousingAlerts.lua) | 9153 | ChatChannelLib, ChatSystemLib, HousingLib, Window | 2 |
| [HousingDatachron](../client-extract/lua/a20c40e80d40-Client-Lua-Script-for-HousingDatachron.lua) | 11104 | HousingLib, Window | 6 |
| [HousingDecorate](../client-extract/lua/2ef1518c91c9-Client-Lua-Script-for-HousingDecorate.lua) | 125434 | Decor, HousingLib, Residence, StorefrontLib, Window | 35 |
| [HousingLandscape](../client-extract/lua/eadc08e112b4-Client-Lua-Script-for-HousingLandscape.lua) | 95330 | GuildLib, HousingLib, HousingPlot, Window | 16 |
| [HousingList](../client-extract/lua/dd3ca1579afa-Client-Lua-Script-for-HousingList.lua) | 15403 | Decor, HousingLib, Residence, Window | 13 |
| [HousingRemodel](../client-extract/lua/21c177829e6f-Client-Lua-Script-for-HousingRemodel.lua) | 126828 | HousingLib, Residence, Window | 27 |
| [InstanceSettings](../client-extract/lua/25489e576693-Client-Lua-Script-for-InstanceSettings.lua) | 16864 | Window | 7 |
| [InterfaceMenuList](../client-extract/lua/622727a236a8-Client-Lua-Script-for-InterfaceMenuList.lua) | 18741 | Apollo, GameLib, Window | 6 |
| [InventoryBag](../client-extract/lua/99e724837933-Client-Lua-Script-for-InventoryBag.lua) | 34380 | AccountItemLib, Apollo, GameLib, Item, Money, StorefrontLib, Window | 30 |
| [ItemPreview](../client-extract/lua/7f471599e0c5-Client-Lua-Script-for-ItemPreview.lua) | 4407 | GameLib, Item, Window | 1 |
| [ItemWindowSubclass-new](../client-extract/lua/87d4f71c7925-ItemWindowSubclass-new.lua) | 4311 | — | 0 |
| [Keybind](../client-extract/lua/717beec9a660-Client-Lua-Script-for-Keybind.lua) | 49451 | Apollo, GameLib, Window | 5 |
| [Leaderboards](../client-extract/lua/64d40fb9ac60-Client-Lua-Script-for-Leaderboards.lua) | 30481 | GameLib, LeaderboardLib, MatchMakingEntry, MatchMakingLib, PublicEvent, Window | 4 |
| [LevelUpUnlocks](../client-extract/lua/fc602a499f0f-Client-Lua-Script-for-LevelUpUnlocks.lua) | 26942 | Apollo, GameLib, Window | 7 |
| [LootNotifications](../client-extract/lua/8a32f772c4c8-Client-Lua-Script-for-LootNotifications.lua) | 7318 | GameLib, Sound, Window | 2 |
| [LootStack](../client-extract/lua/51cedb3e40e6-Client-Lua-Script-for-LootStack.lua) | 9027 | GameLib, Sound, Window | 2 |
| [LoreWindow](../client-extract/lua/4a7d550cb83b-Client-Lua-Script-for-LoreWindow.lua) | 30941 | DatacubeLib, GalacticArchiveArticle, Window | 9 |
| [MalgraveAdventureR](../client-extract/lua/aa29bd764c6e-Client-Lua-Script-for-MalgraveAdventureR.lua) | 8268 | Window | 6 |
| [MarketplaceAuction](../client-extract/lua/d700732b43a8-Client-Lua-Script-for-MarketplaceAuction.lua) | 77293 | AccountItemLib, GameLib, Item, ItemAuction, MarketplaceLib, Money, StorefrontLib, Unit | 16 |
| [MarketplaceCREDD](../client-extract/lua/f155066b6b68-Client-Lua-Script-for-MarketplaceCREDD.lua) | 27146 | AccountItemLib, CREDDExchangeLib, CREDDExchangeOrder, Window | 9 |
| [MarketplaceCommodi](../client-extract/lua/3ff06c5be49b-Client-Lua-Script-for-MarketplaceCommodi.lua) | 61568 | AccountItemLib, CommodityOrder, GameLib, MarketplaceLib, Money, StorefrontLib, Window | 10 |
| [MarketplaceListing](../client-extract/lua/97f9084b286a-Client-Lua-Script-for-MarketplaceListing.lua) | 31184 | AccountItemLib, CommodityOrder, MarketplaceLib, Money, StorefrontLib, Window | 21 |
| [MasterCraftsman](../client-extract/lua/10228cdc0ea2-Client-Lua-Script-for-MasterCraftsman.lua) | 8737 | Apollo, ApolloCursor, CraftingLib, GameLib, Item, Window | 3 |
| [Masterloot](../client-extract/lua/d22ca27f6a55-Client-Lua-Script-for-Masterloot.lua) | 15510 | Apollo, GameLib, GroupLib, Item, Window | 5 |
| [MatchMaker](../client-extract/lua/437350a27489-Client-Lua-Script-for-MatchMaker.lua) | 161419 | Achievement, AchievementsLib, ContentFinderLib, Episode, GameLib, GroupLib, GuildLib, GuildTypeLib | 38 |
| [MatchMaker](../client-extract/lua/623f20cceaf6-Client-Lua-Script-for-MatchMaker.lua) | 5090 | GameLib, GroupLib, MatchMakingEntry, MatchMakingLib, MatchingGameLib, Unit, Window | 5 |
| [MatchMaker](../client-extract/lua/f1ed9440db56-Client-Lua-Script-for-MatchMaker.lua) | 4394 | ChatSystemLib, GameLib, Unit, Window | 4 |
| [MatchTracker](../client-extract/lua/52dcd6cd21ca-Client-Lua-Script-for-MatchTracker.lua) | 33372 | MatchingGameLib, Window | 21 |
| [MicroStore](../client-extract/lua/0a643b25807c-Client-Lua-Script-for-MicroStore.lua) | 28251 | AccountItemLib, StorefrontLib, Window | 7 |
| [MiniMap](../client-extract/lua/83563db55c8e-Client-Lua-Script-for-MiniMap.lua) | 89226 | CraftingLib, DialogSys, FriendshipLib, GameLib, MailSystemLib, MatchMakingLib, PlayerPathLib, PublicEvent | 55 |
| [MountScreen](../client-extract/lua/7e6e4b1ed703-Client-Lua-Script-for-MountScreen.lua) | 19626 | CollectiblesLib, PetCustomization, PetCustomizationLib, PetFlair, Window | 7 |
| [Nameplates](../client-extract/lua/fcb4452399b6-Client-Lua-Script-for-Nameplates.lua) | 56258 | AccountItemLib, Apollo, ChallengesLib, CommunicatorLib, DialogSys, Episode, GameLib, GroupLib | 16 |
| [NeedVsGreed](../client-extract/lua/a84448380964-Client-Lua-Script-for-NeedVsGreed.lua) | 9906 | Sound, Window | 7 |
| [NonCombatSpellbook](../client-extract/lua/2f87c1ed4d51-Client-Lua-Script-for-NonCombatSpellbook.lua) | 11264 | AbilityBook, GameLib, PlayerPathLib, Spell, Window | 6 |
| [NorthernWildsAdv](../client-extract/lua/4ce3bec73d87-Client-Lua-Script-for-NorthernWildsAdv.lua) | 11227 | PublicEvent, Window | 13 |
| [ObjectiveTracker](../client-extract/lua/68ebbbb85c40-Client-Lua-Script-for-ObjectiveTracker.lua) | 15897 | GameLib, Window | 9 |
| [Options](../client-extract/lua/a16fc7de9162-Client-Lua-Script-for-Options.lua) | 110409 | AlienFxLib, Apollo, GenericDialog, Window | 4 |
| [OptionsInterface](../client-extract/lua/d8e5cd4d6bf8-Client-Lua-Script-for-OptionsInterface.lua) | 33322 | GameLib, PlayerPathLib, Window | 11 |
| [PathFrame](../client-extract/lua/ada3e326e2af-Client-Lua-Script-for-PathFrame.lua) | 9516 | AbilityBook, GameLib, PlayerPathLib, Tooltip, Unit, Window | 8 |
| [PathScientistCusto](../client-extract/lua/9a9d4d3f8120-Client-Lua-Script-for-PathScientistCusto.lua) | 18031 | PetCustomization, PetCustomizationLib, PetFlair, ScientistScanBotProfile, Window | 8 |
| [PathScientistExper](../client-extract/lua/a12790b45d5d-Client-Lua-Script-for-PathScientistExper.lua) | 12985 | PathMission, Window | 2 |
| [PathSoldierMission](../client-extract/lua/02cc6c55a29a-Client-Lua-Script-for-PathSoldierMission.lua) | 18263 | Apollo, DialogSys, GameLib, MailSystemLib, PathMission, PlayerPathLib, Quest, SoldierEvent | 9 |
| [PlugPreview](../client-extract/lua/9a17d6bdcb67-Client-Lua-Script-for-PlugPreview.lua) | 5511 | HousingLib, Window | 2 |
| [PopupText](../client-extract/lua/446bf3975e67-Client-Lua-Script-for-PopupText.lua) | 7363 | GameLib, PathMission, PlayerPathLib, Window | 3 |
| [PrimalMatrix](../client-extract/lua/5c28165cb69d-Client-Lua-Script-for-PrimalMatrix.lua) | 58687 | AccountItemLib, GameLib, Item, StorefrontLib, Unit, Window | 9 |
| [ProgressLog](../client-extract/lua/bafc53718dd1-Client-Lua-Script-for-ProgressLog.lua) | 7349 | GameLib, Window | 12 |
| [Protogames](../client-extract/lua/10670e245441-Client-Lua-Script-for-Protogames.lua) | 7196 | Apollo, GameLib, PublicEvent, Sound | 5 |
| [Protogames](../client-extract/lua/c1faf11a6fc4-Client-Lua-Script-for-Protogames.lua) | 7078 | Apollo, GameLib, PublicEvent, Sound | 4 |
| [PublicEventStats](../client-extract/lua/9e4bb3c40e46-Client-Lua-Script-for-PublicEventStats.lua) | 47206 | MatchingGameLib, PublicEvent, Window | 12 |
| [PublicEventVote](../client-extract/lua/4a3d9ec2fc1e-Client-Lua-Script-for-PublicEventVote.lua) | 8499 | PublicEvent, Window | 4 |
| [PvPKillBoard](../client-extract/lua/5329f2cce278-Client-Lua-Script-for-PvPKillBoard.lua) | 7197 | MatchingGameLib, Window | 3 |
| [QuestLog](../client-extract/lua/0016e7561dfb-Client-Lua-Script-for-QuestLog.lua) | 65021 | Episode, Money, Quest, QuestCategory, QuestLib, Unit, Window | 10 |
| [QuestTracker](../client-extract/lua/ec8c27e27875-Client-Lua-Script-for-QuestTracker.lua) | 32938 | Contract, ContractsLib, GameLib, Quest, Window | 7 |
| [QuestTracker](../client-extract/lua/fa2bd9755cad-Client-Lua-Script-for-QuestTracker.lua) | 41651 | ApolloTimer, GameLib, QuestLib, Window | 10 |
| [QuestTracker](../client-extract/lua/fb765521a66a-Client-Lua-Script-for-QuestTracker.lua) | 67865 | Episode, GameLib, Quest, QuestLib, Window | 22 |
| [RaidFrameBase](../client-extract/lua/fbb5391d6792-Client-Lua-Script-for-RaidFrameBase.lua) | 46239 | MatchMakingLib, Window | 17 |
| [RaidFrameLeaderOpt](../client-extract/lua/1d145f999bec-Client-Lua-Script-for-RaidFrameLeaderOpt.lua) | 10444 | Window | 2 |
| [RaidFrameMasterLoo](../client-extract/lua/3743e46cafe8-Client-Lua-Script-for-RaidFrameMasterLoo.lua) | 6646 | Window | 2 |
| [RaidFrameReady](../client-extract/lua/2a5ff7da96db-Client-Lua-Script-for-RaidFrameReady.lua) | 8511 | Window | 3 |
| [RealmBankViewer](../client-extract/lua/b17f5cc02327-Client-Lua-Script-for-RealmBankViewer.lua) | 10790 | AccountItemLib, Apollo, Money, StorefrontLib, Window | 8 |
| [RecallFrame](../client-extract/lua/3fc67b514929-Client-Lua-Script-for-RecallFrame.lua) | 13905 | GameLib, HousingLib, Unit, Window | 10 |
| [ReportPlayer](../client-extract/lua/ef4cbcfae430-Client-Lua-Script-for-ReportPlayer.lua) | 15312 | ChatSystemLib, FriendshipLib, GameLib, GroupLib, IncidentReportLib, MailSystemLib, MatchingGameLib, P2PTrading | 12 |
| [Reputation](../client-extract/lua/d0937f7f7b83-Client-Lua-Script-for-Reputation.lua) | 13053 | GameLib, Window | 3 |
| [ResourceConversion](../client-extract/lua/6bcbeb3bf94f-Client-Lua-Script-for-ResourceConversion.lua) | 14071 | GameLib, Tooltip, Unit, Window, XmlDoc | 5 |
| [RewardIcons](../client-extract/lua/1eb4d816e9e6-Client-Lua-Script-for-RewardIcons.lua) | 23149 | Window | 2 |
| [RuneSets](../client-extract/lua/a34b5f63b42c-Client-Lua-Script-for-RuneSets.lua) | 4673 | Window | 4 |
| [Runecrafting](../client-extract/lua/0c785fe7171e-Client-Lua-Script-for-Runecrafting.lua) | 50330 | CraftingLib, GameLib, Item, Window | 12 |
| [Sabotage](../client-extract/lua/ce353026cd0a-Client-Lua-Script-for-Sabotage.lua) | 9921 | Apollo, GameLib, MatchingGameLib, PublicEvent, Sound | 5 |
| [ServiceTokenConfir](../client-extract/lua/83846cffd1d1-Client-Lua-Script-for-ServiceTokenConfir.lua) | 7248 | AccountItemLib, GameLib, Sound, StorefrontLib, Window | 5 |
| [SocialPanel](../client-extract/lua/03dcdac556ab-Client-Lua-Script-for-SocialPanel.lua) | 18855 | FriendshipLib, StorefrontLib, Window | 25 |
| [SocialPanel](../client-extract/lua/a133e3dd3b5c-Client-Lua-Script-for-SocialPanel.lua) | 8593 | Apollo, ApolloCursor, GameLib, Item, Window | 3 |
| [SprintMeter](../client-extract/lua/a552798a2169-Client-Lua-Script-for-SprintMeter.lua) | 10023 | Apollo, ApolloTimer, GameLib, Window | 9 |
| [Storefront](../client-extract/lua/1cb96d4a496c-Client-Lua-Script-for-Storefront.lua) | 150178 | AccountItemLib, GameLib, Item, Money, PetCustomization, PetCustomizationLib, PetFlair, RewardTrack | 24 |
| [Storefront](../client-extract/lua/1dac0b002b02-Client-Lua-Script-for-Storefront.lua) | 10949 | AccountItemLib, StorefrontLib, Window | 3 |
| [Storefront](../client-extract/lua/a7afe3e2c326-Client-Lua-Script-for-Storefront.lua) | 31731 | AccountItemLib, GameLib, Item, Money, PetCustomizationLib, RewardTrack, RewardTrackLib, Sound | 5 |
| [Storefront](../client-extract/lua/a98c47244377-Client-Lua-Script-for-Storefront.lua) | 12726 | AccountItemLib, Money, Sound, StorefrontLib, Window, WindowLocation | 5 |
| [Storefront](../client-extract/lua/d47aa039ddbd-Client-Lua-Script-for-Storefront.lua) | 28606 | AccountItemLib, Money, Sound, StorefrontLib, Tooltip, Window, WindowLocation | 5 |
| [Storefront](../client-extract/lua/e14e19bce8c1-Client-Lua-Script-for-Storefront.lua) | 5099 | Money, StorefrontLib, Tooltip, Window, WindowLocation | 9 |
| [Stuck](../client-extract/lua/68c2f4bdb353-Client-Lua-Script-for-Stuck.lua) | 4459 | GameLib, HousingLib, Window | 1 |
| [SuggestedMenu](../client-extract/lua/756ef062907c-Client-Lua-Script-for-SuggestedMenu.lua) | 20116 | FriendshipLib, Window | 14 |
| [SuggestedTextBoxSubclass](../client-extract/lua/9e385b15d88c-SuggestedTextBoxSubclass.lua) | 5178 | — | 0 |
| [SupplySatchel](../client-extract/lua/ab88b8c522b2-Client-Lua-Script-for-SupplySatchel.lua) | 16549 | Window | 8 |
| [TaxiMap](../client-extract/lua/1af3e856cecb-Client-Lua-Script-for-TaxiMap.lua) | 35305 | GameLib, HexGroups, PlayerPathLib, Tooltip, Unit, Window, XmlDoc | 14 |
| [ToolTips](../client-extract/lua/950b06eedd13-Client-Lua-Script-for-ToolTips.lua) | 125802 | AccountItemLib, Apollo, ChallengesLib, FriendshipLib, GameLib, Item, PlayerPathLib, Unit | 4 |
| [TradeskillContaine](../client-extract/lua/ce331d3a4d8c-Client-Lua-Script-for-TradeskillContaine.lua) | 8543 | Window | 12 |
| [TradeskillSchemati](../client-extract/lua/5298bf61f912-Client-Lua-Script-for-TradeskillSchemati.lua) | 35759 | AchievementsLib, CraftingLib, Window | 5 |
| [TradeskillTalents](../client-extract/lua/f27887641c1e-Client-Lua-Script-for-TradeskillTalents.lua) | 9816 | Window | 2 |
| [TradeskillTrainer](../client-extract/lua/76e10ca38298-Client-Lua-Script-for-TradeskillTrainer.lua) | 9853 | Apollo, CraftingLib, Window, XmlDoc | 3 |
| [TradeskillTree](../client-extract/lua/649fc3c35f32-Client-Lua-Script-for-TradeskillTree.lua) | 26355 | AchievementsLib, CraftingLib, Window | 2 |
| [Trading](../client-extract/lua/3a4f792e2843-Client-Lua-Script-for-Trading.lua) | 19958 | AccountItemLib, Apollo, GameLib, P2PTrading, Unit, Window | 12 |
| [TutorialMenu](../client-extract/lua/00b99954f335-Client-Lua-Script-for-TutorialMenu.lua) | 19314 | GameLib, Window | 3 |
| [TutorialPrompts](../client-extract/lua/7fcec68eb96d-Client-Lua-Script-for-TutorialPrompts.lua) | 31369 | GameLib, Sound, Window | 8 |
| [Util.lua](../client-extract/lua/0665a56fea06-Util.lua.lua) | 4993 | — | 0 |
| [VanityPets](../client-extract/lua/8a95d9ffc4ce-Client-Lua-Script-for-VanityPets.lua) | 11230 | CollectiblesLib, GameLib, StorefrontLib, Window | 6 |
| [Warparty](../client-extract/lua/d2c6f94300a9-Client-Lua-Script-for-Warparty.lua) | 38121 | GameLib, GroupLib, GuildLib, GuildTypeLib, Window | 12 |
| [Warparty-Boss-Toke](../client-extract/lua/394500ff509a-Client-Lua-Script-for-Warparty-Boss-Toke.lua) | 11565 | GameLib, GroupLib, GuildLib, GuildTypeLib, MatchingGameLib, Window | 7 |
| [Warparty-Registrat](../client-extract/lua/a2b0e1e14121-Client-Lua-Script-for-Warparty-Registrat.lua) | 9135 | GameLib, GuildLib, Unit, Window | 4 |
| [WarpartyBank](../client-extract/lua/2d9bf4db6c09-Client-Lua-Script-for-WarpartyBank.lua) | 28189 | Money, Window | 11 |
| [Warplots](../client-extract/lua/e1a8a5de0a77-Client-Lua-Script-for-Warplots.lua) | 7530 | Apollo, GameLib, MatchingGameLib, PublicEvent, Sound | 3 |
| [WelcomeWindow](../client-extract/lua/10497c839f40-Client-Lua-Script-for-WelcomeWindow.lua) | 17518 | AccountItemLib, Window | 8 |
| [WelcomeWindow](../client-extract/lua/2fcf6aae4d66-Client-Lua-Script-for-WelcomeWindow.lua) | 6207 | Window | 5 |
| [WelcomeWindow](../client-extract/lua/4e70d1f4a21e-Client-Lua-Script-for-WelcomeWindow.lua) | 20444 | GameLib, LiveEvent, LiveEventsLib, StorefrontLib, Window | 6 |
| [WelcomeWindow](../client-extract/lua/7c3b194f7674-Client-Lua-Script-for-WelcomeWindow.lua) | 16482 | ContentFinderLib, MatchMakingEntry, MatchMakingLib, QuestHub, Window | 7 |
| [WelcomeWindow](../client-extract/lua/af1f0179ac20-Client-Lua-Script-for-WelcomeWindow.lua) | 2282 | Window | 4 |
| [WelcomeWindow](../client-extract/lua/e7b4387ffb69-Client-Lua-Script-for-WelcomeWindow.lua) | 6167 | AccountItemLib, GameLib, Window | 10 |
| [Who](../client-extract/lua/9988cb691718-Client-Lua-Script-for-Who.lua) | 17585 | Apollo, ChatSystemLib, DialogSys, GameLib, PlayerPathLib, Tooltip, Window, XmlDoc | 16 |
| [XPBar](../client-extract/lua/3ce1cd1d4ac4-Client-Lua-Script-for-XPBar.lua) | 32117 | AccountItemLib, Apollo, GameLib, GroupLib, PlayerPathLib, Window | 20 |
| [ZoneCompletion](../client-extract/lua/363dc1da9437-Client-Lua-Script-for-ZoneCompletion.lua) | 12968 | Apollo, GameLib, PlayerPathLib, Window | 6 |
| [ZoneMap](../client-extract/lua/87e3ffd98f20-Client-Lua-Script-for-ZoneMap.lua) | 184452 | GameLib, HexGroups, PlayerPathLib, PublicEventsLib, QuestLib, Tooltip, Unit, Window | 95 |
| [assume-it-is-a-string](../client-extract/lua/a4156fb786f6-assume-it-is-a-string.lua) | 929 | — | 0 |
