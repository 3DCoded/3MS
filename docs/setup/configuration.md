# Configuration

Follow this guide to create your 3MS configuration.

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

        [stepper_x]
        step_pin: gpio11
        dir_pin: !gpio10
        enable_pin: !gpio12
        microsteps: 16
        rotation_distance: 40
        endstop_pin: ^gpio4
        position_endstop: 0
        position_max: 235
        homing_speed: 50

        [tmc2209 stepper_x]
        uart_pin: gpio9
        tx_pin: gpio8
        uart_address: 0
        run_current: 0.580
        stealthchop_threshold: 999999

        [stepper_y]
        step_pin: gpio6
        dir_pin: !gpio5
        enable_pin: !gpio7
        microsteps: 16
        rotation_distance: 40
        endstop_pin: ^gpio3
        position_endstop: 0
        position_max: 235
        homing_speed: 50

        [tmc2209 stepper_y]
        uart_pin: gpio9
        tx_pin: gpio8
        uart_address: 2
        run_current: 0.580
        stealthchop_threshold: 999999

        [stepper_z]
        step_pin: gpio19
        dir_pin: gpio28
        enable_pin: !gpio2
        microsteps: 16
        rotation_distance: 8
        endstop_pin: ^gpio25
        position_endstop: 0.0
        position_max: 250

        [tmc2209 stepper_z]
        uart_pin: gpio9
        tx_pin: gpio8
        uart_address: 1
        run_current: 0.580
        stealthchop_threshold: 999999

        [extruder]
        step_pin: gpio14
        dir_pin: !gpio13
        enable_pin: !gpio15
        microsteps: 16
        rotation_distance: 33.500
        nozzle_diameter: 0.400
        filament_diameter: 1.750
        heater_pin: gpio23
        sensor_type: EPCOS 100K B57560G104F
        sensor_pin: gpio27
        control: pid
        pid_Kp: 21.527
        pid_Ki: 1.063
        pid_Kd: 108.982
        min_temp: 0
        max_temp: 250

        [tmc2209 extruder]
        uart_pin: gpio9
        tx_pin: gpio8
        uart_address: 3
        run_current: 0.650
        stealthchop_threshold: 999999

        [heater_bed]
        heater_pin: gpio21
        sensor_type: ATC Semitec 104GT-2
        sensor_pin: gpio26
        control: pid
        pid_Kp: 54.027
        pid_Ki: 0.770
        pid_Kd: 948.182
        min_temp: 0
        max_temp: 130

        [fan]
        pin: gpio17

        [heater_fan heatbreak_cooling_fan]
        pin: gpio18

        [heater_fan controller_fan]
        pin: gpio20

        [temperature_sensor pico]
        sensor_type: temperature_mcu

        [mcu]
        serial: /dev/serial/by-id/usb-Klipper_Klipper_firmware_12345-if00

        [printer]
        kinematics: cartesian
        max_velocity: 300
        max_accel: 3000
        max_z_velocity: 5
        max_z_accel: 100

        [neopixel board_neopixel]
        pin: gpio24
        chain_count: 1
        color_order: GRB
        initial_RED: 0.3
        initial_GREEN: 0.3
        initial_BLUE: 0.3

        #[bltouch]
        #sensor_pin: gpio22
        #control_pin: gpio29

        #[filament_switch_sensor runout_sensor]
        #switch_pin: ^gpio16
        ```

    === "After"
        ``` cfg title="3ms/skr-pico.cfg"
        # This file contains common pin mappings for the BIGTREETECH SKR Pico V1.0
        # To use this config, the firmware should be compiled for the RP2040 with
        # USB communication.

        # The "make flash" command does not work on the SKR Pico V1.0. Instead,
        # after running "make", copy the generated "out/klipper.uf2" file
        # to the mass storage device in RP2040 boot mode

        # See docs/Config_Reference.md for a description of parameters.

        [stepper_x]
        step_pin: gpio11
        dir_pin: !gpio10
        enable_pin: !gpio12
        microsteps: 16
        rotation_distance: 40
        endstop_pin: ^gpio4
        position_endstop: 0
        position_max: 235
        homing_speed: 50

        [tmc2209 stepper_x]
        uart_pin: gpio9
        tx_pin: gpio8
        uart_address: 0
        run_current: 0.580
        stealthchop_threshold: 999999

        [stepper_y]
        step_pin: gpio6
        dir_pin: !gpio5
        enable_pin: !gpio7
        microsteps: 16
        rotation_distance: 40
        endstop_pin: ^gpio3
        position_endstop: 0
        position_max: 235
        homing_speed: 50

        [tmc2209 stepper_y]
        uart_pin: gpio9
        tx_pin: gpio8
        uart_address: 2
        run_current: 0.580
        stealthchop_threshold: 999999

        [stepper_z]
        step_pin: gpio19
        dir_pin: gpio28
        enable_pin: !gpio2
        microsteps: 16
        rotation_distance: 8
        endstop_pin: ^gpio25
        position_endstop: 0.0
        position_max: 250

        [tmc2209 stepper_z]
        uart_pin: gpio9
        tx_pin: gpio8
        uart_address: 1
        run_current: 0.580
        stealthchop_threshold: 999999

        [extruder]
        step_pin: gpio14
        dir_pin: !gpio13
        enable_pin: !gpio15
        microsteps: 16
        rotation_distance: 33.500
        nozzle_diameter: 0.400
        filament_diameter: 1.750
        heater_pin: gpio23
        sensor_type: EPCOS 100K B57560G104F
        sensor_pin: gpio27
        control: pid
        pid_Kp: 21.527
        pid_Ki: 1.063
        pid_Kd: 108.982
        min_temp: 0
        max_temp: 250

        [tmc2209 extruder]
        uart_pin: gpio9
        tx_pin: gpio8
        uart_address: 3
        run_current: 0.650
        stealthchop_threshold: 999999
        ```

### Manual Steppers

Next, replace all the `stepper_`,`extruder`, and `tmc...` with `[manual_stepper 3ms...]` sections, as shown below:

??? "Before/After"
    === "Before"
        ``` cfg title="3ms/generic-bigtreetech-skr-pico-v1.0.cfg"
        # This file contains common pin mappings for the BIGTREETECH SKR Pico V1.0
        # To use this config, the firmware should be compiled for the RP2040 with
        # USB communication.

        # The "make flash" command does not work on the SKR Pico V1.0. Instead,
        # after running "make", copy the generated "out/klipper.uf2" file
        # to the mass storage device in RP2040 boot mode

        # See docs/Config_Reference.md for a description of parameters.

        [stepper_x]
        step_pin: gpio11
        dir_pin: !gpio10
        enable_pin: !gpio12
        microsteps: 16
        rotation_distance: 40
        endstop_pin: ^gpio4
        position_endstop: 0
        position_max: 235
        homing_speed: 50

        [tmc2209 stepper_x]
        uart_pin: gpio9
        tx_pin: gpio8
        uart_address: 0
        run_current: 0.580
        stealthchop_threshold: 999999

        [stepper_y]
        step_pin: gpio6
        dir_pin: !gpio5
        enable_pin: !gpio7
        microsteps: 16
        rotation_distance: 40
        endstop_pin: ^gpio3
        position_endstop: 0
        position_max: 235
        homing_speed: 50

        [tmc2209 stepper_y]
        uart_pin: gpio9
        tx_pin: gpio8
        uart_address: 2
        run_current: 0.580
        stealthchop_threshold: 999999

        [stepper_z]
        step_pin: gpio19
        dir_pin: gpio28
        enable_pin: !gpio2
        microsteps: 16
        rotation_distance: 8
        endstop_pin: ^gpio25
        position_endstop: 0.0
        position_max: 250

        [tmc2209 stepper_z]
        uart_pin: gpio9
        tx_pin: gpio8
        uart_address: 1
        run_current: 0.580
        stealthchop_threshold: 999999

        [extruder]
        step_pin: gpio14
        dir_pin: !gpio13
        enable_pin: !gpio15
        microsteps: 16
        rotation_distance: 33.500
        nozzle_diameter: 0.400
        filament_diameter: 1.750
        heater_pin: gpio23
        sensor_type: EPCOS 100K B57560G104F
        sensor_pin: gpio27
        control: pid
        pid_Kp: 21.527
        pid_Ki: 1.063
        pid_Kd: 108.982
        min_temp: 0
        max_temp: 250

        [tmc2209 extruder]
        uart_pin: gpio9
        tx_pin: gpio8
        uart_address: 3
        run_current: 0.650
        stealthchop_threshold: 999999
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

        [manual_stepper 3ms0]
        step_pin: gpio11
        dir_pin: !gpio10
        enable_pin: !gpio12
        microsteps: 16
        rotation_distance: 40

        [tmc2209 manual_stepper 3ms0]
        uart_pin: gpio9
        tx_pin: gpio8
        uart_address: 0
        run_current: 0.580
        stealthchop_threshold: 999999

        [manual_stepper 3ms1]
        step_pin: gpio6
        dir_pin: !gpio5
        enable_pin: !gpio7
        microsteps: 16
        rotation_distance: 40

        [tmc2209 manual_stepper 3ms1]
        uart_pin: gpio9
        tx_pin: gpio8
        uart_address: 2
        run_current: 0.580
        stealthchop_threshold: 999999

        [manual_stepper 3ms2]
        step_pin: gpio19
        dir_pin: gpio28
        enable_pin: !gpio2
        microsteps: 16
        rotation_distance: 8

        [tmc2209 manual_stepper 3ms2]
        uart_pin: gpio9
        tx_pin: gpio8
        uart_address: 1
        run_current: 0.580
        stealthchop_threshold: 999999

        [manual_stepper 3ms3]
        step_pin: gpio14
        dir_pin: !gpio13
        enable_pin: !gpio15
        microsteps: 16
        rotation_distance: 33.500

        [tmc2209 manual_stepper 3ms3]
        uart_pin: gpio9
        tx_pin: gpio8
        uart_address: 3
        run_current: 0.650
        stealthchop_threshold: 999999
        ```

### Organization

Rename your configuration to `steppers.cfg`. Next, create the following files with these contents:

??? "3ms/main.cfg"
    ``` cfg title="3ms/main.cfg"
    [gcode_macro Toolchange]
    variable_p: -1
    gcode:
    {% set p = printer["gcode_macro Toolchange"].p|int %}
    {% if p > -1 %}
    G100 T{p} E-50 F4500 N0
    {% endif %}
    G100 T{params.T} E55 F4500 N0
    SAVE_GCODE_VARIABLE MACRO=Toolchange VARIABLE=p VALUE={params.T}

    [gcode_macro T0]
    gcode:
    Toolchange T=0

    [gcode_macro T1]
    gcode:
    Toolchange T=1

    [gcode_macro T2]
    gcode:
        Toolchange T=2

    [gcode_macro T3]
    gcode:
        Toolchange T=3

    [include ./g100.cfg]
    [include ./steppers.cfg]
    ```
??? "3ms/g100.cfg"
    ``` cfg title="3ms/g100.cfg"
    [gcode_macro G100]
    gcode:
    {% set T = params.T|int %}
    {% set E = params.E|default(0)|float %}
    {% set F = params.F|default(3000)|float %}
    {% set N = params.N|default(1)|int %}

    MANUAL_STEPPER STEPPER=3ms{T} ENABLE={N} SET_POSITION=0
    MANUAL_STEPPER STEPPER=3ms{T} ENABLE={N} MOVE={E} SPEED={F/60} ACCEL=1000
    ```