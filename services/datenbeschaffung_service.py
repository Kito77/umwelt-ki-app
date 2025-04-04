# services/datenbeschaffung_service.py
"""
Dieses Modul prüft, ob Daten automatisch beschafft werden können, und
erzeugt bei Bedarf E-Mail-Anfragen.
"""

import json
import os
import requests

# JSON-Datei laden
def lade_datenquellen(pfad: str = "data/datenquellen.json") -> dict:
    """Lädt die gespeicherten Datenquelleninformationen aus JSON."""
    if not os.path.exists(pfad):
        return {}
    with open(pfad, encoding="utf-8") as f:
        return json.load(f)

# Automatisierbarkeit prüfen
def ist_automatisch_abrufbar(datenpunkt: str) -> bool:
    quellen = lade_datenquellen()
    return quellen.get(datenpunkt, {}).get("automatisierbar", False)

# Anfrage möglich prüfen
def kann_angeschrieben_werden(datenpunkt: str) -> bool:
    quellen = lade_datenquellen()
    return quellen.get(datenpunkt, {}).get("anfrage_möglich", False)

# Anfrage-E-Mail vorbereiten
def generiere_emailtext(datenpunkt: str) -> str:
    quellen = lade_datenquellen()
    eintrag = quellen.get(datenpunkt)
    if eintrag and eintrag.get("vorlage"):
        return eintrag["vorlage"]
    return f"Für '{datenpunkt}' liegt keine Vorlage vor."

def hole_daten_automatisch(datenpunkt: str) -> str:
    """
    Holt die Daten aus der Quelle, falls automatischer Abruf möglich ist.
    Gibt den Anfang des Inhalts als Textvorschau zurück.
    """
    quellen = lade_datenquellen()
    eintrag = quellen.get(datenpunkt)

    if not eintrag or not eintrag.get("automatisierbar"):
        return f"❌ '{datenpunkt}' ist nicht automatisiert abrufbar."

    url = eintrag.get("quelle")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        inhalt = response.text

        # Vorschau: nur erste 500 Zeichen
        return f"✅ Daten erfolgreich geladen (Auszug):\n\n{inhalt[:500]}"
    except Exception as e:
        return f"⚠️ Fehler beim Abruf von '{datenpunkt}': {e}"