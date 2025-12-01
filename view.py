class View:
    """Darstellungsschicht für Kommandozeile."""

    @staticmethod
    def headline(text: str):
        """Gibt Überschrift aus."""

        print("\n" + "=" * 50)
        print(text)
        print("=" * 50)
    
    @staticmethod
    def zeige_module(sem):
        """Alle Module eines best. Semesters ausgeben"""

        View.headline(f"Module in Semester {sem.semesterNr}")

        if not sem.module:
            print("Keine Module vorhanden.")
            return
        
        for m in sem.module:
            end = m.endnote()
            print(f"{m.modulName} (ECTS: {m.ects}) Endnote: {end}")

    @staticmethod
    def zeige_semesterschnitt(sem):
        """Zeigt Notenschnitt eines Semesters."""

        View.headline(f"Semester {sem.semesterNr}: Schnitt")
        print("Schnitt", sem.berechne_semesterschnitt())

    @staticmethod
    def ampel(diff):
        """Erzeugt textuelle Ampelbewertung anhand Differenz zum Schnittziel."""
        if diff is None:
            return "Keine ausreichenden Daten für Bewertung!"
        
        if diff <=0:
            return "GRÜN"
        elif diff <= 0.5:
            return "GELB"
        else:
            return "ROT"    

    @staticmethod
    def zeige_gesamtschnitt(student, schnitt: float, diff: float | None):
        """Zeigt Gesamtnotenschnitt, Differenz zum Ziel und Ampelbewertung an."""

        View.headline("Gesamtschnitt")

        gesamt = student.berechne_gesamt_schnitt()
        diff = student.berechne_diff_ziel()

        if gesamt is None:
            print("Keine benoteten Module vorhanden.")
            return
        
        print(f"Zielnotenschnitt:       {student.zielNotenschnitt:.2f}")
        print(f"Aktueller Gesamtschnitt:{gesamt:.2f}")

        if diff is not None:
            vorzeichen = "+" if diff > 0 else ""
            print(f"Abweichung vom Ziel: {vorzeichen}{diff:.2f}")
        else:
            print("Abweichung vom Ziel nicht berechenbar.")

        print()
        print(View.ampel(diff))

    @staticmethod
    def info(msg: str):
        """Gibt Info-Nachricht aus."""

        print(msg)

    @staticmethod
    def fehler(msg: str):
        """Gibt Fehlermeldung aus."""

        print("Fehler", msg)