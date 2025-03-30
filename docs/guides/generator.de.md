# Config-Generator

Folge diesem Guide um eine Custom-Config für dein 3MS zu generieren.

## Grundlagen-Config

Als erstes musst du eine Klipper-Config für dein Mainboard finden. Der beste Ort um diese zu finden sind die [official Klipper sample configurations](https://github.com/Klipper3d/klipper/tree/master/config).

In diesem Beispiel wird ein BTT SKR Mini E3 V3 verwendet. Eine Grundlagen-Config ist [hier](https://github.com/Klipper3d/klipper/blob/master/config/generic-bigtreetech-skr-mini-e3-v3.0.cfg) verfügbar.

### Rohdatei

Jetzt hast du die Config, aber sie ist keine Rohdatei, sondern eine volle Website. Um Fortzufahren brauchst du die Rohdatei. Um sie zu erhalten musst du auf den **"Raw"** Button in Ecke Oben-Rechts klicken.

![](generator01.png)

Jetzt wirst du auf eine Seite mit der Rohdatei weitergeleitet. Kopiere die URL aus der Addresszeile.

![](generator02.png)

## [Generieren der Config - Web](https://forked-lined-hour.anvil.app/)

## ODER

## Generieren der Config - Shell

Jetzt wo du die URL der Rohdatei hast, musst du das Generatorskript installieren.

### Installation

1. Klone das 3MS repository:

    ```sh
    cd ~
    git clone https://github.com/3DCoded/3MS
    ```

2. Stelle sicher dass Python 3 installiert ist (nicht Python 2).
3. Installiere `requests`

    ```sh
    pip3 install requests
    ```

### Das Skript ausführen

Starte als erstes das Skript:

```sh
cd ~/3MS
python3 generator.py
```

Jetzt werden dir verschiedene Optionen angezeigt.

#### Config URL

Füge die vorhin erhaltene URL ein.

!!! Tipp "Lokale Datei verwenden"
    Du kannst auch eine lokale Config-Datei verwenden, indem du den `--file` Parameter übergibst.

    ```sh
    python3 generator.py --file
    ```

![](generator03.png)

#### Ausgewählte Stepper

Das Skript wird dir nun alle Stepper Definitionen, die in der Config gefunden wurden, jeweils mit einer Nummer, auflisten. Gebe die gewünschten Stepper, mit Leerzeichen getrennt, ein.

![](generator04.png)

#### TMC Treiber


Für jeden von dir ausgewählten Stepper wird das Skript dich fragen, welchen TMC Treiber du verwenden möchtest. Für den SKR Mini E3 V3 gibt es nur eine Option: TMC2209.

!!! Tipp "Keine TMC Treiber?"
    Wenn du keine TMC-Treiber in deiner Config verwenden willst, übergebe den Parameter `--no-tmc`:
	
    ```sh
    python3 generator.py --no-tmc
    ```

![](generator05.png)

#### MCU Name

Schließlich fragt das Skript dich nach dem Namen der MCU, die dein 3MS steuert. Folge der Namenskonvention, die in der Prompt angegeben ist.

![](generator06.png)

---

Deine Konfiguration wird nun in `~/3MS/mmu.cfg` und `~/3MS/mmu_hardware.cfg` verfügbar sein.