# `.map` — 10 files

Measured across **every .map file in the client**, not sampled from one.

| | |
|---|---|
| files | 10 |
| total decompressed | 0.0 MB |
| smallest / median / largest | 255 / 259 / 337 bytes |

## Magic

- `<Map` — 10 files (100.0%)

## Header words

What each 32-bit slot at the head of the file *does across the population*. A field
that never varies is a magic or version; one that tracks file size is a count,
length or offset. **These are measurements, not a struct definition.**

| offset | behaviour | evidence |
|---|---|---|
| +0 | **constant** | always 0x70614d3c (1885424956) = '<Map' |
| +4 | **varies** | 2 distinct, range 537529662..538970686 |
| +8 | **varies** | 2 distinct, range 1008738336..1329340448 |
| +12 | **varies** | 2 distinct, range 1634034511..1851876707 |
| +16 | **varies** | 2 distinct, range 1702125911..1952536430 |
| +20 | **varies** | 2 distinct, range 1886999666..2035577445 |
| +24 | **varies** | 2 distinct, range 1046759781..1682531696 |
| +28 | **varies** | 2 distinct, range 792473918..1328495665 |
| +32 | **varies** | 2 distinct, range 1634034511..1851876707 |
| +36 | **varies** | 2 distinct, range 1702125911..1952536430 |
| +40 | **varies** | 2 distinct, range 1886999666..2035577445 |
| +44 | **varies** | 2 distinct, range 1046759781..1682531696 |
| +48 | **varies** | 2 distinct, range 537529662..538976266 |
| +52 | **varies** | 2 distinct, range 1008738336..1750285344 |
| +56 | **varies** | 2 distinct, range 1466266223..1919903827 |
| +60 | **varies** | 2 distinct, range 1281717857..1986090853 |
| +64 | **varies** | 2 distinct, range 1919252833..2036419685 |
| +68 | **varies** | 2 distinct, range 1226859593..1682535013 |
| +72 | **varies** | 2 distinct, range 574435396..809781536 |
| +76 | **varies** | 3 distinct, range 539112249..1226842672 |
| +80 | **varies** | 3 distinct, range 574435652..1145643042 |
| +84 | **varies** | 3 distinct, range 573847842..1226842672 |
| +88 | **varies** | 3 distinct, range 574435908..1226842676 |
| +92 | **varies** | 3 distinct, range 574435908..1226842672 |

## Strings it references

13 distinct strings of 5+ characters. The most common name what this format
points at.

| string | files |
|---|---|
| `OceanWaterTypeId` | 10 |
| `/OceanWaterTypeId` | 10 |
| `ShoreWaveLayerId` | 10 |
| `ShoreAngleScale` | 10 |
| `/ShoreAngleScale` | 10 |
| `MaxShoreWaveDepth` | 10 |
| `/MaxShoreWaveDepth` | 10 |
| `OceanShoreWaveLayer` | 10 |
| `/OceanShoreWaveLayer` | 10 |
| `25.00` | 5 |
| `TerrainPresetId` | 2 |
| `IceLayerPresetId` | 1 |
| `/IceLayerPresetId` | 1 |

## Examples

- `Map/AdventureGaleras/AdventureGaleras.map` — 260 bytes
- `Map/AdventureHycrest/AdventureHycrest.map` — 259 bytes
- `Map/AdventureLevianBay/AdventureLevianBay.map` — 257 bytes
- `Map/AdventureMalgrave/AdventureMalgrave.map` — 259 bytes
- `Map/Arcterra/Arcterra.map` — 337 bytes
- `Map/Eastern/Eastern.map` — 255 bytes
- `Map/HalloftheHundred/HalloftheHundred.map` — 307 bytes
- `Map/NewCentral/NewCentral.map` — 259 bytes
