# Einsy RAMBo (main MCU) with SKR Mini E3 V2

!!! danger
    This guide is an expert guide only and under construction.

!!! info
    This modification is designed for the Prusa MK3/S/S+.

## Why?

When printing fast, the TMC2130's on the Einsy RAMBo can get quite loud. The TMC2209's on the SKR Mini are much quieter and support denser microstepping.

## BOM

!!! info
    This section is under construction.

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

!!! info
    This section is under construction.