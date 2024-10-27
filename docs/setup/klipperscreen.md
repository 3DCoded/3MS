---
icon: fontawesome/solid/mobile-screen
comments: true
---

# KlipperScreen

!!! info
    This feature is still in an alpha state.

![](ks_home.png)
![](ks_main.png)
![](ks_settings.png)

---

The 3MS has a [custom fork of KlipperScreen](https://github.com/3DCoded/KlipperScreen-3MS) you can use to control your 3MS.

## Install

To install the 3MS KlipperScreen, first install KlipperScreen following instructions [here](https://klipperscreen.readthedocs.io/en/latest/Installation/). Then, run in your terminal:

```sh
cd ~
mv KlipperScreen KlipperScreen.old
git clone https://github.com/3DCoded/KlipperScreen-3MS KlipperScreen
cd ~/KlipperScreen
./scripts/KlipperScreen-install.sh
```

Restart KlipperScreen.