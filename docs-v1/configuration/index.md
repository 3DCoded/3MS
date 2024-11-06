---
comments: true
---

# Configuration

This guide covers the configuration structure and options of the 3MS.

## main.cfg

`main.cfg` is located in `3ms/main.cfg`. It contains the following:

- `[save_variables]` configuration section. This section sets the location where variables about the previous tool will be saved. 
- `[include]` sections. These reference other configuration files covered in this guide. The included configurations are:
    - `settings.cfg`
    - `macros.cfg`
    - `controllers/xxx/steppers.cfg`

## settings.cfg

`settings.cfg` contains the settings the 3MS uses during toolchanges in `macros.cfg`. Further information is [here](macros.md#3ms-settings).

## macros.cfg

`macros.cfg` contains the macros the 3MS uses during toolchanges. Further information is [here](macros.md#filament-handling).

## controllers/xxx/steppers.cfg

`steppers.cfg` contains the MCU configuration for the 3MS. It contains the following:

- `[extruder_stepper 3msx]` This contains the pin mappings for the motor assigned to 3MS tool x.
- `[tmc2209 extruder_stepper 3msx]` This contains the pin mappings for the TMC2209 controlling the motor assigned to 3MS tool x.
- `[mcu 3ms]` This contains the serial path to the 3MS MCU.
- Other sections: These are configuration sections specific to the MCU and should not be modified.

## KlipperScreen.conf

This contains the [KlipperScreen](https://klipperscreen.readthedocs.io/en/latest/) 3MS menu configuration. For more information, see [KlipperScreen](klipperscreen.md).