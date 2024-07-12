# Installation

Follow this guide to install the 3MS configuration and macros.

## Clone Repository

First, clone the 3MS repository:

```sh
cd ~
git clone https://github.com/3DCoded/3MS
cd 3MS
```

## Install Script

Run the install script:

```sh
sh install.sh
```

## printer.cfg

In your `printer.cfg`, add:

```cfg title="printer.cfg"
[include 3ms/main.cfg]
```

## Moonraker Update Manager

To enable updates for the 3MS, add the following to your `moonraker.conf`:

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
        
    - `main.cfg`
    - `macros.cfg`
    - `KlipperScreen.conf`
    
    If you have any changes in these files, they will be lost when updating.

## Configure MCU ID

Finally, to configure the MCU ID you saved from [Firmware](firmware.md), run in your terminal:

```sh
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