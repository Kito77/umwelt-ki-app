"""
datenanfrage.py – Automatisierte Textbausteine zur Anforderung fehlender Daten

Dieses Modul nimmt eine Liste erkannter Datenbedarfe (z. B. 'artenschutz', 'boden')
und gibt zu jedem Punkt einen konkreten, verständlichen Textbaustein zurück,
der in Berichten oder E-Mails zur Datenanforderung verwendet werden kann.

Beispiel:
- 'Bitte reichen Sie eine Artenschutzkartierung durch ein qualifiziertes Fachbüro ein.'
"""

def generiere_anforderungstexte(datenbedarf_liste: list) -> list:
    """Erzeugt Textvorschläge zur Datenanforderung für jeden Eintrag in der Liste."""

    texte = {
        "artenschutz": "Bitte reichen Sie eine aktuelle Artenschutzkartierung ein, idealerweise durch ein anerkanntes Fachbüro.",
        "boden": "Bitte fügen Sie eine Altlastenuntersuchung oder Bodengutachten bei (z. B. durch das LfU Brandenburg).",
        "wasser": "Bitte stellen Sie wasserwirtschaftliche Angaben bereit, insbesondere zu Grundwasser und Oberflächengewässern.",
        "schutzgebiete": "Bitte klären Sie, ob das Plangebiet innerhalb eines Schutzgebiets liegt (FFH, LSG, NSG) und fügen Sie ggf. eine Verträglichkeitsprüfung bei.",
        "formulare": "Bitte reichen Sie die notwendigen Formulare oder Anzeigen gemäß § XY ein (z. B. Bauanzeige, Umweltanzeige)."
    }

    rückgabe = []
    for punkt in datenbedarf_liste:
        if punkt in texte:
            rückgabe.append(texte[punkt])
        else:
            rückgabe.append(f"Für den Punkt '{punkt}' liegt kein automatischer Text vor.")

    return rückgabe
