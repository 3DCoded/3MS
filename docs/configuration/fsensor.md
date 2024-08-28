---
icon: material/exclamation-thick
---

# Filament Sensor

Follow this guide to configure your filament sensor with the 3MS. 

## Location of Sensor

The filament sensor should be right before the extruder, and after the Y splitter. Other locations, such as between the hotend and extruder, have not been tested.

!!! warning
    The 3MS has only been tested with a `filament_switch_sensor`, and not with a `filament_motion_sensor`

## Configuration

To configure your filament sensor with the 3MS, open `3ms/settings.cfg` and change the following (assuming your filament sensor is named "runout_sensor"):

=== "Before"
    ```cfg title="3ms/settings.cfg"
    fsensor_name: "fsensor"
    ```
=== "After"
    ```cfg title="3ms/settings.cfg"
    fsensor_name: "runout_sensor"
    ```