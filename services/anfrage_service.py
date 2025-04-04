# services/anfrage_service.py
"""
Dieses Modul ist zuständig für das Laden möglicher Anfragequellen
und die Generierung von Textvorschlägen zur Informationsanforderung.
"""

from core.anfrage_manager import lade_anfragequellen, generiere_anfragevorschlaege

def erstelle_anfragevorschlaege(datenbedarf_liste: list[str]) -> list[str]:
    """
    Erzeugt textuelle Vorschläge zur Anforderung fehlender Informationen.

    Args:
        datenbedarf_liste (list): Liste erkannter fehlender Punkte

    Returns:
        list: Liste von Vorschlag-Strings
    """
    quellen = lade_anfragequellen()
    vorschlaege = generiere_anfragevorschlaege(datenbedarf_liste, quellen)
    return vorschlaege
