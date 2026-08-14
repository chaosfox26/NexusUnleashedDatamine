# `.xml` — 560 files

Measured across **every .xml file in the client**, not sampled from one.

| | |
|---|---|
| files | 560 |
| total decompressed | 14.0 MB |
| smallest / median / largest | 11 / 6,814 / 1,344,918 bytes |

## Magic

- `<?xm` — 369 files (65.9%)
- `<Add` — 98 files (17.5%)
- `<For` — 86 files (15.4%)
- `<Eul` — 3 files (0.5%)
- `<Ani` — 1 files (0.2%)
- `<Col` — 1 files (0.2%)
- `<Flo` — 1 files (0.2%)
- `<Doc` — 1 files (0.2%)

## Header words

What each 32-bit slot at the head of the file *does across the population*. A field
that never varies is a magic or version; one that tracks file size is a count,
length or offset. **These are measurements, not a struct definition.**

| offset | behaviour | evidence |
|---|---|---|
| +0 | **varies** | 8 distinct, range 1668236348..1919895100 |
| +4 | **varies** | 10 distinct, range 168640097..1919251553 |
| +8 | **varies** | 11 distinct, range 538970637..1869181810 |
| +12 | **varies** | 74 distinct, range 538970637..2053195810 |
| +16 | **varies** | 95 distinct, range 539111470..2037672300 |
| +20 | **varies** | 87 distinct, range 168640063..2036427888 |
| +24 | **varies** | 75 distinct, range 539126885..1986360425 |
| +28 | **varies** | 67 distinct, range 222175793..2037672300 |
| +32 | **varies** | 59 distinct, range 151653694..2003788910 |
| +36 | **varies** | 64 distinct, range 168640034..1936876886 |
| +40 | **varies** | 74 distinct, range 151653694..3273680243 |
| +44 | **varies** | 75 distinct, range 151653694..1998615401 |
| +48 | **varies** | 89 distinct, range 151653694..3216764706 |
| +52 | **varies** | 112 distinct, range 222175793..2003788910 |
| +56 | **varies** | 176 distinct, range 222178605..2004296253 |
| +60 | **varies** | 182 distinct, range 168632354..2034442274 |
| +64 | **varies** | 185 distinct, range 168640034..2037672300 |
| +68 | **varies** | 208 distinct, range 151653694..2037539181 |
| +72 | **varies** | 239 distinct, range 168640045..2037150819 |
| +76 | **varies** | 232 distinct, range 151653694..2036427856 |
| +80 | **varies** | 204 distinct, range 168640034..2037672302 |
| +84 | **varies** | 222 distinct, range 168640034..2037148001 |
| +88 | **varies** | 239 distinct, range 168640034..2924626260 |
| +92 | **varies** | 230 distinct, range 168640034..3260170580 |

## Four-character codes found in the body

Uppercase 4-byte sequences, which in this client's formats are usually section tags.

| code | occurrences |
|---|---|
| `VCEN` | 4,475 |
| `CENT` | 4,055 |
| `WORD` | 1,030 |
| `BREA` | 1,030 |
| `TEMP` | 832 |
| `RIGH` | 752 |
| `BOTT` | 407 |
| `HUDA` | 180 |
| `DEMO` | 172 |
| `CARB` | 132 |
| `WWWW` | 128 |
| `SING` | 108 |
| `LELI` | 108 |
| `UIKI` | 102 |
| `APIV` | 89 |
| `NESW` | 86 |
| `NWSE` | 86 |
| `ODER` | 64 |
| `DCPP` | 60 |
| `ATIO` | 55 |

## Strings it references

2,697 distinct strings of 5+ characters. The most common name what this format
points at.

| string | files |
|---|---|
| `ffffffff` | 855 |
| `Sprite` | 654 |
| `Frame` | 578 |
| `Texture` | 566 |
| `Default` | 528 |
| `Cycle` | 501 |
| `HotspotX` | 497 |
| `HotspotY` | 484 |
| `Duration` | 462 |
| `StartColor` | 458 |
| `EndColor` | 455 |
| `white` | 436 |
| `Class` | 405 |
| `LAnchorPoint` | 401 |
| `LAnchorOffset` | 400 |
| `TAnchorPoint` | 400 |
| `TAnchorOffset` | 400 |
| `RAnchorPoint` | 400 |
| `RAnchorOffset` | 398 |
| `Stretchy` | 397 |
| `BAnchorPoint` | 394 |
| `BAnchorOffset` | 391 |
| `/Sprite` | 384 |
| `1.000` | 381 |
| `Window` | 378 |

## Examples

- `UI/ActionBarFrame/ActionBarFrame.xml` — 50,211 bytes
- `UI/ActionBarFrame/toc.xml` — 170 bytes
- `UI/ActionBarShortcut/ActionBarShortcut.xml` — 8,815 bytes
- `UI/ActionBarShortcut/ActionBarShortcutSprites.xml` — 45 bytes
- `UI/ActionBarShortcut/toc.xml` — 144 bytes
- `UI/ActionConfirmButton.xml` — 17,176 bytes
- `UI/AdventureClueTracker/AdventureClueTracker.xml` — 4,241 bytes
- `UI/AdventureClueTracker/toc.xml` — 153 bytes
