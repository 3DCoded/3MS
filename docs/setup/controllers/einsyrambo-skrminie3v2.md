---
icon: material/check
comments: true
---

# Einsy RAMBo (main MCU) with SKR Mini E3 V2

!!! danger
    This guide is an expert guide only

!!! info
    This modification is designed for the Prusa MK3/S/S+, and depends on [this](https://github.com/dz0ny/klipper-prusa-mk3s) Klipper configuration.

## Why?

When printing fast, the TMC2130's on the Einsy RAMBo can get quite loud. The TMC2209's on the SKR Mini are much quieter and support denser microstepping.

## BOM

| Name | Price | Quantity | Link | Notes |
| - | - | - | - | - |
| PSU -> Einsy Cable | $7.99 | 1 | [PartsBuilt3D](https://www.partsbuilt.com/cable-psu-to-einsy-for-prusa-mk3-3s-3s-prusa-compatible/) | |
| Stepperonline NEMA17 | $9.99 each | [Amazon](https://a.co/d/el99D6X) | 2 | Replaces current XY motors |

## Wiring

First, unplug the 3MS steppers from the SKR Mini, and the XY steppers from the Einsy RAMBo. The motors will need to be switched due to different connector types between boards.

This table outlines the major wiring of this modification.

| Einsy RAMBo | SKR Mini E3 V2 | Motor
| - | - | - |
| PSU+ | POWER+ | |
| PSU- | POWER- | |
| XM | | 3ms0 |
| YM | | 3ms1 |
| | XM | X |
| | YM | Y | 

## Configuration

In your `printer.cfg`, comment out these lines:

```cfg title="printer.cfg"
#[include klipper-prusa-mk3s/mk3s/steppers.cfg]
#[include klipper-prusa-mk3s/mk3s/tmc2130.cfg]
```

Next, copy the contents of `3ms/controllers/einsy_rambo_with_skr_mini/xy-motors.cfg` and `ze-motors.cfg` to `klipper-prusa-mk3s/skr/xy.cfg`, and `klipper-prusa-mk3s/mk3s/ze.cfg`, respectively.

Add the following new lines:

```cfg title="printer.cfg"
[include klipper-prusa-mk3s/skr/xy.cfg]
[include klipper-prusa-mk3s/mk3s/ze.cfg]
```

Restart Klipper.