---
icon: material/check
comments: true
---

# BTT SKR Pico

**Max filament units: 4**

**MCU Name: `mmu`**

## BOM

| Name | Price | Quantity | Link | Notes |
| - | - | - | - | - |
| SKR Pico | $26.58 | 1 | [BIQU](https://biqu.equipment/products/btt-skr-pico-v1-0?variant=40565262155874) | |
24AWG Power Cables | $9.99 | 1 | [Amazon](https://a.co/d/5iee9KD) | These wires are only sufficient to run steppers, not heaters |
| 24V PSU | $12.98 | 1 | [Amazon](https://a.co/d/6BJT2RP) | This PSU is only sufficient to run steppers, not heaters |

{{ filUnitBOM }}

## Wiring

Route the wires from the NEMA17's to the controller board. Follow this table to determine which port to plug the motors into:

| Filament Unit # | Motor Port |
| - | - |
| 0 | X |
| 1 | Y |
| 2 | Z1 or Z2 |
| 3 | E |

Now, grab your 24V PSU and two M-M duponts, one red and one black (M-M means that there is metal coming out of both ends of the cable). Plug the PSU into the wall, but don't plug the screw terminals into the PSU (the screw terminals have green)

1. Plug the red wire into the positive terminal of the screw terminals
2. Plug the black wire into the negative terminal of the screw terminals

    !!! danger
        These dupont cables are too thin to run much more than the stepper motors. If you run a heater or other power-intensive device off of the SKR board, the duponts and/or PSU can melt/catch fire. To reduce the risk of this, you can double up on the duponts or get thicker wires.

3. Following this image, locate the POWER input
![](skrpicopins.png)
4. Route the two wires inside closest to the POWER input
5. Using the markings on the board, plug the red wire into the positive terminal on the SKR
6. Using the markings on the board, plug the black wire into the negative terminal on the SKR
7. Verify all connections

    !!! warning
        If the wires are plugged into the wrong place, or swapped polarities, your SKR, Stepper motors, and/or PSU can be badly damaged.

8. Plug the PSU screw terminals into the PSU wire

If the SKR lights up, you wired it correctly!

Finally, plug the SKR into your Klipper host with the blue cable that came with it.

## Firmware Installation

Setting up firmware for the SKR Pico can be divided into four major steps:

1. Compile Katapult (bootloader)
2. Flash Katapult
3. Compile Klipper
4. Flash Klipper

### Compiling Katapult

You have two options for installing Katapult to the SKR Pico:

=== "1. Compile Katapult yourself"
    Run the following commands in SSH:

    ```
    cd ~/
    git clone https://github.com/Arksine/katapult
    cd katapult
    make menuconfig
    ```

    Adjust your `menuconfig` parameters to match the following exactly.

    ![](445b5e6f.png)

    Then, run:

    ```
    make clean
    make
    cp out/katapult.uf2 ~/printer_data/config/katapult.uf2
    ```

    Now in Mainsail/Fluidd, download `katapult.uf2` from your printer's config folder onto your computer and proceed to flashing.

=== "2. Download precompiled Katapult (compiled August 4, 2025)"
    Download [katapult.uf2](../assets/klipper/katapult.uf2) to your computer and proceed to flashing.

### Flashing Katapult

Now that you have `katapult.uf2` on your computer, install the BOOT and VUSB jumpers onto the SKR Pico as shown in the below diagram.

![](https://docs.vorondesign.com/build/software/images/SKR_Pico_Pin_Flashing.png)

/// caption
Credits: Voron Design
///

Plug the SKR Pico into your computer with the USB-C cable that came with it. It should show up as a USB drive.

Drag `katapult.uf2` into the drive. It should quickly disconnect then reconnect itself.

Now, remove the BOOT jumper and unplug the Pico from your computer.

### Compiling Klipper

Now, SSH into your Pi again and run the following commands:

```
cd ~/klipper
make menuconfig
```

Adjust your `menuconfig` settings to match this exactly:

![](3b466bdb.png)

Now, run:

```
make clean
make
```

### Flashing Klipper

Run in SSH:

```
ls /dev/serial/by-id/*
```

Plug the Pico into your Pi.

```
ls /dev/serial/by-id/*
```

There should be a new USB device shown after plugging the Pico in. Copy the entire path, including `/dev/serial/by-id/`, and run the final commands:

```
cd ~/klipper
make flash FLASH_DEVICE=<PASTE HERE>
```

Your SKR Pico is now successfully flashed with Katapult and Klipper.