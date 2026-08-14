# `.i3` internal structure

Parsed, not grepped: a chunk is accepted only when its declared size fits the buffer
and lands exactly on the next chunk boundary. A tag failing that is not a chunk,
however much it looks like one.

**1696 distinct files. 0 parsed cleanly as chunked (0.0%).**

## File header

| first 8 bytes | files |
|---|---|
| `464544531e000000` `FEDS....` | 1,283 |
| `4645444929000000` `FEDI)...` | 413 |

## Chunk tags

**None.** No file parsed as a chunk container, so this format
is not chunked in the way `.area` is - the header is followed by something else.

## Leaf payload heads

First bytes of payloads with no further chunk structure — the raw data itself.

