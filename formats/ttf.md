# `.ttf` — 11 files

Measured across **every .ttf file in the client**, not sampled from one.

| | |
|---|---|
| files | 11 |
| total decompressed | 2.6 MB |
| smallest / median / largest | 24,537 / 330,909 / 517,384 bytes |

## Magic

- `00010000` — 11 files (100.0%)

## Header words

What each 32-bit slot at the head of the file *does across the population*. A field
that never varies is a magic or version; one that tracks file size is a count,
length or offset. **These are measurements, not a struct definition.**

| offset | behaviour | evidence |
|---|---|---|
| +0 | **constant** | always 0x00000100 (256) |
| +4 | **varies** | 4 distinct, range 70144..2147487232 |
| +8 | **varies** | 4 distinct, range 536871936..1610613760 |
| +12 | **varies** | 2 distinct, range 841962319..1195987780 |
| +16 | **near-unique** | 11 distinct across 11 files - id or hash |
| +20 | **varies** | 10 distinct, range 81790208..4234479360 |
| +24 | **varies** | 7 distinct, range 1478164480..2887057408 |
| +28 | **varies** | 3 distinct, range 1178944583..1885433187 |
| +32 | **varies** | 10 distinct, range 599193726..3617529116 |
| +36 | **varies** | 10 distinct, range 1013318656..4237361152 |
| +40 | **varies** | 8 distinct, range 587268096..4278190080 |
| +44 | **tracks size** | r=0.940 with file size over 11 files |
| +48 | **near-unique** | 11 distinct across 11 files - id or hash |
| +52 | **varies** | 9 distinct, range 472450304..4099343616 |
| +56 | **varies** | 9 distinct, range 369098752..3732930560 |
| +60 | **varies** | 3 distinct, range 1112888135..1885433187 |
| +64 | **varies** | 7 distinct, range 1032860644..4172803491 |
| +68 | **near-unique** | 11 distinct across 11 files - id or hash |
| +72 | **varies** | 6 distinct, range 84017152..4128571392 |
| +76 | **varies** | 4 distinct, range 544503395..1886609767 |
| +80 | **varies** | 10 distinct, range 50331648..3691900061 |
| +84 | **varies** | 10 distinct, range 1478623232..3355508736 |
| +88 | **varies** | 8 distinct, range 134217728..3523215360 |
| +92 | **varies** | 4 distinct, range 841962319..1835495526 |

## Four-character codes found in the body

Uppercase 4-byte sequences, which in this client's formats are usually section tags.

| code | occurrences |
|---|---|
| `KQZX` | 22 |
| `Y013` | 10 |
| `BBBB` | 10 |
| `DSIG` | 8 |
| `B99B` | 7 |
| `LTSH` | 7 |
| `ZPPZ` | 7 |
| `Y017` | 6 |
| `CSC3` | 6 |
| `VDMX` | 6 |
| `CTXK` | 6 |
| `A77A` | 5 |
| `LEEL` | 4 |
| `GPOS` | 4 |
| `GSUB` | 4 |
| `UKOS` | 4 |
| `C88C` | 3 |
| `GDEF` | 3 |
| `XGDE` | 3 |
| `JPOJ` | 2 |

## Strings it references

220 distinct strings of 5+ characters. The most common name what this format
points at.

| string | files |
|---|---|
| `00000` | 75 |
| `000000000` | 20 |
| `6hhea` | 11 |
| `2654.` | 7 |
| `VDMXvX` | 6 |
| `......` | 5 |
| `1111111111` | 5 |
| `8888888888` | 5 |
| `000000` | 5 |
| `BBBBBBBBBB` | 5 |
| `------` | 5 |
| `111111` | 5 |
| `54632` | 4 |
| `9876543210/.-` | 3 |
| `cmapO` | 2 |
| `sgasp` | 2 |
| `hadRX` | 2 |
| `jadRX` | 2 |
| `KSXED` | 2 |
| `546753` | 2 |
| `53267` | 2 |
| `Y0173` | 2 |
| `gqqeeqw` | 2 |
| `90174` | 2 |
| `ploca` | 2 |

## Examples

- `UI/Fonts/CubeOffcCond.ttf` — 58,148 bytes
- `UI/Fonts/CubeOffcCondLight.ttf` — 58,616 bytes
- `UI/Fonts/ErasMediumBold.ttf` — 48,413 bytes
- `UI/Fonts/WildstarAlienFont.ttf` — 24,537 bytes
- `UI/Fonts/WildstarAlienFontLarge.ttf` — 37,924 bytes
- `UI/Fonts/segoeui.ttf` — 517,384 bytes
- `UI/Fonts/segoeuib.ttf` — 491,860 bytes
- `UI/Fonts/segoeuii.ttf` — 379,716 bytes
