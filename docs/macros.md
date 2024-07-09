# Macros

## MMMS Settings

### MMMS_SETTINGS
Loads the default settings for MMMS.

**Default Settings**

```
variable_load_distance: 210
variable_unload_distance: 200
variable_num_tools: 2
```

**Example Usage**

```
MMMS_SETTINGS
```

### SET_MMMS_SETTINGS
Sets the configuration for MMMS. Allows **temporary** customization of load and unload distances, and the number of tools.

**Example Usage**

```
SET_MMMS_SETTINGS LOAD_DISTANCE=210 UNLOAD_DISTANCE=200 NUM_TOOLS=2
```

## Filament Handling

### MMMS_UNLOAD
Unloads filament by a specified distance. If no distance is specified, it uses the default unload distance from `MMMS_SETTINGS`.

**Example Usage**

```
MMMS_UNLOAD DISTANCE=200
```

### MMMS_LOAD
Loads filament by a specified distance. If no distance is specified, it uses the default load distance from `MMMS_SETTINGS`.

**Example Usage**

```
MMMS_LOAD DISTANCE=210
```

### CHECK_FSENSOR
Checks the filament sensor state. Pauses the print if the sensor state does not match the expected value.

**Example Usage**

```
CHECK_FSENSOR V=1
```

## Tool Sync

### SET_TOOL_SYNC
Sets the sync state of a tool. Syncs or desyncs the specified tool.

**Example Usage**

```
SET_TOOL_SYNC TOOL=0 SYNC=1
```

### SYNC_TOOL
Syncs the specified tool and desyncs all other tools.

**Example Usage**

```
SYNC_TOOL TOOL=0
```

### DESYNC_TOOL
Desyncs the specified tool.

**Example Usage**

```
DESYNC_TOOL TOOL=0
```

### CLEAR_TOOL
Clears the current tool selection by setting it to -1.

**Example Usage**

```
CLEAR_TOOL
```

### DESYNC_ALL_TOOLS
Desyncs all configured tools.

**Example Usage**

```
DESYNC_ALL_TOOLS
```

## Print Start and End

### MMMS_START
Starts the print by checking the filament sensor. If filament is detected, the print is paused and the user is notified. Regardless of the filament sensor state, the initial tool is loaded.

**Example Usage**

```
MMMS_START INITIAL_TOOL=0
```

### MMMS_END
Ends the print by unloading the current tool. If filament is detected after unloading, the user is notified.

**Example Usage**

```
MMMS_END
```

## Tool Change

### T0
Changes to tool 0.

**Example Usage**

```
T0
```

### T1
Changes to tool 1.

**Example Usage**

```
T1
```

### Tx
Changes to a specified tool. Replace `x` with the tool number.

**Example Usage**

```
T2
T3
```