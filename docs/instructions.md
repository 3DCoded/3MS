---
icon: octicons/list-ordered-24
comments: true
---

<link rel="stylesheet" href="../assets/css/badges.css">

# Master Instructions

Due to the modularity of the 3MS, there are many ways to set it up. This guide attempts to encompass all supported ways of setting up the 3MS.

## Chapters

<div class="grid cards" markdown>

- [![](cart.png)](../setup/bom)

    ---

    [**1. Getting a BOM**](bom.md){.md-button}

- [![](https://media.printables.com/media/prints/1108644/images/8694982_810aef1c-c234-4c27-9fc3-0622c43060a5_991d3c58-1fb9-4227-90db-8cb3b15da9e1/thumbs/inside/1600x1200/png/r0.webp)](assembly.md)

    ---

    [**2. Hardware Assembly**](assembly.md){.md-button}

- [![](step08a.jpeg)](../setup/assembly#wiring)

    ---

    [**3. Electrical Assembly**](../setup/assembly#wiring){ .md-button }

- [![](https://github.com/moggieuk/Happy-Hare/wiki/resources/happy_hare_logo.jpg)](https://github.com/moggieuk/Happy-Hare/wiki/Quick-Start-3MS)

    ---
    
    [**4. Software Setup**](https://github.com/moggieuk/Happy-Hare/wiki/Quick-Start-3MS){ .md-button }

- [![](https://www.shutterstock.com/image-photo/electronic-vernier-caliper-close-view-600nw-2290639641.jpg)](#)

    Image credit: Shutterstock

    ---

    [**5. Configuration**](config.md){.md-button}
    [**& Calibration**](calibration.md){.md-button}
</div>

<!-- ## Basic Steps

The basic steps this guide will follow are:

1. [Getting a BOM](#1-getting-a-bom)
2. [Assembling your 3MS](#2-assembling-your-3ms)
3. [Configuring your 3MS](#3-configuring-your-3ms)
4. [Calibrating your 3MS](#4-calibrating-your-3ms)

## 0. Explanations

Before starting the instructions, a basic understanding of how the 3MS works is recommended. There are two types of components in the 3MS:

- Controller

    This controls the 3MS stepper motors. This is usually an extra 3D printer mainboard purchased specifically for the 3MS. If your existing 3D printer mainboard has spare stepper ports, you can use them for the 3MS. 

    The available configurations are specific to either an external mainboard setup, or utilizing spare stepper ports on your existing mainboard. If you are utilizing spare stepper ports, the name of the config will include "(main MCU)"

    **"controller" can be used interchangeably with "MCU" and "control board"**

- Filament Units

    These move the filament. These are standard MK8 extruders (used on Ender 3's). You can use different extruders for the filament units, as long as you can mount them securely and they can attach to a PTFE tube. MK8 extruders are used as the default due to their low cost. 

    **"filament unit" and "gate" can be used interchangeably**

The number of filaments you will be able to print with is equal to the number of filament units you have. For example, two filament units will let you print with two colors. It is important to note that one filament unit will NOT let you print in multimaterial.

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

Set up Happy Hare firmware following [this guide](https://github.com/moggieuk/Happy-Hare/wiki/Quick-Start-3MS).

If you're looking for a configuration, see [generator guide](generator.md).

Next, configure Happy Hare firmware using [this guide](config.md).

## 4. Calibrating your 3MS

After installing and configuring Happy Hare, the 3MS requires some calibrations. Follow [Calibration](calibration.md) to calibrate your 3MS. -->