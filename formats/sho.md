# `.sho` — 311 files

Measured across **every .sho file in the client**, not sampled from one.

| | |
|---|---|
| files | 311 |
| total decompressed | 175.6 MB |
| smallest / median / largest | 128 / 672 / 83,235,808 bytes |

## Magic

- `STGT` — 206 files (66.2%)
- `SHDR` — 105 files (33.8%)

## Header words

What each 32-bit slot at the head of the file *does across the population*. A field
that never varies is a magic or version; one that tracks file size is a count,
length or offset. **These are measurements, not a struct definition.**

| offset | behaviour | evidence |
|---|---|---|
| +0 | **varies** | 2 distinct, range 1380206675..1413960787 |
| +4 | **small set** | 2 distinct, max 3: 3(x206), 2(x105) |
| +8 | **tracks size** | r=0.934 with file size over 311 files |
| +12 | **constant** | always 0x00000000 (0) |
| +16 | **constant** | always 0x00000000 (0) |
| +20 | **constant** | always 0x00000000 (0) |
| +24 | **tracks size** | r=0.937 with file size over 311 files |
| +28 | **constant** | always 0x00000000 (0) |
| +32 | **tracks size** | r=1.000 with file size over 311 files |
| +36 | **constant** | always 0x00000000 (0) |
| +40 | **small set** | 24 distinct, max 84: 1(x193), 29(x14), 27(x13), 32(x11), 28(x11), 30(x9) |
| +44 | **constant** | always 0x00000000 (0) |
| +48 | **tracks size** | r=1.000 with file size over 311 files |
| +52 | **constant** | always 0x00000000 (0) |
| +56 | **tracks size** | r=0.937 with file size over 311 files |
| +60 | **constant** | always 0x00000000 (0) |
| +64 | **tracks size** | r=0.990 with file size over 311 files |
| +68 | **varies** | 2 distinct, range 0..6553697 |
| +72 | **varies** | 6 distinct, range 0..7471205 |
| +76 | **varies** | 2 distinct, range 0..6029427 |
| +80 | **varies** | 157 distinct, range 20..7274567 |
| +84 | **varies** | 6 distinct, range 0..7602291 |
| +88 | **varies** | 6 distinct, range 0..7471205 |
| +92 | **varies** | 6 distinct, range 0..7340078 |

## Four-character codes found in the body

Uppercase 4-byte sequences, which in this client's formats are usually section tags.

| code | occurrences |
|---|---|
| `SHDR` | 721 |
| `DXBC` | 680 |
| `ISGN` | 680 |
| `TEXC` | 648 |
| `OORD` | 648 |
| `OSGN` | 629 |
| `COLO` | 452 |
| `STGT` | 202 |
| `POSI` | 160 |
| `TION` | 160 |
| `NORM` | 42 |
| `BLEN` | 41 |
| `TANG` | 20 |
| `DWEI` | 20 |
| `DIND` | 19 |
| `ICES` | 19 |
| `BINO` | 15 |
| `RMAL` | 12 |
| `PSIZ` | 8 |

## Strings it references

118 distinct strings of 5+ characters. The most common name what this format
points at.

| string | files |
|---|---|
| `TEXCOORD` | 352 |
| `SV_Position` | 351 |
| `SV_Target` | 263 |
| `COLOR` | 260 |
| `ISGNl` | 108 |
| `POSITION` | 94 |
| `OSGNt` | 35 |
| `NORMAL` | 26 |
| `ISGNH` | 20 |
| `SHDR8` | 17 |
| `ISGNP` | 16 |
| `OSGND` | 16 |
| `ISGNh` | 15 |
| `TANGENT` | 13 |
| `BINORMAL` | 12 |
| `SHDRh` | 11 |
| `BLENDWEIGHT` | 10 |
| `POSITIONT` | 8 |
| `OSGNP` | 8 |
| `SHDRH` | 8 |
| `SHDRd` | 8 |
| `OSGNl` | 7 |
| `SHDRl` | 7 |
| `SHDRp` | 7 |
| `BLENDINDICES` | 7 |

## Examples

- `Shaders/DecalPS.sho` — 208 bytes
- `Shaders/DefaultPS.ps_3_0.sho` — 208 bytes
- `Shaders/DefaultPS.ps_4_0.sho` — 576 bytes
- `Shaders/DefaultPS.sho` — 208 bytes
- `Shaders/DefaultVS.sho` — 128 bytes
- `Shaders/DefaultVS.vs_4_0.sho` — 3,248 bytes
- `Shaders/Downsample1_2PS.ps_3_0.sho` — 464 bytes
- `Shaders/Downsample1_2PS.ps_4_0.sho` — 1,056 bytes
