---
title: Electronics Assembly
comments: true
---

<link rel="stylesheet" href="../../../assets/css/kits.css">

# Electronics Assembly

.Stepn Removing Supports: Part 1

gcard

- stepi-e30aa8fc
    stepi-c34ecb1c
    stepi-e6d78a9a

- Remove the built-in supports from the SKR Pico case.

    .rcir. Prepare either `SKR Pico Bottom.stl` or `SKR Pico Bottom (small).stl` (shown)

    .gcir. Remove the indicated built-in support.

.gcard

.stepi-e30aa8fc .red-ol
.stepi-c34ecb1c .green-ol
.stepi-e6d78a9a

.Stepn Removing Supports: Part 2

gcard

- stepi-1c4e396a
    stepi-09ef7f74

- Remove the built-in supports from the case.

    .rcir. Remove the indicated supports from the case.

.gcard

.stepi-1c4e396a .red-ol
.stepi-09ef7f74

.Stepn Installing the Board

gcard

- stepi-774c115b
    stepi-ae32f565
    stepi-97215347

- Install the SKR Pico board into the case.

    Prepare the following for this step:

    &emsp;.rcir. 2mm Hex key

    &emsp;.ocir. 4x mounting bolts (included with the SKR Pico)

    &emsp;.gcir. SKR Pico board

    .bcir. Place the SKR Pico board onto the previously prepared case.

    .pcir. Using the four mounting bolts and the hex key, fasten the SKR Pico onto the case.

.gcard

.stepi-774c115b .red-ol .green2-ol
.stepi-ae32f565 .blue-ol
.stepi-97215347 .purple-ol

.Stepn Preparing the Power Cables

gcard

- stepi-7870312c
    stepi-7870312c
    stepi-7870312c
    stepi-7870312c

- Strip the power cables and prepare for the next steps.

    Prepare the following for this step:

    &emsp;.rcir. Power cables

    &emsp;.ocir. Wire strippers

    .gcir. Split both ends of the wires as shown.

    .bcir. Strip a short length off of all four ends of the wires.

    .pcir. Twist the ends of the wires.

.gcard

.stepi-7870312c .red-ol .orange2-ol
.stepi-7870312c .green-ol
.stepi-7870312c .blue-ol
.stepi-7870312c .purple-ol

.Stepn Connecting the PSU

TODO...

.Stepn Connecting the Power Cables

gcard

- stepi-a54b6b9e
    stepi-c838d2da
    stepi-fd33ee24
    stepi-25994019
    
- Connect the power cables from the PSU to the SKR Pico.

    Prepare the following for this step:

    &emsp;.rcir. Power cables and PSU

    &emsp;.ocir. SKR Pico with case

    &emsp; Flat-head screwdriver

    .gcir. Loosen both power terminals on the SKR.

    .rcir. Plug the **red** wire into the **positive** terminal on the SKR.

    .bcir. Plug the **black** wire into the **negative** terminal on the SKR.

    .pcir. Firmly tighten both power terminals on the SKR.

.gcard

.stepi-a54b6b9e .red-ol
.stepi-c838d2da .green-ol
.stepi-fd33ee24 .red-ol .blue2-ol
.stepi-25994019 .purple-ol

.Stepn Preparing the 3HOME

gcard

- stepi-7870312c
    stepi-7870312c

- Add M3nS to the 3HOME.

    Prepare the following for this step:

    &emsp;.rcir. 3HOME

    &emsp;.gcir. 2x M3nS Square nuts

    .bcir. Insert the two square nuts into any joiner of the 3HOME

.gcard

.stepi-7870312c .red-ol .green2-ol
.stepi-7870312c .blue-ol

.Stepn Attaching to the 3HOME

gcard

- stepi-88e17048
    stepi-6e986e52

- Attach the SKR Pico case to the 3HOME.

    Prepare the following for this step:

    &emsp;.rcir. 2.5mm Hex key

    &emsp;.ocir. 2x M3x30 SHCS

    &emsp;.gcir. SKR Pico case (prepared previously)

    .bcir. Fasten the SKR Pico to the 3HOME with the two M3x30 SHCS using the 2.5mm hex key.

.gcard

.stepi-88e17048 .red-ol .green2-ol
.stepi-6e986e52 .blue-ol

.Stepn Wire Management

Begin by stretching out each stepper motor wire away from the 3HOME as shown.

![](7b9ae602.jpeg){.mdimg}

Next, take the rightmost wire (T0) and form it into the shape shown.

![](64eeec85.jpeg){.mdimg}

Fold it back over itself several times until a short length is remaining. Use a zip tie to secure and cut off the excess from the zip tie.

![](eb382317.jpeg){.mdimg}

Push the cable bundle into the SKR case and route the wire as shown with the green line.

![](6714f09d.jpeg){.mdimg}

Plug the stepper cable into the second-to-left port on the SKR (when viewed upside down as shown)

![](7b693bf8.jpeg){.mdimg}

Repeat the same process for the stepper motor to the left of the previous one. Plug it into the port to the right of the first one.

![](7f892d9d.jpeg){.mdimg}

Repeat the process for the next stepper motor in line, routing the wire as shown with the green line.

![](8c228c68.jpeg){.mdimg}

Plug the stepper into the port to the right of the previous one.

![](7aafd269.jpeg){.mdimg}

Repeat the process for the final stepper, routing the wire as shown with the green line.

![](6125f8b5.jpeg){.mdimg}

Plug this stepper into the leftmost plug on the SKR.

![](3f66eb08.jpeg){.mdimg}