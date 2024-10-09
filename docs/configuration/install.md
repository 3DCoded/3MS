---
icon: material/download
comments: true
---

# Installation

Follow this guide to install the 3MS configuration and macros.

!!! info
    All SSH commands are run on the Klipper Host (usually a Raspberry Pi) and are labeled like the following:
    ```sh title="SSH"
    echo Hello World
    ```
    Notice the "SSH" at the top of the code block.
    ---
    All references to a mainboard usually refer to the 3MS board. If you are using a `(main MCU)` configuration, references to a mainboard refer to your printer's existing mainboard.

## Clone Repository

First, clone the 3MS repository:

```sh title="SSH"
cd ~
git clone https://github.com/3DCoded/3MS
cd 3MS
```

!!! failure "Storage"
    If the `git clone` command fails due to lack of storage on your system, run the following set of commands instead:

    ```sh title="SSH"
    cd ~
    git clone -b main --single-branch https://github.com/3DCoded/3MS
    cd 3MS
    ```

## Install Script

!!! info "K1 Series"
    If you are setting up the 3MS on a Creality K1 Series printer (K1, K1C, K1 Max), use the following install script instead:

    ```sh title="SSH"
    python3 install.py --path /usr/data/printer_data/config/3ms
    ```

Run the install script:

```sh title="SSH"
sh install.sh
```

## printer.cfg

In the Klipper web interface (e.g. Mainsail/Fluidd/OctoPrint), open `printer.cfg` and add:

```cfg title="printer.cfg"
[include 3ms/main.cfg]
```

## DynamicMacros

The 3MS configuration depends on [DynamicMacros](https://github.com/3dcoded/DynamicMacros). If you haven't installed it already, follow the instructions [here](https://3dcoded.github.io/DynamicMacros/setup/) to do so.

Remove the following line from your `3ms/main.cfg` if it exists:

```cfg title="3ms/main.cfg"
[include ./macros.cfg]
```

Add `3ms/macros.cfg` to your `[dynamicmacros]` config section. Example:

=== "Before"
    ```cfg
    [dynamicmacros]
    configs: macros.cfg,othermacros.cfg
    ```
=== "After"
    ```cfg
    [dynamicmacros]
    configs: macros.cfg,othermacros.cfg,3ms/macros.cfg
    ```

## Moonraker Update Manager

To enable updates for the 3MS, add the following to your `moonraker.conf` (in the same folder as your `printer.cfg`):

```cfg title="moonraker.conf"
# 3MS Update Manager
[update_manager mmms]
type: git_repo
path: ~/3MS
origin: https://github.com/3DCoded/3MS.git
primary_branch: main
is_system_service: False
install_script: install.sh
```

!!! warning
    When updating via Moonraker, the following files will be overwritten:
        
    - `macros.cfg`
    - `KlipperScreen.conf`
    - `endless/macros.cfg`
    
    If you have any changes in these files, they will be lost when updating.

## Controller

In `3ms/main.cfg`, edit the `[include ./controllers/xxx/steppers.cfg]` line, replacing `xxx` with the config name of your controller:

| Controller Name | Config Name |
| - | - |
| SKR Mini E3 V2 | `btt_skr_mini_e3_v2` |
| SKR Pico | `btt_skr_pico` |
| BTT MMB | `btt_mmb` |
| BTT Octopus (main MCU) | `btt_octopus_main` |
| Zonestar ZM384 (main MCU) | `zonestar_zm384_main` |
| Mini RAMBo | `mini_rambo` |
| Geetech A30T | `gtm32_103_v1` |

## Configure MCU ID

Finally, to configure the MCU ID you saved from [Firmware](firmware.md), run in your terminal:

```sh title="SSH"
cd ~ && cat mcu.txt
```

Copy the path that is output. Now, in your `3ms/controllers/xxx/steppers.cfg`, in the `[mcu 3ms]` section (towards the bottom), set the MCU ID.

Example:

=== "Before"
    ```cfg title="3ms/controllers/xxx/steppers.cfg"
    [mcu 3ms]
    serial: /dev/serial/by-id/<your-mcu-id>
    ```
=== "After"
    ```cfg title="3ms/controllers/xxx/steppers.cfg"
    [mcu 3ms]
    serial: /dev/serial/by-id/usb-Klipper_stm32f103xe_33FFD1054746333809650557-if00
    ```