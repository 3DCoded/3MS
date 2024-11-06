---
icon: material/fast-forward
comments: true
---

# Toolchanges Without Tip Shaping or Filament Cutter!

Because the 3MS is synchronized to the printer's extruder, it can perform toolchanges without any tip shaping or filament cutter.

## Should Tip Shaping be Used?

See [Materials](materials.md) for information on whether or not tip shaping should be used for your filaments.

## Slicer Setup

Setup your slicer for no tip shaping as follows.

### Disable Filament Ramming

Disable filament ramming in `Filament Settings` -> `Multimaterial` -> `Toolchange parameters with single extruder MM printers`:

![](slicer5.png)
![](slicer6.png)

### Unload/Load Speed

Next, change the `Unloading speed at start` and `Unloading speed` to 300 (faster is better here). Next, change the `Loading speed at start` and `Loading speed` to 300 and 100, respectively.

???+ info "What this does"
    The main idea behind toolchanges without tip shaping relies on the filament being unloaded too fast to form a blob. Setting the `Unloading speed` settings allows this. Next, loading the filament back can be generally optimized by increasing the `Loading speed` settings.

![](slicer7.png)

### Temperature

If your filament has very long strings on the end of them after unloading without tip shaping (longer than 2cm), decrease your filament temperature. 

If your filament tip has a nearly flat tip, increase your filament temperature.

The ideal filament tip has a pointy end and a small string (less than 5mm). When in doubt, it is recommended to aim for a slightly stringy tip over a flat tip.