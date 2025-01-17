<link rel="stylesheet" href="../../assets/css/kits.css">


# 3MS Kit Assembly

!!! info "This page is under construction"
    This page is the assembly instructions for future 3MS kits. Instructions on this page will change, so don't follow it until 3MS Kits are officially released. Anything on this page is subject to change.

!!! tip
    Even though each step only looks like it has one image, if you click on the image you can view several more images for each step.

## Electronics Assembly

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

    :red_circle: Use wire strippers that can strip 16AWG wire.

    :yellow_circle: Split the ends of the power cables

    :green_circle: Strip a short length of insulation off of both ends of both wires.

    :blue_circle: Tightly twist the ends of the stripped wires.
</div>

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

# EVERYTHING AFTER THIS POINT IS INCOMPLETE

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

###**Step 1** Enclosure

<div class="grid cards" markdown>
- 

    === "3HOME (Official) (Beta)"
        [Printables Link](https://www.printables.com/model/1108644-beta-3home-3ms-hybrid-official-modular-enclosure/files)

        ![](https://media.printables.com/media/prints/1108644/images/8561411_33c8e695-bbc6-41cd-8166-20ad7de4a411_c4c521b9-7f8a-4b55-89f5-df56d1c30401/thumbs/inside/1600x1200/png/r0.webp)
    === "Minimalistic Mount"
        [Download](../../assets/stls/mk8m3.stl)

        <iframe id="vs_iframe" src="https://www.viewstl.com/?embedded&url=https%3A%2F%2F3dcoded.github.io%2F3MS%2Fassets%2Fstls%2Fmk8m3.stl&color=blue&noborder=yes&clean=yes&shading=flat&bgcolor=transparent" style="border:0;margin:0;width:100%;height:100%;"></iframe>
    === "chadk Enclosure"
        Designed by [chadk](https://www.printables.com/@Chad_336665)
        
        [Printables Link](https://www.printables.com/model/1067703-wip-3ms-mmu-using-btt-mmb)
        
        ![](https://media.printables.com/media/prints/1067703/images/8088653_02c779e6-ba6e-467c-a42e-ce7769189863_4913595f-da9b-4cf3-b618-52f3373aaaef/thumbs/inside/1600x1200/jpg/20241109_214315.webp)
    === "Marcin1415 Enclosure"
        Designed by [Marcin1415](https://www.printables.com/@Marcin1415_557608)

        [Printables Link](https://www.printables.com/model/1121864-3ms-mmu-mounting-system)

        ![](https://media.printables.com/media/prints/1121864/images/8470904_12d40664-860a-40e5-bea1-21419fed8797_4f180760-d019-49f6-b979-4422aa465063/thumbs/inside/1600x1200/jpg/3ms_mmu_enclosure_newconcept-v40.webp)

- Choose one of the mounting/enclosure options on the left for your 3MS and print them out.
</div>

###**Step 2** Y-Splitter

<div class="grid cards" markdown>
-   
    === "Official Y-Splitter"
        [Printables Link](https://www.printables.com/model/1103095-4-way-y-splitter-with-ecas04)

        ![](https://media.printables.com/media/prints/1103095/images/8338186_1e66aafd-0187-42a4-bed7-420d532541cb_9d93d093-db12-434a-a4c1-8aa2e3bf8fc3/thumbs/inside/1600x1200/png/img_0424.webp)
    === "ImChrono Y-Splitter"
        Designed by [ImChrono](https://www.printables.com/@ImChrono_909974)

        [Printables Link](https://www.printables.com/model/1042279-no-catch-4-way-y-splitter-pc4-m10)

        ![](https://media.printables.com/media/prints/1042279/images/7911671_cf864755-81d4-4b1d-a9f2-1c4f1d77bc24_9ce3f0a3-2276-419e-8c8c-faa9a5ec9ef3/thumbs/inside/1600x1200/jpg/photo_2024-10-18_18-33-02.webp)

        

- Print one of these Y-splitters according to the instructions in its respective Printables page.
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

- Install the MMB in the 3HOME
    
    ---

    :orange_circle: Use 4x M3x10 bolts to secure the MMB CAN to the 3HOME

</div>