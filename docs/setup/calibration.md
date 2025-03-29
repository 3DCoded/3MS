---
comments: true
icon: fontawesome/solid/ruler-horizontal
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