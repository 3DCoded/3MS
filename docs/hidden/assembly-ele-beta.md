---
comments: true
---

<link rel="stylesheet" href="../../assets/css/kits.css">

# Electronics Assembly

###**Step 1** Preparing the Power Cables

<div class="grid cards" markdown>
- ![](step01a.jpeg){data-gallery="prepPower"}
    ![](step01b.jpeg){.hidden data-gallery="prepPower"}
    ![](step01c.jpeg){.hidden data-gallery="prepPower"}
    ![](step01d.jpeg){.hidden data-gallery="prepPower"}

- Strip both ends of the red and black power cables and twist the ends.

    ---

    Prepare the following for this step:

    - Red and black power cables
    - Wire strippers

    :red_circle: Use wire strippers that can strip 24AWG wire.

    :yellow_circle: Split the ends of the power cables

    :green_circle: Strip a short length of insulation off of both ends of both wires.

    :blue_circle: Tightly twist the ends of the stripped wires.

</div>

![](step01a.jpeg){.sm .red-ol}
![](step01b.jpeg){.sm .yellow-ol}
![](step01c.jpeg){.sm .green-ol .blue2-ol}
![](step01d.jpeg){.sm}

###**Step 2** Preparing the Power Supply

<div class="grid cards" markdown>
- ![](step02a.jpeg){data-gallery="prepPSU"}
    ![](step02b.jpeg){.hidden data-gallery="prepPSU"}

- Loosen the PSU terminals.
    
    ---

    Prepare the following for this step:

    - Phillips-head screwdriver
    - PSU adapter

    :red_circle: Loosen both terminals on the PSU.
</div>

![](step02a.jpeg){.sm}
![](step02b.jpeg){.sm .red-ol}

###**Step 3** Preparing the Control Board

<div class="grid cards" markdown>
- ![](step03a.jpeg){data-gallery="prepBoard"}
    ![](step03b.jpeg){.hidden data-gallery="prepBoard"}

- Loosen the HVIN terminals on the BTT MMB CAN board.
    
    ---

    Prepare the following for this step:

    - Flat-head screwdriver
    - BTT MMB CAN board

    :red_circle: Loosen both HVIN terminals on the BTT MMB CAN board.
</div>

![](step03a.jpeg){.sm}
![](step03b.jpeg){.sm .red-ol}

###**Step 4** Connecting the PSU

<div class="grid cards" markdown>
- ![](step04a.jpeg){data-gallery="connPSU"}
    ![](step04b.jpeg){.hidden data-gallery="connPSU"}
    ![](step04c.jpeg){.hidden data-gallery="connPSU"}
    ![](step04d.jpeg){.hidden data-gallery="connPSU"}

- Connect the power cables to the PSU

    ---

    Prepare the following for this step:

    - Phillips-head screwdriver
    - Power cables
    - PSU adapter

    :red_circle: Push the <span style="color:red;background-color:white;padding:3px;font-weight:bold;">red</span> power cable into the **positive** terminal of the PSU.

    :blue_circle: Push the <span style="color:black;background-color:white;padding:3px;font-weight:bold;">black</span> power cable into the **negative** terminal of the PSU.

    :purple_circle: Firmly tighten the PSU screw terminals.
</div>

![](step04a.jpeg){.sm}
![](step04b.jpeg){.sm .red-ol .blue2-ol}
![](step04c.jpeg){.sm}
![](step04d.jpeg){.sm .purple-ol}

###**Step 5** Connecting the Control Board

<div class="grid cards" markdown>
- ![](step05a.jpeg){data-gallery="MMBconnPWR"}
    ![](step05b.jpeg){.hidden data-gallery="MMBconnPWR"}
    ![](step05c.jpeg){.hidden data-gallery="MMBconnPWR"}
    ![](step05d.jpeg){.hidden data-gallery="MMBconnPWR"}

- Connect the power cables to the MMB CAN

    ---

    Prepare the following for this step:
    
    - Flat-head screwdriver
    - Power cables
    - BTT MMB CAN board

    :red_circle: Push the <span style="color:red;background-color:white;padding:3px;font-weight:bold;">red</span> power cable into the **HVIN** terminal of the MMB CAN.

    :blue_circle: Push the <span style="color:black;background-color:white;padding:3px;font-weight:bold;">black</span> power cable into the **GND** terminal of the MMB CAN.

    :purple_circle: Firmly tighten the MMB CAN's HVIN screw terminals.
</div>

![](step05a.jpeg){.sm}
![](step05b.jpeg){.sm .red-ol .blue2-ol}
![](step05c.jpeg){.sm}
![](step05d.jpeg){.sm .purple-ol}

###**Step 6** Adding Jumpers: Part 1

<div class="grid cards" markdown>
- ![](step06a.jpeg){data-gallery="addJumpers1"}
    ![](step06b.jpeg){.hidden data-gallery="addJumpers1"}

- Install the VUSB and HVIN jumpers.
    
    ---

    Prepare the following for this step:

    - BTT MMB CAN
    - 5x Jumpers

    :red_circle: Install the **VUSB** jumper.

    :green_circle: For each stepper driver, select the **HVIN** input by installing a jumper on each driver.
</div>

![](step06a.jpeg){.sm}
![](step06b.jpeg){.sm .red-ol .green2-ol}

###**Step 7** Adding Jumpers: Part 2

<div class="grid cards" markdown>
- ![](step07a.jpeg){data-gallery="addJumpers2"}
    ![](step07b.jpeg){.hidden data-gallery="addJumpers2"}

- Install DIAG jumpers.
    
    ---

    Prepare the following for this step:

    - BTT MMB CAN
    - 4x Jumpers

    :red_circle: For each stepper driver, install a **DIAG** jumper.
</div>

###**Step 8** Installing Stepper Drivers

<div class="grid cards" markdown>
- ![](step08a.jpeg){data-gallery="installDrivers"}
    ![](step08b.jpeg){.hidden data-gallery="installDrivers"}

- Install the four EZ2209 stepper drivers.

    ---

    Prepare the following for this step:

    - BTT MMB CAN
    - 4x EZ2209

    :green_circle: For each stepper driver port, install an EZ2209 stepper driver.
</div>

![](step08a.jpeg){.sm}
![](step08b.jpeg){.sm .green-ol}

###**Step 9** Plugging in Stepper Motors

<div class="grid cards" markdown>
- ![](step09a.jpeg){data-gallery="installSteppers"}
    ![](step09b.jpeg){.hidden data-gallery="installSteppers"}

- Plug in the four stepper motors from each of the filament units.

    ---

    Prepare the following for this step:

    - 4x Filament Units (assembled previously)
    - BTT MMB CAN

    :red_circle: Plug in the stepper motor for **T0** into the port labeled **M1**

    :yellow_circle: Plug in the stepper motor for **T1** into the port labeled **M2**

    :green_circle: Plug in the stepper motor for **T2** into the port labeled **M3**

    :blue_circle: Plug in the stepper motor for **T3** into the port labeled **M4**

</div>

---

###**Step 10 (Optional)** 3HOME for the BTT MMB CAN

