# `.bnk` — 152 files

Measured across **every .bnk file in the client**, not sampled from one.

| | |
|---|---|
| files | 152 |
| total decompressed | 2080.4 MB |
| smallest / median / largest | 32 / 11,467,776 / 56,724,016 bytes |

## Magic

- `BKHD` — 152 files (100.0%)

## Header words

What each 32-bit slot at the head of the file *does across the population*. A field
that never varies is a magic or version; one that tracks file size is a count,
length or offset. **These are measurements, not a struct definition.**

| offset | behaviour | evidence |
|---|---|---|
| +0 | **constant** | always 0x44484b42 (1145588546) = 'BKHD' |
| +4 | **small set** | 4 distinct, max 32: 24(x47), 28(x45), 32(x31), 20(x29) |
| +8 | **constant** | always 0x00000058 (88) |
| +12 | **varies** | 140 distinct, range 33260990..4292356971 |
| +16 | **small set** | 4 distinct, max 16: 0(x134), 12(x6), 15(x6), 16(x6) |
| +20 | **constant** | always 0x00000000 (0) |
| +24 | **constant** | always 0x00000089 (137) |
| +28 | **varies** | 2 distinct, range 0..1480870212 |
| +32 | **varies** | 29 distinct, range 0..1480870212 |
| +36 | **varies** | 67 distinct, range 0..1480870212 |
| +40 | **varies** | 78 distinct, range 0..1480870212 |
| +44 | **varies** | 103 distinct, range 0..1041528808 |
| +48 | **varies** | 101 distinct, range 0..3262198579 |
| +52 | **varies** | 114 distinct, range 0..3120825112 |
| +56 | **near-unique** | 142 distinct across 149 files - id or hash |
| +60 | **varies** | 141 distinct, range 303..3624140800 |
| +64 | **near-unique** | 142 distinct across 149 files - id or hash |
| +68 | **near-unique** | 144 distinct across 149 files - id or hash |
| +72 | **near-unique** | 143 distinct across 149 files - id or hash |
| +76 | **near-unique** | 145 distinct across 149 files - id or hash |
| +80 | **near-unique** | 144 distinct across 149 files - id or hash |
| +84 | **near-unique** | 143 distinct across 149 files - id or hash |
| +88 | **near-unique** | 145 distinct across 149 files - id or hash |
| +92 | **near-unique** | 143 distinct across 149 files - id or hash |

## Four-character codes found in the body

Uppercase 4-byte sequences, which in this client's formats are usually section tags.

| code | occurrences |
|---|---|
| `C3C3` | 794 |
| `C34C` | 762 |
| `CC34` | 739 |
| `C343` | 669 |
| `CCC3` | 490 |
| `CC3C` | 440 |
| `C233` | 394 |
| `C344` | 356 |
| `C334` | 329 |
| `C3CC` | 251 |
| `S344` | 229 |
| `RIFF` | 222 |
| `WAVE` | 222 |
| `CCCC` | 197 |
| `D344` | 162 |
| `C2C2` | 152 |
| `JUNK` | 138 |
| `C3C2` | 123 |
| `C333` | 110 |
| `BKHD` | 109 |

## Strings it references

2,791 distinct strings of 5+ characters. The most common name what this format
points at.

| string | files |
|---|---|
| `WAVEfmt` | 288 |
| `00..-` | 9 |
| `AbB5PTL` | 9 |
| `33333` | 7 |
| `RIFFH` | 7 |
| `DIDXp` | 6 |
| `adtllabl` | 5 |
| `Tempo` | 5 |
| `DATA0` | 5 |
| `datax` | 5 |
| `RIFFh` | 5 |
| `data0` | 5 |
| `DIDXh` | 5 |
| `1DDSCC` | 5 |
| `DIDXT` | 4 |
| `RIFFDW` | 4 |
| `120.0` | 4 |
| `SSS34` | 4 |
| `RIFFp` | 4 |
| `RIFFd` | 4 |
| `2BRbr` | 4 |
| `DIDX4` | 4 |
| `RIFFX` | 4 |
| `datah` | 4 |
| `3333C` | 4 |

## Examples

- `Audio/Quest_03.bnk` — 31,119,260 bytes
- `Audio/Quest_Adventures.bnk` — 11,461,116 bytes
- `Audio/Sandbox.bnk` — 32 bytes
- `Audio/Structure_Music.bnk` — 402,330 bytes
- `Audio/Structure_SFX.bnk` — 3,245,971 bytes
- `Audio/UI.bnk` — 12,933,240 bytes
- `Audio/UI_LoadScreens.bnk` — 627,769 bytes
- `Audio/UI_Player_Equip.bnk` — 2,085,096 bytes
