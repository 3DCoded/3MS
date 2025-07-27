---
comments: true
icon: material/lightbulb-on
---

# Tips / FAQ

## Which board should I use?

The recommended board for the 3MS is the SKR Pico due to its compact size, reliability, and cost-effectiveness.

## What sensors do I need?

To use the 3MS, you need a sensor between the exit of the Y-splitter and your printer's extruder. If it's closer to the Y-splitter, it's considered a shared gate sensor while if it's closer to the extruder it's called an extruder entry sensor.

## Do I need a filament cutter?

Using a filament cutter is _highly_ recommended as it takes a lot of the guesswork out of tuning tip forming. A quick Google search of "filament cutter for [MY PRINTER]" is usually good to find a filament cutter for your printer.

If there isn't a filament cutter published for your printer, you have two options:

- Design your own

- Tune tip forming

The latter option may seem easier at first, but tip forming isn't as straightforward as you might think.

Here are a few general tips:

- If your tips come out stringy, use more cooling moves and a lower temperature. Also, skinnydip string reduction can help here.
- If your tips come out with a larger tip, use less cooling moves and a higher temperature.
- Use Happy Hare's [`_MMU_FORM_TIP`](https://github.com/moggieuk/Happy-Hare/wiki/Tip-Forming-and-Purging#tuning-happy-hare-_mmu_form_tip-macro) macro to help tune your tips.

## Why isn't `MMU_LOAD`/`MMU_UNLOAD` loading/unload the filament enough?

Run the below command in Mainsail/Fluidd:

```
MMU_STATUS DETAIL=1 SHOWCONFIG=1
```

The output will show exactly what Happy Hare does on load and unload. You can look at the referenced parameters (editable in `mmu_parameters.cfg`) and adjust as necessary to get your load/unload just right.

## More Tips / FAQ's always welcome!