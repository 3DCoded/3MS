# Toolchanges Without Tip Shaping or Filament Cutter!

Because the 3MS is synchronized to the printer's extruder, it can potentially toolchange without any tip shaping or filament cutter. So far, the only testing has been done outside of prints. 

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
        - [X] PETG
        - [ ] TPU (not tested even with tip shaping)

## Speed Benefits

| Print Job | Original Time | New Time | New Time Relative To Original Time | Speed Boost |
| - | - | - | - | - |
| Dual Color 3DBenchy | 2h45m | 1h25m | 51.5% | 1.95x |

## Should Tip Shaping be Used?

Check if your filament is in this list:

- Silk PLA
- Matte PLA

If one of your filament was in that list, it will most likely need tip shaping. However, if another of your filaments was not in that list, it won't need tip shaping.

## Slicer Setup

Setup your slicer for no tip shaping as follows.

### Disable Filament Ramming

Disable filament ramming in `Filament Settings` -> `Multimaterial` -> `Toolchange parameters with single extruder MM printers`:

![](slicer5.png)
![](slicer6.png)