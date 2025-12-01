from dataclasses import dataclass
from typing import Optional

@dataclass
class Pruefungsleistung:
    namePruefung: str
    note: Optional[float]

    def ist_benotet(self) -> bool:
        """Prüft, ob bereits für diese Prüfungsleistung eine Note vorliegt."""

        return self.note is not None
    
    
    def to_dict(self) -> dict:
        """Wandelt Objekt in Dictionary um, damit es als JSON gespeichert werden kann."""

        return{
            "namePruefung":self.namePruefung,
            "note": self.note,
        }
    
    @staticmethod
    def from_dict(d: dict) -> "Pruefungsleistung":
        """Erzeugt Pruefungsleistung-Instanz aus Dictionary, das aus JSON-Datei gelesen wurde."""
        
        return Pruefungsleistung(
            namePruefung=d["namePruefung"],
            note=d.get(note),
        )