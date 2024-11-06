---
icon: octicons/list-ordered-24
comments: true
---

<link rel="stylesheet" href="../assets/css/badges.css">

# Master Instructions

Due to the modularity of the 3MS, there are many ways to set it up. This guide attempts to encompass all supported ways of setting up the 3MS.

## Basic Steps

The basic steps this guide will follow are:

1. [Getting a BOM](#1-getting-a-bom)
2. [Assembling your 3MS](#2-assembling-your-3ms)
3. [Configuring your 3MS](#3-configuring-your-3ms)
4. [Stepper motor setup](#4-stepper-motor-setup)
5. [Slicer setup](#5-slicer-setup)
6. [First print](#6-first-print)
7. [Troubleshooting](#7-troubleshooting)
8. [Updating](#8-updating)

## 0. Explanations

Before starting the instructions, a basic understanding of how the 3MS works is recommended. There are two types of components in the 3MS:

- Controller

    This controls the 3MS stepper motors. This is usually an extra 3D printer mainboard purchased specifically for the 3MS. If your existing 3D printer mainboard has spare stepper ports, you can use them for the 3MS. 

    The available configurations are specific to either an external mainboard setup, or utilizing spare stepper ports on your existing mainboard. If you are utilizing spare stepper ports, the name of the config will include "(main MCU)"

- Filament Units

    These move the filament. These are standard MK8 extruders (used on Ender 3's). You can use different extruders for the filament units, as long as you can mount them securely and they can attach to a PTFE tube. MK8 extruders are used as the default due to their low cost. 

The number of filaments you will be able to print with is equal to the number of filament units you have. For example, two filament units will let you print with two colors. It is important to note that one filament unit will NOT let you print in multimaterial.

## 0.5. Choosing a Controller

Choose one of the controllers from [Controllers](setup/controllers/index.md) before continuing.

## 1. Getting a BOM

Go to [BOM](bom.md) to view the bill of materials for the number of filament units you want. Example BOM for two filament units and a SKR Mini E3 V2:

| Name | Price | Quantity | Link | Notes |
| - | - | - | - | - |
| SKR Mini E3 V2 | $34.99 | 1 | [Amazon](https://a.co/d/0hgHU9JX) | |
Duponts | $9.99 | 1 | [Amazon](https://a.co/d/6QwGxhH) | These wires are only sufficient to run steppers, not heaters |
| 12V PSU | $7.39 | 1 | [Amazon](https://a.co/d/gLC1eli) | This PSU is only sufficient to run steppers, not heaters |
| NEMA17 Stepper Motor | $9.99 | 2 | [Amazon](https://a.co/d/06Lsa1qI) | You can use a pancake stepper if you want, but it will have less torque
| MK8 Metal Extruder | $9.99 | 2 | [Amazon](https://a.co/d/0gJ1ghKj) | |
| Capricorn PTFE Tubing | $11.49 | 1 | [Amazon](https://a.co/d/0dLLBGzJ) | You likely won't need this for every unit, as this is usually too long for only one unit |

## 2. Assembling your 3MS

Follow [Assembly](assembly.md) to assemble your 3MS.

## 3. Configuring your 3MS

1. Install Klipper firmware onto the MCU by following [Firmware](firmware.md).
2. Install [DynamicMacros](https://github.com/3dcoded/DynamicMacros), following instructions from [here](https://3dcoded.github.io/DynamicMacros/setup/).
3. Follow [Installation](install.md) to install the 3MS configuration.
4. Follow [Filament Sensor](fsensor.md) to setup your filament sensor with the 3MS.

## 4. Stepper motor setup

Follow [Stepper Setup](steppers.md) to setup and calibrate each of your filament units.

## 5. Slicer setup

Follow [Slicer Setup](slicer.md) to setup your slicer for the 3MS.

## 6. First print

Follow [First Print](firstprint.md) to create your first multimaterial print with the 3MS.

## 7. Troubleshooting

Check [Troubleshooting](troubleshooting/index.md) to find guides to troubleshoot your 3MS.

## 8. Updating

To update the 3MS configuration, go to the Update Manager in Mainsail/Fluidd and refresh the updates. 

![](updating1.png)

Next, find the "mmms" entry in the list. If there is an "Update" button next to it, click it and begin updating. 

After updating, in your terminal, run:

```sh
sh ~/3MS/install.sh
```

This will install the new 3MS configuration. Next, restart Klipper:

!!! info
    It is important to restart the Klipper **service**, and not just run the `RESTART` command.

Run this command in your terminal:

```sh
sudo service klipper restart
```

## 9. Tuning and Optimizations

After your 3MS is installed, it's time to tune and optimize it.

The best starting place for this is in the [Materials Reference](materials.md).