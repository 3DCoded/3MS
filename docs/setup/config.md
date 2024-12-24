# Configuring Happy Hare Firmware

After installing Happy Hare firmware, there are some configurations you need to go through before printing in multimaterial.

<!-- !!! info "Read me first"
    Please **READ** this guide! If you ask for help regarding configuration, I'll likely redirect you to this guide.  -->

!!! info "This page is under construction"

## Filament Sensors

To use the 3MS, you'll need a filament sensor. Assuming you already have one installed, you can configure it in `mmu_hardware.cfg`.

Locate the `[mmu_sensors]` section near the bottom of `mmu_hardware.cfg`.

### Extruder/Toolhead Sensors

To configure an extruder entry sensor (a sensor right **before** your extruder), set your `extruder_switch_pin`:

!!! tip "Don't know your sensor pin?"
    If you don't know your sensor pin, and it's already configured with Klipper, locate your sensor configuration (usually `filament_switch_sensor`) and note the `sensor_pin`.

```cfg title="mmu_hardware.cfg"
[mmu_sensors]
...
extruder_switch_pin: <SOME PIN>
```

To configure your toolhead sensor (a sensor right **after** your extruder), set your `toolhead_switch_pin` the same way as you set your `extruder_switch_pin`.

### Shared Gate Sensor (Optional)

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

#### Post-Gate

Post-gate sensors go **after** each of your filament units. Configure each of these:

```cfg title="mmu_hardware.cfg"
[mmu_sensors]
...
post_gate_switch_pin_0: <SOME PIN>
post_gate_switch_pin_1: <SOME PIN>
post_gate_switch_pin_2: <SOME PIN>
post_gate_switch_pin_3: <SOME PIN>
```

---

!!! warning "Existing Sensors"
    Before moving on, ensure all your existing `filament_switch_sensor` and `filament_motion_sensor` sections are commented out or deleted. Leaving this enabled will lead to unintended issues later on.

---

## Distances

There are many key distances to set up in Happy Hare firmware.

### Homing Endstop

Firstly, when homing filament (checking if it is present), you have three options for the sensor to be used:

- **mmu_gate** Use the shared gate sensor after the Y-splitter
- **mmu_gear** Use the individual post-gate sensors.
- **extruder** Use the extruder entry sensor.

Select one of the three options in `gate_homing_endstop`.

### Homing Distance

Next, configure the maximum distance Happy Hare should attempt to load filament to the homing sensor, before "giving up" and deciding that the spool is empty. This should usually be ~150% the distance from your filament parking position to the sensor.

!!! note
    If you use post-gear endstops (`mmu_gear`), this uses the `gate_preload_homing_max` parameter.

This parameter is called `gate_homing_max`.

### Parking Position

This is the location your filament should park when idle, measured from your gate endstop. This should be set to ~1-2cm above your Y-splitter.

This parameter is called `gate_parking_distance`.

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