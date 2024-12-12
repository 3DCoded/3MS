<link rel="stylesheet" href="../../assets/css/kits.css">


# 3MS Kit Assembly

!!! info "This page is under construction"
    This page is the assembly instructions for future 3MS kits. Instructions on this page will change, so don't follow it until 3MS Kits are officially released. Anything on this page is subject to change.

!!! tip
    Even though each step only looks like it has one image, if you click on the image you can view several more images for each step.

## Electronics Assembly

###**Step 1** Preparing the Power Cables

<div class="grid cards" markdown>
- ![](https://placehold.co/600x400?text=Prepare+Cables){data-gallery="prepPower"}
    ![](https://placehold.co/600x400?text=Prepare+Cables+2){.hidden data-gallery="prepPower"}

- Strip both ends of the red and black power cables and twist the ends.

    ---

    :orange_circle: Use wire cutters that can strip 14AWG wire.

    :green_circle: Strip 5mm of insulation off of both ends of both wires.

    :blue_circle: Twist the ends of the stripped wires tightly.
</div>

###**Step 2** Connecting the Power Supply

<div class="grid cards" markdown>
- ![](https://placehold.co/600x400?text=Connect+PSU){data-gallery="connPSU"}
    ![](https://placehold.co/600x400?text=Connect+PSU+2){.hidden data-gallery="connPSU"}

- Insert both power cables into the power supply.
    
    ---

    :orange_circle: Loosen the terminals with a phillips-head screwdriver.

    :red_circle: Insert the **red** power cable into the **positive** PSU terminal.

    :blue_circle: Insert the **black** power cable into the **negative** PSU terminal.

    :green_circle: Tighten both terminals securely with a phillips-head screwdriver.
</div>

###**Step 3** Connecting the Control Board

<div class="grid cards" markdown>
- ![](https://placehold.co/600x400?text=Connect+Board){data-gallery="connBoard"}
    ![](https://placehold.co/600x400?text=Connect+Board+2){.hidden data-gallery="connBoard"}

- Insert both power cables into the control board.
    
    ---

    :orange_circle: Locate the HVIN power input on the control board and loosen both terminals with a flat-head screwdriver.

    :red_circle: Insert the **red** power cable into the **positive** HVIN terminal.

    :blue_circle: Insert the **black** power cable into the **negative** HVIN terminal.

    :green_circle: Tighten both terminals securely with a flat-head screwdriver.
</div>

###**Step 4** Adding Jumpers

<div class="grid cards" markdown>
- ![](https://placehold.co/600x400?text=Add+Jumpers){data-gallery="addJumpers"}
    ![](https://placehold.co/600x400?text=Add+Jumpers+2){.hidden data-gallery="addJumpers"}

- Install the VUSB and HVIN jumpers.
    
    ---

    :orange_circle: Install the **VUSB** jumper.

    :green_circle: For each stepper driver, select the **HVIN** input by installing a jumper on each driver.
</div>

###**Step 5** Install the Stepper Drivers

<div class="grid cards" markdown>
- ![](https://placehold.co/600x400?text=Add+Drivers){data-gallery="addDrivers"}
    ![](https://placehold.co/600x400?text=Add+Drivers+2){.hidden data-gallery="addDrivers"}

- Install all four EZ2209 stepper drivers.
    
    ---

    :orange_circle: Install an EZ2209 into each stepper driver slot.
</div>

## Printed Parts

###**Step 1** Extruder Mounts

<div class="grid cards" markdown>
- 

    === "Minimalistic Mount"
        [Download](../../assets/stls/mk8m3.stl)

        <iframe id="vs_iframe" src="https://www.viewstl.com/?embedded&url=https%3A%2F%2F3dcoded.github.io%2F3MS%2Fassets%2Fstls%2Fmk8m3.stl&color=blue&noborder=yes&clean=yes&shading=flat&bgcolor=transparent" style="border:0;margin:0;width:100%;height:100%;"></iframe>
    === "Full Enclosure"
        Designed by [chadk](https://www.printables.com/@Chad_336665)
        
        [Printables Link](https://www.printables.com/model/1067703-wip-3ms-mmu-using-btt-mmb)
        
        <iframe id="vs_iframe" src="https://www.viewstl.com/?embedded&url=https%3A%2F%2F3dcoded.github.io%2F3MS%2Fassets%2Fstls%2Fenclosure%2Fbottom-v6.stl&color=blue&bgcolor=transparent&noborder=yes&edges=no" style="border:0;margin:0;width:100%;height:100%;"></iframe>

        <iframe id="vs_iframe" src="https://www.viewstl.com/?embedded&url=https%3A%2F%2F3dcoded.github.io%2F3MS%2Fassets%2Fstls%2Fenclosure%2Ftop-v6.stl&color=blue&bgcolor=transparent&noborder=yes&edges=no" style="border:0;margin:0;width:100%;height:100%;"></iframe>

- Choose either of the mounting/enclosure options on the left for your 3MS and print them out.
</div>

###**Step 2** Y-Splitter

<div class="grid cards" markdown>
- Designed by [ImChrono](https://www.printables.com/@ImChrono_909974)

    [Printables Link](https://www.printables.com/model/1042279-no-catch-4-way-y-splitter-pc4-m10)

    <iframe id="vs_iframe" src="https://www.viewstl.com/?embedded&url=https%3A%2F%2F3dcoded.github.io%2F3MS%2Fassets%2Fstls%2F4ysplitter.stl&color=blue&bgcolor=transparent&noborder=yes&edges=no" style="border:0;margin:0;width:100%;height:100%;"></iframe>

- Print this Y-splitter according to the instructions in its Printables page.
</div>

## Hardware Assembly

###**Step 1** Assemble Extruders

<div class="grid cards" markdown>
- ![](https://placehold.co/600x400?text=Assemble+MK8){data-gallery="assembleMK8"}
    ![](https://placehold.co/600x400?text=Assemble+MK8+2){.hidden data-gallery="assembleMK8"}

- Assemble each of your 3MS extruders
    
    ---

    :orange_circle: Place the mounting plate on the face of the motor

    :red_circle: Assemble the MK8 extruders onto the face of the motors (with the mount in between)

    :green_circle: Repeat for all four 3MS extruders

</div>

###**Step 2** Connecting the Stepper Motors

<div class="grid cards" markdown>
- ![](https://placehold.co/600x400?text=Connect+Motors){data-gallery="connMotors"}
    ![](https://placehold.co/600x400?text=Connect+Motors+2){.hidden data-gallery="connMotors"}

- Connect each stepper motor to the BTT MMB CAN board
    
    ---

    :red_circle: The extruder for T0 connects to the M1 port

    :orange_circle: The extruder for T1 connects to the M2 port

    :green_circle: The extruder for T2 connects to the M3 port

    :blue_circle: The extruder for T3 connects to the M4 port

</div>

###**Step 3** Installing the MMB CAN (optional)

<div class="grid cards" markdown>
- ![](https://placehold.co/600x400?text=Install+MMB){data-gallery="instMMB"}
    ![](https://placehold.co/600x400?text=Install+MMB+2){.hidden data-gallery="instMMB"}

- Install the MMB in the 3MS enclosure
    
    ---

    :orange_circle: Use 4x M3x10 bolts to secure the MMB CAN to the enclosure

</div>