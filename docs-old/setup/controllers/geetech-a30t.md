---
comments: true
---

# Geetech A30T

**Contributed by [@ImChrono](https://github.com/ImChrono)**

---

**Max filament units: 7**

**MCU Name: `3ms`**

## BOM

| Name | Price | Quantity | Link | Notes |
| - | - | - | - | - |
| Geetech A30T | $34.99 | 1 | [Geetech](https://www.geeetech.com/a30t-printer-gtm32103v1-control-board-p-1190.html) | |
Duponts | $9.99 | 1 | [Amazon](https://a.co/d/6QwGxhH) | These wires are only sufficient to run steppers, not heaters |
| 24V PSU | $7.39 | 1 | [Amazon](https://a.co/d/1Ko6QMB) | This PSU is only sufficient to run steppers, not heaters |

## Firmware

To flash Klipper firmware to the A30T, run the following command and see the following screenshot:

```sh
cd ~/klipper
make menuconfig
```

![](a30tfirmware.jpeg)

Next, connect the **BOOT0** jumper on the A30T and run:

```sh
stm32flash -i ',,,,,' -v -w out/klipper.bin -g 0 /dev/serial/by-id/<your-mcu-id-here>
```

## Wiring

Route the wires from the NEMA17's to the controller board. Follow this table to determine which port to plug the motors into:

| Filament Unit # | Motor Port |
| - | - |
| 0 | X |
| 1 | Y |
| 2 | Z0 |
| 3 | Z1 |
| 4 | E1 |
| 5 | E2 |
| 6 | E3 |

Now, grab your 12V PSU and two M-M duponts, one red and one black (M-M means that there is metal coming out of both ends of the cable). Plug the PSU into the wall, but don't plug the screw terminals into the PSU (the screw terminals have green)

1. Plug two red wires into the positive terminal of the screw terminals
2. Plug two black wires into the negative terminal of the screw terminals

    !!! danger
        These dupont cables are too thin to run much more than the stepper motors. If you run a heater or other power-intensive device off of the motherboard, the duponts and/or PSU can melt/catch fire. To reduce the risk of this, you can double up on the duponts or get thicker wires.

4. Route the four wires inside closest to your chosen input
5. Using the markings on the board, plug the two red wires into the positive terminal on the motherboard
6. Using the markings on the board, plug the two black wires into the negative terminal on the motherboard
7. Verify all connections

    !!! warning
        If the wires are plugged into the wrong place, or swapped polarities, your motherboard, Stepper motors, and/or PSU can be badly damaged.

8. Plug the PSU screw terminals into the PSU wire

If the motherboard lights up, you wired it correctly!

Finally, plug the motherboard into your Klipper host with the cable that came with it.