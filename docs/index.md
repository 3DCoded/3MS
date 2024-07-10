# Welcome to the 3MS Documentation

The 3MS is short for MMMS, which stands for **M**odular **M**ulti **M**aterial **S**ystem

## Inspiration

- Prusa MMU1
- Bambu AMS

!!! info
    This documentation is still under construction. If you have any questions not answered by the documentation, please open an issue on Github.

## Sample Prints

![](samplesheep.jpeg){: style="height: 300px"}

Model: [Sheep by Cipis](https://www.printables.com/model/838872-sheep-multi-material-remix)

---


![](samplecalendar.jpeg){: style="width: 300px"}

Model: [Monolith Cryptic Calendar by Sevro](https://www.printables.com/model/698341-monolith-cryptic-calendar)

---

![](samplevoron.jpeg){: style="height: 300px"}

Model: Voron Cube (bundled with OrcaSlicer), painted by me

## Why 3MS?

Why use the 3MS when there are many other multi-material systems? 

Here are a few reasons:

- Extremely simple design increases reliability
- Thorough documentation to help setup, optomize, and troubleshoot
- No slicer custom toolchange G-Code needed
- Easily expandable to any number of filaments (currently up to four)
- In development: [Toolchanges Without Tip Shaping or Filament Cutter!](notip.md)

With that said, there are a few reasons why you might **not** want to/be able to use the 3MS:

- Klipper firmware is a requirement, so Marlin and RRF setups are a no go

## How it works

Here is a example step by step of what goes on during a single 3MS toolchange from T0 to T1:

1. Tip shaping and filament unload is performed by the slicer
2. The 3MS unloads T0 200mm at 4500mm/min (75mm/s)
3. The 3MS desyncs T0 from the extruder
4. The 3MS syncs T1 with the extruder
3. The 3MS loads T1 210mm at 4500mm/min
5. The printer loads the filament to the nozzle

The 3MS's motors work together with your printer's extruder. This way, there won't be any additional resistance from pulling the filament through a disabled extruder. Also, unloads and loads to/from the printer's extruder are fully synchronized with the 3MS. This allows for even faster toolchanges!

## Get Started

To get started with the 3MS, see the [Master Instructions](instructions.md).

## What about the 3DChameleon?

I recently created a klipper plugin for the 3DChameleon after purchasing a unit. I'm sure my Chameleon could have worked if I had tuned it further, but after several months with only partial success, I gave up. I am still open to pull requests for **[3dchameleon-klipper](https://github.com/3dcoded/3dchameleon-klipper)** and will do my best to respond to issues there, but I won't be able to test it myself anymore.

