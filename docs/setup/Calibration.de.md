---
comments: true
icon: fontawesome/solid/ruler-horizontal
---

# Kalibrierung

Folge diesem Guide um dein 3MS zu kalibrieren.

!!! Info "Original Documentation"
    Dieser Guide ist eine vereinfachte Version der [offiziellen Happy Hare Dokumentation](https://github.com/moggieuk/Happy-Hare/wiki/MMU-Calibration). Ich empfehle dir sehr sie zu lesen weil sie nützliche Informationen enthält und tiefer ins Detail geht, falls du Probleme mit dem Kalibrieren hast.

## Filament Sensoren prüfen

Vor dem Kalibrieren ist es wichtig sicherzustellen, dass alle Filamentsensoren ordnungsgemäß funktionieren. 

In der Klipper-Konsole ausführen:

```
QUERY_ENDSTOPS
```

und überprüfe die Ausgabe. Für jeden Endstop bedeutet `open`, dass kein Filament detektiert wird und `TRIGGERED` bedeutet, dass Filament detektiert wurde. Führe das Command mehrfach aus, jeweils vor und nach dem Einführen von Filament um zu überprüfen ob die Sensoren ordnungsgemäß funktionieren.

## Gear Steppers

Zuerst musst du deine Extruder kalibrieren (Filament-Einheiten). Ziel dieser Kalibrierung ist sicherzustellen, dass das Filament nur so weit ausgegeben wird wie beabsichtigt.

Entferne dazu den PTFE-Schlauch von jeder der Filament-Einheiten.

Wiederhole die folgenden Schritte für jede Filament-Einheit (Gate)
    
1. Lade manuell Filament, bis es minimal aus dem Ende der Filament-Einheit herausschaut.
2. Schneide die Spitze des Filaments bündig mit der Schlauchkupplung ab (Seitenschneider eignen sich dafür gut)
3. Führe die folgenden Commands in der Klipper-Konsole aus:

    ```
    MMU_SELECT GATE=n
    MMU_TEST_MOVE MOVE=100
    ```

    wo `n` der Nummer des zu kalibrierenden Gates entspricht (bei Null beginnend).

4. Das Filament sollte sich vorwärts bewegen. Falls es sich rückwärts bewegt, [invertiere den Extruder-Stepper](#Einen MMU-Stepper invertieren). Messe die Distanz, um die sich das FIlament aus dem Extruder herausbewegt hat. Führe das folgende Command in der Klipper-Konsole aus:

    ```
    MMU_CALIBRATE_GEAR MEASURED=n
    ```

    wo  `n` der gemessenen Distanz entspricht.
  
5. Wiederhole Schritt **3**. Das Filament sollte exakt um `100mm` herausgefahren werden.

## Encoder (falls installiert)

Falls du einen Encoder, wie den BTT SFS (Smart Filament Sensor) benutzt, musst du ihn kalibrieren.

1. Lade dein Filament manuell an die Park-Position am Anfang des Y-Splitters. 
2. In der Klipper-Konsole ausführen:

    ```
    MMU_CALIBRATE_ENCODER
    ```

---
  
## Einen MMU-Stepper invertieren

Falls du feststellst, dass einer deiner MMU-Stepper Filament in die falsche Richtung schiebt, musst du ihn invertieren. Dafür gibt es zwei Wege:

- Manuell die Leitungen im Stecker des Stepper-Kabels vertauschen
- In der Software invertieren

Um einen MMU-Stepper in der Software zu invertieren, öffne die Datei `mmu_hardware.cfg` und invertiere den `dir_pin` für den jeweiligen Stepper.

Beispielsweise, falls `T1` sich rückwärts bewegt:

=== "Vorher"
    ```cfg title="mmu_hardware.cfg"
    [stepper_mmu_gear_1]
    ...
    dir_pin: mmu: PC5
    ```
=== "Nachher"
    ```cfg title="mmu_hardware.cfg"
    [stepper_mmu_gear_1]
    ...
    dir_pin: !mmu: PC5 # <-- Note the ! in front of mmu
    ```

!!! Tipp
    Falls der Pin schon ein `!` dort stehen hat, entferne es um ihn zu invertieren.

Starte Klipper neu.