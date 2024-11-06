---
comments: true
---

# Rapid Tip Shaping

!!! warning
    The rapid tip shaping feature is currently experimental. This page is not complete yet.

Rapid tip shaping allows for faster tip shaping and easier tuning of tip shaping.

## Installation

Update your `3ms/main.cfg`:

```cfg title="3ms/main.cfg" hl_lines="7 11"
[save_variables]
filename: ~/printer_data/config/3ms/variables.cfg

[include ./settings.cfg]
[include ./endless/settings.cfg]
#[include ./cutter/settings.cfg]
[include ./form_tip/settings.cfg]
[include ./controllers/btt_skr_mini_e3_v2/steppers.cfg]

[dynamicmacros 3ms]
configs: 3ms/macros.cfg, 3ms/endless/macros.cfg, 3ms/form_tip/macros.cfg #, 3ms/cutter/macros.cfg
```

Note the addition of `3ms/form_tip/macros.cfg` in the `[dynamicmacros]` config section.

## Confiugration

The "cooling tube" refers to the length of PTFE found in your printer's hotend. This is usually in the heatsink of your hotend. 

You want to measure (or Google) three things:

1. The distance from the bottom of the cooling tube to the tip of the nozzle
2. The length of the cooling tube
3. The distance from the top of the cooling tube to your extruder

Update your `3ms/form_tip/settings.cfg` with these settings:

```cfg title="3ms/form_tip/settings.cfg" hl_lines="3-5"
[gcode_macro FORM_TIP_SETTINGS]
# Edit these settings for your printer
variable_cooling_tube_pos: 15 # <-- This is the distance from the bottom of the cooling tube to the tip of the nozzle
variable_cooling_tube_length: 11 # <-- This is the length of the cooling tube
variable_final_retract: 49 # <-- This is the distance from the top of the cooling tube to the extruder gears
```

The "parking position" refers to the location the toolhead will be at during a color swap (not on the wip tower). Ideally, this would be a purge bucket, but this can be anywhere **not** on the bed. 

Update your settings:

```cfg title="3ms/form_tip/settings.cfg"
variable_park_x: 125
variable_park_y: 205
variable_park_speed: 50 # mm/s
```

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

## Slicer Setup

Follow these steps to setup your slicer for rapid tip shaping. 

1. **Disable filament ramming**

    Nagivate to `Printer Settings` -> `Multimaterial` and uncheck the `Enable filament ramming` checkbox.

    ![](slicer9.png)

2. **Filament Settings**

    Repeat the following steps for each of your filaments.

    Navigate to `Filament Settings` -> `Multimaterial`, and disable all multimaterial settings.

    ![](slicer5.png)
    ![](slicer6.png)

3. **Filament G-Code**

    Change your filament start G-code to the following, inserting your tuned values:

    ```
    SET_TIP_SETTINGS PUSH_DISTANCE= PUSH_SPEED= INITIAL_RETRACT_SPEED= COOLING_SPEED= FINAL_SPEED=
    ```

    Add this G-Code to your filament settings in `Advanced`:

    ![](slicer10.png)