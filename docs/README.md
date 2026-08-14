# Text assets recovered from the CDN mirror

`D:\CDN\Mirror\16042` is the game's content store: **197,333 blobs, 17 GB**, every file named for its
SHA1. There is no manifest and there are no filenames, so nothing states what any blob holds until
you open it.

Recovered by `python Tools/cdn-extract-text.py`.

## Provenance — read this before treating a name as real

**These files had no names.** The store is content-addressed. Each name here is
`<sha1-prefix>-<hint>.<ext>` where the hint is taken from **inside** the content — an XML root
element, or a Lua header comment. `0016e7561dfb-Client-Lua-Script-for-QuestLog.lua` is called that
because line 2 of the file says `-- Client Lua Script for QuestLog`, **not** because the client ever
called it `QuestLog.lua`.

A blob whose content suggests no name keeps its hash alone. Inventing a plausible filename would be
the same mistake as inventing an API method — and this project has now made that mistake twice
(`Apollo.GetAddons`, `QuestLib.GetActiveQuests`), both times undetectably.

`MANIFEST.tsv` carries the full SHA1 for every file, so anything here can be traced back to the exact
blob it came from.

## Why these are worth more than the other 99%

The store is overwhelmingly audio (42%), textures (31%) and models (19%). The text seam is a fraction
of a percent — and it is **Carbine's own UI source**, headed `Copyright (c) NCsoft`.

That matters because it shows the Apollo API **being used**, not merely named. The binary gives
2,152 method *names*; these files give argument order, return shapes, event wiring and the idioms the
API was designed around. `QuestLog.lua` opens with `require "Window" / "Quest" / "QuestLib" /
"QuestCategory" / "Unit" / "Episode" / "Money"` — that alone is a dependency map no string table
could produce.

## Ownership, and why "adapt not import" is mechanical rather than a policy

NCsoft's code, recovered from a client the operator owns. **Read all of it and document everything** —
that is the point of having it.

There is nothing here that *could* be pasted into `Source/` even if someone wanted to. These are Lua
scripts running on the Apollo UI runtime; our server is C#, on the other side of the wire, doing a
different job. The client draws a bar; the server owns the vital behind it. No file here has a
counterpart in our tree.

So what we take is never the code. It is **facts about the protocol and the data**:

- Spellslinger reads resource index 4, Stalker 3, the other four class 1
- the sprint meter is driven by `SprintEnergyUpdated`, not a generic vital update
- `tTiers[5]` is the player's Tier 4 — the array is offset by one
- `GetAbilitiesList` takes a spell tag; `GetAbilityInfo` takes two arguments or three

Those are measurements of how the game works, and they are what an independent reimplementation
needs. CLAUDE.md rule 2 already says adapt rather than import, and here adaptation is not a
restriction anyone is choosing — it is the only thing the difference in language and layer permits.

The repo is never pushed, which is the standing rule regardless.

## Layout

| directory | what it holds |
|---|---|
| `lua/` | client UI scripts |
| `xml/` | UI forms and sprite definitions |
| `text/` | everything else that decoded as text |
| `MANIFEST.tsv` | kind · sha1 · length · hint, for every recovered file |

## How the blobs were opened

The container is LZMA, but **not** the `lzma_alone` format Python expects. The header is five bytes —
one properties byte (`0x5D` = lc3 lp0 pb2) and a four-byte dictionary size (1 MB) — with no
uncompressed-size field. `FORMAT_ALONE` fails on every blob with *"Corrupt input data"*, which reads
like a corrupt mirror rather than a wrong reader; it needs `FORMAT_RAW` with an explicit LZMA1 filter
starting at offset 5.

That distinction is the whole reason this data was reachable. See `Tools/cdn-census.py` for the
container census and `docs/reference-data/cdn-blob-census.tsv` for the numbers.
