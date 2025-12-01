from jsonspeicher import JSONSpeicher
from model.student import Student
from cli import CLI

def main():
    """
    Versucht bestehende Daten aus noten.json zu laden, sonst wird neuer Student erzeugt.
    Startet dann CLI-Hauptschleife.
    """
    
    speicher = JSONSpeicher("noten.json")
    student = speicher.load_student(Student)

    if student is None:
        print("Keine Daten gefunden - Neue Datei wird angelegt.")
        try:
            ziel = float(input("Zielnotenschnitt: ").replace(",", "."))
        except ValueError:
            ziel = 2.0
        student = Student(ziel)
    else:
        print("(Daten wurde aus noten.json geladen.)")

    cli = CLI(student, speicher)
    cli.run()


if __name__ == "__main__":
    main()