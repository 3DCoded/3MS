---
icon: material/tools
comments: true
---

# Assembly

Follow this guide to assemble your 3MS.

## Printed Parts

### Mounting

- **[Univeral M3 Mount for Extruder](../assets/stls/mk8m3.stl)** Note that this requires 2-4 M3 bolts and a place to screw the bolts into (like an aluminum extrusion with T-nuts).
- **[3MS Box](https://www.printables.com/model/1067703-wip-3ms-mmu-using-btt-mmb)** This is designed for four filament units and a BTT MMB. Designed by **chadakken**.

### Other

- **[4-way Y-splitter](https://www.printables.com/model/1042279-no-catch-4-way-y-splitter-pc4-m10)** designed by **ImChrono**.

## Filament Units Assembly

1. If using any mounting parts, place it on the face of your NEMA17 motor.
2. Assemble the MK8 extruders using the instructions that came with them.
3. Repeat for all filament units.

## Wiring

!!! note "Note for Certain Printers"
    If your printer has Klipper running internally (not on an external computer like a Raspberry Pi), the controller (if not a main MCU config) is plugged into a USB port on the printer itself.

Follow one of the following guides based on your controller:

**Recommended: [BTT MMB](bttmmb.md#wiring)**

---

**Other Controllers:**

- [SKR Mini E3 V2](skrminie3v2.md#wiring)
- [SKR Pico](skrpico.md#wiring)
- [Mellow Fly D7](mellowflyd7.md#wiring)
- [BTT Octopus (main MCU)](bttoctopusmain.md#wiring)
- [Einsy RAMBo (main MCU) with SKR Mini E3 V2](einsyrambo-skrminie3v2.md)
- [Zonestar ZM384 (main MCU)](zm384main.md)
- [Mi ni RAMBo](minirambo.md)
- [Geetech A30T](geetech-a30t.md)