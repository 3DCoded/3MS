# Welcome to the 3MS Documentation

The 3MS is short for MMMS, which stands for **M**odular **M**ulti **M**aterial **S**ystem

## Inspiration

- Prusa MMU1
- Bambu AMS

## Why 3MS?

Why use the 3MS when there are many other multi-material systems? 

Here are a few reasons:

- Extremely simple design increases reliability
- Extensive documentation to help setup, optomize, and troubleshoot
- No slicer custom G-Code needed
- Easily expandable to any number of filaments
- No need to fine tune tip shaping

With that said, there are a few reasons why you might **not** want to/be able to use the 3MS:

- Klipper firmware is a requirement, so Marlin and RRF setups are a no go
- A strong, dual drive extruder is highly recommended, so budget printers may need to upgrade their extruders first

## How it works

Here is a example step by step of what goes on during a single 3MS toolchange from T0 to T1:

1. Tip shaping and filament unload is performed by the slicer
2. The 3MS unloads T0 175mm at 4500mm/min (75mm/s)
3. The 3MS loads T1 200mm at 4500mm/min
4. The 3MS motors are turned off
5. The printer loads the filament to the nozzle
<!-- 
??? "How it works (detailed)"
    1. Tip shaping and filament unload is performed by the slicer
    2. The T0 command is called
    3. T0 calls Toolchange T=0
    5. If the previous extruder is not -1 (no previous extruder), an unload is performed via G100
    6. CHECK_FSENSOR is called to verify the filament unloaded successfully
    7. A load is performed via G100
    8. CHECK_FSENSOR is called to verify the filament loaded successfully -->

## What about the 3DChameleon?

I recently created a klipper plugin for the 3DChameleon after purchasing a unit. I'm sure my Chameleon could have worked if I had tuned it further, but after several months with only partial success, I gave up. I am still open to pull requests for **[3dchameleon-klipper](https://github.com/3dcoded/3dchameleon-klipper)**, but I won't be able to test it myself anymore.

