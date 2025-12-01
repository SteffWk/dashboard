import json
from pathlib import Path

from model.student import Student

class JSONSpeicher:
    """Speichern/Laden der Daten im JSON-Format"""
    
    def __init__(self, dateiname: str = "noten.json"):
        self.basisordner = Path(__file__).resolve().parent
        self.dateipfad = self.basisordner / dateiname
        self.encoding = "utf-8"

    def speichern(self, daten: dict):
        """Speichert Dictionary als JSON-Datei."""

        with self.dateipfad.open("w", encoding=self.encoding) as f:
            json.dump(daten, f, ensure_ascii=False, indent=2)

    def laden(self) -> dict:
        """Lädt JSON-Datei und gibt Inhalt als Dictionary zurück."""

        if not self.dateipfad.exists():
            return {}
        with self.dateipfad.open("r", encoding=self.encoding) as f:
            return json.load(f)
        
    def save_student(self, student: Student):
        """Speichert aktuellen Zustand des Studenten."""

        self.speichern(student.to_dict())

    def load_student(self, cls=Student):
        """Lädt JSON-Datei und erzeugt daraus Student-Objekt."""
        
        daten = self.laden()
        if not daten:
            return None
        return cls.from_dict(daten)