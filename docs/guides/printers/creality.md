---
comments: true
icon: printers/creality
---

# Creality E3v3 series

## Introduction

The Creality K1 Ender 3 v3 series printers run a heavily modified Klipper and Linux installation. Because of this, setup isn't as straightforward as on a genuine Klipper and Linux install. If you have another printer running mainline Klipper, it is highly recommended to install the 3MS on it instead.

If you would like to use the 3MS on an E3v3, read on.

!!! tip
    Please read every step here carefully. If you run into issues, please reach out on the 3MS Discord (link on homepage) and note the step you are having trouble with.

??? warning "Disclaimer"
    I am not responsible for whatever happens to your machine! You proceed at your own risk and understand that you will likely void your warranty by proceeding.

## Instructions

Thank you **@dr-evil-23** for figuring this out!

1. Compile and flash Katapult to your board.

    If you're using an SKR Pico, select `W25Q080 with CLKDIV 2` as the flash chip.

2. Compile Klipper v0.12.0 and flash to your board.

You can follow the rest of the documentation as usual from here.

[Start Here](../../instructions/index.md){.md-button}