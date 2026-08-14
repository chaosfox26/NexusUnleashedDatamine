# `.lua` — 203 files

Measured across **every .lua file in the client**, not sampled from one.

| | |
|---|---|
| files | 203 |
| total decompressed | 5.9 MB |
| smallest / median / largest | 967 / 18,335 / 204,715 bytes |

## Magic

- `----` — 181 files (89.2%)
- `requ` — 12 files (5.9%)
- `-- C` — 5 files (2.5%)
- `0d0a0d0a` — 2 files (1.0%)
- `loca` — 1 files (0.5%)
- `-- U` — 1 files (0.5%)
- `2d2d0d0a` — 1 files (0.5%)

## Header words

What each 32-bit slot at the head of the file *does across the population*. A field
that never varies is a magic or version; one that tracks file size is a count,
length or offset. **These are measurements, not a struct definition.**

| offset | behaviour | evidence |
|---|---|---|
| +0 | **varies** | 7 distinct, range 168626701..1970365810 |
| +4 | **varies** | 7 distinct, range 543519337..1950949484 |
| +8 | **varies** | 11 distinct, range 224490860..1970020468 |
| +12 | **varies** | 11 distinct, range 539831562..2003788910 |
| +16 | **varies** | 10 distinct, range 218762530..1953524082 |
| +20 | **varies** | 10 distinct, range 543518313..1953524082 |
| +24 | **varies** | 15 distinct, range 220357225..2065710368 |
| +28 | **varies** | 17 distinct, range 168649077..1967347822 |
| +32 | **varies** | 18 distinct, range 168626701..1970105711 |
| +36 | **varies** | 17 distinct, range 151653673..1970365810 |
| +40 | **varies** | 16 distinct, range 168632951..2003788910 |
| +44 | **varies** | 18 distinct, range 220357225..1970365810 |
| +48 | **varies** | 21 distinct, range 220357225..1952670066 |
| +52 | **varies** | 20 distinct, range 168626701..1935961701 |
| +56 | **varies** | 20 distinct, range 168626701..2105221181 |
| +60 | **varies** | 19 distinct, range 168626701..2003788910 |
| +64 | **varies** | 19 distinct, range 168626701..1968385325 |
| +68 | **varies** | 19 distinct, range 168632946..2065710368 |
| +72 | **varies** | 19 distinct, range 218762530..1970365810 |
| +76 | **varies** | 18 distinct, range 168632943..1920234272 |
| +80 | **varies** | 17 distinct, range 220360556..1970497338 |
| +84 | **varies** | 17 distinct, range 168632930..2064256317 |
| +88 | **varies** | 19 distinct, range 151653673..1970365810 |
| +92 | **varies** | 19 distinct, range 168626701..2003788910 |

## Four-character codes found in the body

Uppercase 4-byte sequences, which in this client's formats are usually section tags.

| code | occurrences |
|---|---|
| `TODO` | 287 |
| `CRED` | 253 |
| `HUDA` | 102 |
| `P2PT` | 94 |
| `NCCB` | 66 |
| `GOTC` | 52 |
| `TEMP` | 47 |
| `CTFM` | 33 |
| `AMPP` | 32 |
| `NPCB` | 28 |
| `CTFF` | 28 |
| `HUDI` | 26 |
| `LASS` | 24 |
| `HTLT` | 23 |
| `UIMT` | 22 |
| `AMPS` | 21 |
| `FFFF` | 19 |
| `HACK` | 18 |
| `CODB` | 18 |
| `PVPT` | 17 |

## Strings it references

2,479 distinct strings of 5+ characters. The most common name what this format
points at.

| string | files |
|---|---|
| `require` | 980 |
| `local` | 845 |
| `----------------------------------------------------------------` | 581 |
| `-------------------------------` | 506 |
| `function` | 395 |
| `Apollo.GetString` | 198 |
| `Window` | 189 |
| `Client` | 186 |
| `return` | 186 |
| `Copyright` | 181 |
| `Script` | 180 |
| `NCsoft.` | 180 |
| `rights` | 180 |
| `reserved` | 180 |
| `self.xmlDoc` | 139 |
| `setmetatable` | 122 |
| `self.__index` | 119 |
| `GameLib` | 104 |
| `Apollo.RegisterAddon` | 90 |
| `Apollo.RegisterEventHandler` | 82 |
| `OnDocumentReady` | 77 |
| `OnLoad` | 73 |
| `-----------------------------------` | 69 |
| `ApolloColor.new` | 67 |
| `XmlDoc.CreateFromFile` | 56 |

## Examples

- `UI/Abilities/AbilitiesBuilder.lua` — 45,616 bytes
- `UI/AbilityAMPs/AbilityAMPs.lua` — 35,567 bytes
- `UI/AbilityVendor/AbilityVendor.lua` — 9,026 bytes
- `UI/AccountInventory/AccountInventory.lua` — 9,503 bytes
- `UI/Achievements/Achievements.lua` — 45,306 bytes
- `UI/ActionBarFrame/ActionBarFrame.lua` — 25,438 bytes
- `UI/ActionBarShortcut/ActionBarShortcut.lua` — 18,005 bytes
- `UI/AdventureClueTracker/AdventureClueTracker.lua` — 3,944 bytes
