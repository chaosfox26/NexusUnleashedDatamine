# Every file in WildStar, by name

**218,427 files. 100% present in the mirror.**

The CDN mirror is content-addressed — 197,333 blobs each named for its own SHA1, no manifest, no
filenames. `ClientData.index` and its language siblings are the missing half. Walking them recovers
the complete filesystem, and every recovered name resolves to a blob that is actually there.

Full listing in `FILETREE.tsv`: `path · sha1 · uncompressed · compressed · inMirror`.

## The tree

| folder | files |
|---|---:|
| `Audio/` | 88,419 |
| `Art/` | 83,561 |
| `Map/` | 27,949 |
| `UI/` | 16,311 |
| `Sky/` | 1,291 |
| `DB/` | 384 |
| `Shaders/` | 311 |
| `EnvMap/` | 191 |
| `Common/` | 7 |

| extension | files | what it is |
|---|---:|---|
| `.wem` | 88,267 | Wwise audio |
| `.tex` | 74,673 | textures |
| `.m3` | 34,748 | models |
| `.area` | 15,051 | map areas |
| `.i3` | 1,704 | — |
| `.sky` | 1,291 | sky definitions |
| `.dgn` | 986 | dungeon / structure geometry |
| `.xml` | 564 | UI forms and data |
| `.tbl` | 384 | **the game tables** |
| `.sho` | 311 | shaders |
| `.lua` | 203 | UI scripts |
| `.bnk` | 152 | Wwise sound banks |
| `.form` | 43 | UI forms |
| `.bk2` | 19 | Bink video |
| `.ttf` | 11 | fonts |

`218,427 names > 197,333 blobs` because content addressing deduplicates: the same content referenced
by several paths is stored once. 197,178 distinct hashes are named.

## The entry format

Each block is one directory:

```
u32 dirCount
u32 fileCount
dirCount  x (u32 nameOffset, u32 blockIndex)                    8 bytes
fileCount x (u32 nameOffset, u32 flags, u64 writeTime,         56 bytes
             u64 uncompressedSize, u64 compressedSize, u8 sha1[20], u32)
string table, NUL-separated, shared by both arrays
```

**The SHA1 is the blob filename.** Confirmed on the first row read: hash
`e7a6a2ab0314…` exists in the mirror *and* is 1,543 bytes, matching that row's `compressedSize`
exactly — two independent checks out of one entry, before any of the rest was trusted.

## Three things I read wrong first

Each was caught by arithmetic or by a failure that could not be mistaken for success:

- **`blockCount` is a count, not a byte size.** 8680 × 16 = 138,880, which fills the file from the
  block table to EOF. Read as a size it yielded 542 blocks and nothing parsed.
- **The `16042` at offset 584 is the build number, not a block index.** Using it as an index threw
  out-of-range — the useful kind of wrong.
- **The second `u32` of a block is a file count, not padding.** Reading it as padding parsed only the
  directory half: 2,067 names out of 218,427, with seven of the nine top-level folders showing
  exactly one child. **A tree that lopsided is the shape of a parser giving up, not of a filesystem.**

## What this closed

The census had 1,017 blobs with no recognised magic, of which 780 shared only a shape — a leading
`u32` between 0 and 15 with a decreasing distribution. I recorded that as *a shape, not an
identification*, and refused to name it from the histogram.

The index answers it outright:

| resolved | blobs | example |
|---|---:|---|
| `.dgn` dungeon/structure geometry | 732 | `Art/Structure/Model/Dungeon_Kits/Eldan_Kit/Exolabs/…` |
| `.bnk` Wwise sound banks | 152 | `Audio/NPC_Creature_J.bnk` |
| **not in any index** | **96** | — |
| `.bk2` Bink video | 19 | `Art/Cinematics/Zones/Launch/LaunchTrailer.bk2` |
| `.ttf` fonts | 11 | `UI/Fonts/segoeuil.ttf` |

That leading `0–15` was a LOD or version field inside the DGN format. Guessing it from the histogram
would have produced a plausible, wrong, and permanent answer.

**96 blobs appear in no index.** They exist in the mirror and nothing names them — the only genuinely
unaccounted-for content left, and worth a look precisely because everything else resolved.

## Why this is the unlock

Before this, extracting anything meant decompressing 197,333 anonymous blobs and guessing from magic
bytes. Now any file can be fetched by name:

```
Art/Cinematics/Zones/Launch/LaunchTrailer.bk2  ->  sha1  ->  D:\CDN\Mirror\16042\<sha1>.bin
```

Which means `UI/` yields the complete original interface, `DB/` the 384 game tables already dumped,
and `Map/` all 27,949 area files — each by name, none by guesswork.
