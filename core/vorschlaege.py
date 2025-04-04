"""
vorschlaege.py – Modul zur Erzeugung einfacher Textbausteine und Links,
die Nutzer*innen helfen, fehlende Daten oder Unterlagen zu beschaffen.
"""

def generiere_vorschlaege(datenbedarf_liste: list) -> dict:
    """Gibt für jeden erkannten Bedarf eine kurze Empfehlung oder einen Link zurück."""
    vorschlaege = {
        "artenschutz": "➡️ Artenschutzkartierung einholen (z. B. durch Landschaftsplanungsbüros oder zust. Behörde)",
        "boden": "📄 Altlasten-Auskunft beim LfU Brandenburg: https://lfu.brandenburg.de/",
        "wasser": "💧 Wasserwirtschaftliche Daten über zuständiges Wasseramt oder Umweltamt einholen",
        "schutzgebiete": "📍 Prüfen: Liegt die Fläche im Natura 2000 Gebiet? ➤ [BfN Schutzgebiete](https://www.bfn.de/karten)",
        "formulare": "📑 Reiche ggf. ein Anzeigeformular beim Bauamt oder Umweltamt ein"
    }

    return {key: vorschlaege.get(key, "Keine Empfehlung vorhanden") for key in datenbedarf_liste}
