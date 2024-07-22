# Toolchanges Without Tip Shaping or Filament Cutter!

Because the 3MS is synchronized to the printer's extruder, it can potentially toolchange without any tip shaping or filament cutter.

!!! info
    This page, and the features mentioned on it, are in develpment

???+ "Development Status"
    So far, the following work without tip shaping:
    
    - [X] Toolchanges without tip shaping
    - [X] Print start/end routines without tip shaping
    - [X] Small prints without tip shaping (up to 5 toolchanges)
    - [X] Medium prints without tip shaping (over 50 toolchanges)
    - [X] Long prints without tip shaping (over 100 toolchanges)
    - Common materials:
        - [X] PLA
            - [X] PLA+
            - [X] High Speed PLA
            - [ ] Silk PLA
        - [ ] PETG
        - [ ] TPU (see [Dual Drive 3MS Extruders for TPU](dualdrivetpu.md))

## Speed Benefits

!!! info
    This section is under construction.

## Should Tip Shaping be Used?

See [Materials](materials.md) for information on whether or not tip shaping should be used for your filaments.

## Slicer Setup

Setup your slicer for no tip shaping as follows.

### Disable Filament Ramming

Disable filament ramming in `Filament Settings` -> `Multimaterial` -> `Toolchange parameters with single extruder MM printers`:

![](slicer5.png)
![](slicer6.png)