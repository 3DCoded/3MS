---
comments: true
icon: material/code-json
---

# Configuration

After installing Happy Hare firmware, there are some configurations you need to go through before printing in multimaterial.

## Kit Users (SKR Pico)

If you built your 3MS from a kit or are using the SKR Pico board, make sure to remove the following lines in `mmu_hardware.cfg` under the `[mmu_sensors]` block:

```ini title="mmu_hardware.cfg"
pre_gate_switch_pin_0: ^mmu:MMU_PRE_GATE_0
pre_gate_switch_pin_1: ^mmu:MMU_PRE_GATE_1
pre_gate_switch_pin_2: ^mmu:MMU_PRE_GATE_2
pre_gate_switch_pin_3: ^mmu:MMU_PRE_GATE_3
pre_gate_switch_pin_4: ^mmu:MMU_PRE_GATE_4
pre_gate_switch_pin_5: ^mmu:MMU_PRE_GATE_5
pre_gate_switch_pin_6: ^mmu:MMU_PRE_GATE_6
pre_gate_switch_pin_7: ^mmu:MMU_PRE_GATE_7
pre_gate_switch_pin_8: ^mmu:MMU_PRE_GATE_8
pre_gate_switch_pin_9: ^mmu:MMU_PRE_GATE_9
pre_gate_switch_pin_10: ^mmu:MMU_PRE_GATE_10
pre_gate_switch_pin_11: ^mmu:MMU_PRE_GATE_11

post_gear_switch_pin_0: ^mmu:MMU_POST_GEAR_0
post_gear_switch_pin_1: ^mmu:MMU_POST_GEAR_1
post_gear_switch_pin_2: ^mmu:MMU_POST_GEAR_2
post_gear_switch_pin_3: ^mmu:MMU_POST_GEAR_3
post_gear_switch_pin_4: ^mmu:MMU_POST_GEAR_4
post_gear_switch_pin_5: ^mmu:MMU_POST_GEAR_5
post_gear_switch_pin_6: ^mmu:MMU_POST_GEAR_6
post_gear_switch_pin_7: ^mmu:MMU_POST_GEAR_7
post_gear_switch_pin_8: ^mmu:MMU_POST_GEAR_8
post_gear_switch_pin_9: ^mmu:MMU_POST_GEAR_9
post_gear_switch_pin_10: ^mmu:MMU_POST_GEAR_10
post_gear_switch_pin_11: ^mmu:MMU_POST_GEAR_11
```

Also, set:

```ini title="mmu_hardware.cfg"
gate_switch_pin: # Empty
```

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

## Endstops

There are two main endstops you need to setup in Happy Hare firmware for loading and unloading of filament.

### Gate Homing Endstop

When homing filament (checking if it is present), you have three options for the sensor to be used:

- **mmu_gate** Use the shared gate sensor after the Y-splitter
- **mmu_gear** Use the individual post-gate sensors.
- **extruder** Use the extruder entry sensor.

Select one of the three options in `gate_homing_endstop`, located in `mmu_parameters.cfg`.

### Extruder Homing Endstop

Happy Hare also needs a reference sensor inside the toolhead. You have two main options for this:

- **extruder** Use the extruder entry sensor.
- **none** Don't home inside the extruder.

Select one of those options in `extruder_homing_endstop` in `mmu_parameters.cfg`.

??? note "Advanced Options"
    Happy Hare does support three additional advanced options for this endstop:

    - **filament_compression** Use a sync-feedback sensor like TurtleNeck as a homing endstop
    - **collision** Use StallGuard on the printer's extruder.
    - **mmu_gear_touch** Use StallGuard on the 3MS's extruder.

    Note that since I don't use these options, I won't be able to help much with these options.

## Distances

There are many key distances to set up in Happy Hare firmware. All the distance parameters are located in `mmu_parameters.cfg`.

### Homing Distance

Firstly, configure the maximum distance Happy Hare should attempt to load filament to the homing sensor, before "giving up" and deciding that the spool is empty. This should usually be ~150% the distance from your filament parking position to the sensor.

!!! note
    If you use post-gear endstops (`mmu_gear`), this uses the `gate_preload_homing_max` parameter.

This parameter is called `gate_homing_max`.

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

## Toolhead Distances

There are many key distances to setup in Happy Hare firmware, this time for the measurements of your toolhead. Again, all these parameters are located in `mmu_parameters.cfg`.

There are three main ways to get any of the following distances:

- Find configs available online for your toolhead
- Use CAD models of your toolhead
- Measure (approximate) yourself with a piece of filament and calipers

### Homing Max

`toolhead_homing_max` is the maximum distance from the gate endstop to your extruder endstop HH will attempt to load filament.

!!! info "This parameter is only relevant if you use **both** an extruder entry sensor and a shared gate sensor"

### Internal Dimensions

There are three main parameters to measure inside your toolhead.

- `toolhead_extruder_to_nozzle`

    This is the distance between your extruder gears and the nozzle. If you don't have access to CAD of your printer's toolhead, you can follow the below procedure to approximate it.

    1. Preheat your nozzle to printing temperatures.
    1. Press a piece of filament up against the entrance to your extruder gears.
    1. Using KlipperScreen/Mainsail/Fluidd controls, load the filament in until it barely starts oozing out of the nozzle. Note the total distance traveled. This is your approximate `toolhead_extruder_to_nozzle`

- `toolhead_sensor_to_nozzle`

    !!! info "This parameter is only relevant if you have a toolhead sensor."

    This is the distance between your toolhead sensor and nozzle. An easy way to approximate this is:

    1. Preheat your nozzle to printing temperatures.
    1. Press a piece of filament up against the entrance to your extruder gears.
    1. Using KlipperScreen/Mainsail/Fluidd controls, load the filament in until it triggers the toolhead sensor. Note the total distance traveled. Set `toolhead_sensor_to_nozzle` to `toolhead_extruder_to_nozzle - <MEASURED DISTANCE>`

- `toolhead_entry_to_extruder`

    !!! info "This parameter is only relevant if you have an extruder entry sensor."

    This is the distance between your extruder entry sensor and extruder gears. To approximate this:

    1. Take a scrap of filament and slowly push it into your toolhead until the extruder entry sensor triggers.
    1. Brace a marker against the top of your toolhead and mark the filament.
    1. Push filament further in until it hits the extruder gears.
    1. Put another mark on the filament.
    1. Remove the filament and measure the distance between the two marks. This is your `toolhead_entry_to_extruder` value.