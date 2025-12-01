from dataclasses import dataclass, field
from typing import List, Optional

from .pruefungsleistung import Pruefungsleistung


@dataclass
class Modul:
    modulName: str
    ects: int
    leistungen: List[Pruefungsleistung] = field(default_factory=list)

    def endnote(self) -> Optional[float]:
        """Durchschnitt der vorhandenen Prüfungsleistungen"""

        benotete = [l.note for l in self.leistungen if l.ist_benotet()]
        if not benotete:
            return None
        return round(sum(benotete) / len(benotete), 2)
    
    def to_dict(self) -> dict:
        """Wandelt Modul in Dictionary für die JSON-Speicherung um."""

        return {
            "modulName": self.modulName,
            "ects": self.ects,
            "leistungen": [l.to_dict() for l in self.leistungen],
        }
    
    @staticmethod
    def from_dict(d: dict) -> "Modul":
        """Erzeugt Modul-Objekt aus einem Dictionary"""

        return Modul(
            modulName=d["modulName"],
            ects=d["ects"],
            leistungen=[Pruefungsleistung.from_dict(x) for x in d.get("leistungen", [])],
        )