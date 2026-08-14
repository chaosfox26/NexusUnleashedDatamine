# Namespaces this extraction could not place reliably

The client binary holds far more `Get*`/`Set*` strings than the Lua API — C++
internals and window-control methods among them. A run of method names with no
reference support gets assigned to whichever namespace name is nearest, which is
how `Apollo` collected 132 methods at 0%% agreement and `AaRect`, a geometry
class, collected 97.

These are listed rather than published as namespace files. **An unplaced method is
not a missing method** — it exists in the client, it simply has no trustworthy
owner yet. `docs/reference-data/apollo-api-client.tsv` still carries every name.

Threshold for publishing: **70%** agreement with the community reference.

| namespace | methods collected | agreement |
|---|---|---|
| `Spell` | 222 | 19.4% |
| `DialogSys` | 141 | 5.0% |
| `Apollo` | 132 | 0.0% |
| `CraftingLib` | 112 | 30.4% |
| `AaRect` | 97 | 0.0% |
| `RewardTrack` | 97 | 16.5% |
| `ICComm` | 96 | 9.4% |
| `XmlDoc` | 89 | 10.1% |
| `HousingLib` | 77 | 49.4% |
| `Menu` | 71 | 4.2% |
| `PlayerPathLib` | 58 | 32.8% |
| `Global` | 50 | 16.0% |
| `Money` | 39 | 38.5% |
| `Time` | 37 | 0.0% |
| `AccountItemLib` | 37 | 37.8% |
| `ScientistScanBotProfile` | 19 | 57.9% |
| `CharacterTitle` | 19 | 52.6% |
| `LiveEvent` | 18 | 44.4% |
| `ApolloTimer` | 15 | 6.7% |
| `QuestLib` | 15 | 46.7% |
| `CustomerSurveyTypeLib` | 12 | 66.7% |
| `MacrosLib` | 11 | 54.5% |
| `Sound` | 9 | 0.0% |
| `ContractsLib` | 5 | 60.0% |
| `Vector3` | 4 | 25.0% |
| `EulerAngles` | 4 | 0.0% |
| `Tooltip` | 4 | 25.0% |
