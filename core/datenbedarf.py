"""
datenbedarf.py – Modul zur Erkennung von typischen Datenbedarfen in Umweltplanungsverfahren.

Dieses Modul wird verwendet, um die Antwort einer KI (z. B. Ollama) auf bestimmte Begriffe
zu analysieren, die auf fehlende Informationen oder Dokumente hinweisen.

Es gibt eine Liste zurück, z. B.: ["artenschutz", "boden", "schutzgebiete"]
Diese Liste kann verwendet werden, um Hinweise oder Download-Links in der App anzuzeigen.

Autor: Kito 
"""

def analysiere_datenbedarf(antwort: str) -> list:
    """
    Analysiert einen Antworttext und erkennt, welche Datenarten wahrscheinlich fehlen.

    Parameter:
    - antwort (str): Die Antwort der KI auf eine umweltplanerische Frage

    Rückgabe:
    - list: Liste von Schlüsseln wie "artenschutz", "boden", "schutzgebiete", etc.
    """
    kategorien = {
        "artenschutz": ["artenschutz", "tiere", "fauna", "flora", "artenliste", "vögel", "fledermäuse"],
        "boden": ["altlasten", "boden", "kontamination", "schadstoff"],
        "wasser": ["grundwasser", "gewässer", "abwassereinleitung", "wasserhaushalt"],
        "schutzgebiete": ["ffh", "schutzgebiet", "natura", "naturschutz", "lsg", "nsg"],
        "formulare": ["anzeige", "formular", "meldung", "unterlagen", "einreichen"]
    }

    fehlende_daten = []
    antwort_lower = antwort.lower()

    for kategorie, begriffe in kategorien.items():
        if any(begriff in antwort_lower for begriff in begriffe):
            fehlende_daten.append(kategorie)

    return fehlende_daten
