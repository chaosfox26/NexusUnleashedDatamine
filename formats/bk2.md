# `.bk2` — 19 files

Measured across **every .bk2 file in the client**, not sampled from one.

| | |
|---|---|
| files | 19 |
| total decompressed | 961.7 MB |
| smallest / median / largest | 1,095,120 / 8,692,560 / 177,787,240 bytes |

## Magic

- `KB2i` — 19 files (100.0%)

## Header words

What each 32-bit slot at the head of the file *does across the population*. A field
that never varies is a magic or version; one that tracks file size is a count,
length or offset. **These are measurements, not a struct definition.**

| offset | behaviour | evidence |
|---|---|---|
| +0 | **constant** | always 0x6932424b (1764901451) = 'KB2i' |
| +4 | **tracks size** | r=1.000 with file size over 19 files |
| +8 | **tracks size** | r=0.987 with file size over 19 files |
| +12 | **near-unique** | 19 distinct across 19 files - id or hash |
| +16 | **tracks size** | r=0.987 with file size over 19 files |
| +20 | **varies** | 2 distinct, range 720..1920 |
| +24 | **varies** | 2 distinct, range 405..1080 |
| +28 | **constant** | always 0x0000001e (30) |
| +32 | **constant** | always 0x00000001 (1) |
| +36 | **constant** | always 0x00000010 (16) |
| +40 | **small set** | 3 distinct, max 3: 0(x10), 1(x6), 3(x3) |
| +44 | **constant** | always 0x02040100 (33816832) |
| +48 | **varies** | 10 distinct, range 1997..145920 |
| +52 | **varies** | 11 distinct, range 3121..1879096192 |
| +56 | **varies** | 11 distinct, range 0..145920 |
| +60 | **varies** | 15 distinct, range 397..1879096192 |
| +64 | **varies** | 17 distinct, range 5605..1879096192 |
| +68 | **varies** | 17 distinct, range 7845..1879096192 |
| +72 | **varies** | 17 distinct, range 0..69289 |
| +76 | **varies** | 17 distinct, range 1..88209 |
| +80 | **varies** | 17 distinct, range 2..108721 |
| +84 | **near-unique** | 19 distinct across 19 files - id or hash |
| +88 | **near-unique** | 19 distinct across 19 files - id or hash |
| +92 | **near-unique** | 19 distinct across 19 files - id or hash |

## Four-character codes found in the body

Uppercase 4-byte sequences, which in this client's formats are usually section tags.

| code | occurrences |
|---|---|
| `SSSS` | 442 |
| `MMMM` | 124 |
| `LMMM` | 6 |
| `PPPP` | 6 |
| `PSSS` | 4 |
| `JJJJ` | 4 |
| `RR2R` | 3 |
| `PTPX` | 3 |
| `HRLF` | 3 |
| `PRJR` | 3 |
| `RFFD` | 3 |
| `BLJ2` | 3 |
| `AS0H` | 3 |
| `WDRH` | 3 |
| `AABM` | 3 |
| `RCEQ` | 3 |
| `BVY7` | 3 |
| `GFB5` | 3 |
| `HMKB` | 3 |
| `J1N4` | 3 |

## Strings it references

356 distinct strings of 5+ characters. The most common name what this format
points at.

| string | files |
|---|---|
| `5555555555555555555555555555555555555555555555555555555555555555` | 12 |
| `5555555555555555555555` | 3 |
| `pMMMMMMMMMMMMMMMMMMM` | 3 |
| `We545` | 2 |
| `aDeiE` | 2 |
| `qgBrsJ` | 2 |
| `iajjjjj` | 2 |
| `5a0Umi` | 2 |
| `5UH8w` | 2 |
| `KLMMMMM` | 2 |
| `m7SgZ` | 2 |
| `RSSSSSSSSSSSSSSSSSSSx` | 2 |
| `F242MS` | 2 |
| `q7q71` | 2 |
| `-20d\N` | 2 |
| `f42zD` | 2 |
| `UBKkBVY7` | 2 |
| `YAsdSb` | 2 |
| `1a40I` | 2 |
| `808hP` | 2 |
| `Mddjr` | 2 |
| `8jJI0` | 2 |
| `bb2B2` | 1 |
| `-q\4d` | 1 |
| `k-mQk` | 1 |

## Examples

- `Art/Cinematics/Zones/Launch/StoryTrailer.bk2` — 169,669,088 bytes
- `Art/Cinematics/Zones/Launch/StoryTrailer.bk2` — 169,664,388 bytes
- `Art/Cinematics/Zones/Launch/StoryTrailer.bk2` — 169,674,680 bytes
- `Art/Cinematics/Zones/CHSelect/CHSelect_Path_EXPLORER.bk2` — 8,265,712 bytes
- `Art/Cinematics/Zones/CHSelect/CHSelect_Path_SCIENTIST.bk2` — 10,380,648 bytes
- `Art/Cinematics/Zones/CHSelect/CHSelect_Path_SETTLER.bk2` — 9,703,980 bytes
- `Art/Cinematics/Zones/CHSelect/CHSelect_Path_SOLIDER.bk2` — 8,245,172 bytes
- `Art/Cinematics/Zones/CHSelect/CHSelect_class_eng.bk2` — 8,097,748 bytes
