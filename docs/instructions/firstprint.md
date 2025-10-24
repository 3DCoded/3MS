---
comments: true
icon: fontawesome/solid/flag-checkered
title: First Print
---

# First Print

Congratulations on building your 3MS! Now to get started with a first print.

## Slicer Setup

This tutorial will walk you through setting up the 3MS with OrcaSlicer. If you use another slicer, some settings may differ.

!!! info "Credit"
    This tutorial is based off of the original Happy Hare slicer setup docs, available [here](https://github.com/moggieuk/Happy-Hare/wiki/Slicer-Setup).

### Machine Settings

Begin by opening your machine settings.

![](9c52e9c3.png)

Navigate to `Machine G-Code`.

![](2f542723.png)

#### Start G-Code

Prepend your `Machine start G-code` with the following:

```yaml
MMU_START_SETUP INITIAL_TOOL={initial_tool} TOTAL_TOOLCHANGES=!total_toolchanges! REFERENCED_TOOLS=!referenced_tools! TOOL_COLORS=!colors! TOOL_TEMPS=!temperatures! TOOL_MATERIALS=!materials! FILAMENT_NAMES=!filament_names! PURGE_VOLUMES=!purge_volumes!
MMU_START_CHECK
```

Then, append the following below your existing G-code:

```yaml
MMU_START_LOAD_INITIAL_TOOL
; Optionally add YOUR additional start logic (like purging) here to run just prior to start
SET_PRINT_STATS_INFO TOTAL_LAYER={total_layer_count} ; For pause at layer functionality and better print stats
```

#### End G-Code

Prepend your `Machine end G-Code` with the following:

```yaml
MMU_END
```

Then, append the following below your existing G-code:

```yaml
MMU_PRINT_END ; Only required if using Octoprint
```

#### Layer Change G-Code

Scroll down and edit your layer change G-Code.

Add the following:

```yaml
_MMU_UPDATE_HEIGHT

; If you want enhanced pausing feature with Happy Hare client macros also add this
SET_PRINT_STATS_INFO CURRENT_LAYER={layer_num} ; For pause at layer functionality and better print stats
```

Save this machine preset with a new name.

### Filament Settings

!!! tip "Filament Cutting vs. Tip Forming"
    It is recommended you install a filament cutter on your printer. This will make your toolchanges much more reliable and negate the tuning tip forming requires.

    You can find user-submitted tip cutting/forming configurations [here](https://link.3dcoded.xyz/tipconfigs/).

    If you want to do tip forming and can't find the right configs for your setup at the above link, you will have to tune the values yourself. In general:

    - Less cooling moves or higher temperature = stringy tips
    - More cooling moves or lower temperature = blobby tips
    - Skinnydip string reduction = less strings

    Please upload your settings [here](https://link.3dcoded.xyz/tipconfigs/) once you tune yours in so other users can benefit!

Begin by opening your filament settings.

![](2b0730ee.png)

Navigate to `Multimaterial`.

![](3c8e4a50.png)

#### Disable Tip Forming

Set all the indicated fields to `0` and open the ramming settings.

![](eb7458be.png)

Set the ramming time to `0`.

![](6acdfb10.png)

## Your First Print

This section will cover one way to start multicolor 3D prints. Note that typically, multicolor 3D models will come pre-painted or in multiple parts, so the process will be slightly different.

Begin by loading the model into the slicer.

![](0f8f127c.png)

Select the model and click multicolor painting.

![](391028e7.png)

Paint the model as you like.

![](273e81cf.png)

Ensure the prime tower is enabled.

![](7c99d620.png)

Arrange the prime tower on the plater.

![](dd4b1862.png)

Slice and print!

# :tada:

_I would really appreciate a star on [GitHub](https://github.com/3DCoded/3MS) if you enjoyed this project!_