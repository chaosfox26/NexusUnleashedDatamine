# CombatFloater

*Library, documented by the client itself.*

**8 calls.**

### `AddDigitSpriteSet(strSpriteSetName)`

Registers a sprite set that contains digits with the combat floater system.

| parameter | type | meaning |
|---|---|---|
| `strSpriteSetName` | String | The path and file name of the sprite set that was registered with the system. |

**Returns** — `Integer` The index that is assigned to the sprite set that was added to the system.

### `AddTextBGSprite(strSpriteName)`

Registers a background sprite with the float text system.

| parameter | type | meaning |
|---|---|---|
| `strSpriteName` | String | The path and file name of the sprite that should be registered with the system. |

**Returns** — `Integer` The index that was assigned to the sprite after it was registered.

### `HideTextFloater()`

Hides the CombatFloater from the screen.

### `SetMaxFloaterCount(nMaxFloaterCount)`

Sets the maximum number of floaters that can be on the screen at any one time.

| parameter | type | meaning |
|---|---|---|
| `nMaxFloaterCount` | Integer | The new maximum number of floaters. |

### `SetMaxFloaterPerUnitCount(nNewMaxFloaterCount)`

Sets the maximum number of floating text messages that will be shown for any single unit at the same time.

| parameter | type | meaning |
|---|---|---|
| `nNewMaxFloaterCount` | Integer | The new maximum number of floaters per unit. |

### `ShowParticleEffect(unitSource, tSettings)`

Displays a particle effect.

| parameter | type | meaning |
|---|---|---|
| `unitSource` | Unit | The unit that the floater is attached to. |
| `tSettings` | Table | A table that contains the various options that should be set for the particle effect. |

> Carbine's own note: Either this does not work or I'm doing it wrong.  I'm leaning towards doing it wrong.

### `ShowTextFloater(unitSource, nValue, strValue, tOptions)`

Displays a text floater coming from the specified unit.

| parameter | type | meaning |
|---|---|---|
| `unitSource` | Unit | The unit that the floater will be tied to. |
| `nValue` | Integer | The value that should be shown on the floater. |
| `strValue` | String | The text that should be shown on the floater. |
| `tOptions` | Table | A table that contains a laundry list of ways the text floater can be manipulated. |

> Carbine's own note: There's quite a few things in here that I'm kinda iffy about and would like to get clarification on.

### `TestTextFloater(eDamageType, nHealthChange, nShieldAbsorbAmount, bCritical)`

Passes the information given to the function back to the game in the form of a DamageOrHealingDone event.

| parameter | type | meaning |
|---|---|---|
| `eDamageType` | GameLib.CodeEnumDamageType | The type of damage that should be sent with the DamageOrHealingDone event. |
| `nHealthChange` | Integer | The amount that the player's health changed by (according to the test floater). |
| `nShieldAbsorbAmount` | Integer | The amount of damage that the unit's shield absorbed (according to the floater) |
| `bCritical` | Boolean | Whether the test floater should show a critical hit or not. |

