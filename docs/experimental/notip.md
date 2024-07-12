# Toolchanges Without Tip Shaping or Filament Cutter!

Because the 3MS is synchronized to the printer's extruder, it can potentially toolchange without any tip shaping or filament cutter. So far, the only testing has been done outside of prints. 

!!! info
    This page, and the features mentioned on it, are in develpment

???+ "Development Status"
    So far, the following have been tested:
    
    - [X] Toolchanges without tip shaping
    - [X] Print start/end routines without tip shaping
    - [X] Small prints without tip shaping (up to 5 toolchanges)
    - [ ] Long prints without tip shaping (over 100 toolchanges)
    - [ ] Common materials:
        - [X] PLA
        - [ ] PETG
        - [ ] TPU (not tested even with tip shaping)

## Speed Benefits

| Print Job | Original Time | New Time | New Time Relative To Original Time | Speed Boost |
| - | - | - | - | - |
| Dual Color 3DBenchy | 2h45m | 1h25m | 51.5% | 1.95x |

## Configuration

In your `3ms/settings.cfg`, chagne the `unload_distance` and `load_distance` to be equal. Next, add the distance from your extruder to your hotend to both.

Example (assuming extruder-to-hotend distance is 65mm):

=== "Before"
    ```cfg title="3ms/settings.cfg"
    variable_unload_distance: 200
    variable_load_distance: 210
    ```
=== "After"
    ```cfg title="3ms/settings.cfg"
    variable_unload_distance: 265
    variable_load_distance: 265
    ```

!!! info
    It is also recommended to increase your unload speed slightly and increase your load speed significantly to help with reliability without tip shaping.

    Example:

    === "Before"
        ```cfg title="3ms/settings.cfg"
        variable_unload_speed: 4500
        variable_load_speed: 4500
        ```
    === "After"
        ```cfg title="3ms/settings.cfg"
        variable_unload_speed: 6000
        variable_load_speed: 7500
        ```

## Slicer Setup

Setup your slicer for no tip shaping as follows.

### Disable Printer Ramming

First, disable printer ramming by going to `Printer Settings` -> `Multimaterial` -> `Single extruder multimaterial parameters`:

![](slicer4.png)

!!! info
    Don't change  `Filament parking position` and `Extra loading distance`.

### Disable Filament Ramming

Disable filament ramming in `Filament Settings` -> `Multimaterial` -> `Toolchange parameters with single extruder MM printers`:

![](slicer5.png)
![](slicer6.png)