# The 1,017 blobs with no recognised magic

Every blob in the mirror was classified by its first four bytes. 1,017 matched nothing known. This is
what they turned out to be — the place an unnamed format would hide, so it was worth opening all of
them rather than leaving a bucket labelled "unknown".

## Identified

| magic | blobs | what it is |
|---|---:|---|
| `BKHD` | 152 | **Wwise SoundBank.** Audiokinetic's format — the header of a compiled sound bank |
| `MZ\x90` | 23 | **Windows PE binaries.** The client's own executables and DLLs, shipped through the CDN alongside its data |
| `KB2i` | 19 | **Bink 2 video.** RAD Game Tools; the client ships `bink2w64.dll` to play them |
| `\x00\x01\x00\x00` | 17 | **TrueType/OpenType fonts** — `DSIG` and `GDEF` tables visible in the header |
| `XETL` | 3 | `LTEX` reversed — a texture container |

The PE files are the client itself: `d3dx9_43.dll` (2.4 MB, importing `d3d10.dll`/`d3d9d.dll`), a
371 KB library importing `WINMM.dll`, and two binaries over 10 MB that are almost certainly
`WildStar64.exe` and `Houston64.exe`. **The CDN mirror carries the program as well as the data**,
which means a complete client can be reconstructed from it.

## Not identified: the numbered family

**780 blobs** — the largest slice — share a shape rather than a magic. The first four bytes are a
small integer, and the header runs:

```
u32  n          0 … 15
u32  0
u32  count      varies
u32  0
u32  0, 0
u32  k          small
```

Distribution of `n`:

| n | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| blobs | 199 | 172 | 105 | 66 | 104 | 39 | 29 | 21 | 14 | 8 | 7 | 6 | 3 | 3 | 2 | 2 |

A monotonically decreasing count across a dense 0–15 range is characteristic of a **level, tier or
part index** — most assets having part 0, progressively fewer having higher parts.

**That is a shape, not an identification, and it is recorded as one.** Candidate readings include a
LOD level, a chunk sequence within a multi-part asset, and a version field; nothing here
distinguishes between them. Naming it on the strength of a plausible histogram is precisely the
inference that put 83 methods under `AaRect` earlier tonight.

The way to settle it is the same as every other question here: find one of these blobs whose content
is known from another direction — via `ClientData.index`, which holds 45,004 real filenames — and
read what it actually is.

## Why this matters more than 1,017 blobs

`BKHD` and `KB2i` mean the audio and video pipelines are standard third-party formats with existing
tooling, not bespoke Carbine containers. `MZ` means the mirror is a complete distribution rather than
a data-only cache.

And the 780 unnamed blobs are the largest single unexplained thing left in the client. Whatever they
are, no public tool names them.
