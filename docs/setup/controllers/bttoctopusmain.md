# BTT Octopus (main MCU)

!!! warning
    This configuration may not work with the BTT Octopus Pro.

**Max filament units: 4**

**MCU Name: `main`**

## main MCU

This configuration is a `main MCU` configuration, meaning that your printer should already be running off a BTT Octopus and you don't need to purchase one.

## BOM

Per filament unit:

[1x TMC2209](https://a.co/d/01KA3Y1) ($7 each)

## Wiring

Route the wires from the NEMA17's to the controller board. Follow this table to determine which port to plug the motors into:

| Filament Unit # | Motor Port |
| - | - |
| 0 | MOTOR7 |
| 1 | MOTOR6 |
| 2 | MOTOR5 |
| 3 | MOTOR4 |