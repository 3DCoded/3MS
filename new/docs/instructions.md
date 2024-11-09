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

Set up Happy Hare firmware following [this guide](happy-hare.md).

