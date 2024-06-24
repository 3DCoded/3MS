# Stepper Setup

Follow this guide to calibrate each of the stepper motors.

## Is the motor spinning?

Run this command for each of your filament units, replacing `T0` with `T1`, `T2`, etc.

```gcode
G100 T0 E50 F4500
```

If the motor spins, skip to the next step. If not, check your wiring first. If your wiring is fine, go to `3ms/steppers.cfg`. Locate the section named `[manual_stepper 3ms0]`, replacing `0` with the `T` number of the motor not spinning. In front of the `enable_pin`, add, an `!`. If there already is one, remove it. Example:

=== "Before"
    ``` cfg title="3ms/steppers.cfg"
    enable_pin: !arduino: PD7
    ```
=== "After"
    ``` cfg title="3ms/steppers.cfg"
    enable_pin: arduino: PD7
    ```

## Is the motor spinning backwards?

Preload each of the filament units with a piece of scrap filament by pushing the lever to release the tension, inserting filament, then releasing the lever to restore tension. Next, run this command for each of your filament units, replacing `T0` with `T1`, `T2`, etc.

```gcode
G100 T0 E50 F4500
```

Note which way the filament moves. If it moves forwards, away from the PTFE coupler, skip to the last step. If it moves backwards, you have two choices:

- Switch the motor's wires
- Invert the pin in the configuration

To invert the pin in the configuration, locate the configuration section for the filament unit spinning backwards, and invert the `dir_pin`. See the previous section for how to invert the pin.

## How far does the filament move?

