---
comments: true
---

# Zonestar ZM384 (main MCU)

**Max filament units: 3**

**MCU Name: `main`**

## main MCU

This configuration is a `main MCU` configuration, meaning that your printer should already be running off a ZM384 and you don't need to purchase one.

## Configuration

In your `3ms/macros.cfg`, edit the following section:

=== "Before"
    ```cfg title="macros.cfg"
    # Set the sync of provided TOOL to SYNC with extruder
    ### --- Comment if using the 3MS instead of your printer's extruder --- ###
    [gcode_macro SET_TOOL_SYNC]
    gcode:
        {% set tool = params.TOOL|int %}
        {% set sync = params.SYNC|int %}
        {% set motion_queue = "extruder" if sync == 1 else "" %}
        SYNC_EXTRUDER_MOTION EXTRUDER=3ms{ tool } MOTION_QUEUE={ motion_queue }
    ### --- Comment if using the 3MS instead of your printer's extruder --- ###
    # [gcode_macro SET_TOOL_SYNC]
    # gcode:
    #   {% set tool = params.TOOL|int %}
    #   {% set sync = params.SYNC|int %}
    #   {% set ext_name = "3ms"+(tool|str) %}
    #   {% if tool == 0 %}
    #     {% set ext_name = "extruder" %}
    #   {% endif %}
    #   {% set motion_queue = "extruder" if sync == 1 else "" %}
    #   SYNC_EXTRUDER_MOTION EXTRUDER={ext_name} MOTION_QUEUE={ motion_queue }
    ```
=== "After"
    ```cfg title="macros.cfg"
    # Set the sync of provided TOOL to SYNC with extruder
    ### --- Comment if using the 3MS instead of your printer's extruder --- ###
    # [gcode_macro SET_TOOL_SYNC]
    # gcode:
    #   {% set tool = params.TOOL|int %}
    #   {% set sync = params.SYNC|int %}
    #   {% set motion_queue = "extruder" if sync == 1 else "" %}
    #   SYNC_EXTRUDER_MOTION EXTRUDER=3ms{ tool } MOTION_QUEUE={ motion_queue }
    ### --- Comment if using the 3MS instead of your printer's extruder --- ###
    [gcode_macro SET_TOOL_SYNC]
    gcode:
      {% set tool = params.TOOL|int %}
      {% set sync = params.SYNC|int %}
      {% set ext_name = "3ms"+(tool|str) %}
      {% if tool == 0 %}
        {% set ext_name = "extruder" %}
      {% endif %}
      {% set motion_queue = "extruder" if sync == 1 else "" %}
      SYNC_EXTRUDER_MOTION EXTRUDER={ext_name} MOTION_QUEUE={ motion_queue }
    ```

## Wiring

Route the wires from the NEMA17's to the controller board. Follow this table to determine which port to plug the motors into:

| Filament Unit # | Motor Port |
| - | - 
| 0 | E0 |
| 1 | E1 |
| 2 | E2 |
| 3 | E3 |
