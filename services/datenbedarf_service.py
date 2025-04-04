# services/datenbedarf_service.py
"""
Dieses Modul analysiert die KI-Antwort auf fehlende Daten oder Informationen
und generiert darauf basierend passende Vorschläge.
"""

from core.datenbedarf import analysiere_datenbedarf
from core.vorschlaege import generiere_vorschlaege

def datenbedarf_ermitteln(antwort: str) -> tuple[list[str], dict]:
    """
    Führt eine Analyse des Datenbedarfs durch und liefert eine Liste erkannter Punkte
    sowie zugehörige Vorschläge.

    Args:
        antwort (str): Die Antwort der KI

    Returns:
        tuple: (datenbedarf_liste, vorschlaege_dict)
    """
    datenbedarf_liste = analysiere_datenbedarf(antwort)
    vorschlaege_dict = generiere_vorschlaege(datenbedarf_liste)
    return datenbedarf_liste, vorschlaege_dict
