---
icon: octicons/cpu-24
comments: true
---

# Controller Support

Follow this guide to add support for a new 3MS controller.

## Requirements

To add support for a new 3MS controller, the following requirements must be met:

- Klipper natively supports the controller
- There is an [official Klipper configuration](https://github.com/Klipper3d/klipper/tree/master/config) for the controller

## Request a new Controller

If you don't want to create the new controller configuration yourself, you can submit a [Controller Request](https://github.com/3DCoded/3MS/issues/new?assignees=3dcoded&labels=controller&projects=&template=controller.yml&title=%5BMCU%5D%3A+).

## Supporting a new Controller

If the controller meets the aforementioned requirements, you can proceed with adding support for it.

The following example will be for a SKR Mini E3 V2.0 controller.

### Removing Extra Config Sections

1. Remove all sections from the configuration **except** the following:
    
    - Stepper configurations (e.g. `[stepper_x]`)
    - TMC driver configurations (e.g. `[tmc2209 stepper_x]`)
    - Extruder configurations (e.g. `[extruder]`)
    - `[static_digital_output]`
    - `[board_pins]`

2. If the configuration is a main MCU configuration, remove the `[mcu]` section.
3. Add the following line to all `[static_digital_output]` and `[board_pins]` sections:

    ```cfg
    mcu: 3ms
    ```

4. If the configuration is **NOT** a main MCU, replace `[mcu]` with `[mcu 3ms]`. 

??? "Full Configuration Before/After"
    === "Before"
        ```cfg
        # This file contains common pin mappings for the BIGTREETECH SKR mini
        # E3 v2.0. To use this config, the firmware should be compiled for the
        # STM32F103 with a "28KiB bootloader" and USB communication. Also,
        # select "Enable extra low-level configuration options" and configure
        # "GPIO pins to set at micro-controller startup" to "!PA14".

        # The "make flash" command does not work on the SKR mini E3. Instead,
        # after running "make", copy the generated "out/klipper.bin" file to a
        # file named "firmware.bin" on an SD card and then restart the SKR
        # mini E3 with that SD card.

        # See docs/Config_Reference.md for a description of parameters.

        [stepper_x]
        step_pin: PB13
        dir_pin: !PB12
        enable_pin: !PB14
        microsteps: 16
        rotation_distance: 40
        endstop_pin: ^PC0
        position_endstop: 0
        position_max: 235
        homing_speed: 50

        [tmc2209 stepper_x]
        uart_pin: PC11
        tx_pin: PC10
        uart_address: 0
        run_current: 0.580
        stealthchop_threshold: 999999

        [stepper_y]
        step_pin: PB10
        dir_pin: !PB2
        enable_pin: !PB11
        microsteps: 16
        rotation_distance: 40
        endstop_pin: ^PC1
        position_endstop: 0
        position_max: 235
        homing_speed: 50

        [tmc2209 stepper_y]
        uart_pin: PC11
        tx_pin: PC10
        uart_address: 2
        run_current: 0.580
        stealthchop_threshold: 999999

        [stepper_z]
        step_pin: PB0
        dir_pin: PC5
        enable_pin: !PB1
        microsteps: 16
        rotation_distance: 8
        endstop_pin: ^PC2
        position_endstop: 0.0
        position_max: 250

        [tmc2209 stepper_z]
        uart_pin: PC11
        tx_pin: PC10
        uart_address: 1
        run_current: 0.580
        stealthchop_threshold: 999999

        [extruder]
        step_pin: PB3
        dir_pin: !PB4
        enable_pin: !PD2
        microsteps: 16
        rotation_distance: 33.500
        nozzle_diameter: 0.400
        filament_diameter: 1.750
        heater_pin: PC8
        sensor_type: EPCOS 100K B57560G104F
        sensor_pin: PA0
        control: pid
        pid_Kp: 21.527
        pid_Ki: 1.063
        pid_Kd: 108.982
        min_temp: 0
        max_temp: 250

        [tmc2209 extruder]
        uart_pin: PC11
        tx_pin: PC10
        uart_address: 3
        run_current: 0.650
        stealthchop_threshold: 999999

        [heater_bed]
        heater_pin: PC9
        sensor_type: ATC Semitec 104GT-2
        sensor_pin: PC3
        control: pid
        pid_Kp: 54.027
        pid_Ki: 0.770
        pid_Kd: 948.182
        min_temp: 0
        max_temp: 130

        [heater_fan heatbreak_cooling_fan]
        pin: PC7

        [fan]
        pin: PC6

        [mcu]
        serial: /dev/serial/by-id/usb-Klipper_Klipper_firmware_12345-if00

        [printer]
        kinematics: cartesian
        max_velocity: 300
        max_accel: 3000
        max_z_velocity: 5
        max_z_accel: 100

        [static_digital_output usb_pullup_enable]
        pins: !PA14

        [board_pins]
        aliases:
            # EXP1 header
            EXP1_1=PB5,  EXP1_3=PA9,   EXP1_5=PA10, EXP1_7=PB8,  EXP1_9=<GND>,
            EXP1_2=PA15, EXP1_4=<RST>, EXP1_6=PB9,  EXP1_8=PB15, EXP1_10=<5V>

        # See the sample-lcd.cfg file for definitions of common LCD displays.
        ```
    === "After"
        ```cfg
        # This file contains common pin mappings for the BIGTREETECH SKR mini
        # E3 v2.0. To use this config, the firmware should be compiled for the
        # STM32F103 with a "28KiB bootloader" and USB communication. Also,
        # select "Enable extra low-level configuration options" and configure
        # "GPIO pins to set at micro-controller startup" to "!PA14".

        # The "make flash" command does not work on the SKR mini E3. Instead,
        # after running "make", copy the generated "out/klipper.bin" file to a
        # file named "firmware.bin" on an SD card and then restart the SKR
        # mini E3 with that SD card.

        # See docs/Config_Reference.md for a description of parameters.

        [stepper_x]
        step_pin: PB13
        dir_pin: !PB12
        enable_pin: !PB14
        microsteps: 16
        rotation_distance: 40
        endstop_pin: ^PC0
        position_endstop: 0
        position_max: 235
        homing_speed: 50

        [tmc2209 stepper_x]
        uart_pin: PC11
        tx_pin: PC10
        uart_address: 0
        run_current: 0.580
        stealthchop_threshold: 999999

        [stepper_y]
        step_pin: PB10
        dir_pin: !PB2
        enable_pin: !PB11
        microsteps: 16
        rotation_distance: 40
        endstop_pin: ^PC1
        position_endstop: 0
        position_max: 235
        homing_speed: 50

        [tmc2209 stepper_y]
        uart_pin: PC11
        tx_pin: PC10
        uart_address: 2
        run_current: 0.580
        stealthchop_threshold: 999999

        [stepper_z]
        step_pin: PB0
        dir_pin: PC5
        enable_pin: !PB1
        microsteps: 16
        rotation_distance: 8
        endstop_pin: ^PC2
        position_endstop: 0.0
        position_max: 250

        [tmc2209 stepper_z]
        uart_pin: PC11
        tx_pin: PC10
        uart_address: 1
        run_current: 0.580
        stealthchop_threshold: 999999

        [extruder]
        step_pin: PB3
        dir_pin: !PB4
        enable_pin: !PD2
        microsteps: 16
        rotation_distance: 33.500
        nozzle_diameter: 0.400
        filament_diameter: 1.750
        heater_pin: PC8
        sensor_type: EPCOS 100K B57560G104F
        sensor_pin: PA0
        control: pid
        pid_Kp: 21.527
        pid_Ki: 1.063
        pid_Kd: 108.982
        min_temp: 0
        max_temp: 250

        [tmc2209 extruder]
        uart_pin: PC11
        tx_pin: PC10
        uart_address: 3
        run_current: 0.650
        stealthchop_threshold: 999999

        [mcu]
        serial: /dev/serial/by-id/usb-Klipper_Klipper_firmware_12345-if00

        [static_digital_output usb_pullup_enable]
        pins: !PA14

        [board_pins]
        mcu: 3ms
        aliases:
            # EXP1 header
            EXP1_1=PB5,  EXP1_3=PA9,   EXP1_5=PA10, EXP1_7=PB8,  EXP1_9=<GND>,
            EXP1_2=PA15, EXP1_4=<RST>, EXP1_6=PB9,  EXP1_8=PB15, EXP1_10=<5V>
        ```

### Stepper Configuration

!!! note
    In the following examples, the Z stepper is not included. When creating a 3MS configuration, you can (and probably will) use the Z steppers.

1. Change any stepper sections to an `extruder_stepper` named `3ms0`, `3ms1`, `3ms2`, etc. Example:

    === "Before"
        ```cfg
        [stepper_x]
        ...

        [stepper_y]
        ...
        ```
    === "After"
        ```cfg
        [extruder_stepper 3ms0]
        ...

        [extruder_stepper 3ms1]
        ...
        ```

2. Change any extruder sections to an `extruder_stepper`. Example:

    === "Before"
        ```cfg
        [extruder]
        ...

        [extruder1]
        ...
        ```
    === "After"
        ```cfg
        [extruder_stepper 3ms2]
        ...

        [extruder_stepper 3ms3]
        ...
        ```

3. Remove the extruder-specific configurations from the former extruders. Example:

    === "Before"
        ```cfg
        [extruder_stepper 3ms2]
        step_pin: PB3
        dir_pin: !PB4
        enable_pin: !PD1
        microsteps: 16
        rotation_distance: 33.500
        nozzle_diameter: 0.400
        filament_diameter: 1.750
        heater_pin: PC8
        sensor_type: EPCOS 100K B57560G104F
        sensor_pin: PA0
        control: pid
        pid_Kp: 21.527
        pid_Ki: 1.063
        pid_Kd: 108.982
        min_temp: 0
        max_temp: 250
        ```
    === "After"
        ```cfg
        [extruder_stepper 3ms2]
        step_pin: PB3
        dir_pin: !PB4
        enable_pin: !PD1
        microsteps: 16
        rotation_distance: 33.500
        ```

4. Update any TMC configuration sections to reflect the new `extruder_steppers`. Example:

    === "Before"
        ```cfg
        [tmc2209 stepper_x]
        ...

        [tmc2209 stepper_y]
        ...

        [tmc2209 extruder]
        ...

        [tmc2209 extruder1]
        ...
        ```

    === "After"
        ```cfg
        [tmc2209 extruder_stepper 3ms0]
        ...

        [tmc2209 extruder_stepper 3ms1]
        ...

        [tmc2209 extruder_stepper 3ms2]
        ...

        [tmc2209 extruder_stepper 3ms3]
        ...
        ```
??? "Full Configuration Before/After"
    === "Before"
        ```cfg
        # This file contains common pin mappings for the BIGTREETECH SKR mini
        # E3 v2.0. To use this config, the firmware should be compiled for the
        # STM32F103 with a "28KiB bootloader" and USB communication. Also,
        # select "Enable extra low-level configuration options" and configure
        # "GPIO pins to set at micro-controller startup" to "!PA14".

        # The "make flash" command does not work on the SKR mini E3. Instead,
        # after running "make", copy the generated "out/klipper.bin" file to a
        # file named "firmware.bin" on an SD card and then restart the SKR
        # mini E3 with that SD card.

        # See docs/Config_Reference.md for a description of parameters.

        [stepper_x]
        step_pin: PB13
        dir_pin: !PB12
        enable_pin: !PB14
        microsteps: 16
        rotation_distance: 40
        endstop_pin: ^PC0
        position_endstop: 0
        position_max: 235
        homing_speed: 50

        [tmc2209 stepper_x]
        uart_pin: PC11
        tx_pin: PC10
        uart_address: 0
        run_current: 0.580
        stealthchop_threshold: 999999

        [stepper_y]
        step_pin: PB10
        dir_pin: !PB2
        enable_pin: !PB11
        microsteps: 16
        rotation_distance: 40
        endstop_pin: ^PC1
        position_endstop: 0
        position_max: 235
        homing_speed: 50

        [tmc2209 stepper_y]
        uart_pin: PC11
        tx_pin: PC10
        uart_address: 2
        run_current: 0.580
        stealthchop_threshold: 999999

        [stepper_z]
        step_pin: PB0
        dir_pin: PC5
        enable_pin: !PB1
        microsteps: 16
        rotation_distance: 8
        endstop_pin: ^PC2
        position_endstop: 0.0
        position_max: 250

        [tmc2209 stepper_z]
        uart_pin: PC11
        tx_pin: PC10
        uart_address: 1
        run_current: 0.580
        stealthchop_threshold: 999999

        [extruder]
        step_pin: PB3
        dir_pin: !PB4
        enable_pin: !PD2
        microsteps: 16
        rotation_distance: 33.500
        nozzle_diameter: 0.400
        filament_diameter: 1.750
        heater_pin: PC8
        sensor_type: EPCOS 100K B57560G104F
        sensor_pin: PA0
        control: pid
        pid_Kp: 21.527
        pid_Ki: 1.063
        pid_Kd: 108.982
        min_temp: 0
        max_temp: 250

        [tmc2209 extruder]
        uart_pin: PC11
        tx_pin: PC10
        uart_address: 3
        run_current: 0.650
        stealthchop_threshold: 999999

        [mcu]
        serial: /dev/serial/by-id/usb-Klipper_Klipper_firmware_12345-if00

        [static_digital_output usb_pullup_enable]
        pins: !PA14

        [board_pins]
        mcu: 3ms
        aliases:
            # EXP1 header
            EXP1_1=PB5,  EXP1_3=PA9,   EXP1_5=PA10, EXP1_7=PB8,  EXP1_9=<GND>,
            EXP1_2=PA15, EXP1_4=<RST>, EXP1_6=PB9,  EXP1_8=PB15, EXP1_10=<5V>
        ```
    === "After"
        ```cfg
        # This file contains common pin mappings for the BIGTREETECH SKR mini
        # E3 v2.0. To use this config, the firmware should be compiled for the
        # STM32F103 with a "28KiB bootloader" and USB communication. Also,
        # select "Enable extra low-level configuration options" and configure
        # "GPIO pins to set at micro-controller startup" to "!PA14".

        # The "make flash" command does not work on the SKR mini E3. Instead,
        # after running "make", copy the generated "out/klipper.bin" file to a
        # file named "firmware.bin" on an SD card and then restart the SKR
        # mini E3 with that SD card.

        # See docs/Config_Reference.md for a description of parameters.

        [extruder_stepper 3ms0]
        step_pin: PB13
        dir_pin: !PB12
        enable_pin: !PB14
        microsteps: 16
        rotation_distance: 40
        endstop_pin: ^PC0
        position_endstop: 0
        position_max: 235
        homing_speed: 50

        [tmc2209 extruder_stepper 3ms0]
        uart_pin: PC11
        tx_pin: PC10
        uart_address: 0
        run_current: 0.580
        stealthchop_threshold: 999999

        [extruder_stepper 3ms1]
        step_pin: PB10
        dir_pin: !PB2
        enable_pin: !PB11
        microsteps: 16
        rotation_distance: 40
        endstop_pin: ^PC1
        position_endstop: 0
        position_max: 235
        homing_speed: 50

        [tmc2209 extruder_stepper 3ms1]
        uart_pin: PC11
        tx_pin: PC10
        uart_address: 2
        run_current: 0.580
        stealthchop_threshold: 999999

        [extruder_stepper 3ms2]
        step_pin: PB0
        dir_pin: PC5
        enable_pin: !PB1
        microsteps: 16
        rotation_distance: 8
        endstop_pin: ^PC2
        position_endstop: 0.0
        position_max: 250

        [tmc2209 extruder_stepper 3ms2]
        uart_pin: PC11
        tx_pin: PC10
        uart_address: 1
        run_current: 0.580
        stealthchop_threshold: 999999

        [extruder_stepper 3ms3]
        step_pin: PB3
        dir_pin: !PB4
        enable_pin: !PD2
        microsteps: 16
        rotation_distance: 33.500

        [tmc2209 extruder_stepper 3ms3]
        uart_pin: PC11
        tx_pin: PC10
        uart_address: 3
        run_current: 0.650
        stealthchop_threshold: 999999

        [mcu]
        serial: /dev/serial/by-id/usb-Klipper_Klipper_firmware_12345-if00

        [static_digital_output usb_pullup_enable]
        pins: !PA14

        [board_pins]
        mcu: 3ms
        aliases:
            # EXP1 header
            EXP1_1=PB5,  EXP1_3=PA9,   EXP1_5=PA10, EXP1_7=PB8,  EXP1_9=<GND>,
            EXP1_2=PA15, EXP1_4=<RST>, EXP1_6=PB9,  EXP1_8=PB15, EXP1_10=<5V>
        ```

### Final Important Details

Change the `[mcu]` section (if present) to `[mcu 3ms]`. Add a `3ms: ` prefix to all pin names (if not a main MCU config). Any `!` or `^` should go **before** the `3ms: ` prefix. Remove the `filament_diameter` and `nozzle_diameter` options from the former `[extruder]` section. Remove all homing/endstop-related sections from the stepper configurations. Append a `extruder: extruder` option to all `[extruder_stepper]` sections.

1. Prefix all pin names **IN ALL SECTIONS** (not just motors) with `3ms: `. Example:

    === "Before"
        ```cfg
        [extruder_stepper 3ms0]
        step_pin: PB13
        dir_pin: !PB12
        enable_pin: !PB14
        microsteps: 16
        rotation_distance: 40
        ```
    === "After"
        ```cfg
        [extruder_stepper 3ms0]
        step_pin: 3ms: PB13
        dir_pin: !3ms: PB12
        enable_pin: !3ms: PB14
        microsteps: 16
        rotation_distance: 40
        ```
??? "Full Configuration Before/After"
    === "Before"
        ```cfg
        # This file contains common pin mappings for the BIGTREETECH SKR mini
        # E3 v2.0. To use this config, the firmware should be compiled for the
        # STM32F103 with a "28KiB bootloader" and USB communication. Also,
        # select "Enable extra low-level configuration options" and configure
        # "GPIO pins to set at micro-controller startup" to "!PA14".

        # The "make flash" command does not work on the SKR mini E3. Instead,
        # after running "make", copy the generated "out/klipper.bin" file to a
        # file named "firmware.bin" on an SD card and then restart the SKR
        # mini E3 with that SD card.

        # See docs/Config_Reference.md for a description of parameters.

        [extruder_stepper 3ms0]
        step_pin: PB13
        dir_pin: !PB12
        enable_pin: !PB14
        microsteps: 16
        rotation_distance: 40
        endstop_pin: ^PC0
        position_endstop: 0
        position_max: 235
        homing_speed: 50

        [tmc2209 extruder_stepper 3ms0]
        uart_pin: PC11
        tx_pin: PC10
        uart_address: 0
        run_current: 0.580
        stealthchop_threshold: 999999

        [extruder_stepper 3ms1]
        step_pin: PB10
        dir_pin: !PB2
        enable_pin: !PB11
        microsteps: 16
        rotation_distance: 40
        endstop_pin: ^PC1
        position_endstop: 0
        position_max: 235
        homing_speed: 50

        [tmc2209 extruder_stepper 3ms1]
        uart_pin: PC11
        tx_pin: PC10
        uart_address: 2
        run_current: 0.580
        stealthchop_threshold: 999999

        [extruder_stepper 3ms2]
        step_pin: PB0
        dir_pin: PC5
        enable_pin: !PB1
        microsteps: 16
        rotation_distance: 8
        endstop_pin: ^PC2
        position_endstop: 0.0
        position_max: 250

        [tmc2209 extruder_stepper 3ms2]
        uart_pin: PC11
        tx_pin: PC10
        uart_address: 1
        run_current: 0.580
        stealthchop_threshold: 999999

        [extruder_stepper 3ms3]
        step_pin: PB3
        dir_pin: !PB4
        enable_pin: !PD2
        microsteps: 16
        rotation_distance: 33.500
        nozzle_diameter: 0.400
        filament_diameter: 1.750

        [tmc2209 extruder_stepper 3ms3]
        uart_pin: PC11
        tx_pin: PC10
        uart_address: 3
        run_current: 0.650
        stealthchop_threshold: 999999

        [mcu]
        serial: /dev/serial/by-id/usb-Klipper_Klipper_firmware_12345-if00

        [static_digital_output usb_pullup_enable]
        pins: !PA14

        [board_pins]
        mcu: 3ms
        aliases:
            # EXP1 header
            EXP1_1=PB5,  EXP1_3=PA9,   EXP1_5=PA10, EXP1_7=PB8,  EXP1_9=<GND>,
            EXP1_2=PA15, EXP1_4=<RST>, EXP1_6=PB9,  EXP1_8=PB15, EXP1_10=<5V>
        ```
    === "After"
        ```cfg
        # This file contains common pin mappings for the BIGTREETECH SKR mini
        # E3 v2.0. To use this config, the firmware should be compiled for the
        # STM32F103 with a "28KiB bootloader" and USB communication. Also,
        # select "Enable extra low-level configuration options" and configure
        # "GPIO pins to set at micro-controller startup" to "!PA14".

        # The "make flash" command does not work on the SKR mini E3. Instead,
        # after running "make", copy the generated "out/klipper.bin" file to a
        # file named "firmware.bin" on an SD card and then restart the SKR
        # mini E3 with that SD card.

        # See docs/Config_Reference.md for a description of parameters.

        [extruder_stepper 3ms0]
        extruder: extruder
        step_pin: 3ms: PB13
        dir_pin: !3ms: PB12
        enable_pin: !3ms: PB14
        microsteps: 16
        rotation_distance: 40

        [tmc2209 extruder_stepper 3ms0]
        uart_pin: 3ms: PC11
        tx_pin: 3ms: PC10
        uart_address: 0
        run_current: 0.580
        stealthchop_threshold: 999999

        [extruder_stepper 3ms1]
        extruder: extruder
        step_pin: 3ms: PB10
        dir_pin: !3ms: PB2
        enable_pin: !3ms: PB11
        microsteps: 16
        rotation_distance: 40

        [tmc2209 extruder_stepper 3ms1]
        uart_pin: 3ms: PC11
        tx_pin: 3ms: PC10
        uart_address: 2
        run_current: 0.580
        stealthchop_threshold: 999999

        [extruder_stepper 3ms2]
        extruder: extruder
        step_pin: 3ms: PB0
        dir_pin: 3ms: PC5
        enable_pin: !3ms: PB1
        microsteps: 16
        rotation_distance: 8

        [tmc2209 extruder_stepper 3ms2]
        uart_pin: 3ms: PC11
        tx_pin: 3ms: PC10
        uart_address: 1
        run_current: 0.580
        stealthchop_threshold: 999999

        [extruder_stepper 3ms3]
        extruder: extruder
        step_pin: 3ms: PB3
        dir_pin: !3ms: PB4
        enable_pin: !3ms: PD2
        microsteps: 16
        rotation_distance: 33.500

        [tmc2209 extruder_stepper 3ms3]
        uart_pin: 3ms: PC11
        tx_pin: 3ms: PC10
        uart_address: 3
        run_current: 0.650
        stealthchop_threshold: 999999

        [mcu]
        serial: /dev/serial/by-id/usb-Klipper_Klipper_firmware_12345-if00

        [static_digital_output usb_pullup_enable]
        pins: !PA14

        [board_pins]
        mcu: 3ms
        aliases:
            # EXP1 header
            EXP1_1=PB5,  EXP1_3=PA9,   EXP1_5=PA10, EXP1_7=PB8,  EXP1_9=<GND>,
            EXP1_2=PA15, EXP1_4=<RST>, EXP1_6=PB9,  EXP1_8=PB15, EXP1_10=<5V>
        ```