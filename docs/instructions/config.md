---
comments: true
icon: material/code-json
---

# Configuration

After installing Happy Hare firmware, there are some configurations you need to go through before printing in multimaterial.

## Filament Sensors

!!! info "Required Sensors"
    To use the 3MS, you'll need a filament sensor somewhere between your Y-splitter and printer extruder.

    There are two options for this sensor:

    - [**Shared gate sensor**](#shared-gate-sensor) is closer to the Y-splitter
    - [**Extruder entry sensor**](#extrudertoolhead-sensors) is closer to the printer's extruder.

    Assuming you already have one installed, you can configure it in `mmu_hardware.cfg`.

Locate the `[mmu_sensors]` section near the bottom of `mmu_hardware.cfg`.

### Extruder/Toolhead Sensors

To configure an extruder entry sensor (a sensor right **before** your extruder), set your `extruder_switch_pin`:

!!! tip "Don't know where to find a sensor?"
    If you don't know where to find a good sensor for your printer, here are a few tips:

    - Search [Printables](https://www.printables.com/) and [Thangs](https://thangs.com/) for a sensor.
    - Build a [Filatector](https://github.com/ArmoredTurtle/Filatector) universal filament sensor.

!!! tip "Don't know your sensor pin?"
    If you don't know your sensor pin, and it's already configured with Klipper, locate your sensor configuration (usually `filament_switch_sensor`) and note the `sensor_pin`.

```cfg title="mmu_hardware.cfg"
[mmu_sensors]
...
extruder_switch_pin: <SOME PIN>
```

To configure your toolhead sensor (a sensor right **after** your extruder), set your `toolhead_switch_pin` the same way as you set your `extruder_switch_pin`.

### Shared Gate Sensor

Moving backwards from the extruder, the next possible sensor you may have installed is a shared gate sensor. This goes right **after** the Y-splitter.

If you have a gate sensor installed, set your `gate_switch_pin`:

```cfg title="mmu_hardware.cfg"
[mmu_sensors]
...
gate_switch_pin: <SOME PIN>
```

### Pre/Post Gate Sensors (Optional)

If you have a filament sensor before or after each of your 3MS filament units, configure a `pre_` or `post_gate` sensor.

#### Pre-Gate

Pre-gate sensors go **before** each of your filament units. Configure each of these:

```cfg title="mmu_hardware.cfg"
[mmu_sensors]
pre_gate_switch_pin_0: <SOME PIN>
pre_gate_switch_pin_1: <SOME PIN>
pre_gate_switch_pin_2: <SOME PIN>
pre_gate_switch_pin_3: <SOME PIN>
```

#### Post-Gear

Post-gear sensors go **after** each of your filament units. Configure each of these:

```cfg title="mmu_hardware.cfg"
[mmu_sensors]
...
post_gear_switch_pin_0: <SOME PIN>
post_gear_switch_pin_1: <SOME PIN>
post_gear_switch_pin_2: <SOME PIN>
post_gear_switch_pin_3: <SOME PIN>
```

---

!!! warning "Existing Sensors"
    Before moving on, ensure all your existing `filament_switch_sensor` and `filament_motion_sensor` sections are commented out or deleted. Leaving this enabled will lead to unintended issues later on.

---

## Distances

There are many key distances to set up in Happy Hare firmware. All the distance parameters are located in `mmu_parameters.cfg`.

### Homing Endstop

Firstly, when homing filament (checking if it is present), you have three options for the sensor to be used:

- **mmu_gate** Use the shared gate sensor after the Y-splitter
- **mmu_gear** Use the individual post-gate sensors.
- **extruder** Use the extruder entry sensor.

Select one of the three options in `gate_homing_endstop`, located in `mmu_parameters.cfg`.

### Homing Distance

Next, configure the maximum distance Happy Hare should attempt to load filament to the homing sensor, before "giving up" and deciding that the spool is empty. This should usually be ~150% the distance from your filament parking position to the sensor.

!!! note
    If you use post-gear endstops (`mmu_gear`), this uses the `gate_preload_homing_max` parameter.

This parameter is called `gate_homing_max`.

### Parking Position

This is the location your filament should park when idle, measured from your gate endstop. This should be set to ~1-2cm above your Y-splitter.

This parameter is called `gate_parking_distance`.

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

### Eject Distance

Finally, if you want to switch out which filament is in a filament unit, edit your `gate_final_eject_distance`. This should be the distance from your parking position to your filament unit gears, plus a small margin.

## Speeds

There are many different speeds you can configure with Happy Hare firmware.

These are located in the speeds section of `mmu_parameters.cfg` (near the top).

### Homing Speed

"Homing" is when the HH moves the filament into your extruder entry sensor to ensure they are present. You can adjust the speed at which this happens by editing the `gear_homing_speed` parameter.

### First Load Speeds

Happy Hare allows for slowing down the initial load to deal with additional drag from the filament spool. To adjust this speed, adjust `gear_from_spool_speed`.

### Load/Unload Speeds

To adjust your load/unload speeds during a toolchange, adjust the `gear_from_buffer_speed` parameter.