<link rel="stylesheet" href="../assets/css/badges.css">

# Master Instructions

Due to the modularity of the 3MS, there are many ways to set it up. This guide attempts to encompass all supported ways of setting up the 3MS.

## Basic Steps

The basic steps this guide will follow are:

1. Getting a BOM
2. Assembling your 3MS
3. Configuring your 3MS
4. Stepper motor setup
5. Slicer setup
6. First print
7. Troubleshooting

## 0. Explanations

Before starting the instructions, a basic understanding of how the 3MS works is recommended. There are two types of components in the 3MS:

- Controller

    This controls the stepper motors

- Filament Units

    This moves the filament

The number of filaments you will be able to print with is equal to the number of filament units you have. For example, two filament units will let you print with two colors. It is important to note that one filament unit will NOT let you print in multimaterial.

## 1. Getting a BOM

Go to [BOM](bom.md) to view the bill of materials for the number of filament units you want. Example BOM for two filament units:

| Name | Price | Quantity | Link | Notes |
| - | - | - | - | - |
| SKR Mini E3 V2 | $34.99 | 1 | [Amazon](https://a.co/d/0hgHU9JX) | |
Duponts | $9.99 | 1 | [Amazon](https://a.co/d/6QwGxhH) | These wires are only sufficient to run steppers, not heaters |
| 12V PSU | $7.39 | 1 | [Amazon](https://a.co/d/gLC1eli) | This PSU is only sufficient to run steppers, not heaters |
| NEMA17 Stepper Motor | $9.99 | 2 | [Amazon](https://a.co/d/06Lsa1qI) | You can use a pancake stepper if you want, but it will have less torque
| MK8 Metal Extruder | $9.99 | 2 | [Amazon](https://a.co/d/0gJ1ghKj) | |
| Capricorn PTFE Tubing | $11.49 | 1 | [Amazon](https://a.co/d/0dLLBGzJ) | You likely won't need this for every unit, as this is usually too long for only one unit |

## 2. Assembling your 3MS

An optional board enclosure for the SKR Mini E3 is available [here](https://www.printables.com/model/459809-bigtreetech-skr-mini-e3-v3-enclosure).

Additionaly, an optional univeral mount for the MK8 extruder using M3 bolts is available [here](assets/stls/mk8m3.stl).

Next, assemble the MK8 extruders onto the NEMA17 motors using the provided instructions that came with them. If you use the mount above, make sure it is in between the MK8 and NEMA17. 

After that, route the wires from the NEMA17 to the controller board. Follow this table to determine which port to plug the motors into:

| Filament Unit # | Motor Port |
| - | - |
| 0 | XM |
| 1 | YM |
| 2 | ZAM or ZBM |
| 3 | E0M |

Now, grab your 12V PSU and two M-M duponts, one red and one black (M-M means that there is metal coming out of both ends of the cable). Plug the PSU into the wall, but don't plug the screw terminals into the PSU (the screw terminals have green)

1. Plug the red wire into the positive terminal of the screw termianls
2. Plug the black wire into the negative terminal of the screw terminals
3. Following this image, choose either the DCIN or POWER input
![](skrminie3v2pins.jpg)
4. Route the two wires inside closest to your chosen input
5. Using the markings on the board, plug the red wire into the positive terminal on the SKR
6. Using the markings on the board, plug the black wire into the negative terminal on the SKR
7. Verify all connections
8. Plug the PSU screw terminals into the PSU wire

If the SKR lights up, you wired it correctly!

Finally, plug the SKR into your Klipper host with the blue cable that came with it.

## 3. Configuring your 3MS

### 3.1. Flash Klipper Firmware

After assembling your 3MS, the next step is to configure it. First, make sure it is plugged into your Klipper Host. Run in your terminal:

```sh
cd ~/klipper
make menuconfig
```

In the menuconfig, configure it to your controller. Instructions are included at the top of `3ms/steppers.cfg` for future reference. A copy of it is provided here:
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

The `klipper.bin` file, located in `~/klipper/out/klipper.bin` needs to be copied to a MicroSD card and renamed to `firmware.bin` (case-sensitive). Next, unplug the 3MS board from the PSU and your Klipper Host and insert the SD Card. Next, plug in the PSU, THEN the Klipper Host to the 3MS board. The firmware is now flashed.

In the terminal, run:

``` sh
ls /dev/serial/by-id/*
```

Example output:

``` sh
/dev/serial/by-id/usb-Klipper_stm32f103xe_33FFD1054746333809650557-if00
/dev/serial/by-id/usb-Prusa_Research__prusa3d.com__Original_Prusa_i3_MK3_xxx-if00
```

In this case, the first line is the 3MS, and the second line is the 3D printer. Now that you know the path to the 3MS, copy it.

### 3.2. Install 3MS Configuration

Next, clone the 3MS repository:

```sh
cd ~
git clone https://github.com/3DCoded/3MS
cd 3MS
```

To install the 3MS config, use:

```sh
python3 install.py
```

In your `printer.cfg`, add:

```cfg title="printer.cfg"
[include 3ms/main.cfg]
```

In your `moonraker.conf`, add:
```cfg title="moonraker.conf"
# 3MS Update Manager
[update_manager mmms]
type: git_repo
path: ~/3MS
origin: https://github.com/3DCoded/3MS
install_script: ~/3MS/install.sh
```

## 4. Stepper motor setup

Follow [Stepper Setup](steppers.md) to setup and calibrate each of your filament units.

## 5. Slicer setup

Follow [Slicer Setup](slicer.md) to setup your slicer for the 3MS.

## 6. First print

!!! info
    This section is a work in progress.

## 7. Troubleshooting

!!! info
    This section is a work in progress (collecting possible failures). If you experienced a failure with the 3MS, please submit it as an issue on Github.