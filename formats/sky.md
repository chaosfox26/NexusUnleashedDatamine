# `.sky` — 1291 files

Measured across **every .sky file in the client**, not sampled from one.

| | |
|---|---|
| files | 1291 |
| total decompressed | 9.1 MB |
| smallest / median / largest | 1,392 / 5,473 / 31,152 bytes |

## Magic

- `YKSX` — 1291 files (100.0%)

## Header words

What each 32-bit slot at the head of the file *does across the population*. A field
that never varies is a magic or version; one that tracks file size is a count,
length or offset. **These are measurements, not a struct definition.**

| offset | behaviour | evidence |
|---|---|---|
| +0 | **constant** | always 0x58534b59 (1481853785) = 'YKSX' |
| +4 | **constant** | always 0x00000010 (16) |
| +8 | **small set** | 6 distinct, max 6: 0(x573), 1(x534), 4(x130), 5(x44), 6(x7), 2(x3) |
| +12 | **small set** | 18 distinct, max 33: 0(x849), 2(x110), 1(x102), 4(x44), 7(x44), 3(x34) |
| +16 | **varies** | 21 distinct, range 881153232..1259902592 |
| +20 | **constant** | always 0x00000000 (0) |
| +24 | **varies** | 43 distinct, range 48..93 |
| +28 | **constant** | always 0x00000000 (0) |
| +32 | **constant** | always 0x00000000 (0) |
| +36 | **constant** | always 0x00000000 (0) |
| +40 | **small set** | 2 distinct, max 1: 1(x760), 0(x531) |
| +44 | **constant** | always 0x00000000 (0) |
| +48 | **small set** | 2 distinct, max 1: 0(x923), 1(x368) |
| +52 | **constant** | always 0x00000000 (0) |
| +56 | **small set** | 6 distinct, max 176: 0(x923), 128(x140), 144(x133), 160(x45), 112(x38), 176(x12) |
| +60 | **constant** | always 0x00000000 (0) |
| +64 | **small set** | 10 distinct, max 9: 0(x601), 4(x198), 1(x159), 2(x128), 6(x80), 3(x68) |
| +68 | **constant** | always 0x00000000 (0) |
| +72 | **varies** | 21 distinct, range 0..400 |
| +76 | **constant** | always 0x00000000 (0) |
| +80 | **small set** | 4 distinct, max 3: 1(x976), 0(x301), 2(x13), 3(x1) |
| +84 | **constant** | always 0x00000000 (0) |
| +88 | **varies** | 100 distinct, range 0..3504 |
| +92 | **constant** | always 0x00000000 (0) |

## Four-character codes found in the body

Uppercase 4-byte sequences, which in this client's formats are usually section tags.

| code | occurrences |
|---|---|
| `YKSX` | 1,291 |
| `UI2G` | 4 |
| `GY9J` | 2 |

## Strings it references

1 distinct strings of 5+ characters. The most common name what this format
points at.

| string | files |
|---|---|
| `a1APW` | 6 |

## Examples

- `Sky/Arcterra_EXT_TowerMain.sky` — 5,600 bytes
- `Sky/Arcterra_INT_BlackHoods.sky` — 3,104 bytes
- `Sky/Arcterra_INT_ICI_Research.sky` — 3,120 bytes
- `Sky/Arcterra_INT_IceBlood_Burrow.sky` — 3,121 bytes
- `Sky/Arcterra_INT_IceCave_GirrokCave.sky` — 3,136 bytes
- `Sky/Arcterra_INT_IceCave_KeepFish.sky` — 3,120 bytes
- `Sky/Arcterra_INT_IceCave_MineralCave.sky` — 3,136 bytes
- `Sky/Arcterra_INT_IceCave_Misc_Small.sky` — 3,137 bytes
