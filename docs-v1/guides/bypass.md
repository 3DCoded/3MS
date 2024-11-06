---
icon: fontawesome/solid/x
comments: true
---

# 3MS Bypass

Follow this guide to allow manually loading a spool to your printer, and bypassing the 3MS system.

## Klipper Macros

Replace the `MMMS_START` line in your `PRINT_START` macro with:

```cfg
{% if (params.BYPASS|default(0)|int) %}
    DESYNC_ALL_TOOLS
{% else %}
    # You can also put your ENDLESS_START line here too
    MMMS_START INITIAL_TOOL={params.INITIAL_EXTRUDER}
{% endif %}
```

Replace the `MMMS_END` line in your `PRINT_END` macro with:

```cfg
{% if not (params.BYPASS|default(0)|int) %}
    MMMS_END
{% endif %}
```

## Slicer GCode

1. Navigate to `Printer Settings` -> `Machine G-code`. 
1. In your `Machine start G-code`, pass the `BYPASS=1` parameter to your `PRINT_START` macro. 
1. In your `Machine end G-code`, pass the `BYPASS=1` parameter to your `PRINT_END` macro.
1. Save the new preset with a different name to differentiate it from your main preset.