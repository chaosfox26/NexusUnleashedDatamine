# `.area` internal structure

Parsed, not grepped: a chunk is accepted only when its declared size fits the buffer
and lands exactly on the next chunk boundary. A tag failing that is not a chunk,
however much it looks like one.

**1200 distinct files. 1200 parsed cleanly as chunked (100.0%).**

## File header

| first 8 bytes | files |
|---|---|
| `6165726100000000` `aera....` | 1,196 |
| `4145524100000000` `AERA....` | 4 |

## Chunk tags, by nesting depth

`depth:TAG` — depth 0 is a top-level chunk. **Occurrences** counts every instance;
**files** counts how many files contain at least one.

| tag | occurrences | files |
|---|---|---|
| `0:CHNK` | 1,200 | 1,200 |
| `0:PROp` | 503 | 503 |
| `0:CURT` | 164 | 164 |

## Leaf payload heads

First bytes of payloads with no further chunk structure — the raw data itself.

- `CHNK` — `e7120000010021108221842185218521`
- `PROp` — `01000000406000000000000000000000`
- `CHNK` — `f614000001200010ff1fff1fff1fff1f`
- `CHNK` — `14000001000000105d12000000000000`
- `CHNK` — `f61400000120001085218c218e218e21`
- `CHNK` — `f6140000012000109b20a120a420a520`
- `CHNK` — `8a0800ff00060000ff1fff1fff1fff1f`
- `CHNK` — `8a0800f000060000ff1fff1fff1fff1f`
- `CHNK` — `8a08000f00060000ff1fff1fff1fff1f`
- `CHNK` — `1000000000000000504f525004000000`
- `PROp` — `01000000000202000000000000000000`
- `CHNK` — `1000000000000000504f525004000000`
- `PROp` — `01000000000202000000000000000000`
