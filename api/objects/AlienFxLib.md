# AlienFxLib

*Object, documented by the client itself.*

Integration with Alienware's Alien FX library allowing lua to control hardware lights.

**11 calls.**

### `CanUse()`

Can the AlienFx library be used.

**Returns** — `Boolean` 

### `GetDeviceCount()`

How many devices are connected.

**Returns** — `Integer` 

### `GetDeviceDescription(nDeviceIndex)`

The description and type of the device.

| parameter | type | meaning |
|---|---|---|
| `nDeviceIndex` | Integer |  |

**Returns** — `Table` 

### `GetLightColor(nDeviceIndex, nLightIndex)`

What color is a certain light currently displaying.

| parameter | type | meaning |
|---|---|---|
| `nDeviceIndex` | Integer |  |
| `nLightIndex` | Integer |  |

**Returns** — `CColor` 

### `GetLightCount(nDeviceIndex)`

How many lights does a device have.

| parameter | type | meaning |
|---|---|---|
| `nDeviceIndex` | Integer |  |

**Returns** — `Integer` 

### `GetLightDescription(nDeviceIndex, nLightIndex)`

Get the description of a light.

| parameter | type | meaning |
|---|---|---|
| `nDeviceIndex` | Integer |  |
| `nLightIndex` | Integer |  |

**Returns** — `String` 

### `GetLightLocation(nDeviceIndex, nLightIndex)`

Get a lights x,y,z physical position, in centimeters, of any given light relative to the lower, left, rear corner of the device's bounding box.

| parameter | type | meaning |
|---|---|---|
| `nDeviceIndex` | Integer |  |
| `nLightIndex` | Integer |  |

**Returns** — `Table` 

### `IsReady()`

Is the Alien Fx library ready to be used.

**Returns** — `Boolean` 

### `Reset()`

*no description in the client's documentation*

### `SetLightColor(nDeviceIndex, nLightIndex, crLightColor)`

*no description in the client's documentation*

| parameter | type | meaning |
|---|---|---|
| `nDeviceIndex` | Integer |  |
| `nLightIndex` | Integer |  |
| `crLightColor` | CColor |  |

### `SetLocationColor(nLocationMask, crLightColor)`

Sets all lights for a location mask to a certain color.

| parameter | type | meaning |
|---|---|---|
| `nLocationMask` | Integer | Is a 32-bit mask that denotes one or more light positions in terms of the device's bounding box. There are 27 bits for each smaller cube within this bounding box, divided evenly. |
| `crLightColor` | CColor |  |

