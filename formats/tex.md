# `.tex` — 61857 files

Measured across **every .tex file in the client**, not sampled from one.

| | |
|---|---|
| files | 61857 |
| total decompressed | 7722.1 MB |
| smallest / median / largest | 117 / 61,792 / 8,640,112 bytes |

## Magic

- `58464700` — 61857 files (100.0%)

## Header words

What each 32-bit slot at the head of the file *does across the population*. A field
that never varies is a magic or version; one that tracks file size is a count,
length or offset. **These are measurements, not a struct definition.**

| offset | behaviour | evidence |
|---|---|---|
| +0 | **constant** | always 0x00474658 (4671064) |
| +4 | **constant** | always 0x00000003 (3) |
| +8 | **varies** | 527 distinct, range 1..2048 |
| +12 | **varies** | 406 distinct, range 1..2048 |
| +16 | **small set** | 2 distinct, max 16: 1(x61771), 16(x86) |
| +20 | **small set** | 2 distinct, max 6: 1(x61579), 6(x278) |
| +24 | **small set** | 11 distinct, max 12: 10(x16667), 11(x13156), 9(x10784), 1(x10514), 7(x8571), 8(x1889) |
| +28 | **small set** | 7 distinct, max 18: 0(x42321), 13(x9047), 6(x5384), 15(x3684), 1(x1404), 5(x15) |
| +32 | **small set** | 2 distinct, max 1: 1(x38686), 0(x23171) |
| +36 | **small set** | 3 distinct, max 2: 0(x36622), 1(x13073), 2(x12162) |
| +40 | **varies** | 4 distinct, range 0..1543503964 |
| +44 | **varies** | 4 distinct, range 0..21692416 |
| +48 | **varies** | 72 distinct, range 0..4278275071 |
| +52 | **small set** | 11 distinct, max 12: 0(x23171), 11(x12740), 9(x10476), 10(x9701), 7(x3853), 8(x1760) |
| +56 | **small set** | 2 distinct, max 16: 16(x38686), 0(x23171) |
| +60 | **small set** | 8 distinct, max 112: 0(x23171), 32(x14622), 16(x13643), 48(x7966), 64(x2001), 80(x352) |
| +64 | **small set** | 10 distinct, max 144: 0(x23171), 48(x9393), 64(x9151), 32(x8229), 16(x6301), 80(x3955) |
| +68 | **varies** | 28 distinct, range 0..448 |
| +72 | **varies** | 68 distinct, range 0..1104 |
| +76 | **varies** | 190 distinct, range 0..3424 |
| +80 | **varies** | 557 distinct, range 0..10896 |
| +84 | **varies** | 1469 distinct, range 0..31136 |
| +88 | **varies** | 3737 distinct, range 0..101200 |
| +92 | **varies** | 6869 distinct, range 0..407904 |

## Four-character codes found in the body

Uppercase 4-byte sequences, which in this client's formats are usually section tags.

| code | occurrences |
|---|---|
| `VVVV` | 445,626 |
| `ZZZZ` | 77,140 |
| `FRFR` | 69,432 |
| `YYYY` | 54,531 |
| `XXXX` | 50,090 |
| `PPPP` | 39,271 |
| `TTTT` | 35,284 |
| `YYUU` | 35,080 |
| `WWWW` | 29,552 |
| `C1C1` | 26,708 |
| `AAAA` | 13,498 |
| `UUUT` | 12,682 |
| `TUUU` | 12,595 |
| `EZFR` | 11,164 |
| `DDDD` | 8,197 |
| `RRRR` | 7,797 |
| `EEEE` | 7,194 |
| `GGGG` | 6,875 |
| `UUUU` | 6,860 |
| `CCCC` | 6,833 |

## Strings it references

695,525 distinct strings of 5+ characters. The most common name what this format
points at.

| string | files |
|---|---|
| `1TTTT` | 4,122 |
| `9pppp` | 4,097 |
| `1pppp` | 2,125 |
| `VVVVV` | 674 |
| `VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV` | 629 |
| `V\XpA` | 606 |
| `iRhJU` | 576 |
| `ZBBBB` | 542 |
| `2\_UU` | 535 |
| `UUUnk` | 520 |
| `VVVVVV` | 444 |
| `_____` | 397 |
| `1\\\\` | 364 |
| `UWV\A` | 327 |
| `VWUUA` | 322 |
| `UUUxA` | 321 |
| `TWUUA` | 319 |
| `UUW\A` | 315 |
| `rUeUU` | 315 |
| `X\VWA` | 313 |
| `\XrbA` | 310 |
| `UUWTA` | 309 |
| `UUUmk` | 309 |
| `\\\\\` | 306 |
| `WV\XA` | 305 |

## Examples

- `Art/Character/Aurin/Female/Textures/CHR_Aurin_f_hair_05_normal.Skin_Head.tex` — 81,600 bytes
- `Art/Character/Aurin/Female/Textures/CHR_Bra_Aurin_F_Color.Skin_Body.tex` — 24,192 bytes
- `Art/Character/Aurin/Female/Textures/CHR_Bra_Aurin_F_Mask.Skin_Body.tex` — 524,460 bytes
- `Art/Character/Aurin/Female/Textures/CHR_Eye_07_Aurin_F_Color.Skin_Ear_Horn.tex` — 6,080 bytes
- `Art/Character/Aurin/Female/Textures/CHR_Eye_07_Aurin_F_Color.Skin_Eye.tex` — 13,248 bytes
- `Art/Character/Aurin/Female/Textures/CHR_Eye_Brown_07_Aurin_F_Color.Skin_Eye.tex` — 12,352 bytes
- `Art/Character/Aurin/Female/Textures/CHR_Eye_DarkBlue_07_Aurin_F_Color.Skin_Eye.tex` — 13,728 bytes
- `Art/Character/Aurin/Female/Textures/CHR_Eye_Fuchia_07_Aurin_F_Color.Skin_Eye.tex` — 13,440 bytes
