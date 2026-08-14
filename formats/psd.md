# `.psd` — 1 files

Measured across **every .psd file in the client**, not sampled from one.

| | |
|---|---|
| files | 1 |
| total decompressed | 1.2 MB |
| smallest / median / largest | 1,256,469 / 1,256,469 / 1,256,469 bytes |

## Magic

- `8BPS` — 1 files (100.0%)

## Header words

What each 32-bit slot at the head of the file *does across the population*. A field
that never varies is a magic or version; one that tracks file size is a count,
length or offset. **These are measurements, not a struct definition.**

| offset | behaviour | evidence |
|---|---|---|
| +0 | **constant** | always 0x53504238 (1397768760) = '8BPS' |
| +4 | **constant** | always 0x00000100 (256) |
| +8 | **constant** | always 0x00000000 (0) |
| +12 | **constant** | always 0x00000400 (1024) |
| +16 | **constant** | always 0x00000001 (1) |
| +20 | **constant** | always 0x08000001 (134217729) |
| +24 | **constant** | always 0x00000300 (768) |
| +28 | **constant** | always 0x00000000 (0) |
| +32 | **constant** | always 0x4238c655 (1111017045) |
| +36 | **constant** | always 0x04044d49 (67390793) |
| +40 | **constant** | always 0x00000000 (0) |
| +44 | **constant** | always 0x021c0700 (35391232) |
| +48 | **constant** | always 0x00020000 (131072) |
| +52 | **constant** | always 0x42380002 (1110966274) |
| +56 | **constant** | always 0x25044d49 (621038921) |
| +60 | **constant** | always 0x00000000 (0) |
| +64 | **constant** | always 0x0c461000 (205918208) |
| +68 | **constant** | always 0xb82689f2 (3089533426) |
| +72 | **constant** | always 0x9cb0da56 (2628835926) |
| +76 | **constant** | always 0xa7b0a101 (2813370625) |
| +80 | **constant** | always 0x42387790 (1110996880) |
| +84 | **constant** | always 0x24044d49 (604261705) |
| +88 | **constant** | always 0x00000000 (0) |
| +92 | **constant** | always 0x3f3ca83a (1060939834) |

## Four-character codes found in the body

Uppercase 4-byte sequences, which in this client's formats are usually section tags.

| code | occurrences |
|---|---|
| `RGBC` | 87 |
| `TEXT` | 29 |
| `BIMS` | 14 |
| `F8BI` | 3 |
| `B8BI` | 3 |
| `J8BI` | 3 |
| `ICCP` | 2 |
| `DA11` | 2 |
| `B053` | 2 |
| `DAE1` | 2 |
| `C617` | 2 |
| `BETE` | 2 |

## Strings it references

43 distinct strings of 5+ characters. The most common name what this format
points at.

| string | files |
|---|---|
| `xmlns` | 3 |
| `/exif` | 3 |
| `PixelXDimension` | 2 |
| `PixelYDimension` | 2 |
| `ColorSpace` | 2 |
| `w8BIM` | 1 |
| `xpacket` | 1 |
| `begin` | 1 |
| `W5M0MpCehiHzreSzNTczkc9d` | 1 |
| `xmpmeta` | 1 |
| `adobe` | 1 |
| `meta/` | 1 |
| `xmptk` | 1 |
| `3.1.1-111` | 1 |
| `//www.w3.org/1999/02/22-rdf-syntax-ns` | 1 |
| `Description` | 1 |
| `about` | 1 |
| `//ns.adobe.com/exif/1.0/` | 1 |
| `NativeDigest` | 1 |
| `36864` | 1 |
| `40960` | 1 |
| `40961` | 1 |
| `37121` | 1 |
| `37122` | 1 |
| `40962` | 1 |

## Examples

- `UI/_OLD/256WindowTech.psd` — 1,256,469 bytes
