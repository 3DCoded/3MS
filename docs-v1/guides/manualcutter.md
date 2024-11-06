---
comments: true
icon: material/content-cut
---

# Manual filament cutter

This guide explains how to integrate a filament cutter with the 3MS system, allowing automatic cutting during the filament swap. This negates the need for tip shaping, makinng color swaps much faster and more reliable.

## Table of Contents
- [Installation](#installation)
- [Configuration](#configuration)
- [Using Cutter Macros](#using-cutter-macros)
- [Troubleshooting](#troubleshooting)


## Installation
To install the filament cutter, update your `3ms/main.cfg`:

```cfg title="3ms/main.cfg" hl_lines="6 10"
[save_variables]
filename: ~/printer_data/config/3ms/variables.cfg

[include ./settings.cfg]
[include ./endless/settings.cfg]
[include ./cutter/settings.cfg]
[include ./controllers/btt_skr_mini_e3_v2/steppers.cfg]

[dynamicmacros 3ms]
configs: 3ms/macros.cfg, 3ms/endless/macros.cfg, 3ms/cutter/macros.cfg
```

---

## Configuration

### Cutter Settings

Edit your `3ms/cutter/settings.cfg`:

| Variable                   | Example Value  | Description                             |
|----------------------------|----------------|-----------------------------------------|
| `parking_x_position`        | 280 mm         | X parking position (near compress pin) |
| `parking_y_position`        | -1 mm          | Y parking position (near compress pin) |
| `start_x_cutter_position`   | 285 mm         | X start position for cutting           |
| `end_x_cutter_position`     | 310 mm         | X position when blade is pushed        |
| `start_y_cutter_position`   | -1  mm         | Y start position for cutting           |
| `end_y_cutter_position`     | -1  mm         | Y position when blade is pushed        |
| `travel_speed`              | 6000 mm/min    | Speed to move to cutting position      |
| `pushing_speed`             | 1600 mm/min    | Speed to push the blade                |
| `retries`                   | 2              | Number of repetions                    |

!!! note 
    If X or Y is set to `-1`, it indicates that the toolhead moves along one axis to reach the parking position.
    The printer will adjust movement accordingly. If both axes are used, define both positions.

### Modifying Settings
To change values temporarily, use the `SET_CUTTER_SETTINGS` macro. this can be usefull during troubleshooting and testing

```gcode
SET_CUTTER_SETTINGS PARKING_X=290 PUSHING_SPEED=1700
```