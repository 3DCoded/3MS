# Configuration Generator

Follow this guide to create a custom configuration for your 3MS.

## Base Configuration

First, find the case configuration for your mainboard. The best place to find these is in the [official Klipper sample configurations](https://github.com/Klipper3d/klipper/tree/master/config).

In this example, a BTT SKR Mini E3 V3 will be used. A base configuration is available in the official configuration [here](https://github.com/Klipper3d/klipper/blob/master/config/generic-bigtreetech-skr-mini-e3-v3.0.cfg).

### Raw File

Now you have the configuration, but it isn't a raw file. It's a full webpage. To continue, you need the raw configuration. To do this, find the **"Raw"** button in the upper-right corner of the page.

![](generator01.png)

Now, you will be redirected to a page with the raw configuration. Copy the URL.

![](generator02.png)

## Generating the Configuration

Now that you have the raw URL, you need to install the generator script.

### Installation

1. Clone the 3MS repository:

    ```sh
    cd ~
    git clone https://github.com/3DCoded/3MS
    ```

2. Ensure Python 3 is installed (not Python 2).
3. Install `requests`

    ```sh
    pip3 install requests
    ```

### Running the Script

First, start the script:

```sh
cd ~/3MS
python3 generator.py
```

Now, you will be presented with several options.

#### Configuration URL

Paste in the URL you found earlier.

![](generator03.png)

#### Selected Steppers

The script will now list all the stepper motor configurations that were found in the configuration, with a number next to each. Enter the desired steppers, seperated by spaces.

![](generator04.png)

#### TMC Drivers

For each stepper you selected, the script will ask you which TMC driver to use. For the SKR Mini E3 V3, there is only one option: TMC2209.

![](generator05.png)

#### MCU Name

Finally, the script will ask you for the name of the MCU controlling your 3MS. Follow the naming convention outlined in the prompt.

![](generator06.png)

---

Your configuration will now be available in `~/3MS/mmu.cfg` and `~/3MS/mmu_hardware.cfg`.