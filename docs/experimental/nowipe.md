# Filament Purging without Wipe Tower

For printers with a dedicated purge bucket or similar system, wipe towers may not be necessary.

!!! info
    This page, and the features mentioned on it, are in develpment

???+ "Development Status"
    So far, the following have been tested:
    
    - [ ] `SET_PURGE_SETTINGS` functionality
    - [ ] `GET_PURGE_SETTINGS` functionality
    - [ ] `PURGE` routine
        - [ ] Only purge if enabled
        - [ ] Properly run `start_macro`
        - [ ] Properly run `end_macro`

The macros mentioned on this page are available in the `nowipetower` branch.

## Settings

A new `PURGE_SETTINGS` macro contains the following settings:

- `enable` 0 is disabled, and 1 is enabled
- `purge_x` X-cooridnate of purge bucket
- `purge_y` Y-corodinate of purge bucket
- `move_speed` Speed, in mm/min to move to/from purge bucket
- `extrude_speed` Speed, in mm/min (multiply by 0.04 for mm^3/s) to purge filament
- `start_macro` Macro to run before purging
- `end_macro` Macro to run after purging

## Routine

The new `PURGE` macro runs the purge routine as follows:

1. If `enable` == 1, continue
2. Save current toolhead position
3. Run `start_macro`
4. Move to `purge_x` and `purge_y` at `move_speed`
5. Purge provided `purge_amount` at `extrude_speed`
6. Run `end_macro`
7. Return to saved toolhead position