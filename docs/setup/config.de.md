---
comments: true
icon: material/code-json
---

# Konfiguration

Nach dem Installieren der Happy Hare Firmware musst du ein paar Einstellungen vornehmen, bevor du mit mehreren Materialien drucken kannst.

## Filament Sensoren

Um das 3MS nutzen zu können brauchst du einen Filament Sensor. Angenommen du hast bereits einen eingebaut, kannst du ihn in `mmu_hardware.cfg` konfigurieren.

Du findest ihn im `[mmu_sensors]`-Abschnitt kurz vor dem Ende der `mmu_hardware.cfg`.

### Extruder/Werkzeugkopf Sensoren

Um einen Extruder-Eintrittssensor (ein Sensor direkt **vor** deinem Extruder) zu konfigurieren, setze deinen `extruder_switch_pin`:

!!! tip "Du kennst weißt deinen Sensor Pin nicht?"
    Falls du deinen Sensor Pin nicht kennst und er schon in Klipper eingerichtet ist, dann kannst du ihn in deiner Sensor Konfiguration (normalerweise als `filament_switch_sensor`) finden und dir den `sensor_pin` notieren.

```cfg title="mmu_hardware.cfg"
[mmu_sensors]
...
extruder_switch_pin: <IRGENDEIN PIN>
```

Um einen Werkzeugkopfsensor (ein Sensor direkt **nach** deinem Extruder) zu konfigurieren, setze deinen `toolhead_switch_pin` auf die gleiche Weise wie den `extruder_switch_pin`.

### Gemeinsamer Gate Sensor (Optional) #####CHECK

Moving backwards from the extruder, the next possible sensor you may have installed is a shared gate sensor. This goes right **after** the Y-splitter.

If you have a gate sensor installed, set your `gate_switch_pin`:

```cfg title="mmu_hardware.cfg"
[mmu_sensors]
...
gate_switch_pin: <IRGENDEIN PIN>
```

### Pre/Post Gate Sensors (Optional)
Falls du einen Filament-Sensor vor oder nach jeder deiner 3MS Filament-Einheiten hast, konfiguriere einen `pre_` oder `post_gate` Sensor.

#### Pre-Gate

Pre-Gate Sensoren sitzen **vor** jeder deiner Filament-Einheiten. Konfiguriere sie wie folgt:

```cfg title="mmu_hardware.cfg"
[mmu_sensors]
pre_gate_switch_pin_0: <IRGENDEIN PIN>
pre_gate_switch_pin_1: <IRGENDEIN PIN>
pre_gate_switch_pin_2: <IRGENDEIN PIN>
pre_gate_switch_pin_3: <IRGENDEIN PIN>
```

#### Post-Gate

Post-Gate Sensoren sitzen **hinter** jeder deiner Filament-Einheiten. Konfiguriere sie wie folgt:

```cfg title="mmu_hardware.cfg"
[mmu_sensors]
...
post_gate_switch_pin_0: <IRGENDEIN PIN>
post_gate_switch_pin_1: <IRGENDEIN PIN>
post_gate_switch_pin_2: <IRGENDEIN PIN>
post_gate_switch_pin_3: <IRGENDEIN PIN>
```

---

!!! Warnung "Existing Sensors"
    Bevor du weitermachst, stelle sicher, dass all deine existierenden `filament_switch_sensor` und `filament_motion_sensor` Abschnitte auskommentiert oder gelöscht sind. Sie aktiv zu lassen würde später zu Problemen führen.

---

## Entfernungen

In der Happy Hare Firmware gibt es viele wichtige Entfernungen zu konfigurieren. Alle Entfernungs-Parameter sind in `mmu_parameters.cfg` zu finden.

### Endstop Homen

Wennn du die Filamentposition homen willst, hast du drei Optionen für den zu verwendenden Sensor:

- **mmu_gate** Verwende den gemeinsamen Gate Sensor nach dem Y-Splitter.
- **mmu_gear** verwende die jeweiligen Post-Gate-Sensoren.
- **extruder** Verwende den Extruder-Eingangssensor.

Wähle eine dieser Optionen aus und setze sie als `gate_homing_endstop`, in der `mmu_parameters.cfg`.

### Homing Entfernung 

Als nächstes konfigurierst du die maximale Strecke die Happy Hare Filament zum Homing Sensor schieben soll, bevor er "aufgibt" und die Spule als "leer" meldet. Diese Länge sollte gewöhnlich ca 150% der Distanz von der Filament-Parkposition zum Filament-Sensor entsprechen.

!!! Anmerkung
    Falls du Post-Gear Endstops (`mmu_gear`) verwendest, wird der `gate_preload_homing_max` Parameter verwendet. 

Dieser Parameter heißt `gate_homing_max`.

### Parkposition

Das ist die Position an der dein Filament warten soll, wenn es nicht verwendet wird (gemessen vom Gate-Endstop). Sie sollte ungefähr 1-2cm oberhalpt deines Y-splitters liegen.

Dieser Parameter heißt `gate_parking_distance`.

### Ausgabeentfernung

Abschließend, falls du Filament in einer Filament-Einheit mit einem anderen Filament austauschen willst, editiere `gate_final_eject_distance`. Sie sollte der Entfernung von deiner Parkposition zur Filament-Einheit entsprechen, plus einer kleinen Strecke.

## Geschwindigkeiten

Es gibt viele verschiedene Geschwindigkeiten, die du in der Happy Hare Firmware konfigurieren kannst.

Du findest sie im "speeds"-Abschnitt der `mmu_parameters.cfg` (nahe des Anfangs).

### Homing Geschwindigkeit

"Homing" ist wenn Happy Hare Filament zu deinem oben ausgewählten Filament-Endstop schiebt, um sicherzustellen, dass Filament vorhanden ist. Du kannst die verwendete Geschwindigkeit anpassen, indem du den `gear_homing_speed` Parameter anpasst.

### "First Load"-Geschwindigkeiten

Happy Hare erlaubt dir das erste Laden eines Filaments langsamer zu ausführen zu lassen um zusätzlichen Wiederstand durch die Spule auszugleichen. Um diese Geschwindigkeit anzupassen, editiere `gear_from_spool_speed`.

### Be- und Entladegeschwindikeiten

Um deine Be- und Entladegeschwindikeiten während eines Werkzeugwechsels anzupassen, editiere den `gear_from_buffer_speed` Parameter.
