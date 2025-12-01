from dataclasses import dataclass, field
from typing import List, Optional

from .modul import Modul


@dataclass
class Semester:
    semesterNr: int
    module: List[Modul] = field(default_factory=list)

    def get_modul(self, modulName: str) -> Optional[Modul]:
        for m in self.module:
            if m.modulName == modulName:
                return m
        return None
        
    def berechne_semesterschnitt(self) -> Optional[float]:
        """"ECTS-gewichteter Schnitt über alle Module mit Endnote"""
        paare = [(m.endnote(), m.ects) for m in self.module if m.endnote() is not None]
        if not paare:
            return None
        num = sum(n * e for n, e in paare)
        den = sum(e for _, e in paare)
        if den == 0:
            return None
        return round(num / den, 2)
    
    def to_dict(self) -> dict:
        return {
            "semesterNr": self.semesterNr,
            "module": [m.to_dict() for m in self.module],
        }
    
    @staticmethod
    def from_dict(d:dict) -> "Semester":
        return Semester(
            semesterNr=d["semesterNr"],
            module=[Modul.from_dict(m) for m in d.get("module", [])],
        )