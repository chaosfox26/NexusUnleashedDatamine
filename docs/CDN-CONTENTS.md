# What is actually in the 17 GB

Every one of the **197,333** blobs in `D:\CDN\Mirror\16042` has been decompressed and classified.
Full per-blob record in `CENSUS.tsv` — one row each, **including the failures**, because a blob
missing from a census is indistinguishable from one that was never examined.

**16.4 GB compressed → 37.1 GB decoded, in 15.5 seconds.**

| what it is | blobs | share |
|---|---:|---:|
| audio (`RIFF`) | 83,462 | 42.3% |
| graphics (`XFG`) | 61,857 | 31.3% |
| models (`MODL`) | 34,568 | 17.5% |
| **area / map data** | **11,651** | 5.9% |
| sky (`XSKY`) | 1,291 | 0.7% |
| shader definitions | 1,283 | 0.7% |
| **unknown** | **1,017** | 0.5% |
| XML | 631 | 0.3% |
| `idef` | 413 | 0.2% |
| **game tables (`DTBL`)** | **384** | 0.2% |
| engine (`DNGN`) | 221 | 0.1% |
| `tgts` | 206 | 0.1% |
| **Lua** | **191** | 0.1% |
| shaders | 105 | 0.1% |
| text | 29 | 0.0% |
| PNG | 13 | 0.0% |
| nested archives (`KCAP`) | 10 | 0.0% |
| undecodable text | 1 | 0.0% |

## The check that says the mirror is complete

**384 blobs classified as game tables. 384 `.tbl` files on disk.** Exact match, arrived at from two
directions that share no code — one by decompressing anonymous blobs and reading their magic bytes,
the other by listing a directory. That is the strongest evidence available that the mirror holds the
whole client and nothing was missed.

## Hardware, and what actually helped

The run used a 9950X3D (16C/32T) with 61.7 GB of RAM.

- **32 processes gave ~12,700 blobs/sec**, against roughly 200/sec single-threaded. Every blob is
  independent, so this is a clean parallel map and scaling is near linear.
- **RAM meant the mirror stays in page cache.** 17 GB against 61.7 GB — after the first pass there is
  effectively no disk cost.
- **The RTX 5090 contributed nothing, by design.** LZMA is sequential and branch-heavy: each symbol
  depends on decoder state left by the last one, which is the opposite of what a GPU accelerates.
  No CUDA LZMA beats 32 CPU threads here and writing one would cost more than the run saves. Stated
  rather than leaving the card idle and letting that look considered.

Multiprocessing rather than threads: `lzma` releases the GIL, but the classification work between
decompressions is Python and would serialise.

## What is written to disk, and what is not

Only the **text seam** becomes files — 191 Lua, 631 XML, 29 other. Everything else is censused and
discarded.

That is deliberate. 37 GB of decoded audio and textures answers no question this project has, and
would cost more to store than to regenerate in 15 seconds. The census keeps the hash, the kind, and
both sizes, so any blob can be re-decoded on demand.

## Where the value is

The text seam is 0.4% of the blobs and carries almost everything useful: Carbine's own UI source, the
UI forms, and — the single richest file in the mirror — `Documentation.xml`, the client's own API
reference, now expanded into 147 documents under `docs/client-api/`.

## Still unopened

- **11,651 area blobs** — map and zone data, format unexamined
- **1,017 unknown** — no recognised magic; the most likely place a format nobody has named is hiding
- **10 nested `KCAP` archives** — archives inside the archive
- **`ClientData.archive`**, 13.1 GB, separate from this mirror, with a 12.4 MB index holding
  **45,004 real filenames**. The mirror is content-addressed and nameless; that index is the thing
  that could give all 197,333 blobs their real names.
