<script src="../../static/js/steppers.js"></script>

# Stepper Motors

Follow this guide to calibrate each of the stepper motors. Each of these steps should be repeated for each of your filament units, replacing `TOOL=0` with `TOOL=1`, and so on. Also replacing `3ms0` with `3ms1`, and so on.

!!! info
    If your stepper motor shakes erratically while running any of these commands, your wiring may be incorrect.

## Is the motor spinning?

Run this command:

```gcode
SYNC_TOOL TOOL=0
G1 E50 F4500
```

If the motor spins, skip to the next step. If not, check your wiring first. If your wiring is fine, go to `3ms/steppers.cfg`. Locate the section named `[extruder_stepper 3ms0]`. In front of the `enable_pin`, add, an `!`. If there already is one, remove it. Example:

=== "Before"
    ``` cfg title="3ms/steppers.cfg"
    enable_pin: !3ms: PD7
    ```
=== "After"
    ``` cfg title="3ms/steppers.cfg"
    enable_pin: 3ms: PD7
    ```

## Is the motor spinning backwards?

Preload each of the filament units with a piece of scrap filament by pushing the lever to release the tension, inserting filament, then releasing the lever to restore tension. Next, run this command:

```gcode
SYNC_TOOL TOOL=0
G1 E50 F4500
```

Note which way the filament moves. If it moves forwards, away from the PTFE coupler, skip to the last step. If it moves backwards, you have two choices:

- Switch the motor's wires
- Invert the pin in the configuration

To invert the pin in the configuration, locate the configuration section for the filament unit spinning backwards, and invert the `dir_pin`. See the previous section for how to invert the pin.

## How far does the filament move?

This section is a modified version of the [Klipper Docs](https://www.klipper3d.org/Rotation_Distance.html#calibrating-rotation_distance-on-extruders)

Preload each of the filament units with a piece of scrap filament at least 200mm long by pushing the lever to release the tension, inserting filament, then releasing the lever to restore tension.

Use a ruler and a marker to place a mark 70mm from the inlet of the filament unit. Use calipers to measure the actual distance. Write it down, as it will be referred to as `<initial_mark_distance>`.

Next, run this command:

```gcode
SYNC_TOOL TOOL=0
G1 E50 F1500
```

Use calipers to measure the new distance between the inlet of the filament unit and the mark. Write it down, as it will be referred to as `<next_mark_distance>`. 

Calculate `<actual_extrude_distance> = <initial_mark_distance> - <next_mark_distance>`

In the `steppers.cfg` file (located in `3ms/controllers/xxx/steppers.cfg`), locate the configuration section for the current extruder. Example:

```cfg title="3ms/controllers/btt_skr_mini_e3_v2/steppers.cfg"
[extruder_stepper 3ms0]
extruder: extruder
step_pin: 3ms: PB13
dir_pin: !3ms: PB12
enable_pin: !3ms: PB14
microsteps: 16
rotation_distance: 32.8450
```

Note the `rotation_distance` (last line). In this case, it is `32.8450`.

Calculate the new rotation distance: `new_rotation_distance = <rotation_distance> * <actual_extrude_distance> / 50`. 

Round this result to three or four decimal places. Decrease it by 0.005 (this is so that if this result is slightly off, the 3MS filament unit will skip, instead of the printer's extruder stripping the filament during a print). 

Previous `rotation_distance`: <input id="prevRotDist" type="number" min="0" />

New `rotation_distance`: <span id="result"></span>

[Compute](javascript:compute_rotation_distance()){.md-button}

Set the new `rotation_distance` in your config. Save it and restart Klipper.

!!! info
    If you use the same stepper motor brand and model for each of your filament units, you likely only have to do this step for one stepper, then copy over the rotation_distance to all the others.