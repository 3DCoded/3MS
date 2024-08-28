---
icon: material/table
---

# Materials

Follow this guide to determine if your filament will work with the 3MS.

## Materials Table

This table contains which filaments work in single mode and/or multimaterial mode with the 3MS.

| Filament | Single Mode | Multimaterial Mode | Notes |
| - | - | - | - |
| [PLA](#pla) | Yes | Yes | |
| [PLA+](#pla) | Yes | Yes | |
| [Silk PLA](#silkmatte-pla) | Yes | No | |
| [Matte PLA](#silkmatte-pla) | Yes | No | |
| [PETG](#petg) | Yes | Yes | |
| [TPU](#tpu) | Untested | No | |

## PLA(+)

PLA/PLA+/PLA Pro, etc. filaments are very easy to print in multimaterial with the 3MS. They also support the [No Tip Shaping](notip.md) feature.

## Silk/Matte PLA

Silk/Matte PLA filaments are slightly more difficult to print with or without the 3MS. They generally require tip shaping to work with the 3MS in multimaterial mode.

## PETG

PETG filaments are easy to print in multimaterial with the 3MS. They will likely require tip shaping. Suggested settings options are provided below. Ideal settings for your setup will likely include a combination of the options.

??? "Tip Shaping"
    === "Option 1"
        | Setting Name | Setting Value |
        | - | - |
        | Nozzle Temperature | 250ºC |
        | Loading speed at the start | 19mm/s |
        | Loading speed | 14mm/s |
        | Unloading speed at start | 200mm/s |
        | Unloading speed | 90mm/s |
        | Delay after unloading | 4s |
        | # Cooling moves | 3 |
        | Speed of first cooling move | 1mm/s |
        | Speed of last cooling move | 20mm/s |
        | Ramming settings | ![](petg1.0.png){data-gallery="petg"} |
        Source: [Prusa Forums](https://forum.prusa3d.com/forum/postid/382759/)

    === "Option 2"
        | Setting Name | Setting Value |
        | - | - |
        | Nozzle Temperature | 250ºC |
        | Loading speed at the start | 15mm/s |
        | Loading speed | 14mm/s |
        | Unloading speed at start | 120mm/s |
        | Unloading speed | 20mm/s |
        | Delay after unloading | 0s |
        | # Cooling moves | 1 |
        | Speed of first cooling move | 1mm/s |
        | Speed of last cooling move | 15mm/s |
        | Ramming settings | ![](petg2.0.png){data-gallery="petg"} |
        Source: [Prusa Forums](https://forum.prusa3d.com/forum/postid/124370/)

## TPU

TPU filaments are very difficult to print with or without the 3MS. If your printer can reliably print TPU, you can likely use it with the 3MS in single mode. To use it in multimaterial mode and/or improve reliability, see the experimental [Dual Drive 3MS Extruders for TPU](dualdrivetpu.md) feature.