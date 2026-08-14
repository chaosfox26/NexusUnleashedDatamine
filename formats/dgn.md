# `.dgn` — 953 files

Measured across **every .dgn file in the client**, not sampled from one.

| | |
|---|---|
| files | 953 |
| total decompressed | 106.2 MB |
| smallest / median / largest | 48 / 29,248 / 2,216,992 bytes |

## Magic

- `NGND` — 221 files (23.2%)
- `00000000` — 199 files (20.9%)
- `01000000` — 172 files (18.0%)
- `02000000` — 105 files (11.0%)
- `03000000` — 66 files (6.9%)
- `04000000` — 49 files (5.1%)
- `05000000` — 39 files (4.1%)
- `06000000` — 29 files (3.0%)

## Header words

What each 32-bit slot at the head of the file *does across the population*. A field
that never varies is a magic or version; one that tracks file size is a count,
length or offset. **These are measurements, not a struct definition.**

| offset | behaviour | evidence |
|---|---|---|
| +0 | **varies** | 22 distinct, range 0..1145980750 |
| +4 | **small set** | 2 distinct, max 6: 0(x732), 6(x221) |
| +8 | **tracks size** | r=0.999 with file size over 953 files |
| +12 | **constant** | always 0x00000000 (0) |
| +16 | **constant** | always 0x00000000 (0) |
| +20 | **constant** | always 0x00000000 (0) |
| +24 | **varies** | 50 distinct, range 0..51 |
| +28 | **constant** | always 0x00000000 (0) |
| +32 | **tracks size** | r=1.000 with file size over 953 files |
| +36 | **constant** | always 0x00000000 (0) |
| +40 | **varies** | 48 distinct, range 0..123 |
| +44 | **constant** | always 0x00000000 (0) |
| +48 | **varies** | 355 distinct, range 1..4129334627 |
| +52 | **varies** | 36 distinct, range 0..1184 |
| +56 | **varies** | 72 distinct, range 0..101 |
| +60 | **constant** | always 0x00000000 (0) |
| +64 | **varies** | 14 distinct, range 0..416 |
| +68 | **varies** | 50 distinct, range 0..4067139188 |
| +72 | **varies** | 36 distinct, range 0..759 |
| +76 | **constant** | always 0x00000000 (0) |
| +80 | **varies** | 238 distinct, range 0..1073610207 |
| +84 | **varies** | 233 distinct, range 0..1073610207 |
| +88 | **varies** | 279 distinct, range 0..3826631131 |
| +92 | **varies** | 174 distinct, range 0..1065353216 |

## Four-character codes found in the body

Uppercase 4-byte sequences, which in this client's formats are usually section tags.

| code | occurrences |
|---|---|
| `NGND` | 221 |
| `U0SA` | 16 |
| `OD80` | 10 |
| `NBEC` | 9 |
| `QU2B` | 8 |
| `XYWC` | 8 |
| `QKBM` | 8 |
| `BPSS` | 8 |
| `XCZD` | 7 |
| `ATC7` | 7 |
| `TR0B` | 7 |
| `U0ZA` | 7 |
| `U0OB` | 6 |
| `ARIM` | 6 |
| `A4A4` | 6 |
| `NB7C` | 6 |
| `L70B` | 5 |
| `BNEX` | 5 |
| `ARIX` | 5 |
| `B1YL` | 5 |

## Strings it references

1,733 distinct strings of 5+ characters. The most common name what this format
points at.

| string | files |
|---|---|
| `A0jgB` | 22 |
| `ByiDC` | 18 |
| `AfwKB` | 18 |
| `tFBAj0` | 17 |
| `AyImC` | 12 |
| `AXygC` | 12 |
| `k3hxs` | 11 |
| `IAhq6C` | 10 |
| `Bb0GC` | 10 |
| `ADiCB` | 10 |
| `yU4z7` | 9 |
| `mJ-0f` | 9 |
| `9QU2B` | 8 |
| `-0Gq.` | 8 |
| `4QKBM-` | 8 |
| `r97BFv` | 8 |
| `A9V3B` | 8 |
| `hlAha` | 8 |
| `k3yxs` | 7 |
| `oreCj` | 7 |
| `M68ky` | 7 |
| `qATC7C` | 7 |
| `AJlhC` | 6 |
| `xzZAg` | 6 |
| `A4A4.` | 6 |

## Examples

- `Art/Dev/GamePreview_Dungeon_Placeholder.0.dgn` — 48 bytes
- `Art/Dev/GamePreview_Dungeon_Placeholder.1.dgn` — 48 bytes
- `Art/Dev/GamePreview_Dungeon_Placeholder.2.dgn` — 48 bytes
- `Art/Dev/GamePreview_Dungeon_Placeholder.3.dgn` — 48 bytes
- `Art/Dev/GamePreview_Dungeon_Placeholder.4.dgn` — 48 bytes
- `Art/Dev/GamePreview_Dungeon_Placeholder.5.dgn` — 48 bytes
- `Art/Dev/GamePreview_Dungeon_Placeholder.6.dgn` — 48 bytes
- `Art/Dev/GamePreview_Dungeon_Placeholder.7.dgn` — 48 bytes
