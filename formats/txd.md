# `.txd` — 1 files

Measured across **every .txd file in the client**, not sampled from one.

| | |
|---|---|
| files | 1 |
| total decompressed | 0.0 MB |
| smallest / median / largest | 7,632 / 7,632 / 7,632 bytes |

## Magic

- `halb` — 1 files (100.0%)

## Header words

What each 32-bit slot at the head of the file *does across the population*. A field
that never varies is a magic or version; one that tracks file size is a count,
length or offset. **These are measurements, not a struct definition.**

| offset | behaviour | evidence |
|---|---|---|
| +0 | **constant** | always 0x626c6168 (1651269992) = 'halb' |
| +4 | **constant** | always 0x00000000 (0) |
| +8 | **constant** | always 0x0000001b (27) |
| +12 | **constant** | always 0x00000000 (0) |
| +16 | **constant** | always 0x00000030 (48) |
| +20 | **constant** | always 0x00000000 (0) |
| +24 | **constant** | always 0x00000014 (20) |
| +28 | **constant** | always 0x00000000 (0) |
| +32 | **constant** | always 0x00000070 (112) |
| +36 | **constant** | always 0x00000000 (0) |
| +40 | **constant** | always 0x00000000 (0) |
| +44 | **constant** | always 0x00000000 (0) |
| +48 | **constant** | always 0x00490055 (4784213) |
| +52 | **constant** | always 0x005f005c (6226012) |
| +56 | **constant** | always 0x004c004f (4980815) |
| +60 | **constant** | always 0x005c0044 (6029380) |
| +64 | **constant** | always 0x00350032 (3473458) |
| +68 | **constant** | always 0x00570036 (5701686) |
| +72 | **constant** | always 0x006e0069 (7209065) |
| +76 | **constant** | always 0x006f0064 (7274596) |
| +80 | **constant** | always 0x00540077 (5505143) |
| +84 | **constant** | always 0x00630065 (6488165) |
| +88 | **constant** | always 0x00320068 (3276904) |
| +92 | **constant** | always 0x0062002e (6422574) |

## Examples

- `UI/_OLD/256WindowTech.txd` — 7,632 bytes
