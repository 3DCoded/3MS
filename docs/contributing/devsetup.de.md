---
icon: octicons/terminal-24
comments: true
---

# Development Setup

Folge dieser Anleitung, um dein System für die Entwicklung mit dem 3MS einzurichten.

## Veränderungen der Dokumentation

1. Erstelle eine Fork des 3MS Repositories
2. Erstelle einen neuen Branch für deine Anfrage (aus dem `docs` Branch)1. Install [Python](https://www.python.org/).
3. Installiere [Pipenv](https://pipenv.pypa.io/en/latest/).
4. Navigiere in deinem Terminal zum Ordner 3MS und führe aus:
    ```sh
    pipenv install
    pipenv shell
    ```
5. Entwickle die Änderungen im neuen Branch und benutze den folgenden Befehl, um die Dokumentation lokal auszuführen:
    ```sh
    mkdocs serve
    ```