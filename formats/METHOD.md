# How these formats were mapped

Carbine published no specification for `.m3`, `.tex`, `.area`, `.dgn`, `.i3`, `.sky` or `.sho`. No
public tool documents most of them. This is how they were characterised anyway, and — just as
important — where the characterisation stops.

## Populations, not files

Reading one file's bytes and proposing a layout is guesswork dressed as analysis. Reading **every
file of a type** turns it into measurement, because a field's behaviour across thousands of files
tells you what it is without anyone knowing the format:

| behaviour across the population | what it means |
|---|---|
| never varies | magic number or format version |
| correlates with file size (`r > 0.9`) | a count, a length, or an offset |
| always small, few distinct values | version, flag set, or enum |
| near-unique per file | an id or a hash |
| a run of printable bytes | a name the format references |

Correlation is Pearson's *r* against decompressed file size, computed over the whole population. Only
`r > 0.9` is reported as "tracks size". Nothing weaker is given a name.

## What this produced immediately

On `.dgn` — 953 files, 106 MB — the header analysis separated **two different formats sharing one
extension**:

- **221 files** with magic `NGND` (`DNGN` little-endian) and the value `6` at offset +4
- **732 files** with no magic at all, a small integer 0–6+ at offset 0, and `0` at offset +4

Offset +4 is the discriminator, and it was found by counting rather than by inspection. Two offsets
track size almost perfectly — `+8` at `r=0.999` and `+32` at `r=1.000` — so both are lengths or
offsets, and three slots are always zero across all 953 files.

Those 732 files are the ones the earlier census could not name at all. They only became visible as a
group once every file of the type was measured together.

## What it deliberately does not do

**It never prints a struct definition.** A plausible layout that nobody verified is worse than no
layout, because it gets used and then defended. Every line of every format document states what was
measured and over how many files.

This project has already paid for the alternative twice in one night: 83 methods filed under a
geometry class because adjacency looked convincing, and a spell scaling table read as player data
because the row counts were large. Both were confident, both were wrong, and neither announced
itself.

So where a field's role is genuinely unknown, the document says `varies` and gives the range. That is
a smaller claim than a struct, and it is one that will still be true next year.

## Deduplication matters

The client is content-addressed: 218,427 filenames resolve to 197,178 distinct hashes. Measuring by
filename would count the same bytes several times and skew every distribution toward whatever content
is most reused. Each format is analysed over **distinct hashes**, not names.

## Reproducing it

    python Tools/cdn-deep-analyse.py                 # every format
    python Tools/cdn-deep-analyse.py --ext .m3       # one
    python Tools/cdn-deep-analyse.py --sample 500    # quick pass

Each run rewrites `docs/client-formats/<ext>.md` from the files themselves. Nothing is cached, so a
document can never drift from the data it describes.
