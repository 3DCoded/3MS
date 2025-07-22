---
comments: true
icon: fontawesome/solid/flag-checkered
title: First Print
---

# First Print

!!! info "Page is under construction"

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

