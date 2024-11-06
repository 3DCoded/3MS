---
icon: material/alarm-light
comments: true
---

# Filament Sensor False Alarm/Extra Pauses

If during toolchanges, a failed toolchange false alarm occurs (print pauses even though toolchange was successful), follow this troubleshooting guide to fix it.

## fsensor_delay

The main culprit for this issue is likely your `fsensor_delay` in `3ms/settings.cfg` is too short. Short values will cause more false alarms, and long values will cause less. Generally, the default 2000ms is good for most setups, but if you are having false alarms, you will have to increase it. To set it, use the `SET_MMMS_SETTINGS` command:

```title="Klipper Console"
SET_MMMS_SETTINGS FSENSOR_DELAY=3000
```

To save it permanently:

=== "Before"
    ```cfg title="3ms/settings.cfg"
    fsensor_delay: 2000
    ```
=== "After"
    ```cfg title="3ms/settings.cfg"
    fsensor_delay: 3000
    ```