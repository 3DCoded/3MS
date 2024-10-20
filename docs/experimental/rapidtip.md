---
comments: true
---

# Rapid Tip Shaping

!!! warning
    The rapid tip shaping feature is under construction. This page is not complete yet.

Rapid tip shaping allows for faster tip shaping and easier tuning of tip shaping.

## Installation

!!! info "TODO"

## Confiugration

!!! info "TODO"

## Tip Tuning

A standard tip tuning routine would look like this:

1. Load T0 to the nozzle

    ```gcode
    SYNC_TOOL TOOL=0
    MMMS_LOAD
    LOAD_FILAMENT
    ```

2. Run tip shaping:

    ```gcode
    FORM_TIP
    ```

3. Check your filament tip
4. Load the filament back to the nozzle for further tuning:

    ```gcode
    LOAD_FILAMENT
    ```

Steps 2-4 are repeated until your filament tip comes out looking like one of these:

!!! info "TODO Picture"

You can alter step 2 to get better tips, changing any of the following settings:

- `PUSH_DISTANCE`

    This changes how much filament is pushed out initially. Generally, you don't need to change this.

- `PUSH_SPEED`

    This changes how fast the filament is pushed out initially. Increasing this generally creates a sharper filament tip. However, if this is too high, your printer's hotend may not be able to melt the filament quickly enough and result in your extruder skipping steps.

- `INITIAL_RETRACT_SPEED`

    This changes how fast the filament tip is retracted to the cooling tube. If this is too low, your filament tip may have a large string on the end. If this is too high, a small piece of filament may be left in your nozzle.

- `COOLING_SPEED`

    This changes how fast the filament tip is retracted through the cooling tube. If this is too high, your filament tip may come out still molten.

- `FINAL_SPEED`

    This changes how fast the filament tip is retracted from the top of the cooling tube to outside the extruder. Generally, you can increase this until your printer's extruder starts skipping.

When you get a good tip, change to T1, repeat, T2, etc:

```
MMMS_UNLOAD
SYNC_TOOL TOOL=1
MMMS_LOAD
LOAD_FILAMENT
```

## Examples

!!! info "TODO show pictures of filament tips when a specific settings is altered"