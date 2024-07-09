# Configuration

Follow this guide to create your 3MS configuration.

## Premade Configurations

The easiest way to get a configuration for your 3MS is to download a premade one. Premade configurations are available for the following controller(s):

!!! info
    At this time, the only fully supported controller is the SKR Mini E3 V2.0


- [BTT Skr Mini E3 V2.0](https://github.com/3DCoded/3MS/blob/main/controllers/btt_skr_mini_e3_v2/steppers.cfg)

If your controller is in the list above, use that configuration and skip the rest of this guide. If you are using a different controller, read on.

!!! warning
    The rest of this page is under development and may contain INCORRECT INFORMATION. Do not follow the rest of this guide. If you want support for a different controller, please open an issue on Github.

## Controller Configuration

First, find a configuration that works with your control board. Klipper official configurations: [Github](https://github.com/Klipper3d/klipper/tree/master/config)

## 3MS Configuration

After you have downloaded your controller configuration, create a new folder in the same folder as your `printer.cfg`. Name it `3ms`. Inside it, copy and paste your controller configuration. In this example, an **SKR Pico** configuration will be used.

### Only Motors

First, remove all parts of the configuration not about motors/extruders. Example:

??? "Before/After"
    === "Before"
        ``` cfg title="3ms/skr-pico.cfg"
        # This file contains common pin mappings for the BIGTREETECH SKR Pico V1.0
        # To use this config, the firmware should be compiled for the RP2040 with
        # USB communication.

        # The "make flash" command does not work on the SKR Pico V1.0. Instead,
        # after running "make", copy the generated "out/klipper.uf2" file
        # to the mass storage device in RP2040 boot mode

        # See docs/Config_Reference.md for a description of parameters.
        ```

    === "After"
        ``` cfg title="3ms/generic-bigtreetech-skr-pico-v1.0.cfg"
        # This file contains common pin mappings for the BIGTREETECH SKR Pico V1.0
        # To use this config, the firmware should be compiled for the RP2040 with
        # USB communication.

        # The "make flash" command does not work on the SKR Pico V1.0. Instead,
        # after running "make", copy the generated "out/klipper.uf2" file
        # to the mass storage device in RP2040 boot mode

        # See docs/Config_Reference.md for a description of parameters.
        ```