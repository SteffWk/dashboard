class View:

    @staticmethod
    def headline(text: str):
        print("\n" + "=" * 50)
        print(text)
        print("=" * 50)

    @staticmethod
    def zeige_semester(student):
        View.headline("Semesterübersicht")

        if not student.semester:
            print("Keine Semester gefunden.")
            return
        
        for sem in student.semester:
            print(f"\nSemester {sem.semesterNr}")

            if not sem.module:
                print("  (keine Module)")
                continue
            for m in sem.module:
                print(f"  {m.modulName} (ECTS {m.ects}) -> Endnote: {m.endnote()}")

    
    @staticmethod
    def zeige_module(sem):
        """Alle Module eines best. Semesters ausgeben"""
        View.headline(f"Module in Semester {sem.semesterNr}")

        if not sem.module:
            end = m.endnote()
            print(f"{m.modulName} (ECTS: {m.ects}) Endnote: {end}")

    @staticmethod
    def zeige_semesterschnitt(sem):
        View.headline(f"Semester {sem.semesterNr}: Schnitt")
        print("Schnitt", sem.berechne_semesterschnitt())

    def ampel(diff):
        if diff is None:
            return
        
        if diff <=0:
            return "GRÜN"
        elif diff <= 0.5:
            return "GELB"
        else:
            return "ROT"    

    @staticmethod
    def zeige_gesamtschnitt(student, schnitt: float, diff: float | None):
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

        #Ampel ausgeben
        print()
        print(View.ampel(diff))

    @staticmethod
    def info(msg: str):
        print(msg)

    @staticmethod
    def fehler(msg: str):
        print("Fehler", msg)