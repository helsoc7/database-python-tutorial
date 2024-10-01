import sqlite3

# Verbindung zur SQLite-Datenbank herstellen (Datei wird erstellt, falls nicht vorhanden)
conn = sqlite3.connect('studenten.db')

# Cursor-Objekt zum Ausführen von SQL-Befehlen
cursor = conn.cursor()

# Tabelle erstellen (falls nicht existiert)
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    course TEXT NOT NULL
)
''')

# Daten in die Tabelle einfügen
def student_hinzufuegen(name, age, course):
    cursor.execute('''
    INSERT INTO students (name, age, course) 
    VALUES (?, ?, ?)
    ''', (name, age, course))
    conn.commit()
    print(f'Student {name} hinzugefügt.')

# Daten abrufen
def studenten_anzeigen():
    cursor.execute('SELECT * FROM students')
    studenten = cursor.fetchall()
    print("Alle Studenten:")
    for student in studenten:
        print(student)

# Beispielaufrufe
student_hinzufuegen("Max Mustermann", 21, "Informatik")
student_hinzufuegen("Anna Schmidt", 22, "Mathematik")
student_hinzufuegen("Lisa Müller", 20, "Physik")

studenten_anzeigen()

# Verbindung schließen
conn.close()
