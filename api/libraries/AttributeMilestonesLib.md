# AttributeMilestonesLib

*Library, documented by the client itself.*

This library contains functions for viewing a character's Attribute Milestones.  These milestones are reached when the player's attribute reaches a specific threshold.

**1 calls.**

### `GetAttributeMilestoneInfo(eClass)`

Gets information on all of the Attribute Milestones for the given class.

| parameter | type | meaning |
|---|---|---|
| `eClass` | GameLib.CodeEnumClass | The function will return the Attribute Milestones for this class. |

**Returns** — `Table` The Attribute Milestones and stat gains for the class.

> Carbine's own note: Do we still care about mini vs major milestones?

