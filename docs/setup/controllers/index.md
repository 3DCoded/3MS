# Controllers

Follow this guide to determine which controller to use in your 3MS.

## Options

The 3MS works on multiple different controllers. 

!!! info
    If your printer's mainboard has spare stepper ports, you can use them to control 3MS steppers. You can open an issue on Github (there's a template) to get a configuration made for your specific setup. Any controllers listed with "(main MCU)" use those spare stepper plugs.

Choose one of the following supported controllers (a checkmark indicates it is fully tested):

- [X] [SKR Mini E3 V2.0 (4 colors)](skrminie3v2.md)

    !!! success "Fully Tested"

- [ ] [BTT Octopus (main MCU) (4 colors)](bttoctopusmain.md)

    !!! warning "Untested"

- [ ] [Einsy RAMBo (main MCU) with SKR Mini E3 V2.0 (3ms MCU)](einsyrambo-skrminie3v2.md)

    !!! danger "Expert modification, in development"