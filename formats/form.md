# `.form` — 43 files

Measured across **every .form file in the client**, not sampled from one.

| | |
|---|---|
| files | 43 |
| total decompressed | 0.3 MB |
| smallest / median / largest | 324 / 3,898 / 37,977 bytes |

## Magic

- `fffe3c00` — 33 files (76.7%)
- `<?xm` — 10 files (23.3%)

## Header words

What each 32-bit slot at the head of the file *does across the population*. A field
that never varies is a magic or version; one that tracks file size is a count,
length or offset. **These are measurements, not a struct definition.**

| offset | behaviour | evidence |
|---|---|---|
| +0 | **varies** | 2 distinct, range 3997439..1836597052 |
| +4 | **varies** | 2 distinct, range 7864383..1702240364 |
| +8 | **varies** | 2 distinct, range 7077997..1869181810 |
| +12 | **varies** | 2 distinct, range 7733280..824327534 |
| +16 | **varies** | 2 distinct, range 7471205..539111470 |
| +20 | **varies** | 2 distinct, range 6881395..168640063 |
| +24 | **varies** | 2 distinct, range 7209071..1634887228 |
| +28 | **varies** | 2 distinct, range 2228285..1663067501 |
| +32 | **varies** | 2 distinct, range 3014705..1936941420 |
| +36 | **varies** | 3 distinct, range 2228272..1917198909 |
| +40 | **varies** | 3 distinct, range 4128800..1631741284 |
| +44 | **varies** | 3 distinct, range 852030..1768974624 |
| +48 | **varies** | 4 distinct, range 3932170..1867719229 |
| +52 | **varies** | 6 distinct, range 7471206..1868983881 |
| +56 | **varies** | 8 distinct, range 7143521..1970228594 |
| +60 | **varies** | 8 distinct, range 2097253..1952533792 |
| +64 | **varies** | 8 distinct, range 7077987..1953720652 |
| +68 | **varies** | 8 distinct, range 7536737..1953391986 |
| +72 | **varies** | 8 distinct, range 3997811..1852142177 |
| +76 | **varies** | 9 distinct, range 4587554..1952999273 |
| +80 | **varies** | 9 distinct, range 6357106..1768245364 |
| +84 | **varies** | 9 distinct, range 4325477..1953391986 |
| +88 | **varies** | 9 distinct, range 2097186..1734960456 |
| +92 | **varies** | 9 distinct, range 2097186..1953391986 |

## Four-character codes found in the body

Uppercase 4-byte sequences, which in this client's formats are usually section tags.

| code | occurrences |
|---|---|
| `TXDN` | 130 |
| `TXDF` | 15 |
| `XXXX` | 3 |
| `KKKO` | 2 |
| `YYYY` | 1 |
| `ZZZZ` | 1 |
| `GMMM` | 1 |

## Strings it references

119 distinct strings of 5+ characters. The most common name what this format
points at.

| string | files |
|---|---|
| `source` | 33 |
| `target` | 33 |
| `input-redirect` | 31 |
| `targetname` | 28 |
| `class` | 16 |
| `MatchParentHeight` | 15 |
| `MatchParentWidth` | 15 |
| `moveable` | 15 |
| `position.height` | 15 |
| `position.relative` | 15 |
| `position.width` | 15 |
| `position.x` | 14 |
| `position.y` | 14 |
| `TXDName` | 13 |
| `SetText` | 13 |
| `visible` | 12 |
| `TXDFileName` | 11 |
| `UI\_OLD\256WindowTech.txd` | 11 |
| `version` | 10 |
| `frame` | 10 |
| `transparent` | 10 |
| `Frame` | 9 |
| `Array` | 7 |
| `PromptFrame` | 6 |
| `control` | 6 |

## Examples

- `UI/_OLD/Genesis/SpawnPickerFrame.form` — 2,524 bytes
- `UI/_OLD/Genesis/TextureDialog.form` — 12,230 bytes
- `UI/_OLD/Genesis/TexturePicker.form` — 8,324 bytes
- `UI/_OLD/Genesis/TexturePickerElement.form` — 2,450 bytes
- `UI/_OLD/MessageBox.form` — 2,744 bytes
- `UI/_OLD/MessageBoxColorPicker.form` — 10,084 bytes
- `UI/_OLD/MessageBoxOkay.form` — 2,756 bytes
- `UI/_OLD/MessageBoxOkayCancel.form` — 3,898 bytes
