# `.area` and `.i3` — what parsing them actually showed

Two formats, 14.9 GB between them, no published spec. Both were opened with a parser that accepts a
chunk **only** when its declared size fits the buffer and lands exactly on the next boundary.

## First, a correction

An earlier pass reported *"88,255 `PROP` records — every object placed in the world."* **That was
wrong on every count.**

It came from a regex counting uppercase four-byte sequences in the first 64 KB of each file. So it
counted byte patterns rather than parsed records, any four bytes that happened to be uppercase ASCII
matched, and the 64 KB window made the total an artefact of the window rather than a measurement.

Parsed properly: `.area` files contain **one `PROp` chunk each, in 42% of files** — 503 of 1,200
sampled. Not 88,255 records. The 19,005 raw byte-hits across 300 files scale to roughly 738,000, so
even as a byte count the published figure was wrong.

The tool that produced it is the same one whose documentation says it will not print a struct
definition. **Writing the rule down did not stop me breaking it.** What caught it was opening one
file by hand and finding zero `PROP` in it.

## `.area` — 11,651 files, 12.9 GB

**Parses 100% as chunked.** 1,200 of 1,200 sampled.

```
header  8 bytes   'aera' + u32
chunk   4-byte tag (stored reversed), u32 payload size, payload
```

| top-level chunk | files | note |
|---|---:|---|
| `CHNK` | 1,200 / 1,200 | every file. Payload = filesize − 16 exactly |
| `PROp` | 503 | one per file, mixed case in the source bytes |
| `CURT` | 164 | |

No nesting: all three sit at depth 0, and nothing inside them parses as a further chunk.

### Inside `PROp`

The payload is object placement data. That much is visible in the bytes rather than inferred:

```
30ea5f45 59b437c4 ea0ebec5   →  (3582.6, -734.8, -6081.9)    world coordinates
0000803f 00000000 00000000
00000000 0000803f            →  1.0 / 0.0 pattern             rotation matrix or quaternion
```

The dominant periodicity is **104 bytes** — the most common spacing between `1.0f` markers, with 208
and 312 appearing as exact multiples, which is what a 104-byte record produces when some entries lack
the marker at every slot.

**The record layout is NOT established, and here is precisely why.** Payload lengths do not divide
evenly by 104, nor by the leading `u32`:

| file | leading u32 | payload | payload ÷ u32 |
|---|---:|---:|---|
| `ExileArkShipTutorial.434a` | 3 | 1,004 | 332 |
| `ExileArkShipTutorial.3e46` | 2 | 510 | 251 |
| `Datascape.3e40` | 10 | 1,408 | 140 |
| `ShiphandLevel6.3447` | 405 | 58,748 | 145.05 — **not integer** |

Three different quotients and one that is not a whole number. So either the leading `u32` is not a
record count, or the records are variable-length, or there is a header of unknown size before them.
**Nothing here distinguishes those three, so none of them is written down as the answer.**

## `.i3` — 1,696 files, 2.0 GB, magic `SDEF`

**Zero of 1,696 parse as a chunk container.** Not a partial parse, not a low rate — none.

That is a clean negative result and it is worth as much as a positive one: the obvious hypothesis for
an unknown binary format in this client is "it's chunked like `.area`", and it is definitively not.
The 8-byte header is followed by something else — a fixed struct, an array, or a compressed block.

`.i3` remains the largest unidentified format in the game.

## What would settle both

The same thing that settled every other question here: a second source. For `PROp`, the server-side
`world` and `entity` tables already carry object placements for maps we run — cross-referencing a
known placement against the bytes at a known offset would pin the record layout in one step, without
guessing a struct.
