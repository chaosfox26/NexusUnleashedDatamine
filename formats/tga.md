# `.tga` — 1 files

Measured across **every .tga file in the client**, not sampled from one.

| | |
|---|---|
| files | 1 |
| total decompressed | 16.0 MB |
| smallest / median / largest | 16,777,260 / 16,777,260 / 16,777,260 bytes |

## Magic

- `00000200` — 1 files (100.0%)

## Header words

What each 32-bit slot at the head of the file *does across the population*. A field
that never varies is a magic or version; one that tracks file size is a count,
length or offset. **These are measurements, not a struct definition.**

| offset | behaviour | evidence |
|---|---|---|
| +0 | **constant** | always 0x00020000 (131072) |
| +4 | **constant** | always 0x00000000 (0) |
| +8 | **constant** | always 0x00000000 (0) |
| +12 | **constant** | always 0x08000800 (134219776) |
| +16 | **constant** | always 0x00000820 (2080) |
| +20 | **constant** | always 0x00000000 (0) |
| +24 | **constant** | always 0x00000000 (0) |
| +28 | **constant** | always 0x00000000 (0) |
| +32 | **constant** | always 0x00000000 (0) |
| +36 | **constant** | always 0x00000000 (0) |
| +40 | **constant** | always 0x00000000 (0) |
| +44 | **constant** | always 0x00000000 (0) |
| +48 | **constant** | always 0x00000000 (0) |
| +52 | **constant** | always 0x00000000 (0) |
| +56 | **constant** | always 0x00000000 (0) |
| +60 | **constant** | always 0x00000000 (0) |
| +64 | **constant** | always 0x00000000 (0) |
| +68 | **constant** | always 0x00000000 (0) |
| +72 | **constant** | always 0x00000000 (0) |
| +76 | **constant** | always 0x00000000 (0) |
| +80 | **constant** | always 0x00000000 (0) |
| +84 | **constant** | always 0x00000000 (0) |
| +88 | **constant** | always 0x00000000 (0) |
| +92 | **constant** | always 0x00000000 (0) |

## Examples

- `Art/Item/Armor/Medium/Medium_015/Medium_015A_DEPRICATE.tga` — 16,777,260 bytes
