from dataclasses import dataclass, field
from typing import List, Optional

from .semester import Semester


@dataclass
class Student:
    """Student mit Zielnotenschnitt und Semesterdaten"""

    zielNotenschnitt: float
    semester: List[Semester] = field(default_factory=list)

    def get_semester(self, semesterNr: int) -> Optional[Semester]:
        """Sucht in Semesterliste nach dem angegebenen Semester."""

        for s in self.semester:
            if s.semesterNr == semesterNr:
                return s
        return None
        
    def berechne_gesamt_schnitt(self) -> Optional[float]:
        """Berechnet Gesamtschnitt aller Module mit Endnote"""

        paare = []
        for sem in self.semester:
            for m in sem.module:
                n = m.endnote()
                if n is not None:
                    paare.append((n, m.ects))
                    
        if not paare:
            return None
        
        num = sum(n * e for n, e in paare)
        den = sum(e for _, e in paare)

        return round(num / den, 2)
    
    def berechne_diff_ziel(self) -> Optional[float]:
        """Berechnet die Differenz zum Zielnotenschnitt"""
        
        g = self.berechne_gesamt_schnitt()
        if g is None:
            return None
        return round(g - self.zielNotenschnitt, 2)
    
    def to_dict(self) -> dict:
        """Wandelt Student in Dictionary um."""

        return{
            "zielNotenschnitt": self.zielNotenschnitt,
            "semester": [s.to_dict() for s in self.semester],
        }
    
    @staticmethod
    def from_dict(d: dict) -> "Student":
        """Erzeugt Student aus einem Dictionary, das aus JSON geladen wurde."""
        ziel = d.get("zielNotenschnitt", 2.0)
        st = Student(ziel)
        st.semester = [Semester.from_dict(s) for s in d.get("semester", [])]
        return st