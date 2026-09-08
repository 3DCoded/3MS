---
comments: true
icon: material/code-json
---

# Configuration

After installing Happy Hare firmware, there are some configurations you need to go through before printing in multimaterial.

## Kit Users (SKR Pico)

If you built your 3MS from a kit or are using the SKR Pico board, set a starting rotation distance as shown:

<video src="/assets/videos/gearratio.mp4" controls></video>

Set `Other Settings` → `Gear Stepper` → `Gear Ratio` → `50:17`

## Filament Sensors

!!! info "Required Sensors"
    To use the 3MS, you'll need a filament sensor somewhere between your Y-splitter and printer extruder.

    There are two options for this sensor:

    - [**Shared gate sensor**](#shared-gate-sensor) is closer to the Y-splitter
    - [**Extruder entry sensor**](#extrudertoolhead-sensors) is closer to the printer's extruder.

    Assuming you already have one installed, you can configure it in the installer.

### Extruder/Toolhead Sensors

To configure an extruder entry sensor (a sensor right **before** your extruder):

!!! tip "Don't know where to find a sensor?"
    If you don't know where to find a good sensor for your printer, here are a few tips:

    - Search [Printables](https://www.printables.com/) and [Thangs](https://thangs.com/) for a sensor.
    - Build a [Filatector](https://github.com/ArmoredTurtle/Filatector) universal filament sensor.

!!! tip "Don't know your sensor pin?"
    If you don't know your sensor pin, and it's already configured with Klipper, locate your sensor configuration (usually `filament_switch_sensor`) and note the `sensor_pin`.

The below video shows where to find the pin settings. Note that your pins will likely be different.

<video src="/assets/videos/extsensor.mp4" controls></video>

To configure your toolhead sensor (a sensor right **after** your extruder), set your `toolhead_switch_pin` the same way as you set your `extruder_switch_pin`.

---

!!! warning "Existing Sensors"
    Before moving on, ensure all your existing `filament_switch_sensor` and `filament_motion_sensor` sections are commented out or deleted. Leaving this enabled will lead to unintended issues later on.

---

## Distances

There are many key distances to set up in Happy Hare firmware.

### Homing Distance

Firstly, configure the maximum distance Happy Hare should attempt to load filament to the homing sensor, before "giving up" and deciding that the spool is empty. This should usually be ~150% the distance from your filament parking position to the sensor.

<video src="/assets/videos/homingdistance.mp4" controls></video>

### Eject Distance

Finally, if you want to switch out which filament is in a filament unit, edit your final eject distance. This should be the distance from your parking position to your filament unit gears, plus a small margin.

<video src="/assets/videos/ejectdistance.mp4" controls></video>

## Speeds

There are a few main speeds you can configure with Happy Hare firmware.

- **Homing Speed**: This is when the HH moves the filament into your extruder entry sensor to ensure they are present.
- **Load/Unload Speed**: This is the speed at which Happy Hare will load/unload filament during a toolchange.
- **Extruder Speed**: This is the speed at which your extruder will load/unload filament during a toolchange.

<video src="/assets/videos/speeds.mp4" controls></video>

## Toolhead Distances

There are many key distances to setup in Happy Hare firmware, this time for the measurements of your toolhead.

There are three main ways to get any of the following distances:

- **Recommended:** Find and select your toolhead in the installer
- Find configs available online for your toolhead
- Use CAD models of your toolhead
- Measure (approximate) yourself with a piece of filament and calipers

All the below settings can be found in the `Toolhead Settings` section of the installer.

<video src="/assets/videos/toolheadsettings.mp4" controls></video>

### Homing Max

`toolhead_homing_max` is the maximum distance from the gate endstop to your extruder endstop HH will attempt to load filament.

!!! info "This parameter is only relevant if you use **both** an extruder entry sensor and a shared gate sensor"

### Manual Configuration

If you cannot find a pre-configured toolhead, you can manually configure the distances.

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

## Optional Settings

Most users likely won't have to follow the below steps, as they are automatically set on most systems.

### Shared Gate Sensor

This is not required on most systems (most systems use an extruder entry sensor instead).

Moving backwards from the extruder, the next possible sensor you may have installed is a shared gate sensor. This goes right **after** the Y-splitter.

If you have a gate sensor installed, set your `gate_switch_pin`:

<video src="/assets/videos/sharedgate.mp4" controls></video>

### Pre-Gate or Post-Gear

This is not required on most systems.

Pre-gate sensors go **before** each of your filament units. Post-gear sensors go **after** each of your filament units.

<video src="/assets/videos/prepostgate.mp4" controls></video>

### Gate Homing Endstop

This is an optional step as on most systems this is automatically set.

When homing filament (checking if it is present), you have three options for the sensor to be used:

- **Shared Gate Sensor** Use the shared gate sensor after the Y-splitter
- **Post Gate Sensors** Use the individual post-gate sensors.
- **Extruder Sensor** Use the extruder entry sensor.

Select one of the three options. Note that only the available options will be enabled. In the below example only an extruder sensor is configured, so it is the only displayed option.

<video src="/assets/videos/gatehoming.mp4" controls></video>

### Extruder Homing Endstop

This is an optional step as on most systems this is automatically set.

Happy Hare also needs a reference sensor inside the toolhead. You have two main options for this:

- **Toolhead Sensor** Use the extruder entry sensor.
- **Compression Sensor** Use a sync-feedback sensor as a homing endstop.
- **None** Don't home inside the extruder.

Select one of the three options. Note that only available options will be shown depending on your setup.

<video src="/assets/videos/extruderhoming.mp4" controls></video>