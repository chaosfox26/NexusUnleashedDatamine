# Unit

*Object, documented by the client itself.*

Any character in game, including players, NPCs, Banks, summoned Pets and Mounts, Vendors, and Ability Vendors

**273 calls.** 11 carry `Deprecated="true"` — reported, not filtered, because that flag is set on entries known to be alive in 16042.

### `AddTextBubble(?)`

Adds a text bubble above the unit with the specified text

| parameter | type | meaning |
|---|---|---|
| `?` | String | The text to put in the text bubble |

### `CanBeHarvestedBy(unitPlayer)`

Returns whether or not the player can harvest the selected unit.  Returns false if the unit is not a harvestable unit.

| parameter | type | meaning |
|---|---|---|
| `unitPlayer` | Unit | The function checks against this unit's tradeskills to see if the calling unit is harvestable |

**Returns** — `Boolean` Whether or not the unit can be harvested by the unit that was passed in

### `CanGrantXp()`

*no description in the client's documentation*

### `CanUpgradeWarplotStructure()`

Returns whether or not a character has permissions to upgrade a warplot structure during a match

**Returns** — `Boolean` Whether or not the player has permissions to upgrade structures

### `ClearTargetMarker()`

Removes a target marker from the unit

**Returns** — `Boolean` Whether or not the function finished successfully

### `ConvertResource(idConversion)`

Perform this unit's resource conversion operation if it has one

| parameter | type | meaning |
|---|---|---|
| `idConversion` | Integer | The id number for the resource conversion.  This value will generally come  from unit:GetResourceConversions() |

### `CreatureRisk()`

`deprecated flag set` *no description in the client's documentation*

### `FloatLootText(itemLooted, nCount)`

Spawns a floating display for the items the character loots

| parameter | type | meaning |
|---|---|---|
| `itemLooted` | Item | The item that was looted |
| `nCount` | Integer | The number of items in the stack that was looted |

### `GetAbsorptionMax()`

Returns the current maximum absorption amount for the character.   If the character has nothing giving them absorption, this returns 0.   If the unit has no health bar, this returns nil.

**Returns** — `Integer` The character's maximum absorption amount

### `GetAbsorptionValue()`

Returns the character's current absorption value.  If the unit loses whatever effect gave them absorption, this will return any unused absorption even though the max absorption value is 0.

**Returns** — `Integer` The character's current absorption value.

### `GetAchievementPoints()`

`deprecated flag set` Returns the character's achievement points.

**Returns** — `Integer` The number of achievement points the character has earned.

### `GetActivationState()`

Passes a table with information on whether a unit can be interacted with, as well as who can interact with them.

**Returns** — `Table` This table is indexed by CUnit's s_ActivationInfo array

> Carbine's own note: Not all elements in the return table have descriptions at  the moment

### `GetAffiliationName()`

Returns the name of the faction that the character is affiliated with

**Returns** — `String` The name of the faction that the unit is affiliated with

### `GetAlternateTarget()`

Gets the unit's current focus target

**Returns** — `Unit` The unit currently set as the player's focus target

### `GetArchetype()`

Returns an NPC's archetype

**Returns** — `Table` 

> Carbine's own note: This needs TCreature2ArcheTypeId to be accessible by Lua

### `GetArmorPierce()`

*no description in the client's documentation*

### `GetArmorPierceRating()`

*no description in the client's documentation*

### `GetArmorPierceRatingPercent()`

*no description in the client's documentation*

### `GetAssaultAndSupportPowerSoftcap()`

Returns the softcap for Assault and Support power

**Returns** — `Integer` The current softcap for both Assault and Support power

### `GetAssaultPower()`

Returns the player's current Assault Power

**Returns** — `Integer` The player's Assault Power

### `GetAssaultRating()`

*no description in the client's documentation*

### `GetAttachmentPosition(nAttachmentIdx)`

Gets the position of the selected attachment

| parameter | type | meaning |
|---|---|---|
| `nAttachmentIdx` | Integer | The attachment you want to find the position for |

**Returns** — `Table` 

### `GetAuctionableItems()`

Gets a list of all the items the player can throw up on the Auction House

**Returns** — `itemSellable` An array of items that the player is able to sell on the Auction House

### `GetBankItems()`

*no description in the client's documentation*

### `GetBaseLifesteal()`

`deprecated flag set` Gets the unit's base life-steal amount

**Returns** — `Float` The base amount of life-steal the unit has

### `GetBasicStats()`

Returns a table containing a unit's most basic information

**Returns** — `Table` 

### `GetBindPointString()`

Returns the name of the last place the character set their bind point.

**Returns** — `String` The name of the character's current bind point

### `GetBuffs()`

Returns a table containing all of the positive and negative buffs on the unit

**Returns** — `Table` A table containing information on all of the positive and negative buffs on the unit

### `GetBuybackItems()`

Returns a list with info on the items that the players can buy back from a vendor

**Returns** — `Table` 

### `GetCCDurationModifier()`

Returns any modifiers to Crowd Control duration on the player.

**Returns** — `Integer` The crowd control duration modifier on the player

### `GetCCDurationRatingPercent()`

*no description in the client's documentation*

### `GetCCResilience()`

*no description in the client's documentation*

### `GetCCStateTimeRemaining()`

Returns the remaining time that the unit is under crowd control effects

**Returns** — `Integer` The remaining time the unit has to spend in a crowd control state (in milliseconds)

### `GetCCStateTotalTime()`

*no description in the client's documentation*

### `GetCastBarType()`

Returns the player's current cast bar type from the Unit.CodeEnumCastBarType table

**Returns** — `Integer` The type of cast bar that should be displayed when the unit uses an ability

### `GetCastDuration()`

Returns the cast time of the spell that the unit is currently attempting to cast.  If no spell is being cast, this returns 0.

**Returns** — `Integer` The cast time of the spell that the unit is currently attempting to cast (in milliseconds)

### `GetCastElapsed()`

Returns the amount of time since the unit began to cast an ability.  If the unit is not currently casting an ability, this returns 0.

**Returns** — `Integer` The amount of time since the the unit began to cast the ability (in milliseconds)

### `GetCastName()`

Returns the name of the spell that the unit is currently casting.  Returns an empty string if the character is not casting.

**Returns** — `String` Returns the name of the spell that the unit is casting.

### `GetCastTotalPercent()`

Returns the percentage of the cast time that has elapsed for the spell that the unit is casting

**Returns** — `Integer` The percentage of the cast time that is completed

### `GetClassId()`

Returns the unit's class ID

**Returns** — `Integer` The unit's class ID.  This value corresponds with the GameLib.CodeEnumClass enum.

### `GetClusterContributionValue()`

*no description in the client's documentation*

> Carbine's own note: Unknown.  Will have to speak with designers on this one

### `GetClusterInformation()`

Returns information on the cluster that the unit belongs to

**Returns** — `Table` 

> Carbine's own note: This function needs an enum for cluster difficulty

### `GetClusterUnits()`

Returns a list of units in the unit's cluster

**Returns** — `Unit` An array of the units in the cluster

### `GetCommodityItems()`

Returns list of the player's commodity items.  This does not work for NPCs

**Returns** — `Item` An array of commodity items in the player's inventory

### `GetConColor()`

Returns a color that corresponds with the unit's difficulty in relation to the player's.

**Returns** — `CColor` The color value representing the level difference between the player and the unit.

> Carbine's own note: This needs to be changed to ApolloColor

### `GetConValue()`

Returns the integer representing the level difference between the player and the unit

**Returns** — `Integer` The integer representing the level difference between the player and the unit.  This value corresponds with the CodeEnumLevelDifferentialAttribute enum

### `GetCooldownReductionModifier()`

The modifier that the unit's cooldowns are reduced by

**Returns** — `Integer` The unit's cooldowns are reduced by this amount

### `GetCraftingStationTradeskills()`

Returns a list of tradeskills that can be used at this crafting station.  Returns nil if the unit is not a crafting station

**Returns** — `Table` This array will contain info on every tradeskill that can be used at this station

### `GetCreatureRisk()`

*no description in the client's documentation*

### `GetCritChance()`

Returns the chance that the unit's attacks will be a critical hit

**Returns** — `Float` The chance that the unit's attacks will be a critical hit

### `GetCritRating()`

*no description in the client's documentation*

### `GetCritRatingPercent()`

*no description in the client's documentation*

### `GetCritSeverity()`

Returns how much extra damage is done when one of the unit's abilities lands a critical hit

**Returns** — `Float` The amount of extra damage that is done when the unit lands a critical hit

### `GetCritSeverityRating()`

*no description in the client's documentation*

### `GetCritSeverityRatingPercent()`

*no description in the client's documentation*

### `GetCriticalMitigation()`

*no description in the client's documentation*

### `GetCriticalMitigationRating()`

*no description in the client's documentation*

### `GetCriticalMitigationRatingPercent()`

*no description in the client's documentation*

### `GetCurrentWarplotTier()`

Returns the tier of a Warplot plug.  If this is called for any unit other than a Warplot plug, this returns nil.

**Returns** — `Integer` The current tier of a Warplot plug

### `GetCurrentWarplotUpgradeCost()`

Returns the number of Nanopacks needed to upgrade the selected Warplot plug.  This returns nil if called from any unit that is not a Warplot plug.

**Returns** — `Integer` The number of Nanopacks needed to upgrade the selected Warplot plug.

### `GetDamageReflectAmount()`

*no description in the client's documentation*

### `GetDamageReflectAmountRating()`

*no description in the client's documentation*

### `GetDamageReflectAmountRatingPercent()`

*no description in the client's documentation*

### `GetDamageReflectChance()`

*no description in the client's documentation*

### `GetDamageReflectRating()`

*no description in the client's documentation*

### `GetDamageReflectRatingPercent()`

*no description in the client's documentation*

### `GetDeflectChance()`

Returns the unit's chance to deflect attacks

**Returns** — `Float` The unit's chance to deflect attacks

### `GetDeflectCritChance()`

The unit's chance to deflect critical hits

**Returns** — `Float` The unit's chance to deflect critical hits

### `GetDeflectCritRating()`

*no description in the client's documentation*

### `GetDeflectCritRatingPercent()`

*no description in the client's documentation*

### `GetDeflectRating()`

*no description in the client's documentation*

### `GetDeflectRatingPercent()`

*no description in the client's documentation*

### `GetDifficulty()`

Returns the difficulty of the cluster

**Returns** — `Integer` The cluster's difficulty.

> Carbine's own note: This should be depricated.  We get the same info (and more) in  GetClusterInformation

### `GetDispositionTo(?)`

Returns a unit's disposition to another unit

| parameter | type | meaning |
|---|---|---|
| `?` | Unit | The unit that the calling unit is being compared to |

**Returns** — `Integer` A number representing the calling unit's disposition to another unit.  This number correlates to CodeEnumDisposition.

### `GetEffectiveItemLevel()`

*no description in the client's documentation*

### `GetEliteness()`

Returns an enum representing the unit's eliteness level

**Returns** — `Integer` The unit's eliteness level.  This number corresponds with CodeEnumEliteness

### `GetEquippedItems()`

Returns an array containing all of the unit's equipped items.

**Returns** — `Item` An array of all of the items the unit has equipped

### `GetFacing()`

Returns the direction the unit is facing, in x,y,z coordinates.

**Returns** — `Table` 

### `GetFaction()`

Gets the ID for the faction that the unit belongs to

**Returns** — `Unit.CodeEnumFaction` The ID for the faction that the unit belongs to

### `GetFlightPathToPoint()`

Returns a table containing the price of the flight and each node that the path passes through

**Returns** — `Table` 

### `GetFlightPaths()`

Returns a list of flight paths that are available from a Taxi NPC. Returns nil if the unit isn't a Taxi NPC

**Returns** — `Table` An array containing information for each of the Taxi's connections.

### `GetFocus()`

*no description in the client's documentation*

### `GetFocusCostModifier()`

*no description in the client's documentation*

### `GetFocusRegenInCombat()`

*no description in the client's documentation*

### `GetFocusRegenNonCombat()`

*no description in the client's documentation*

### `GetFocusRegenRatingPercent()`

*no description in the client's documentation*

### `GetGender()`

Returns an integer representing the unit's gender.

**Returns** — `Integer` Returns an integer representing the unit's gender.  This corresponds with the CodeEnumGender enum

### `GetGlanceAmount()`

*no description in the client's documentation*

### `GetGlanceAmountRating()`

*no description in the client's documentation*

### `GetGlanceAmountRatingPercent()`

*no description in the client's documentation*

### `GetGlanceChance()`

*no description in the client's documentation*

### `GetGlanceRating()`

*no description in the client's documentation*

### `GetGlanceRatingPercent()`

*no description in the client's documentation*

### `GetGroupValue()`

Returns the cluster's difficulty value

**Returns** — `Integer` 

> Carbine's own note: How is this different from the cluster's difficulty?  What does the return value correspond with?

### `GetGuildName()`

Returns the unit's guild's name.  Note that this will specifically get the guild and not other guild types such as warparties, circles, or arena teams.

**Returns** — `String` The name of the player's guild

### `GetGuildType()`

Returns the unit's guild type

**Returns** — `Integer` 

> Carbine's own note: What should this return?  The type of the guild that's on their  nameplate?

### `GetHarvestRequiredTradeskillName()`

Returns the name of the tradeskill required to harvest a node.  Note, some units are labeled as "Harvestable", but do not require a tradeskill and generally  do not provide materials.

**Returns** — `String` The name of the tradeskill required to harvest the node.

### `GetHarvestRequiredTradeskillTier()`

Returns the tier of the tradeskill required to harvest a node.  Note that there are some nodes that are labeled as "Harvest", but do not require a tradeskill. These nodes do not provide mats.

**Returns** — `Integer` The tradeskill tier required to harvest the node

### `GetHeading()`

Returns the heading of the unit

**Returns** — `Float` The heading of the unit in degrees.

> Carbine's own note: What is this?  In degrees?

### `GetHealth()`

Returns the unit's current HP

**Returns** — `Integer` The unit's current HP

### `GetId()`

Returns the unit's ID

**Returns** — `Integer` The unit's ID

### `GetIgnoreArmorBase()`

`deprecated flag set` Returns unit's armor penetration percent

**Returns** — `Float` The unit's armor penetration percent

### `GetIgnoreShieldBase()`

Returns the unit's shield penetration percent

**Returns** — `Float` The unit's shield penetration percent

### `GetInfo()`

*no description in the client's documentation*

> Carbine's own note: This should be deleted in the code

### `GetInstancePortalCompletionTime()`

Returns the expected completion time of the instance inside an instance portal

**Returns** — `Integer` The expected completion time of the instance, in minutes

### `GetInstancePortalLevelRange()`

Returns the level range for an instance inside an instance portal.  Returns nil if the unit is not an instance portal.

**Returns** — `Table` 

### `GetInstancePortalRemainingTime()`

The group's remaining time to finish an instance.

**Returns** — `Integer` The group's remaining time to finish an instance, in seconds

### `GetIntensity()`

*no description in the client's documentation*

### `GetIntensityRating()`

*no description in the client's documentation*

### `GetIntensityRatingPercent()`

*no description in the client's documentation*

### `GetInterruptArmorMax()`

Returns the maximum amount of interrupt armor the unit can have

**Returns** — `Integer` The maximum amount of interrupt armor for the unit

### `GetInterruptArmorValue()`

The amount of interrupt armor currently on the unit

**Returns** — `Integer` The amount of interrupt armor currently on the unit

### `GetInventoryItems()`

Returns a list of the player's inventory items.  Calling this on anyone but the current player returns an empty table.

**Returns** — `Table` An array containing player's items and the corresponding bag slot that they are found in

### `GetLevel()`

Returns the unit's level

**Returns** — `Integer` The unit's level

### `GetLevelDifferential(unitTarget)`

Returns an integer representing the unit's level differential with the specified unit

| parameter | type | meaning |
|---|---|---|
| `unitTarget` | unit | The unit that the source unit is being compared to |

**Returns** — `Integer` An integer representing the level differential between the source unit and the target.  This value corresponds with the CodeEnumLevelDifferential enum

### `GetLevelString()`

Returns a localized string that includes a label and the unit's effective level

**Returns** — `String` A string containing a label ("Level: " in English) and the unit's effective level

### `GetLifesteal()`

*no description in the client's documentation*

### `GetLifestealRating()`

*no description in the client's documentation*

### `GetLifestealRatingPercent()`

*no description in the client's documentation*

### `GetLoot()`

Returns a list of dropped loot that belongs to the player

**Returns** — `Table` There are multiple combinations of variables found in the table.  Each combination is dependant on which  type

### `GetMagicMitigation()`

Returns the unit's magic resistance

**Returns** — `Float` The percentage of magic abilities that are mitigated by the unit

### `GetMagicMitigationRating()`

*no description in the client's documentation*

### `GetMagicMitigationRatingPercent()`

*no description in the client's documentation*

### `GetMana()`

`deprecated flag set` Returns the unit's current amount of mana

**Returns** — `Float` The unit's current amount of mana

### `GetManaCostModifier()`

`deprecated flag set` Returns the current modifier to the mana cost of the unit's abilities

**Returns** — `Float` The modifier to the mana cost of the unit's abilities

### `GetManaRegenInCombat()`

`deprecated flag set` Returns the amount of Focus the unit regens during combat

**Returns** — `Float` The amount of Focus the unit regens in combat

### `GetManaRegenNonCombat()`

`deprecated flag set` The amount of Focus the unit regens outside of combat

**Returns** — `Float` The amount of Focus the unit regens outside of combat

### `GetMaxFocus()`

*no description in the client's documentation*

### `GetMaxHealth()`

Returns the unit's maximum health

**Returns** — `Integer` The unit's maximum health

### `GetMaxMana()`

`deprecated flag set` Returns the unit's maximum Focus

**Returns** — `Integer` The unit's maximum Focus

### `GetMaxResource(iResource)`

The maximum value for the specified resource

| parameter | type | meaning |
|---|---|---|
| `iResource` | Integer | An integer representing the various resources.  0 = Endurance.  Endurance is the resource used while sprinting.  1 = Kinetic Energy (Warriors), Volatility (Engineers), Psi Points (Esper), Power Cores (Medic), and is not used for stalkers   2 - 3 = Unused  4 = Suit Power (stalkers) 5-7 = Unused |

**Returns** — `Integer` The maximum value for the specified resource

### `GetMinResource(iResource)`

Returns the minimum amount of the given resource that the unit can have

| parameter | type | meaning |
|---|---|---|
| `iResource` | Integer | An integer representing the various resources.  0 = Endurance.  Endurance is the resource used while sprinting.  1 = Kinetic Energy (Warriors), Volatility (Engineers), Psi Points (Esper), Power Cores (Medic), and is not used for stalkers   2 - 3 = Unused  4 = Suit Power (stalkers) 5-7 = Unused |

**Returns** — `Integer` The minimum amount of a given resource that the unit can have

### `GetMiniMapMarker()`

`deprecated flag set` Returns the name for the character's marker on the minimap

**Returns** — `String` A string representing the character's position on the minimap

> Carbine's own note: Is this even being used correctly?

### `GetMiniMapMarkers()`

*no description in the client's documentation*

### `GetMountHealth()`

Returns the current health of the mount that the unit is riding

**Returns** — `Integer` The current health of the omount that the unit is riding

### `GetMountMaxHealth()`

The maximum health of the mount that the unit is riding

**Returns** — `Integer` The maximum health of the mount that the unit is riding

### `GetMouseOverType()`

Returns a string describing the unit's target frame type

**Returns** — `String` Returns "Simple" for units that have no HP and cannot be attacked or "Normal" for the rest

### `GetMultiHitAmount()`

*no description in the client's documentation*

### `GetMultiHitAmountRating()`

*no description in the client's documentation*

### `GetMultiHitAmountRatingPercent()`

*no description in the client's documentation*

### `GetMultiHitChance()`

*no description in the client's documentation*

### `GetMultiHitRating()`

*no description in the client's documentation*

### `GetMultiHitRatingPercent()`

*no description in the client's documentation*

### `GetName()`

Returns the name of the unit

**Returns** — `String` The unit's name

### `GetNameplateColor()`

Returns an ApolloColor for the unit's nameplate

**Returns** — `ApolloColor` The current color of the unit's nameplate

### `GetOverheadAnchor()`

Returns a table with the x, y, and z positions for the unit's nameplate (in relation to the model)

**Returns** — `Table` A table containing the x, y, and z positions for the unit's nameplate

### `GetPhysicalMitigation()`

Returns the unit's physical mitigation percent

**Returns** — `Float` The percent of physical damage that is mitigated by the unit

### `GetPhysicalMitigationRating()`

*no description in the client's documentation*

### `GetPhysicalMitigationRatingPercent()`

*no description in the client's documentation*

### `GetPlayerMovementSpeed()`

*no description in the client's documentation*

### `GetPlayerPathType()`

Returns the unit's path.  If the unit is not a player, returns nil.

**Returns** — `Integer` A number representing the unit's path.  This value corresponds with the  PlayerPathLib.PlayerPathType int constants.

### `GetPosition()`

Returns a table with the unit's position in x, y, and z coordinates

**Returns** — `Table` The unit's position in x, y, and z coordinates

### `GetPrereqInfo(idPrereq)`

Validates that the player meets the prerequisites for an item and returns a table with the results

| parameter | type | meaning |
|---|---|---|
| `idPrereq` | Integer | The ID number for the item whose prerequisites are being checked |

**Returns** — `Table` 

### `GetPvPDamageI()`

*no description in the client's documentation*

### `GetPvPDamageO()`

*no description in the client's documentation*

### `GetPvPDefenseI()`

*no description in the client's documentation*

### `GetPvPDefenseO()`

*no description in the client's documentation*

### `GetPvPDefensePercent()`

Returns the percent of damage that is mitigated during PvP

**Returns** — `Float` The percent of damage that is mitigated during PvP

### `GetPvPDefenseRating()`

Returns the unit's PvP Defense Rating

**Returns** — `Float` The unit's PvP Defense Rating

### `GetPvPDefenseRatingPercent()`

*no description in the client's documentation*

### `GetPvPHealingI()`

*no description in the client's documentation*

### `GetPvPHealingO()`

*no description in the client's documentation*

### `GetPvPOffensePercent()`

Returns the percent of extra damage the player does in PvP

**Returns** — `Float` The percent of extra damage the unit does in PvP

### `GetPvPOffenseRating()`

Returns the unit's PvP Offense Rating

**Returns** — `Float` The unit's PvP Offense Rating

### `GetPvPOffenseRatingPercent()`

*no description in the client's documentation*

### `GetRaceId()`

Returns a number representing the unit's race

**Returns** — `Integer` A number representing the unit's race.  This value corresponds with the GameLib.CodeEnumRace enum

> Carbine's own note: Why do we have a GetRaceID and GetUnitRaceId?

### `GetRank()`

Returns an integer representing the unit's difficulty rank

**Returns** — `Integer` An integer representing the unit's difficulty rank.  This value corresponds with the  Unit.CodeEnumRank enum

### `GetRechargeableItems()`

*no description in the client's documentation*

### `GetRepTurninItems()`

Returns information on what items the player is carrying that can count as reputation for the given unit's faction

**Returns** — `Table` An array containing information on each of the items that the player is holding that can be turned in for reputation

> Carbine's own note: Not currently used in UI

### `GetRepairableItems()`

Returns a list with information on the items that the unit owns that can be repaired

**Returns** — `Table` 

### `GetResource(nResource)`

Returns the amount of the specified resource that the unit has

| parameter | type | meaning |
|---|---|---|
| `nResource` | Integer | The Resource number that the player is polling |

**Returns** — `Integer` The amount of the given resource that the unit has

### `GetResourceConversions()`

Returns a list of resource conversions that the unit is able to perform.  If the unit is not able to perform resource conversions, this returns nil.

**Returns** — `Table` An array containing each of the conversions available through the NPC

### `GetResourceIcon(nResource)`

Returns the name of a resource's icon

| parameter | type | meaning |
|---|---|---|
| `nResource` | Integer | The Resource being polled. |

**Returns** — `String` The name of the given resource's icon.

> Carbine's own note: Not currently used in UI

### `GetResourceTooltip(nResource)`

Returns the tooltip string for the given resource

| parameter | type | meaning |
|---|---|---|
| `nResource` | Integer | The resource being polled for its tooltip |

**Returns** — `String` The tooltip string for the given resource

> Carbine's own note: Not called by UI

### `GetRewardInfo()`

Returns a table containing information on all of the active quests, missions, challenges, and public events that this unit is the target of

**Returns** — `Table` An array containing information on each thing that the unit is the objective of.  Each type has its own variables.

### `GetSettlerImprovementInfo()`

Returns information on Settler Improvements.  Returns an empty table if the unit is not a Settler Improvment

**Returns** — `Table` 

### `GetSettlerRewardName()`

*no description in the client's documentation*

> Carbine's own note: Unknown.  It's used in tooltips, but I can't seem to find anything that is one.

### `GetShieldCapacity()`

Returns the unit's current shield value

**Returns** — `Integer` The unit's current shield value

### `GetShieldCapacityMax()`

Returns the unit's maximum shield value

**Returns** — `Integer` The unit's maximum shield value

### `GetShieldMitigationPct()`

*no description in the client's documentation*

### `GetShieldRebootTime()`

Returns the amount of time the unit needs to go without taking damage before their shields start to regenerate

**Returns** — `Float` The amount of time between shield regen tics

### `GetShieldRegenPct()`

Returns the percent of the unit's maximum shields that are regenerated each tic

**Returns** — `Float` The percent of the unit's maximum shields that are regenerated each tic

### `GetShieldTickTime()`

Returns the intervals at which the unit's shields regenerate, in seconds

**Returns** — `Float` The intervals at which the unit's shields regenerate, in seconds.

### `GetSpellMechanicId()`

Returns the unit's spell mechanic ID number

**Returns** — `Integer` The unit's spell mechanic ID number

> Carbine's own note: Depricated?

### `GetSpellMechanicPercentage(nResource)`

Returns the percentage of the given resource the unit has.

| parameter | type | meaning |
|---|---|---|
| `nResource` | Integer | The resource that is being polled |

**Returns** — `Float` The percentage of the given resource the unit has

> Carbine's own note: Depricated?

### `GetStandState()`

Returns the unit's stand state

**Returns** — `String` The unit's stand state.

### `GetStrikethroughChance()`

Returns the unit's strikethrough chance

**Returns** — `Float` The percent chance the unit has to not have the target deflect the attack

### `GetStrikethroughRating()`

*no description in the client's documentation*

### `GetStrikethroughRatingPercent()`

*no description in the client's documentation*

### `GetSupplySatchelItems()`

Returns a list of items and information on the contents of the player's Supply Satchel.  Note, this returns an empty table if this is called on someone other than the player

**Returns** — `Table` 

### `GetSupportPower()`

Returns the unit's support power

**Returns** — `Float` The unit's support power

### `GetSupportRating()`

*no description in the client's documentation*

### `GetTarget()`

Returns the unit's current target

**Returns** — `Unit` The unit's current target

### `GetTargetMarker()`

Returns a number representing the target marker on the unit

**Returns** — `Integer` A number representing the target marker on the unit

### `GetTargetOfTarget()`

Returns the target of the unit being targeted by the calling unit

**Returns** — `Unit` The target of the unit being targeted by the calling unit

### `GetTechMitigation()`

Returns the percent of tech damage that is mitigated by the unit

**Returns** — `Float` The percent of tech damage that is mitigated by the unit

### `GetTechMitigationRating()`

*no description in the client's documentation*

### `GetTechMitigationRatingPercent()`

*no description in the client's documentation*

### `GetTitle()`

Returns the title that the unit is displaying

**Returns** — `String` The title that the unit is displaying

### `GetTitleOrName()`

If the unit has a title set, this returns it.  If it doesn't, this returns the name of the unit

**Returns** — `String` The title of the unit if it has one set.  The name of the unit if it doesn't.

### `GetTrainerTradeskills()`

Returns a list of tradeskills available at the trainer.  If the unit is not a tradeskill trainer, this returns nil.

**Returns** — `Table` The name and ID of each tradeskill available

### `GetTransferDestination()`

Returns the destination of a taxi route that transfers the player to another zone

**Returns** — `String` The name of the destination

### `GetType()`

Returns the unit's type

**Returns** — `String` The unit's type

### `GetUnitMount()`

Returns the unit's mount

**Returns** — `Unit` The unit's current mount

### `GetUnitOwner()`

Returns the owner of a pet.

**Returns** — `Unit` The unit who owns the pet

### `GetUnitProperties()`

Returns a table with information on each of the unit's properties

**Returns** — `Table` 

### `GetUnitProperty(eProperty)`

Returns information on the specified property for the unit

| parameter | type | meaning |
|---|---|---|
| `eProperty` | Integer | This value corresponds with the Unit.CodeEnumProperties table |

**Returns** — `Table` 

### `GetUnitRaceId()`

Returns the ID number for the unit's race

**Returns** — `Integer` The race's ID number.  This value corresponds with the GameLib.CodeEnumRace enum

> Carbine's own note: Why do we have a GetRaceID and GetUnitRaceId?

### `GetVehicle()`

Returns the vehicle the unit is currently riding

**Returns** — `Unit` The vehicle that the unit is riding

### `GetVendorGroups()`

Returns a table with item categories for a vendor.  If this unit is not a vendor, this table is empty

**Returns** — `Table` 

### `GetVendorItems()`

Returns an array containing information on each item the vendor sells

**Returns** — `Table` 

### `GetVigor()`

*no description in the client's documentation*

### `GetVigorRating()`

*no description in the client's documentation*

### `GetVigorRatingPercent()`

*no description in the client's documentation*

### `GetVitalTable(?)`

A function that returns a list of several of the character's vital statistics.  This table is indexed by the CodeEnumVital enum.

| parameter | type | meaning |
|---|---|---|
| `?` | Table | A table containing a list of the character's vitals, sorted by index, using the values from CodeEnumVitals as indexes |

### `HasTextBubble()`

A function that determines whether or not the unit has a text bubble over their head

**Returns** — `Boolean` Whether or not the unit has a text bubble over their head

### `HasTitle()`

Determines whether or not the unit is displaying a title

**Returns** — `Boolean` 

### `Inspect()`

Performs the Inspect action on the given unit.  This will cause the Inspect event to be fired

### `InviteToGroup()`

Sends a group invitation request to the target player

### `IsACharacter()`

Determines whether the unit is a player or not.

### `IsAccountFriend()`

Determines whether or not the specified unit is an Account Friend

**Returns** — `Boolean` 

### `IsCasting()`

Determines whether or not the unit is casting

**Returns** — `Boolean` 

### `IsCertainDeath()`

*no description in the client's documentation*

### `IsCurrentBindPoint()`

Determines whether or not the specified bind point is the user's current bind point.

**Returns** — `Boolean` 

### `IsDead()`

Determines whether or not the unit is dead or not

**Returns** — `Boolean` 

### `IsElite()`

Not currently returning anything

> Carbine's own note: Does this have a use anymore?

### `IsFriend()`

Determines whether or not the unit is a friend.  This does not include account level friends

**Returns** — `Boolean` 

### `IsFriendlyWarplotStructure()`

Determines whether or not the selected unit is both a warplot plug and if it's friendly

**Returns** — `Boolean` Returns true if both the unit is a plug and if it is friendly

### `IsIgnored()`

Determines whether or not the selected player is ignored

**Returns** — `Boolean` 

### `IsInCCState()`

Determines whether or not the unit is being affected by crowd control

**Returns** — `Boolean` 

### `IsInCombat()`

*no description in the client's documentation*

### `IsInVehicle()`

*no description in the client's documentation*

### `IsInYourGroup()`

Determines whether or not the given unit is in the player's group

**Returns** — `Boolean` 

### `IsInstanceLockbox()`

*no description in the client's documentation*

### `IsInventorySlotLocked(nLocation)`

Determines whether or not the specified inventory slot is locked

| parameter | type | meaning |
|---|---|---|
| `nLocation` | Integer | The inventory location of the item |

**Returns** — `Boolean` 

### `IsMentoring()`

Determines whether or not the selected unit is mentoring another player

**Returns** — `Boolean` 

### `IsMounted()`

Determines whether or not the unit is riding a mount

**Returns** — `Boolean` 

### `IsMyGhost()`

Determines whether or not the selected unit is the player's own ghost

**Returns** — `Boolean` 

### `IsOccluded()`

Determines whether or not the unit is currently hidden behind an object or terrain

**Returns** — `Boolean` 

### `IsPublicEventHub()`

Determines whether or not the unit is a Settler Infrastructure

**Returns** — `Boolean` 

### `IsPvpFlagged()`

Determines whether or not the unit is flagged for PvP

**Returns** — `Boolean` 

### `IsRallied()`

Determines whether or not the unit's level has been fixed due to rallying

**Returns** — `Boolean` 

### `IsRare()`

*no description in the client's documentation*

### `IsRival()`

Determines whether or not the unit is a rival

**Returns** — `Boolean` 

### `IsScaled()`

Determines whether or not the unit is scaled to the player's level

**Returns** — `Boolean` 

### `IsSettlerImprovement()`

Determines whether or not the unit is a settler improvement

**Returns** — `Boolean` 

### `IsSettlerReward()`

Determines whether or not the unit is a settler improvement with a reward

### `IsShieldOverloaded()`

Determines whether or not the unit's shields are overloaded

### `IsSoftKill()`

Determines whether or not the unit is eligible for open tagging.

**Returns** — `Boolean` 

### `IsTagged()`

Determines whether or not the unit has been tagged

**Returns** — `Boolean` 

### `IsTaggedByMe()`

Determines whether or not the current unit was tagged by the player

**Returns** — `Boolean` 

### `IsThePlayer()`

Determines whether or not the targeted unit is the player

**Returns** — `Boolean` 

### `IsValid()`

Determines whether or not the unit is valid.  Invalid units do not exist in the world.

### `IsVisibleInstancePortal()`

Determines whether or not the unit is an instance portal and if it is visible

**Returns** — `Boolean` 

### `IsVisibleOnCurrentZoneMinimap()`

Determines whether or not the unit is currently in the same section of the map and in the same instance

**Returns** — `Boolean` 

### `LockInventorySlot(nLocation)`

Locks the specified inventory slot for the current player

| parameter | type | meaning |
|---|---|---|
| `nLocation` | Integer | The inventory slot that should be locked |

### `PrepareInfractionReport()`

*no description in the client's documentation*

### `PurchaseFlightPath(idDestination)`

Purchases the flight path to the specified destination

| parameter | type | meaning |
|---|---|---|
| `idDestination` | Integer | The ID number of the flight path's destination. |

### `RequestRealmName()`

*no description in the client's documentation*

### `Resurrect(nRezTypeChoice, nRezData)`

Resurrect's the player based on the parameters passed

| parameter | type | meaning |
|---|---|---|
| `nRezTypeChoice` | Integer | Where the player should be resurrected |
| `nRezData` | Integer |  |

> Carbine's own note: Need enum for RezType.  Currently hardcoded in Death.lua. Need explanation for RezData.

### `SetAlternateTarget(unitNewFocus)`

Changes the player's focus target to the specified unit.  Clear the focus target by passing in nil.

| parameter | type | meaning |
|---|---|---|
| `unitNewFocus` | Unit | The unit that is set as the new focus target. |

### `SetTargetMarker(nMarker)`

Places the specified target marker above the unit.

| parameter | type | meaning |
|---|---|---|
| `nMarker` | Integer | The integer representing which target marker to assign to the unit |

### `ShouldDisplayMountHealth()`

*no description in the client's documentation*

### `ShouldShowBreathBar()`

Determines whether the player's breath bar should be shown.  This function will return false if it is called for any unit other than the current player.

**Returns** — `Boolean` Whether or not the player's breath bar should be shown.

### `ShouldShowCastBar()`

Determines whether or not the unit's cast bar should be shown.

**Returns** — `Boolean` Whether or not the unit's cast bar should be shown.

### `ShouldShowCraftingBar()`

Determines whether or not the unit's crafting progress bar should be shown.  This function returns false if called for any unit other than the current player.

**Returns** — `Boolean` Whether or not the unit's crafting progress bar should be shown

### `ShouldShowNamePlate()`

Determines whether or not the unit's nameplate should be shown.

**Returns** — `Boolean` Determines whether or not the unit's nameplate should be shown

### `ShowHintArrow()`

Places a guide arrow above the player's head that points them in the direction of the unit that called the function.

### `TakeShuttle()`

When called from a taxi NPC, this will summon the taxi for the player.

### `UnlockAllInventorySlots()`

Removes the locked state from all of the player's inventory slots.

### `UnlockInventorySlot(nInventoryLocation)`

Unlocks the specified inventory slot for the player.

| parameter | type | meaning |
|---|---|---|
| `nInventoryLocation` | Integer | The inventory slot number that should be unlocked |

### `__eq()`

`deprecated flag set` *no description in the client's documentation*

### `is()`

*no description in the client's documentation*

