---
comments: true
---

# Mellow Fly D7

**Max filament units: 7**

**MCU Name: `3ms`**

## BOM

| Name | Price | Quantity | Link | Notes |
| - | - | - | - | - |
| Mellow Fly D7 |  | 1 | | |
22AWG Cables | $9.99 | 1 | [Amazon](https://a.co/d/0oP9cD3) | These wires are only sufficient to run steppers, not heaters |
| 12V PSU | $7.39 | 1 | [Amazon](https://a.co/d/gLC1eli) | This PSU is only sufficient to run steppers, not heaters |

{{ filUnitBOM }}

## Wiring

Route the wires from the NEMA17's to the controller board. Follow this table to determine which port to plug the motors into:

| Filament Unit # | Motor Port |
| - | - |
| 0 | X |
| 1 | Y |
| 2 | Z |
| 3 | Z1 |
| 4 | Z2 |
| 5 | E0 |

Now, grab your 12V PSU and two M-M duponts, one red and one black (M-M means that there is metal coming out of both ends of the cable). Plug the PSU into the wall, but don't plug the screw terminals into the PSU (the screw terminals have green)

1. Plug the red wire into the positive terminal of the screw terminals
2. Plug the black wire into the negative terminal of the screw terminals

    !!! danger
        These dupont cables are too thin to run much more than the stepper motors. If you run a heater or other power-intensive device off of the board board, the duponts and/or PSU can melt/catch fire. To reduce the risk of this, you can double up on the duponts or get thicker wires.

5. Using the markings on the board, plug the red wire into the positive terminal on the board
6. Using the markings on the board, plug the black wire into the negative terminal on the board
7. Verify all connections

    !!! warning
        If the wires are plugged into the wrong place, or swapped polarities, your board, Stepper motors, and/or PSU can be badly damaged.

8. Plug the PSU screw terminals into the PSU wire

If the board lights up, you wired it correctly!

Finally, plug the board into your Klipper host with the cable that came with it.