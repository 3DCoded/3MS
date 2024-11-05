---
title: 3MS Home
icon: material/home
---

# Welcome to the 3MS Documentation

The 3MS is short for MMMS, which stands for **M**odular **M**ulti **M**aterial **S**ystem

<img src="./assets/logo.png" alt="drawing" width="200"/>

## Inspiration

- Prusa MMU1
- Bambu AMS

## Sample Prints

???+ "Sample Prints"
    === "Sheep" 
        ![](samplesheep.jpeg){: style="height: 300px"}

        Model: [Sheep by Cipis](https://www.printables.com/model/838872-sheep-multi-material-remix)
    === "Calendar"
        ![](samplecalendar.jpeg){: style="width: 300px"}

        Model: [Monolith Cryptic Calendar by Sevro](https://www.printables.com/model/698341-monolith-cryptic-calendar)
    === "Voron Cube"
        ![](samplevoron.jpeg){: style="height: 300px"}

        Model: Voron Cube (bundled with OrcaSlicer), painted by me in OrcaSlicer
    === "T-Rex"
        ![](sampletrex.jpeg){: style="width: 300px"}

        Printed at 50% scale

        Model: [T-rex by Cipis](https://www.printables.com/model/5481-t-rex-multi-material)
    === "Lizard"
        ![](samplelizard.jpeg){: style="width: 300px"}

        Model: [Striped lizard with pupils by EngMike](https://www.printables.com/model/236193-striped-lizard-multi-material-with-pupils)

## Photos

???+ "Photos"
    === "Full Printer"
        ![](IMG_0318.jpeg)
    === "3MS"
        ![](IMG_0320.jpeg)
    === "Y Splitter"
        ![](IMG_0321.jpeg)

## Videos

???+ "West3D Video Series"
    Thank you to Allen Rowand from [West3D](https://west3d.com/) for making this ongoing series on the 3MS.
    
    <iframe width="560" height="315" src="https://www.youtube.com/embed/XfjHtymdHao?si=cHG1jreb8FfjpWaL" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

    <iframe width="560" height="315" src="https://www.youtube.com/embed/o4Fvtdl-XjM?si=16Prr2Djn4XP0n6q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Why 3MS?

Why use the 3MS when there are many other multi-material systems?

Here are a few reasons:

- **Simplified Design**: Minimal mechanical complexity for increased reliability.
- **Comprehensive Documentation**: Step-by-step guides to ensure smooth setup and operation.
- **Slicer-Agnostic**: No need for custom toolchange G-Code in your slicer.
- **Scalable**: Easily expand the system to handle any number of filaments.
- **Auto-Retries**: Automatic retries on failed tool changes to reduce downtime.
- **No Filament Cutter Needed**: Achieve clean tool changes without the need for filament cutters.
- **In Development: Rapid Tip Shaping**: Achieve even faster tool changes!

With that said, there are a few reasons why you might **not** want to/be able to use the 3MS:

- Klipper firmware is a requirement, so Marlin and RRF setups are a no go
- A filament sensor is required, so if you don't have one/don't plan to get one, the 3MS won't work with your setup

## Requirements

To use the 3MS, your setup has to meet the following requirements:

- Run Klipper firmware
- Have SSH (PuTTY) access (99.9% of Klipper installations have this, and if you don't you really should setup SSH)
- Have one spare USB port
- Have an adapter to install a PTFE tube to the inlet of your printer's extruder.

## How it works

!!! info "TODO"

Think of the 3MS as an extension to your current extruder's length. It allows for switching filaments without compromising any of the benefits of your printer's extruder.

The 3MS's motors work together with your printer's extruder. This way, there won't be any additional resistance from pulling the filament through a disabled extruder. Also, unloads and loads to/from the printer's extruder are fully synchronized with the 3MS. This allows for even faster toolchanges!

## Get Started

To get started with the 3MS, see the [Master Instructions](instructions.md).

[Get Started :material-format-list-numbered:](instructions.md){ .md-button }

## What about the 3DChameleon?

Several months ago, I created a klipper plugin for the 3DChameleon after purchasing a unit. While my Chameleon may have worked if I had tuned it further, I gave up after half a year with only partial success. I am still open to pull requests for **[3dchameleon-klipper](https://github.com/3dcoded/3dchameleon-klipper)**, but I won't be able to test it myself anymore.

If you are having reliability issues with the 3DChameleon, see [3DChameleon Conversion](3dchameleon.md).