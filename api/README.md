# The client's own API documentation

Recovered from `Documentation.xml`, shipped inside the game and pulled out of the CDN
mirror. This is Carbine's reference, not a community reconstruction.

| source | names | arguments | types | descriptions |
|---|---|---|---|---|
| community reference | partial | some | some | some |
| binary strings | **all** | no | no | no |
| the client's own Lua | used-only | **yes** | inferred | no |
| **this** | **all** | **yes** | **yes** | **yes** |

`Deprecated="true"` appears on entries that are demonstrably alive in 16042, so it
looks wholesale rather than per-entry. It is **reported and never used to filter**.

- `libraries/` — 46 files
- `objects/` — 65 files
- `window-controls/` — 36 files
- `ENUMS.md` — 234 sets
- `EVENTS.md` — 915 events

| document | calls | flagged deprecated |
|---|---|---|
| [Unit](objects/Unit.md) | 273 | 11 |
| [GameLib](libraries/GameLib.md) | 247 | 20 |
| [Item](objects/Item.md) | 181 | 96 |
| [Window](window-controls/Window.md) | 153 | 4 |
| [HousingLib](libraries/HousingLib.md) | 137 | 85 |
| [GuildTypeLib](objects/GuildTypeLib.md) | 90 | 2 |
| [Quest](objects/Quest.md) | 85 | 4 |
| [Guild](objects/Guild.md) | 77 | 77 |
| [ZoneMapWindow](window-controls/ZoneMapWindow.md) | 76 | — |
| [Apollo](libraries/Apollo.md) | 69 | 2 |
| [MatchingGame](objects/MatchingGame.md) | 65 | 5 |
| [PathMission](objects/PathMission.md) | 56 | 3 |
| [GroupLib](libraries/GroupLib.md) | 54 | — |
| [CraftingLib](libraries/CraftingLib.md) | 54 | 15 |
| [Spell](objects/Spell.md) | 49 | 4 |
| [Residence](objects/Residence.md) | 44 | — |
| [CostumeWindow](window-controls/CostumeWindow.md) | 43 | 1 |
| [FriendshipLib](objects/FriendshipLib.md) | 41 | — |
| [GridWindow](window-controls/GridWindow.md) | 40 | — |
| [PublicEventObjective](objects/PublicEventObjective.md) | 37 | 2 |
| [PublicEvent](objects/PublicEvent.md) | 35 | 2 |
| [Challenges](objects/Challenges.md) | 34 | 4 |
| [MarketplaceLib](libraries/MarketplaceLib.md) | 33 | 2 |
| [AaRect](objects/AaRect.md) | 33 | 9 |
| [MovieWindow](window-controls/MovieWindow.md) | 33 | 32 |
| [Decor](objects/Decor.md) | 32 | — |
| [Achievement](objects/Achievement.md) | 31 | 3 |
| [ChatChannelLib](objects/ChatChannelLib.md) | 30 | 29 |
| [PlayerPathLib](libraries/PlayerPathLib.md) | 29 | — |
| [Vector2](objects/Vector2.md) | 29 | 9 |
| [Vector3](objects/Vector3.md) | 29 | 9 |
| [ChatChannel](objects/ChatChannel.md) | 29 | 29 |
| [Quaternion](objects/Quaternion.md) | 28 | 9 |
| [BagWindow](window-controls/BagWindow.md) | 28 | — |
| [AccountItemLib](libraries/AccountItemLib.md) | 27 | 11 |
| [MailSystemLib](libraries/MailSystemLib.md) | 26 | — |
| [CharacterScreenLib](libraries/CharacterScreenLib.md) | 26 | 2 |
| [TreeControl](window-controls/TreeControl.md) | 26 | — |
| [ScreenModelActor](objects/ScreenModelActor.md) | 25 | 1 |
| [MiniMapWindow](window-controls/MiniMapWindow.md) | 25 | — |
| [AbilityBook](libraries/AbilityBook.md) | 24 | 1 |
| [Episode](objects/Episode.md) | 23 | 3 |
| [HousingPlot](objects/HousingPlot.md) | 23 | — |
| [GalacticArchiveArticle](objects/GalacticArchiveArticle.md) | 22 | 2 |
| [Money](objects/Money.md) | 21 | 1 |
| [SoldierEvent](objects/SoldierEvent.md) | 21 | 2 |
| [CommodityOrder](objects/CommodityOrder.md) | 21 | 4 |
| [ChallengesLib](libraries/ChallengesLib.md) | 19 | 7 |
| [GuildLib](libraries/GuildLib.md) | 19 | — |
| [EditBox](window-controls/EditBox.md) | 19 | 1 |
| [DatacubeLib](libraries/DatacubeLib.md) | 18 | — |
| [DemoSummary](libraries/DemoSummary.md) | 18 | — |
| [XmlDoc](objects/XmlDoc.md) | 18 | 1 |
| [RewardTrack](objects/RewardTrack.md) | 18 | — |
| [ProgressBar](window-controls/ProgressBar.md) | 18 | — |
| [PreGameLib](libraries/PreGameLib.md) | 17 | — |
| [ComboBox](window-controls/ComboBox.md) | 17 | — |
| [P2PTrading](libraries/P2PTrading.md) | 16 | — |
| [GalacticArchiveEntry](objects/GalacticArchiveEntry.md) | 16 | 2 |
| [LiveEvent](objects/LiveEvent.md) | 16 | 2 |
| [ItemAuction](objects/ItemAuction.md) | 15 | 4 |
| [BinkWindow](window-controls/BinkWindow.md) | 15 | — |
| [CColor](objects/CColor.md) | 14 | 9 |
| [ScientistScanBotProfile](objects/ScientistScanBotProfile.md) | 14 | 2 |
| [CREDDExchangeOrder](objects/CREDDExchangeOrder.md) | 14 | 2 |
| [Button](window-controls/Button.md) | 14 | — |
| [ModelWindow](window-controls/ModelWindow.md) | 14 | — |
| [CharacterTitle](objects/CharacterTitle.md) | 13 | 2 |
| [Contract](objects/Contract.md) | 13 | — |
| [Costume](objects/Costume.md) | 13 | — |
| [IconButton](window-controls/IconButton.md) | 13 | — |
| [AchievementsLib](libraries/AchievementsLib.md) | 12 | — |
| [CommunicatorLib](libraries/CommunicatorLib.md) | 12 | 1 |
| [SettlerImprovement](objects/SettlerImprovement.md) | 12 | 2 |
| [PetCustomization](objects/PetCustomization.md) | 12 | 2 |
| [CustomerSurveyTypeLib](objects/CustomerSurveyTypeLib.md) | 12 | 2 |
| [IncidentReportLib](objects/IncidentReportLib.md) | 12 | 2 |
| [StorefrontLib](libraries/StorefrontLib.md) | 11 | 8 |
| [PetFlair](objects/PetFlair.md) | 11 | 2 |
| [AlienFxLib](objects/AlienFxLib.md) | 11 | — |
| [CostumesLib](libraries/CostumesLib.md) | 10 | 1 |
| [PathEpisode](objects/PathEpisode.md) | 10 | 2 |
| [SoldierImprovement](objects/SoldierImprovement.md) | 10 | 2 |
| [ICComm](objects/ICComm.md) | 10 | — |
| [CashWindow](window-controls/CashWindow.md) | 10 | — |
| [GenericDialog](libraries/GenericDialog.md) | 9 | — |
| [ScreenModelManager](objects/ScreenModelManager.md) | 9 | 1 |
| [ApolloColor](objects/ApolloColor.md) | 9 | 3 |
| [DialogSys](objects/DialogSys.md) | 9 | — |
| [GenericMapNode](objects/GenericMapNode.md) | 9 | 1 |
| [ChatSystemLib](libraries/ChatSystemLib.md) | 8 | — |
| [CombatFloater](libraries/CombatFloater.md) | 8 | — |
| [MacrosLib](libraries/MacrosLib.md) | 8 | — |
| [CombatFloaters](libraries/CombatFloaters.md) | 8 | 8 |
| [DialogResponse](objects/DialogResponse.md) | 8 | 1 |
| [EulerAngles](objects/EulerAngles.md) | 8 | 3 |
| [Menu](objects/Menu.md) | 8 | 2 |
| [HexGroups](objects/HexGroups.md) | 8 | 2 |
| [MLWindow](window-controls/MLWindow.md) | 8 | — |
| [ActionBarButton](window-controls/ActionBarButton.md) | 8 | — |
| [ICCommLib](libraries/ICCommLib.md) | 7 | 7 |
| [CSIsLib](libraries/CSIsLib.md) | 7 | — |
| [QuestLib](libraries/QuestLib.md) | 7 | — |
| [WindowLocation](objects/WindowLocation.md) | 7 | — |
| [QuestCategory](objects/QuestCategory.md) | 7 | 2 |
| [ApolloTimer](objects/ApolloTimer.md) | 7 | 2 |
| [QuestHub](objects/QuestHub.md) | 7 | — |
| [ActionSetLib](libraries/ActionSetLib.md) | 6 | 3 |
| [Tooltip](libraries/Tooltip.md) | 6 | 2 |
| [RealmSelectScreenLib](libraries/RealmSelectScreenLib.md) | 6 | — |
| [Spinner](window-controls/Spinner.md) | 6 | — |
| [TabWindow](window-controls/TabWindow.md) | 6 | — |
| [AbilityItemWindow](window-controls/AbilityItemWindow.md) | 6 | — |
| [ProtostarMapWindow](window-controls/ProtostarMapWindow.md) | 6 | — |
| [WorldFixedWindow](window-controls/WorldFixedWindow.md) | 6 | — |
| [Time](objects/Time.md) | 5 | 3 |
| [ActorFixedWindow](window-controls/ActorFixedWindow.md) | 5 | — |
| [LiveEventsLib](libraries/LiveEventsLib.md) | 4 | — |
| [RewardTrackLib](libraries/RewardTrackLib.md) | 4 | — |
| [ApolloCursor](objects/ApolloCursor.md) | 4 | 1 |
| [CommDialog](objects/CommDialog.md) | 4 | — |
| [SliderBar](window-controls/SliderBar.md) | 4 | — |
| [PetCustomizationLib](libraries/PetCustomizationLib.md) | 3 | — |
| [CREDDExchangeLib](libraries/CREDDExchangeLib.md) | 3 | — |
| [ContractsLib](libraries/ContractsLib.md) | 3 | — |
| [CollectiblesLib](libraries/CollectiblesLib.md) | 3 | — |
| [RecruitmentGuildTypeLib](objects/RecruitmentGuildTypeLib.md) | 3 | — |
| [ItemSlotWindow](window-controls/ItemSlotWindow.md) | 3 | — |
| [SendEmailButton](window-controls/SendEmailButton.md) | 3 | — |
| [MessageManagerLib](libraries/MessageManagerLib.md) | 2 | — |
| [HazardsLib](libraries/HazardsLib.md) | 2 | — |
| [Sound](libraries/Sound.md) | 2 | — |
| [CustomerSurveyLib](libraries/CustomerSurveyLib.md) | 2 | — |
| [ContentFinderLib](libraries/ContentFinderLib.md) | 2 | — |
| [Sprite](objects/Sprite.md) | 2 | — |
| [IconListBox](window-controls/IconListBox.md) | 2 | — |
| [BuffWindow](window-controls/BuffWindow.md) | 2 | — |
| [TickerWnd](window-controls/TickerWnd.md) | 2 | — |
| [MannequinSlotWindow](window-controls/MannequinSlotWindow.md) | 2 | — |
| [ColorPicker](window-controls/ColorPicker.md) | 2 | — |
| [AttributeMilestonesLib](libraries/AttributeMilestonesLib.md) | 1 | — |
| [PublicEventsLib](libraries/PublicEventsLib.md) | 1 | — |
| [FortunesLib](libraries/FortunesLib.md) | 1 | — |
| [MenuBarWindow](window-controls/MenuBarWindow.md) | 1 | — |
| [DragDropFrame](window-controls/DragDropFrame.md) | 1 | — |
| [BuffContainerWindow](window-controls/BuffContainerWindow.md) | 1 | — |
| [ActionConfirmButton](window-controls/ActionConfirmButton.md) | 1 | — |
