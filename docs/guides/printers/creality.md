---
comments: true
icon: printers/creality
---

# Creality E3v3 series

## Introduction

The Creality K1 Ender 3 v3 series printers run a heavily modified Klipper and Linux installation. Because of this, setup isn't as straightforward as on a genuine Klipper and Linux install. If you have another printer running mainline Klipper, it is highly recommended to install the 3MS on it instead.

If you would like to use the 3MS on an E3v3, read on.

!!! tip
    Please read every step here carefully. If you run into issues, please reach out on the 3MS Discord (link on homepage) and note the step you are having trouble with.

??? warning "Disclaimer"
    I am not responsible for whatever happens to your machine! You proceed at your own risk and understand that you will likely void your warranty by proceeding.

## Instructions

### Rooting

Follow [this](https://guilouz.github.io/Creality-Helper-Script-Wiki/firmwares/install-and-update-rooted-firmware-ender3/) guide to root your printer.

### SSH

Follow [this](https://guilouz.github.io/Creality-Helper-Script-Wiki/firmwares/ssh-connection/) guide to connect to your printer via SSH.

### Moonraker, Mainsail, and Entware

Follow the below guides to install:

1. [Moonraker](https://guilouz.github.io/Creality-Helper-Script-Wiki/helper-script/moonraker-ender3/)
2. [Mainsail](https://guilouz.github.io/Creality-Helper-Script-Wiki/helper-script/mainsail/)
3. [Entware (opkg)](https://guilouz.github.io/Creality-Helper-Script-Wiki/helper-script/entware/)
4. Restart your printer.

### Compile and Flash Firmware

TODO

### Install Bash

In SSH, run the following commands:

```sh
opkg update
opkg install bash
```

### Install Happy Hare

First, clone the repository.

```sh
cd /usr/data
git clone https://github.com/moggieuk/Happy-Hare
```

Then, make the install script executable.

```sh
cd Happy-Hare
chmod u+x install.sh
```

Download a modified `mmu_toolhead.py`

```sh
cd extras
wget https://raw.githubusercontent.com/k1-801/Happy-Hare/k1/extras/mmu_toolhead.py
cd ..
```

Finally, install Happy Hare.

```sh
bash ./install.sh -i
```

### Disable LEDs

Currently, this approach doesn't allow for setting up LEDs on your 3MS. Please feel free to reach out to me on the 3MS Discord if you want to test a few methods of setting up LEDs.

In `mmu_hardware.cfg`, remove the following sections located at the bottom of the file:

```yaml
[neopixel mmu_leds]
pin: mmu:MMU_NEOPIXEL
chain_count: {chain_count}			# Need number gates x1 or x2 + status leds
color_order: {color_order}		# Set based on your particular neopixel specification (can be comma separated list)

...

[mmu_leds]
exit_leds:   {exit_leds}
entry_leds:  {entry_leds}
status_leds: {status_leds}
logo_leds:   {logo_leds}
frame_rate: 24
```

---

You can follow the rest of the documentation as usual from here.

[Start Here](../../instructions/index.md){.md-button}