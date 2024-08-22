# Firmware

Follow this guide to install Klipper firmware onto your 3MS MCU. This guide is a modified version of the [Klipper Documentation](https://www.klipper3d.org/Installation.html#building-and-flashing-the-micro-controller).

!!! info
    The following controller(s) can skip this guide:
    
    - BTT Octopus (main MCU)
    - Zonestar ZM384 (main MCU)

## Create firmware.bin

Make sure your 3MS MCU is plugged into your Klipper Host. Run in your terminal:

```sh
cd ~/klipper
make menuconfig
```

In the menuconfig, configure it to your MCU. Instructions are included at the top of `3ms/controllers/xxx/steppers.cfg` for future reference. A copy of it is provided here:

```cfg
# This file contains common pin mappings for the BIGTREETECH SKR mini
# E3 v2.0. To use this config, the firmware should be compiled for the
# STM32F103 with a "28KiB bootloader" and USB communication. Also,
# select "Enable extra low-level configuration options" and configure
# "GPIO pins to set at micro-controller startup" to "!PA14".
```

Run in your terminal:

```sh
make clean
make
```

The `klipper.bin` file, located in `~/klipper/out/klipper.bin` needs to be copied to a MicroSD card and renamed to `firmware.bin` (case-sensitive). 

## Install firmware.bin

Next, unplug the 3MS board from the PSU and your Klipper Host and insert the SD Card. Next, plug in the PSU, THEN the Klipper Host to the 3MS board. The firmware is now flashed.

## Get MCU ID

In the terminal, run:

```sh
ls /dev/serial/by-id/
```

Example output:

```sh
usb-Klipper_stm32f103xe_33FFD1054746333809650557-if00
usb-Prusa_Research__prusa3d.com__Original_Prusa_i3_MK3_xxx-if00
```

In this case, the first line is the 3MS, and the second line is the 3D printer. Now that you know the id of the 3MS MCU, copy it and save it to a file:

```sh
cd ~ && echo "<your-mcu-id>" >> mcu.txt 
```
