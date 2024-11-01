# Happy Hare Firmware Setup

Follow this guide to install Happy Hare firmware and set it up with your 3MS. 

!!! info
    This guide will go through the bare minimum setup required to set up a functional 3MS. It is **highly** recommended that you read the official Happy Hare documentation available [here](https://github.com/moggieuk/Happy-Hare/wiki).

## Installation

First, follow the Happy Hare installation instructions available [here](https://github.com/moggieuk/Happy-Hare/wiki/Installation). In the installation wizard, select **`3MS`** as the MMU type.

If you are using one of the Happy Hare supported controllers, Happy Hare will automatically set up the hardware configuration for you.

## Other Controllers

If you are using another controller, you can use one of the 3MS controller configurations available [here](https://github.com/3DCoded/3MS/tree/main/happy-hare/configurations). 

### Naming Scheme

The naming scheme of the configurations is as follows:

1. The first words are the MCU name. If it is `MMU`, this is an external mainboard. If it is `MAIN`, it is using your printer's existing mainboard.
2. The numbers are the tool numbers. If this is your first MMU controller board, look for one that starts with `0`. If this is an additional MMU controller board (you are adding to an existing 3MS), the first number should be one more than the last number of your previous controller. This allows for stacking 3MS controllers.
3. The last part of the name is the name of the mainboard itself.

### Examples

```
MMU_0_3_btt_skr_pico
```

This is an external SKR Pico controlling four tools numbered `0` to `3`.

```
MMU_0_6_gtm32_103_v1
```

This is an external GTM32 103 V1 controlling seven tools numbered `0` to `6`.

```
MAIN_0_3_btt_octopus
```

This is an internal BTT Octopus controlling four tools numbered `0` to `3`.

### Configuring Other Controllers

To configure a 3MS controller that Happy Hare doesn't natively support, open the corresponding folder for the controller's name. In this example, `MMU_0_3_btt_skr_pico` will be used.

In the `MMU_0_3_btt_skr_pico` folder, there are two files:

- `mmu.cfg`
- `mmu_hardware.cfg`

Copy those two files into your `mmu/base` folder, replacing the two existing files. 

Your 3MS is now configured with Happy Hare.

---

!!! info
    To finish setting up the 3MS and your printer, you will can follow Happy Hare's documentation available [here](https://github.com/moggieuk/Happy-Hare/wiki).