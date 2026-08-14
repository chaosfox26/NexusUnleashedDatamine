# `.wem` — 83462 files

Measured across **every .wem file in the client**, not sampled from one.

| | |
|---|---|
| files | 83462 |
| total decompressed | 5304.2 MB |
| smallest / median / largest | 303 / 30,680 / 12,863,451 bytes |

## Magic

- `RIFF` — 83462 files (100.0%)

## Header words

What each 32-bit slot at the head of the file *does across the population*. A field
that never varies is a magic or version; one that tracks file size is a count,
length or offset. **These are measurements, not a struct definition.**

| offset | behaviour | evidence |
|---|---|---|
| +0 | **constant** | always 0x46464952 (1179011410) = 'RIFF' |
| +4 | **tracks size** | r=1.000 with file size over 83462 files |
| +8 | **constant** | always 0x45564157 (1163280727) = 'WAVE' |
| +12 | **constant** | always 0x20746d66 (544501094) = 'fmt ' |
| +16 | **small set** | 2 distinct, max 66: 66(x83141), 24(x321) |
| +20 | **varies** | 5 distinct, range 65538..458751 |
| +24 | **varies** | 2 distinct, range 44100..48000 |
| +28 | **varies** | 10683 distinct, range 585..78375 |
| +32 | **varies** | 3 distinct, range 0..262216 |
| +36 | **varies** | 5 distinct, range 6..1572912 |
| +40 | **small set** | 3 distinct, max 63: 4(x55247), 3(x28213), 63(x2) |
| +44 | **varies** | 67352 distinct, range 128..1819307379 |
| +48 | **varies** | 9 distinct, range 4..7116 |
| +52 | **varies** | 48538 distinct, range 0..1082108859 |
| +56 | **varies** | 1027 distinct, range 0..1635017060 |
| +60 | **varies** | 617 distinct, range 0..3456000 |
| +64 | **varies** | 564 distinct, range 0..1635017060 |
| +68 | **varies** | 52847 distinct, range 0..3978019191 |
| +72 | **varies** | 144 distinct, range 0..3927192353 |
| +76 | **varies** | 194 distinct, range 0..4236460561 |
| +80 | **varies** | 182 distinct, range 0..3966356248 |
| +84 | **varies** | 184 distinct, range 0..4271472640 |
| +88 | **varies** | 42457 distinct, range 0..4294926708 |
| +92 | **varies** | 431 distinct, range 0..4183007240 |

## Four-character codes found in the body

Uppercase 4-byte sequences, which in this client's formats are usually section tags.

| code | occurrences |
|---|---|
| `RIFF` | 83,362 |
| `WAVE` | 83,361 |
| `B5PT` | 27,471 |
| `C34C` | 3,377 |
| `C3C3` | 2,767 |
| `CC34` | 2,565 |
| `C343` | 2,316 |
| `C344` | 2,006 |
| `C3CC` | 1,403 |
| `CC3C` | 1,400 |
| `CCC3` | 1,343 |
| `DD33` | 1,312 |
| `C334` | 887 |
| `C233` | 611 |
| `C2C3` | 475 |
| `LIST` | 337 |
| `CCCC` | 333 |
| `C2C2` | 319 |
| `C333` | 293 |
| `C3C2` | 290 |

## Strings it references

1,166,805 distinct strings of 5+ characters. The most common name what this format
points at.

| string | files |
|---|---|
| `WAVEfmt` | 83,462 |
| `00..-` | 27,468 |
| `AbB5PTL` | 27,468 |
| `2BRbr` | 1,272 |
| `Tempo` | 415 |
| `adtllabl` | 339 |
| `RIFF8` | 233 |
| `RIFFb` | 201 |
| `datax` | 199 |
| `RIFFH` | 199 |
| `dataO` | 199 |
| `datae` | 199 |
| `dataG` | 197 |
| `RIFFg` | 196 |
| `data7` | 195 |
| `datac` | 194 |
| `dataM` | 194 |
| `dataX` | 194 |
| `data-` | 193 |
| `RIFF3` | 193 |
| `RIFFc` | 193 |
| `RIFFX` | 193 |
| `datay` | 193 |
| `dataH` | 191 |
| `dataz` | 191 |

## Examples

- `Audio/1014262441.wem` — 1,255,334 bytes
- `Audio/101572874.wem` — 327,873 bytes
- `Audio/1016344771.wem` — 76,960 bytes
- `Audio/1016995092.wem` — 358,593 bytes
- `Audio/1017211106.wem` — 793,944 bytes
- `Audio/1017273924.wem` — 217,397 bytes
- `Audio/1017356583.wem` — 2,730,208 bytes
- `Audio/1017471519.wem` — 148,904 bytes
