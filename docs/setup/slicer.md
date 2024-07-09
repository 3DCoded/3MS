# Slicer Setup

Follow this guide to setup the 3MS with your slicer. OrcaSlicer will be used in this guide, but these same settings (with different names) can be applied to PrusaSlicer and SuperSlicer.

## Number of Filament Units

Set the number of filaments in your slicer to the number of filament units in your 3MS. 

![](slicer1.png)

In OrcaSlicer, press the filament plus button until there are as many filaments displayed as you have filament units.

## Klipper Start/End G-Code

In your Klipper `PRINT_START` macro, add the following right before your purge line:

```cfg
MMMS_START INITIAL_EXTRUDER={params.INITIAL_EXTRUDER}
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

This is the last non-optional part of slicer setup.

## Optional: klipper_estimator

If you use [klipper_estimator](https://github.com/Annex-Engineering/klipper_estimator) and want the toolchange represented in the time estimate, time your toolchange, then change your Change filament G-Code:

![](slicer3.png)