# `.area` — 11651 files

Measured across **every .area file in the client**, not sampled from one.

| | |
|---|---|
| files | 11651 |
| total decompressed | 12885.6 MB |
| smallest / median / largest | 40 / 350,016 / 25,711,374 bytes |

## Magic

- `aera` — 11627 files (99.8%)
- `AERA` — 24 files (0.2%)

## Header words

What each 32-bit slot at the head of the file *does across the population*. A field
that never varies is a magic or version; one that tracks file size is a count,
length or offset. **These are measurements, not a struct definition.**

| offset | behaviour | evidence |
|---|---|---|
| +0 | **varies** | 2 distinct, range 1095910721..1634887009 |
| +4 | **constant** | always 0x00000000 (0) |
| +8 | **constant** | always 0x43484e4b (1128812107) = 'KNHC' |
| +12 | **tracks size** | r=1.000 with file size over 11651 files |
| +16 | **varies** | 1996 distinct, range 5..4278197838 |
| +20 | **varies** | 392 distinct, range 0..3519388792 |
| +24 | **varies** | 2508 distinct, range 0..4294967295 |
| +28 | **varies** | 2361 distinct, range 0..4294967295 |
| +32 | **varies** | 2841 distinct, range 0..4294967040 |
| +36 | **varies** | 2579 distinct, range 0..4294967295 |
| +40 | **varies** | 2468 distinct, range 0..4294967295 |
| +44 | **varies** | 2415 distinct, range 0..4294967295 |
| +48 | **varies** | 2476 distinct, range 0..4294967295 |
| +52 | **varies** | 2731 distinct, range 0..4294967295 |
| +56 | **varies** | 2588 distinct, range 0..4294967295 |
| +60 | **varies** | 2831 distinct, range 0..4294967295 |
| +64 | **varies** | 2450 distinct, range 0..4294967295 |
| +68 | **varies** | 2430 distinct, range 0..4294967295 |
| +72 | **varies** | 2735 distinct, range 0..4294967295 |
| +76 | **varies** | 2465 distinct, range 0..4294967295 |
| +80 | **varies** | 2498 distinct, range 0..4294967295 |
| +84 | **varies** | 2490 distinct, range 0..4294967295 |
| +88 | **varies** | 2506 distinct, range 0..4294967295 |
| +92 | **varies** | 2645 distinct, range 0..4294967295 |

## Four-character codes found in the body

Uppercase 4-byte sequences, which in this client's formats are usually section tags.

| code | occurrences |
|---|---|
| `PORP` | 88,255 |
| `K0K0` | 35,004 |
| `PPPP` | 25,827 |
| `TUUU` | 25,639 |
| `UUUT` | 23,325 |
| `TTTT` | 16,516 |
| `WWWW` | 12,387 |
| `DDDD` | 12,134 |
| `HHHH` | 12,057 |
| `KNHC` | 9,386 |
| `T8T8` | 9,301 |
| `G5G5` | 7,486 |
| `UUEE` | 7,460 |
| `PTUU` | 7,024 |
| `TTUU` | 6,965 |
| `UUTT` | 6,956 |
| `PUUU` | 6,250 |
| `UUTP` | 6,203 |
| `IJIJ` | 6,139 |
| `UUUP` | 5,702 |

## Strings it references

57,079 distinct strings of 5+ characters. The most common name what this format
points at.

| string | files |
|---|---|
| `ffvvffvv` | 1,839 |
| `wwwwwwww` | 1,335 |
| `33333333` | 1,249 |
| `VVeeVVee` | 1,101 |
| `UUEEUUEE` | 1,004 |
| `DDDDDDDD` | 719 |
| `o4o4o4o4o4o4o4o4o4o4o4o4o4o4o4o4o4o4o4o4o4o4o4o4o4o4o4o4o4o4o4o4` | 653 |
| `0000000000000000000000000000000000000000000000000000000000000000` | 527 |
| `mCmCmCmCmCmCmCmCmCmCmCmCmCmCmCmCmCmCmCmCmCmCmCmCmCmCmCmCmCmCmCmC` | 416 |
| `DUTUDeTd` | 411 |
| `0K0K0K0K0K0K0K0K0K0K0K0K0K0K0K0K0K0K0K0K0K0K0K0K0K0K0K0K0K0K0K0K` | 375 |
| `TTVVww` | 362 |
| `3UBT3UBT` | 349 |
| `wwUU33` | 346 |
| `y5i5y5i5` | 278 |
| `WWWWPORP` | 263 |
| `sTUUU` | 259 |
| `PORP0` | 220 |
| `HHHHHHHHHHHH` | 217 |
| `UUUPORP` | 205 |
| `xxwwff` | 199 |
| `3U3U3U3U` | 176 |
| `PORP4` | 175 |
| `TvTvTvTv` | 169 |
| `sPPPP` | 163 |

## Examples

- `Map/1x1HousingGamblingInterior/1x1HousingGamblingInterior.3f3f.area` — 5,416 bytes
- `Map/1x1HousingGamblingInterior/1x1HousingGamblingInterior.3f40.area` — 5,416 bytes
- `Map/1x1HousingGamblingInterior/1x1HousingGamblingInterior.403f.area` — 5,416 bytes
- `Map/1x1HousingGamblingInterior/1x1HousingGamblingInterior.4040.area` — 5,781 bytes
- `Map/AcceleratedOmniplasmLab/AcceleratedOmniplasmLab.3f3f.area` — 937,708 bytes
- `Map/AcceleratedOmniplasmLab/AcceleratedOmniplasmLab.3f40.area` — 1,002,942 bytes
- `Map/AcceleratedOmniplasmLab/AcceleratedOmniplasmLab.3f41.area` — 5,416 bytes
- `Map/AcceleratedOmniplasmLab/AcceleratedOmniplasmLab.403f.area` — 1,090,278 bytes
