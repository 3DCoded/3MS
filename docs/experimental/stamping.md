# Stamping (Improving No Tip Shaping)

Currently the [No Tip Shaping](notip.md) feature works with most standard PLA's. However, when printing too hot, or using any filament other than standard PLA, the No Tip Shaping feature can result in tips with long strings (>2cm). This feature attempts to reduce strings without using tip shaping.

!!! example "Experimental"
    The features on this page are experimental.

## Slicer

!!! info "Compatibility"
    This feature works on the  **latest** OrcaSlicer Nightly build

### Printer Settings

To use the stamping feature, first navigate to `Printer Settings` -> `Multimaterial` -> `Single extruder multimaterial parameters`. Locate the `Cooling Tube Position` and `Cooling Tube Length` settings.

![](slicerstamping.png)

For my printer, the parameters are `15` and `11`, respectively. Next, calculate:

```
Cooling Tube Position + (Cooling Tube Length / 2)
```

For my printer, this is:

```
15 + (11/2) = 20.5mm
```

### Filament Settings

After that, navigate to `Filament Settings` -> `Multimaterial` -> `Toolchange parameters with single extruder MM printers`.

Set the `Stamping loading speed` to `100`. Set the `Stamping distance measured from the center of the cooling tube` to the value you previously calculated (for my printer, this is `20.5`).

![](slicerstamping2.png)

## Tuning

Now, do a multimaterial test print. This should be a short print, just long enough to do a few toolchanges for each of your loaded filaments.

After the print is done, press down on the lever for each of the 3MS extruders, and pull out the filament. Examine the tip. If the tip has a long string (>2cm), reduce the `Stamping loading speed` value. If the tip has a small blob on the end, decrease the `Stamping distance measured from the center of the cooling tube`.

Your goal is to get filament tips with short strings (<2cm) as fast as possible. Repeat this tuning procedure to find the highest value for the `Stamping loading speed` that yields clean tips reliably for your printer.