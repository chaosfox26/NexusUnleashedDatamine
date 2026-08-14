# DatacubeLib

*Library, documented by the client itself.*

A library that allows the player to interact with and get information on Datacubes, Journals, and Tales from Beyond the Fringe entries

**18 calls.**

### `GetDatacubesForVolume(idJournal)`

Gets a list of datacube sub-entries for a journal.

| parameter | type | meaning |
|---|---|---|
| `idJournal` | Integer | The id number for the journal entry that the results belong to. |

**Returns** — `Table` An array of tables that contain information on each sub-entry associated with the specified journal.

> Carbine's own note: Needs enum for DatacubeType.

### `GetDatacubesForZone(idZone)`

Gets a list of datacube entries that are found in a specific zone.

| parameter | type | meaning |
|---|---|---|
| `idZone` | Integer | The function will return the datacube entries found in the zone with this id. |

**Returns** — `Table` An array of tables that contain information on each datacube entry in the specified zone.

> Carbine's own note: Need enum for DatacubeType.

### `GetJournalsForZone(idZone)`

Gets a list of all the journal entries within a zone.

| parameter | type | meaning |
|---|---|---|
| `idZone` | Integer | The function will return the journal entries found in this zone. |

**Returns** — `Table` An array of tables that contain information on all of the journal entries within the zone.

### `GetLastUpdatedDatacube()`

Gets the information for the last datacube entry that was updated for the player.

**Returns** — `Table` Information on the player's most recently updated datacube entry.

### `GetTales()`

Gets information on all the Tales from Beyond the Fringe entries that the player has unlocked at least one part of.

**Returns** — `Table` Information on each Tales entry that the player has made progress on.

### `GetTalesForZone(idZone)`

Gets a list of all of the Tales entries that the player has made progress on within a specific zone.

| parameter | type | meaning |
|---|---|---|
| `idZone` | Integer | The function will get a list of Tales that are associated with the zone with this id. |

**Returns** — `Table` Information on each of the Tales entries that the player has unlocked at least one entry for in the specified zone.

### `GetTotalCollectionSize(eDatacubeType)`

Gets the total number of entries that the player has made progress on of a specific type.

| parameter | type | meaning |
|---|---|---|
| `eDatacubeType` | Integer | The function will return the number of entries that the player knows about of this type. This value corresponds with the DatacubeLib.DatacubeType set of constants. |

**Returns** — `Integer` The number of entries of a specific type that the player has made progress on.

### `GetTotalDatacubesForZone(idZone)`

Gets the number of entries within a zone that have the Datacube type.

| parameter | type | meaning |
|---|---|---|
| `idZone` | Integer | The function will get the number of Datacube entries in the zone with this id. |

**Returns** — `Integer` The number of datacube entries in the specified zone.

### `GetTotalJournalsForZone(idZone)`

Gets the number of journal entries within a specific zone.

| parameter | type | meaning |
|---|---|---|
| `idZone` | Integer | The function will get the number of journal entries in the zone with this id. |

**Returns** — `Integer` The number of journal entries found in the specified zone.

### `GetTotalTalesForZone(idZone)`

Gets the number of Tales entries in a specific zone.

| parameter | type | meaning |
|---|---|---|
| `idZone` | Integer | The function will get the number of Tales in the zone with this id. |

**Returns** — `Integer` The number of Tales entries in the specified zone.

### `GetTotalVolumeCount(idZone)`

Gets the number of journal entries within a specific zone.

| parameter | type | meaning |
|---|---|---|
| `idZone` | Integer | The id of the zone that the function will look through. |

**Returns** — `Integer` The number of journal entries within the specified zone.

### `GetVolumes()`

Gets a info on each journal entry that the player has unlocked at least one entry for.

**Returns** — `Table` Information on each journal entry that the player has unlocked at least one entry for.

### `GetZonesWithDatacubes()`

Gets a list of each zone that has a Datacube entry.

**Returns** — `Table` The id number and name of each zone that has a Datacube entry associated with it.

### `GetZonesWithJournals()`

Gets a list of each zone that has a journal entry associated with it.

**Returns** — `Table` The id number and name of each zone that has a journal entry associated with it.

### `GetZonesWithTales()`

Gets a list of each zone with a Tales entry associated with it.

**Returns** — `Table` A list with the id and name of each zone that has a Tales entry associated with it.

### `IsDatacubeComplete(idDatacube)`

Determines if an entry is complete.  This generally means whether the player has found all of the unlocks / sub-entries for the specified entry.

| parameter | type | meaning |
|---|---|---|
| `idDatacube` | Integer | The id for the entry that the function will check. |

**Returns** — `Boolean` Whether the player has interacted with each of the entry's unlocks / sub-entries or not.

### `PlayDatacubeSound(idDatacube)`

Plays the sound associated with the entry.

| parameter | type | meaning |
|---|---|---|
| `idDatacube` | Integer | The function will cause the entry with this id to play its sound. |

### `StopDatacubeSound(idDatacube)`

Stops the sound associated with a specific entry.

| parameter | type | meaning |
|---|---|---|
| `idDatacube` | Integer | The function will stop the sound associated with the datacube with this id. |

