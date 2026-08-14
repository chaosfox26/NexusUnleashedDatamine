# The Apollo API, read from the client binary

One file per namespace, extracted from `D:\CDN\Install\Client64\WildStar64.exe` — the
client the game actually runs. Not from any external reference; the community docs are
missing roughly 30%% of the surface and were wrong in the place it mattered (they omit
`GetTenacity`, `GetToughness` and `GetHope`, which the live character sheet displays).

Produced by `python Tools/split-client-api.py`.

## How a method gets filed here

The binary stores each Lua method name as a string, and the registration tables put a
namespace's methods next to its name — but **in both directions**: `AbilityBook` precedes
its methods, `QuestLib` follows them. So runs of method names are cut out and the two
bounding namespace names compete for each run, with the community reference breaking
the tie.

That is a claim about layout, so it is **measured**: each file is published only if the
reference corroborates at least **70%%** of what was extracted. `GameLib` scores 100%%
(203/203), `Quest` 98.6%%, `Unit` 94.6%%.

27 namespaces fell below the bar and are listed in [UNATTRIBUTED.md](UNATTRIBUTED.md)
rather than published. **An unplaced method is not a missing method** — every name is
still in `docs/reference-data/apollo-api-client.tsv`.

| namespace | methods | not in the community reference |
|---|---|---|
| [Unit](Unit.md) | 258 | **14** |
| [GameLib](GameLib.md) | 203 | — |
| [Quest](Quest.md) | 74 | **1** |
| [Guild](Guild.md) | 65 | **14** |
| [PathMission](PathMission.md) | 51 | **1** |
| [PublicEventObjective](PublicEventObjective.md) | 41 | **11** |
| [GroupLib](GroupLib.md) | 40 | **3** |
| [Residence](Residence.md) | 36 | **2** |
| [PublicEvent](PublicEvent.md) | 32 | **5** |
| [FriendshipLib](FriendshipLib.md) | 30 | — |
| [Decor](Decor.md) | 28 | **7** |
| [Achievement](Achievement.md) | 27 | — |
| [MarketplaceLib](MarketplaceLib.md) | 24 | **1** |
| [AbilityBook](AbilityBook.md) | 23 | **2** |
| [Challenges](Challenges.md) | 19 | — |
| [HousingPlot](HousingPlot.md) | 19 | — |
| [DatacubeLib](DatacubeLib.md) | 17 | — |
| [Episode](Episode.md) | 17 | **1** |
| [SoldierEvent](SoldierEvent.md) | 17 | — |
| [GalacticArchiveArticle](GalacticArchiveArticle.md) | 16 | — |
| [GalacticArchiveEntry](GalacticArchiveEntry.md) | 16 | **3** |
| [AchievementsLib](AchievementsLib.md) | 13 | **1** |
| [MailSystemLib](MailSystemLib.md) | 13 | — |
| [ChatChannel](ChatChannel.md) | 12 | **1** |
| [CommodityOrder](CommodityOrder.md) | 12 | — |
| [CostumesLib](CostumesLib.md) | 12 | **3** |
| [AlienFxLib](AlienFxLib.md) | 11 | **1** |
| [ChallengesLib](ChallengesLib.md) | 11 | — |
| [ChatChannelLib](ChatChannelLib.md) | 11 | — |
| [Contract](Contract.md) | 10 | — |
| [SettlerImprovement](SettlerImprovement.md) | 10 | **2** |
| [Costume](Costume.md) | 9 | — |
| [IncidentReportLib](IncidentReportLib.md) | 9 | — |
| [ItemAuction](ItemAuction.md) | 9 | — |
| [P2PTrading](P2PTrading.md) | 9 | **1** |
| [PathEpisode](PathEpisode.md) | 8 | **1** |
| [PetFlair](PetFlair.md) | 8 | — |
| [QuestHub](QuestHub.md) | 8 | **2** |
| [CREDDExchangeOrder](CREDDExchangeOrder.md) | 7 | — |
| [CombatFloater](CombatFloater.md) | 7 | — |
| [GenericMapNode](GenericMapNode.md) | 7 | **1** |
| [PetCustomization](PetCustomization.md) | 7 | — |
| [SoldierImprovement](SoldierImprovement.md) | 6 | — |
| [CSIsLib](CSIsLib.md) | 5 | — |
| [CommunicatorLib](CommunicatorLib.md) | 5 | — |
| [DialogResponse](DialogResponse.md) | 5 | — |
| [HexGroups](HexGroups.md) | 5 | — |
| [ApolloColor](ApolloColor.md) | 4 | **1** |
| [LiveEventsLib](LiveEventsLib.md) | 4 | **1** |
| [QuestCategory](QuestCategory.md) | 4 | — |
