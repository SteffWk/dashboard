from model.semester import Semester
from model.modul import Modul
from model.pruefungsleistung import Pruefungsleistung
from view import View

class CLI:
    """Kommandozeilen-Steuerung"""

    def __init__(self, student, speicher):
        """Initialisiert CLI mit Student-Objekt und JSONSpeicher."""

        self.student = student
        self.speicher = speicher

    def run(self):
        """Hauptschleife des Programms. Zeigt Menü an und reagiert auf Benutzereingaben."""

        while True:
            print("\n=== Notenübersicht Cyber Security ===")
            print("")
            print("1) Semester anzeigen")
            print("2) Semester hinzufügen")
            print("3) Modul hinzufügen")
            print("4) Prüfungsleistung hinzufügen")
            print("5) Zielnotenschnitt setzen")
            print("6) Semester-Durchschnitt")
            print("7) Gesamt-Durchschnitt")
            print("8) Speichern")
            print("9) Module eines Semesters anzeigen")
            print("0) Beenden")

            auswahl = input("Auswahl: ").strip()

            if auswahl == "1":
                View.zeige_semester(self.student)
            elif auswahl == "2":
                self.semester_hinzufuegen()
            elif auswahl == "3":
                self.modul_hinzufuegen()
            elif auswahl == "4":
                self.pruefungsleistung_hinzufuegen()
            elif auswahl == "5":
                self.ziel_setzen()
            elif auswahl == "6":
                self.semesterschnitt()
            elif auswahl == "7":
                self.gesamtschnitt()
            elif auswahl == "8":
                self.speichern()
            elif auswahl == "9":
                self.module_anzeigen()
            elif auswahl == "0":
                print("Programm beendet.")
                break
            else:
                View.fehler("Ungültige Eingabe!")
                return
            
    def semester_hinzufuegen(self):
        """Fragt Benutzer nach Semester-Nummer und legt ein neues Semester an, sofern Nummer nicht vergeben ist."""

        try:
            semesterNr = int(input("Semester-Nummer: "))
        except ValueError:
            View.fehler("Bitte eine Zahl eingeben!")
            return
        
        if self.student.get_semester(semesterNr):
            View.fehler("Semester existiert bereits!")
            return
        
        sem = Semester(semesterNr)
        self.student.semester.append(sem)
        View.info("Semester hinzugefügt.")

    def modul_hinzufuegen(self):
        """Legt neues Modul in bestehendem Semester an."""

        try:
            semesterNr = int(input("Semester-Nummer: "))
        except ValueError:
            View.fehler("Nur Zahlen erlaubt")
            return
        
        sem = self.student.get_semester(semesterNr)
        if not sem:
            View.fehler("Semester existiert nicht.")
            return
        
        modulName = input("Modulname: ")
        try:
            ects = int(input("ECTS: "))
        except ValueError:
            View.fehler("Bitte Zahl für ECTS eingeben.")
            return
        
        sem.module.append(Modul(modulName, ects))
        View.info("Modul hinzugefügt")

    def pruefungsleistung_hinzufuegen(self):
        """Fügt bestehendem Modul eine Prüfungsleistung hinu."""

        try:
            semesterNr = int(input("Semester: "))
        except ValueError:
            View.fehler("Bitte Zahl eingeben!")
            return
        
        sem = self.student.get_semester(semesterNr)
        if not sem:
            View.fehler("Semester existiert nicht")
            return
        
        modulName = input("Modulname: ")
        modul = sem.get_modul(modulName)
        if not modul:
            View.fehler("Modul nicht gefunden.")
            return
        
        pname = input("Name der Prüfungsleistung: ")
        try:
            note = float(input("Note: ").replace(",", "."))
        except ValueError:
            View.fehler("Ungültige Eingabe.")
            return
        
        modul.leistungen.append(Pruefungsleistung(pname, note))
        View.info("Prüfungsleistung hinzugefügt.")

    def ziel_setzen(self):
        """Ändert Zielnotenschnitt des Studenten."""

        try:
            wert = float(input("Zielnotenschnitt: ").replace(",", "."))
        except ValueError:
            View.fehler("Ungültige Eingabe.")
            return
        
        self.student.zielNotenschnitt = wert
        View.info("Ziel aktualisiert.")

    def semesterschnitt(self):
        """Zeigt Notenschnitt eines ausgewählten Semesters an."""

        try:
            semesterNr = int(input("Semester: "))
        except ValueError:
            View.fehler("Bitte Zahl eingeben!")
            return
        
        sem = self.student.get_semester(semesterNr)
        if not sem:
            View.fehler("Semester nicht gefunden.")
            return
        View.zeige_semesterschnitt(sem)

    def gesamtschnitt(self):
        """Zeigt den Gesamtschnitt + Ampelbewertung an."""

        schnitt = self.student.berechne_gesamt_schnitt()
        if schnitt is None:
            View.info("Es sind noch keine benoteten Module vorhanden.")
            return
        
        diff = self.student.berechne_diff_ziel()
        View.zeige_gesamtschnitt(self.student, schnitt, diff)

    def module_anzeigen(self):
        """Zeigt alle Module eines bestimmten Semesters an."""

        try:
            semesterNr = int(input("Semester-Nummer: "))
        except ValueError:
            View.fehler("Bitte eine Zahl eingeben!")
            return
        
        sem = self.student.get_semester(semesterNr)
        if not sem:
            View.fehler("Semester nicht gefunden.")
            return
        
        View.zeige_module(sem)

    def speichern(self):
        """Speichert den aktuellen Zustand in die JSON-Datei."""
        
        self.speicher.save_student(self.student)
        View.info("Daten gespeichert.")
