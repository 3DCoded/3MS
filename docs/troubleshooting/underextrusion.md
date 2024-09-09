---
comments: true
---

# Underextrusion

If your prints start to have gaps in the walls, you are likely experiencing underextrusion. Follow this troubleshooting guide to diagnose the issue and fix it.

## Extruder/Hotend Issues

First, try the solutions in [this](https://all3dp.com/2/under-extrusion-3d-printing-all-you-need-to-know/) article in case there are any issues with your printer's extruder/hotend.

## 3MS rotation_distance

If your extruder and hotend are working fine, the next likely cause of underextrusion is your 3MS rotation_distance is too high. There are two likely causes and solutions, based on where in the print the underextrusion occurs:

- Whole print - 3MS motors working backwards from the extruder or not working at all

    Follow the wiring section of [Assembly](assembly.md#wiring).
    
    Follow the first two steps of [Stepper Setup](steppers.md).

- Partially through print - 3MS motors not turning enough

    Follow the last step of [Stepper Setup](steppers.md#how-far-does-the-filament-move).
