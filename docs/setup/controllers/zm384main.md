# Zonestar ZM384 (main MCU)

**Max filament units: 3**

**MCU Name: `main`**

## main MCU

This configuration is a `main MCU` configuration, meaning that your printer should already be running off a ZM384 and you don't need to purchase one.

## Additional Setup

Ensure that E0 is the only extruder going directly to the hotend. Then, print out Y splitters (on the [Assembly](assembly.md) page) to combine E1, E2, and E3 into the main extruder. (E1, E2, and E3 will now be referred to as T0, T1, and T2, respectively.)

## Wiring

Route the wires from the NEMA17's to the controller board. Follow this table to determine which port to plug the motors into:

| Filament Unit # | Motor Port |
| - | - |
| 0 | E3 |
| 1 | E2 |
| 2 | E1 |