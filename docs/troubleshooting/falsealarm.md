---
comments: true
---

# Filament Sensor False Alarm

If during toolchanges, a failed toolchange false alarm occurs (print pauses even though toolchange was successful), follow this troubleshooting guide to fix it.

## fsensor_delay

The main culprit for this issue is likely your `fsensor_delay` in `3ms/settings.cfg` is too short. Short values will cause more false alarms, and long values will cause less. Generally, the default 2000ms is good for most setups, but if you are having false alarms, you will have to increase it. Example:

=== "Before"
    ```cfg title="3ms/settings.cfg"
    fsensor_delay: 2000
    ```
=== "After"
    ```cfg title="3ms/settings.cfg"
    fsensor_delay: 3000
    ```