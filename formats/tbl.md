# `.tbl` — 384 files

Measured across **every .tbl file in the client**, not sampled from one.

| | |
|---|---|
| files | 384 |
| total decompressed | 227.0 MB |
| smallest / median / largest | 192 / 6,033 / 42,963,648 bytes |

## Magic

- `LBTD` — 384 files (100.0%)

## Header words

What each 32-bit slot at the head of the file *does across the population*. A field
that never varies is a magic or version; one that tracks file size is a count,
length or offset. **These are measurements, not a struct definition.**

| offset | behaviour | evidence |
|---|---|---|
| +0 | **constant** | always 0x4454424c (1146372684) = 'LBTD' |
| +4 | **constant** | always 0x00000000 (0) |
| +8 | **varies** | 30 distinct, range 5..36 |
| +12 | **constant** | always 0x00000000 (0) |
| +16 | **constant** | always 0x00000000 (0) |
| +20 | **constant** | always 0x00000000 (0) |
| +24 | **varies** | 56 distinct, range 4..824 |
| +28 | **constant** | always 0x00000000 (0) |
| +32 | **varies** | 53 distinct, range 1..206 |
| +36 | **constant** | always 0x00000000 (0) |
| +40 | **small set** | 5 distinct, max 80: 32(x183), 48(x141), 64(x42), 16(x15), 80(x3) |
| +44 | **constant** | always 0x00000000 (0) |
| +48 | **varies** | 252 distinct, range 0..539251 |
| +52 | **constant** | always 0x00000000 (0) |
| +56 | **tracks size** | r=0.999 with file size over 384 files |
| +60 | **constant** | always 0x00000000 (0) |
| +64 | **varies** | 116 distinct, range 0..18064 |
| +68 | **constant** | always 0x00000000 (0) |
| +72 | **varies** | 269 distinct, range 0..771980 |
| +76 | **constant** | always 0x00000000 (0) |
| +80 | **tracks size** | r=0.999 with file size over 384 files |
| +84 | **constant** | always 0x00000000 (0) |
| +88 | **constant** | always 0x00000000 (0) |
| +92 | **constant** | always 0x00000000 (0) |

## Four-character codes found in the body

Uppercase 4-byte sequences, which in this client's formats are usually section tags.

| code | occurrences |
|---|---|
| `LBTD` | 384 |
| `BGDE` | 2 |
| `APBE` | 1 |
| `HBX9` | 1 |
| `BAKX` | 1 |
| `BI2D` | 1 |
| `KQS2` | 1 |
| `R1CD` | 1 |
| `D4L6` | 1 |
| `CKKC` | 1 |
| `HBV2` | 1 |
| `HBZ2` | 1 |
| `HBLP` | 1 |
| `HBPP` | 1 |
| `PCHH` | 1 |
| `PCHM` | 1 |
| `E6BJ` | 1 |
| `A8BR` | 1 |
| `OMCW` | 1 |
| `B4EB` | 1 |

## Strings it references

34 distinct strings of 5+ characters. The most common name what this format
points at.

| string | files |
|---|---|
| `F\_pE` | 1 |
| `AffPA` | 1 |
| `oEo\z` | 1 |
| `wD3Dc` | 1 |
| `.D33p` | 1 |
| `oC.6s` | 1 |
| `wbnC6` | 1 |
| `Bk.0A` | 1 |
| `CKKCC` | 1 |
| `C-kRC` | 1 |
| `CHgSC` | 1 |
| `6EaDy` | 1 |
| `vYEE/Fu` | 1 |
| `9EpNv` | 1 |
| `WBHD-` | 1 |
| `HTBvt.` | 1 |
| `CTOqB` | 1 |
| `PBt_L` | 1 |
| `RBeQJ` | 1 |
| `YBAlL` | 1 |
| `BnGuB` | 1 |
| `ASz/C` | 1 |
| `\AH34` | 1 |
| `\AH54` | 1 |
| `PCGY8` | 1 |

## Examples

- `DB/Creature2Resist.tbl` — 496 bytes
- `DB/Creature2Tier.tbl` — 39,616 bytes
- `DB/CreatureLevel.tbl` — 48,609 bytes
- `DB/CurrencyType.tbl` — 2,512 bytes
- `DB/CustomerSurvey.tbl` — 945 bytes
- `DB/CustomizationParameter.tbl` — 1,777 bytes
- `DB/CustomizationParameterMap.tbl` — 16,368 bytes
- `DB/DailyLoginReward.tbl` — 9,936 bytes
