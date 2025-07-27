---
comments: true
icon: fontawesome/solid/ruler
---

# Calibration

Follow this guide to calibrate your 3MS.

!!! info "Original Documentation"
    This guide is a simplified version of [the official Happy Hare documentation](https://github.com/moggieuk/Happy-Hare/wiki/MMU-Calibration). I highly recommend you read it as it contains useful information and goes more in detail if you are having trouble with the calibrations.

## Verify Filament Sensors

Before calibrating, it is important to ensure that your filament sensors are working properly.

Run in your Klipper console:

```
QUERY_ENDSTOPS
```

and verify the output. For each endstop, `open` means no filament detected, and `TRIGGERED` means filament present. Re-run the command several times, inserting/removing filament to each of the sensors, to verify that each filament sensor properly detects filament.

## Gear Steppers

First, calibrate your gear steppers (filament units). The goal of this calibration is to ensure the filament actually moves as far as expected.

First, detach the PTFE tubing from each of the filament units.

For each filament unit (gate), repeat the following steps:

1. Manually load filament until it sticks out slightly from the end of the filament unit
1. Cut the tip of the filament to be flush with the PTFE coupler (side cutters are good for this).
1. Run the following commands in your Klipper console:

    ```
    MMU_SELECT GATE=n
    MMU_TEST_MOVE MOVE=100
    ```

    where `n` is the gate number you are calibrating (starting at zero).

1. The filament should move forwards. If it moves backwards, [invert your gear stepper](#inverting-a-gear-stepper). Measure the distance the filament moved out of the extruder. Using side cutters the same as before can be helpful for this. Run the following command in your Klipper console:

    ```
    MMU_CALIBRATE_GEAR MEASURED=n
    ```

    where `n` is the measured distance.

1. Repeat step **3**. The filament should move exactly `100mm`.

## Configuring the Parking Position

The parking position is the location your filament should park when idle, measured from your gate endstop. This should be set to ~1-2cm above your Y-splitter.

This parameter is called `gate_parking_distance` in `mmu_parameters.cfg`.

To determine this value, begin by moving the filament in gate 0 to the ideal parking position by hand.

![](6ed86262.png)

=== "With an extruder entry sensor"
    If you have an extruder entry sensor configured, determining your parking distance from here is super easy.

    Run the following commands in Mainsail:

    ```
    MMU_SELECT GATE=0
    MMU_TEST_HOMING_MOVE MOTOR=gear MOVE=999 SPEED=50 ENDSTOP=extruder STOP_ON_ENDSTOP=1
    ```

    !!! failure "Operation not possible. MMU has filament loaded"
        If Mainsail reports this error after trying to select a gate, run the following command to tell HH that filament is _not_ loaded.

        ```
        MMU_RECOVER LOADED=0
        ```

    Note the distance displayed.

    ```
    Homed after 450.00mm
    ```

    Read your `toolhead_entry_to_extruder` value from `mmu_parameters.cfg`.

    Set your `gate_parking_distance` to:

    ```
    <displayed distance> + <toolhead_entry_to_extruder> + 50
    ```

=== "Without an extruder entry sensor"
    To tune this value, start by estimating the distance from your extruder to the ideal parking position. You can use a piece of filament outside of the tube and use a ruler to help measure this. In the diagram above, it's the distance between the red and blue dots.

    Set this starting value in `mmu_parameters.cfg`:

    ```yaml
    gate_parking_distance: xxx
    ```

    Run the following commands in Mainsail:

    ```
    MMU_SELECT GATE=0
    MMU_LOAD
    MMU_UNLOAD
    ```

    !!! failure "Operation not possible. MMU has filament loaded"
        If Mainsail reports this error after trying to select a gate, run the following command to tell HH that filament is _not_ loaded.

        ```
        MMU_RECOVER LOADED=0
        ```

    The filament should load to the extruder then unload to the parking position.

    If it unloaded to the correct spot (around the red dot), then your parking distance is good.

    If not, use the below command to move the filament until it's at the correct position (positive is towards the extruder, negative is away from it):

    ```
    MMU_TEST_MOVE MOVE=xxx
    ```

    Finally, run `MMU_STATUS` and note the "UNLOADED" value shown.

    ```
    UNLOADED 450.0mm
    ```

    Save the shown value as your parking distance.

## Encoder (if installed)

If you are using an encoder, like a BTT SFS (Smart Filament Sensor), you need to calibrate your encoder.

1. Load your filament manually to its parking position at the start of the Y-splitter.
2. Run in your Klipper console:

    ```
    MMU_CALIBRATE_ENCODER
    ```

---

## Inverting a Gear Stepper

If you notice any of your gear steppers moving filament in the opposite direction as expected, you need to invert the gear stepper. There are two options to do this:

- Physically flip the stepper cables
- Invert it in software

To invert a gear stepper in software, open `mmu_hardware.cfg` and invert the `dir_pin` for the respective stepper.

Example, if `T1` is moving backwards:

=== "Before"
    ```cfg title="mmu_hardware.cfg"
    [stepper_mmu_gear_1]
    ...
    dir_pin: mmu: PC5
    ```
=== "After"
    ```cfg title="mmu_hardware.cfg"
    [stepper_mmu_gear_1]
    ...
    dir_pin: !mmu: PC5 # <-- Note the ! in front of mmu
    ```

!!! tip
    If the pin already has a `!` in front of it, remove it to invert it.

Restart Klipper.