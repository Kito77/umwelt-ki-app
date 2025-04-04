"""
anfrage_manager.py – Liest aus der JSON-Datei anfragequellen.json
und gibt passende Texte/Links zur Datenanforderung zurück.
"""

import json
import os

# Pfad zur JSON-Datei (dynamisch für WSL, Linux, Windows, etc.)
PFAD = os.path.join("data", "metadata", "anfragequellen.json")

def lade_anfragequellen():
    """Liest die JSON-Datei mit allen bekannten Datenanforderungen ein."""
    with open(PFAD, encoding="utf-8") as f:
        return json.load(f)

def generiere_anfragevorschlaege(datenbedarf_liste, quellen_dict):
    """Gibt eine Liste mit klaren Vorschlägen zurück."""
    ausgabe = []
    for punkt in datenbedarf_liste:
        eintrag = quellen_dict.get(punkt)
        if eintrag:
            text = (f"📌 **{eintrag['bezeichnung']}** – {eintrag['beschreibung']}\n"
            f"🔗 [{eintrag['zuständig']}]({eintrag['link']})")

            ausgabe.append(text)
    return ausgabe
