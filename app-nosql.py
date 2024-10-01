from tinydb import TinyDB, Query

# Verbindung zur TinyDB herstellen (Daten werden in einer JSON-Datei gespeichert)
db = TinyDB('students.json')

# Studenten-Collection in der TinyDB
students_table = db.table('students')

# Student hinzufügen
def student_hinzufuegen(name, age, course):
    student = {
        'name': name,
        'age': age,
        'course': course
    }
    students_table.insert(student)
    print(f'Student {name} hinzugefügt.')

# Alle Studenten anzeigen
def studenten_anzeigen():
    students = students_table.all()
    print("Alle Studenten:")
    for student in students:
        print(student)

# Beispielaufrufe
student_hinzufuegen("Max Mustermann", 21, "Informatik")
student_hinzufuegen("Anna Schmidt", 22, "Mathematik")
student_hinzufuegen("Lisa Müller", 20, "Physik")

studenten_anzeigen()

# Optional: Verbindung schließen
db.close()
