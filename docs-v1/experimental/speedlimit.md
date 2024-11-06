---
comments: true
---

# Speed Limiting for TPU

TPU filament has a tendency to buckle when extruded at high speeds. This feature attempts to slow down the 3MS extruders during toolchanges only when TPU is involved in the toolchange.

!!! info
    This page, and the features mentioned on it, are in development

## Installation

To install the speed limiting feature, run in your terminal:

```sh
cd ~/3MS
git fetch
git checkout 
git pull limited-speed
sh install.sh
```

Restart Klipper.

## Configuration

Update your `3ms/main.cfg`:

```cfg title="3ms/main.cfg" hl_lines="8"
[save_variables]
filename: ~/printer_data/config/3ms/variables.cfg

[include ./settings.cfg]
[include ./controllers/btt_skr_mini_e3_v2/steppers.cfg]

[dynamicmacros 3ms]
configs: 3ms/macros.cfg, 3ms/speedlimit.cfg
```

## Usage

!!! info
    This section is under construction