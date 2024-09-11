---
comments: true
---

# Endless Spool

This feature is based off of [Happy Hare](https://github.com/moggieuk/Happy-Hare) firmware.

!!! info
    The features on this page are still in development.

## Install

To install the endless spool feature, run in your terminal:

```sh
cd ~/3MS
git fetch
git checkout endless-spool
git pull
sh install.sh
```

Update your `3ms/main.cfg`:

```cfg title="3ms/main.cfg" hl_lines="5 9"
[save_variables]
filename: ~/printer_data/config/3ms/variables.cfg

[include ./settings.cfg]
[include ./endless/settings.cfg]
[include ./controllers/btt_skr_mini_e3_v2/steppers.cfg]

[dynamicmacros 3ms]
configs: 3ms/macros.cfg, 3ms/endless/macros.cfg
```

## Usage

To setup endless spool, first choose which filaments can be used as backups for each other. Example with three tools:

- T0 (PLA) -> T1(PLA)
- T1(PLA) -> T0(PLA)
- T2 (PETG) -> PAUSE

In this case, since T0 and T1 are backups for each other, they can be considered in the same "group" and assigned a group number. In this case, `1` will be used. Since T2 doesn't have a backup, it will be its own group. In this case, `2` will be used.

If your printer has a filament sensor before each of the 3MS's filament units, set the `single` setting to `0`. If your printer has only one filamnet sensor before its main extruder, set the `single` setting to `1`.

Edit your `3ms/endless/settings.cfg`:

```cfg title="3ms/endless/settings.cfg" hl_lines="2-4 6"
[gcode_macro ENDLESS_SETTINGS]
single: 1 # <-- Set to 0 if you have a filament sensor before each of your 3MS extruders. Set to 1 if you have one filament sensor right before your printer's extruder.
variable_t0: 1
variable_t1: 1
### --- Uncomment below for more than two tools --- ###
variable_t2: 2
# variable_t3: -1
gcode:
    RESPOND MSG=""
```

Change your filament sensors' `runout_gcode` to:

```cfg
ENDLESS_RUNOUT T=0
```

For the filament sensor associated with T1, change the code from `T=0` to `T=1`, and so on.