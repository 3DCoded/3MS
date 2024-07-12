# Assembly

Follow this guide to assemble your 3MS.

## Printed Parts

An optional board enclosure for the SKR Mini E3 is available [here](https://www.printables.com/model/459809-bigtreetech-skr-mini-e3-v3-enclosure).

Additionaly, an optional univeral mount for the MK8 extruder using M3 bolts is available [here](../assets/stls/mk8m3.stl). Note that this requires 2-4 M3 bolts and a place to screw the bolts into.

Finally, you will need to print enough of [these](https://www.printables.com/model/541678-bambu-ams-no-catch-y-splitter-pc4-m10) Y splitters for the filament.

## MK8 Assembly

Next, assemble the MK8 extruders onto the NEMA17 motors using the provided instructions that came with them. If you use the mount provided above, make sure it is in between the MK8 and NEMA17. 

## Wiring

After that, route the wires from the NEMA17 to the controller board. Follow this table to determine which port to plug the motors into:

| Filament Unit # | Motor Port |
| - | - |
| 0 | XM |
| 1 | YM |
| 2 | ZAM or ZBM |
| 3 | E0M |

Now, grab your 12V PSU and two M-M duponts, one red and one black (M-M means that there is metal coming out of both ends of the cable). Plug the PSU into the wall, but don't plug the screw terminals into the PSU (the screw terminals have green)

1. Plug the red wire into the positive terminal of the screw termianls
2. Plug the black wire into the negative terminal of the screw terminals

    !!! danger
        These dupont cables are too thin to run much more than the stepper motors. If you run a heater or other power-intensive device off of the SKR board, the duponts and/or PSU can melt/catch fire. To reduce the risk of this, you can double up on the duponts or get thicker wires.

3. Following this image, choose either the DCIN or POWER input
![](skrminie3v2pins.jpg)
4. Route the two wires inside closest to your chosen input
5. Using the markings on the board, plug the red wire into the positive terminal on the SKR
6. Using the markings on the board, plug the black wire into the negative terminal on the SKR
7. Verify all connections

    !!! warning
        If the wires are plugged into the wrong place, or swapped polarities, your SKR, Stepper motors, and/or PSU can be badly damaged.

8. Plug the PSU screw terminals into the PSU wire

If the SKR lights up, you wired it correctly!

Finally, plug the SKR into your Klipper host with the blue cable that came with it.