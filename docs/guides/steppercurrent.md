---
title: Tuning Stepper Current
icon: material/tune
comments: true
---

# Tuning Stepper Current

Tuning stepper current is an important part of any 3D printer, including MMU's. Follow this guide to find the optimal `run_current` setting for your 3MS gear steppers.

## Why Tune Stepper Current?

Firstly, why tune stepper current in the first place?

If your stepper current is too **low**, you might notice your stepper skipping when trying to move filament.

If your stepper current is too **high**, you might notice your stepper grinding filament if something is preventing its motion.

![](grinding.jpeg)
/// caption
Grinding filament

Source: Simplify3D
///

---

Follow the below steps to tune your 3MS gear steppers.

## Hardware Limits

Firstly, find the maximum current your stepper can safely run at. There are three main things that can limit this. For this example, components from [3MS Kits](../kits/index.md) will be used.

- PSU rated current. The PSU included in 3MS kits is rated to 2A. The stepper current cannot exceed this.
- Driver rated current. The TMC2209's on the SKR Pico included in 3MS kits are rated to 2A continuous current. The stepper current cannot exceed this.
- Stepper rated current. The steppers included in 3MS kits are rated to 1A. Generally, you don't want to exceed 75% of your stepper's rated current, bringing down our safe limit to 0.75A. The stepper current cannot exceed this.

The lowest of the three values (for this example) is 0.75A. Therefore, your `run_current` cannot exceed 0.75A of current.

### Maximum Current

Now that the maximum safe current for the steppers is known, we can test the stepper at the max current to see if it can drive filament at its max current.

First, set your `run_current` to the maximum calculated previously.

```cfg title="mmu_hardware.cfg"
[tmc2209 stepper_mmu_gear]
run_current: 0.75
```

Restart Klipper.

There are two parts to this test:

1. Free filament test
2. Blocked filament test

## Free Filament Test

Begin by detaching the PTFE from the exit of the 3MS extruder and manually loading filament into the extruder. Next, run in your Mainsail/Fluidd console:

```
MMU_SELECT GATE=0
MMU_TEST_MOVE MOVE=100
```

Observe the behavior of the stepper. If your stepper moves the filament without any skipping, move onto the next test.

If the stepper skips when it tries to move the filament, there are a couple things you can try:

- Reducing `gear_max_velocity` and/or `gear_max_accel` in `mmu_parameters.cfg`
- Lowering extruder tension by loosening the tension screw

## Blocked Filament Test

Begin by inserting a loose piece of filament into the Y-splitter (blue in the below diagram).

![](stuck-y.png)

Next, attach PTFE to the end of the 3MS extruder and to another input on the Y-splitter. Load the filament manually through the 3MS extruder until it wedges itself against the loose filament. In the above diagram, the green filament represents the filament in the 3MS extruder.

In the Mainsail/Fluidd console, run:

```
MMU_SELECT GATE=0
MMU_TEST_MOVE MOVE=50
```

If the stepper skips steps, your `run_current` is properly set.

If the stepper grinds the filament, your `run_current` is too high. Reduce it by 0.05-0.1, restart Klipper, and repeat this test until the stepper skips steps.

!!! warning
    Make sure when reducing stepper current that it also passes the [free filament test](#free-filament-test) as well as the [blocked filament test](#blocked-filament-test).