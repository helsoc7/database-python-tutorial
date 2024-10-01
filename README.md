## Python Skript mit SQLite-Datenbank und NoSQL-Datenbank (TinyDB)
In diesem Abschnitt wird ein Python-Skript erstellt, das eine SQLite-Datenbank und eine NoSQL-Datenbank (TinyDB) verwendet. Die SQLite-Datenbank wird verwendet, um Daten in einer relationalen Datenbank zu speichern, während die NoSQL-Datenbank (TinyDB) verwendet wird, um Daten in einem JSON-ähnlichen Format zu speichern.
### Schritt 1: Erstellen der virtuellen Umgebung
Erstelle eine virtuelle Umgebung mit dem Namen `venv`:
```bash
python3 -m venv venv
```
Aktiviere die virtuelle Umgebung:
- Unter Windows:
```bash
venv\Scripts\activate
```
- Unter macOS und Linux:
```bash
source venv/bin/activate
```
### Schritt 2: Installation der erforderlichen Pakete
Installiere die erforderlichen Pakete mit dem folgenden Befehl:
```bash
pip install -r requirements.txt
```
### Schritt 3: Skript ausführen
Führe das Python-Skript `app-sql.py` aus, um die SQLite-Datenbank zu erstellen und Daten hinzuzufügen:
```bash
python app-sql.py
```
Führe das Python-Skript `app-nosql.py` aus, um die NoSQL-Datenbank (TinyDB) zu erstellen und Daten hinzuzufügen:
```bash
python app-nosql.py
```
### Schritt 4: Überprüfen der Datenbanken
Öffne die Datei `studenten.db` mit einem SQLite-Viewer, um die Daten in der SQLite-Datenbank anzuzeigen. Öffne die Datei `studenten.json` mit einem Texteditor, um die Daten in der NoSQL-Datenbank (TinyDB) anzuzeigen.
Was fällt dir auf?