---
icon: octicons/list-ordered-24
comments: true
---

# Slicer Setup

Follow this guide to setup the 3MS with your slicer. OrcaSlicer will be used in this guide, but these same settings (with different names) can be applied to PrusaSlicer and SuperSlicer.

## Number of Filament Units

Set the number of filaments in your slicer to the number of filament units in your 3MS. 

![](slicer1.png)

In OrcaSlicer, press the filament plus button until there are as many filaments displayed as you have filament units.

## Klipper Start/End G-Code

In your Klipper `PRINT_START` macro, add the following right before your purge line:

```cfg
MMMS_START INITIAL_TOOL={params.INITIAL_EXTRUDER}
```

In your `PRINT_END` macro, add the following before the cooldown command is called:

```cfg
MMMS_END
```

## Slicer Start G-Code

In your slicer's Start G-Code, add the following parameter to your `PRINT_START`:

```
INITIAL_EXTRUDER=[initial_extruder]
```

![](slicer2.png)

## Multimaterial Parameters

The last required step of setting up your slicer for the 3MS is setting the multimaterial parameters. 

Navigate to `Printer Settings` -> `Multimaterial`. Check off the `Single Extruder Multi Material` checkbox.

### Cooling Tube

The first two `Single extruder multi-material parameters` are hotend-specific.

The cooling tube refers to the length of PTFE tube in your hotend. For most hotends, this is usually in the heat sink.

Its position is measured as the distance from the **bottom** of the cooling tube to the **tip** of the nozzle.

Set those two parameters in your slicer.

### Parking Position

The third parameter is extruder/printhead-specific.

The `Filament parking position` refers to the position where the filament is just above the extruder gears. During color swaps, the filament is unloaded to this position before the 3MS takes over. At the end of the toolchange, the next filament is in this same position.

Its position is measured as its distance to the **tip** of the nozzle.

### Extra loading distance

This parameter refers to the extra distance the filament is loaded after a color swap is complete. This is usually a negative number.

When a color swap is performed, the nozzle stays in the same place while the 3MS switches colors. This section will refer to this position as the "Swap position".

If you notice blobs forming around the swap positions, **decrease** the `Extra loading distance` (set it to a **negative** number **further** from zero).

If you notice gaps around the swap positions, **increase** the `Extra loading distance` (set it to a **negative** number **closer** to zero).

### Example Settings

Example settings are shown below for a Prusa MK3S+ with a Mosquito hotend.

![](slicer8.png)

!!! info
    This is the last required part of slicer setup.

---

## Optional: klipper_estimator

If you use [klipper_estimator](https://github.com/Annex-Engineering/klipper_estimator) and want the toolchange represented in the time estimate, time your toolchange, then change your Change filament G-Code:

![](slicer3.png)