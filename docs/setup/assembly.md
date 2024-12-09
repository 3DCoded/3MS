---
icon: material/tools
comments: true
---

# Assembly

Follow this guide to assemble your 3MS.

## Printed Parts

### Mounting

<div class="grid cards" markdown>

- <iframe id="vs_iframe" src="https://www.viewstl.com/?embedded&url=https%3A%2F%2F3dcoded.github.io%2F3MS%2Fassets%2Fstls%2Fmk8m3.stl&color=blue&bgcolor=transparent&noborder=yes" style="border:0;margin:0;width:100%;height:100%;"></iframe>

    **[Univeral M3 Mount for Extruder](../assets/stls/mk8m3.stl)** Note that this requires 2-4 M3 bolts and a place to screw the bolts into (like an aluminum extrusion with T-nuts). Designed by **3DCoded**.

- <img src="https://media.printables.com/media/prints/1067703/images/8088653_02c779e6-ba6e-467c-a42e-ce7769189863_4913595f-da9b-4cf3-b618-52f3373aaaef/thumbs/inside/1600x1200/jpg/20241109_214315.webp" height="100" />

    **[3MS Box](https://www.printables.com/model/1067703-wip-3ms-mmu-using-btt-mmb)** This is designed for four filament units and a BTT MMB. Designed by **chadakken**.

</div>

### Y-Splitters

<div class="grid cards" markdown>

- <img src="https://media.printables.com/media/prints/1042279/images/7911671_cf864755-81d4-4b1d-a9f2-1c4f1d77bc24_9ce3f0a3-2276-419e-8c8c-faa9a5ec9ef3/thumbs/inside/1600x1200/jpg/photo_2024-10-18_18-33-02.webp" height="50" />

    **[4-way Y-splitter](https://www.printables.com/model/1042279-no-catch-4-way-y-splitter-pc4-m10)** designed by **ImChrono**.

- <img src="https://media.printables.com/media/prints/1092036/images/8258786_8a2ebad0-2344-4455-8620-5de05c3bdb3c_712845da-7242-48d9-b5d1-c9bc95b64d00/thumbs/inside/1600x1200/png/5.webp" height="100" />

    **[4-way Y-splitter with ECAS04 and M3 Bolt](https://www.printables.com/model/1092036-4-tube-y-splitter-for-mmu)** designed by **Jager-f**.

- <img src="https://media.printables.com/media/prints/1103095/images/8338186_1e66aafd-0187-42a4-bed7-420d532541cb_9d93d093-db12-434a-a4c1-8aa2e3bf8fc3/thumbs/inside/1600x1200/png/img_0424.webp" height="100" />

    **[4-way Y splitter with ECAS04](https://www.printables.com/model/1103095-4-way-y-splitter-with-ecas04)** designed by **3DCoded**.

</div>

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