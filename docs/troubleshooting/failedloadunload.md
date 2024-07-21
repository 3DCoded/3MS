# Failed Load/Unload

If your printer is paused and displaying `Please load` or `Please unload`, follow this troubleshooting guide to diagnose the problem and fix it.

## False Alarm

First, see [False Alarm](falsealarm.md) to ensure your filament sensor is properly configured and is being properly read by the 3MS macros.

## Failed Unload

When your printer displays a `Please unload` message, pay attention to the `Tx` number it shows. For example, if it displays the message `Please unload T0`, it failed to unload the filament at T0. Follow these steps to recover the toolchange:

1. Detach the PTFE tube from the inlet of your printer's extruder (you may need to push down the lever on the 3MS extruder for that tool while doing this).
2. Manually pull the filament out of the printer's extruder.

    If it is stuck, try one of the following:

    - Reload the filament until it is extruding out of the nozzle, then unload the filament quickly while pulling firmly.
    - Open your printer's extruder assembly, pull the filament through, and cut off the tip.

    Also, see [Skipping](skipping.md)

3. Next, manually pull the filament all the way to where the filament is usually parked between toolchanges (before the Y-splitter).
4. Manually load the next filament. Check the console for a message like `T0 -> T1` indicating which filament is next (in this case T1). It shoudl be loaded to the entry of the printer's extruder gears.
5. Resume your print.

Next, diagnose the problem based on these possible scenarios:

- Filament never unloaded out of printer's extruder

    This is a sign of poor tip shaping. The quick fix for this is to increase print temperatures. Also, see [Skipping](skipping.md).

- Filament unloaded out of printer's extruder, but stopped before filament sensor

    This is a sign of your filament sensor causing excess friction on the filament, or your 3MS extruder tension too loose. For the 3MS tension too lose, simply rotate the tensioning screw on the 3MS extruder clockwise a couple rotations.

## Failed Load

When your printer displays a `Please load` message, pay attention to the `Tx` number it shows. For example, if it displays the message `Please load T1`, it failed to load the filament at T1. Follow these steps to recover the toolchange:

1. Manually push the filament all the way to the inlet of your printer's extruder.

    If your filament isn't able to load, the previous tool may not have completely unloaded. See [Failed Unload](#failed-unload) for more information.

2. Resume your print.

Next, diagnose the problem based on these possible scenarios:

- Previous filament didn't unload enough

    Increase your `unload_distance` in `MMMS_SETTINGS` (`3ms/settings.py`). You can test different values by using `SET_MMMS_SETTINGS` at runtime. Example:

    ```
    SET_MMMS_SETTINGS UNLOAD_DISTANCE=210
    ```

- Filament didn't load enough

    Increase your `load_distance` in `MMMS_SETTINGS` (`3ms/settings.py`). You can test different values by using `SET_MMMS_SETTINGS` at runtime. Example:

    ```
    SET_MMMS_SETTINGS LOAD_DISTANCE=220
    ```