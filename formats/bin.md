# `.bin` — 3 files

Measured across **every .bin file in the client**, not sampled from one.

| | |
|---|---|
| files | 3 |
| total decompressed | 130.1 MB |
| smallest / median / largest | 41,690,224 / 47,002,208 / 47,740,240 bytes |

## Magic

- `XETL` — 3 files (100.0%)

## Header words

What each 32-bit slot at the head of the file *does across the population*. A field
that never varies is a magic or version; one that tracks file size is a count,
length or offset. **These are measurements, not a struct definition.**

| offset | behaviour | evidence |
|---|---|---|
| +0 | **constant** | always 0x4c544558 (1280591192) = 'XETL' |
| +4 | **constant** | always 0x00000004 (4) |
| +8 | **small set** | 3 distinct, max 3: 2(x1), 1(x1), 3(x1) |
| +12 | **near-unique** | 3 distinct across 3 files - id or hash |
| +16 | **constant** | always 0x00000006 (6) |
| +20 | **constant** | always 0x00000000 (0) |
| +24 | **constant** | always 0x00000000 (0) |
| +28 | **constant** | always 0x00000000 (0) |
| +32 | **constant** | always 0x00000003 (3) |
| +36 | **constant** | always 0x00000000 (0) |
| +40 | **constant** | always 0x00000010 (16) |
| +44 | **constant** | always 0x00000000 (0) |
| +48 | **small set** | 3 distinct, max 15: 7(x1), 12(x1), 15(x1) |
| +52 | **constant** | always 0x00000000 (0) |
| +56 | **constant** | always 0x00000020 (32) |
| +60 | **constant** | always 0x00000000 (0) |
| +64 | **constant** | always 0x00083a73 (539251) |
| +68 | **constant** | always 0x00000000 (0) |
| +72 | **small set** | 2 distinct, max 64: 64(x2), 48(x1) |
| +76 | **constant** | always 0x00000000 (0) |
| +80 | **near-unique** | 3 distinct across 3 files - id or hash |
| +84 | **constant** | always 0x00000000 (0) |
| +88 | **varies** | 2 distinct, range 4314064..4314080 |
| +92 | **constant** | always 0x00000000 (0) |

## Four-character codes found in the body

Uppercase 4-byte sequences, which in this client's formats are usually section tags.

| code | occurrences |
|---|---|
| `XETL` | 3 |

## Examples

- `de-DE.bin` — 47,740,240 bytes
- `en-US.bin` — 41,690,224 bytes
- `fr-FR.bin` — 47,002,208 bytes
