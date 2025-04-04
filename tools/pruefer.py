import requests
import pandas as pd
import os
import json
import requests

PFAD = os.path.join(os.path.dirname(__file__), "..", "data", "datenquellen.json")
PFAD = os.path.abspath(PFAD)

def lade_daten():
    if not os.path.exists(PFAD):
        return {}
    with open(PFAD, encoding="utf-8") as f:
        return json.load(f)

def pruefe_datenquellen():
    daten = lade_daten()
    fehlerliste = []

    for key, eintrag in daten.items():
        # Pflichtfelder
        pflichtfelder = ["beschreibung", "region", "thema", "quelle", "aktualisiert_am"]
        for feld in pflichtfelder:
            if feld not in eintrag or not eintrag[feld]:
                fehlerliste.append({
                    "Schlüssel": key,
                    "Typ": "Fehlendes Feld",
                    "Detail": f"{feld} fehlt"
                })

        # Wenn automatisierbar → URL testen
        if eintrag.get("automatisierbar") and "quelle" in eintrag:
            try:
                response = requests.get(eintrag["quelle"], timeout=5)
                if response.status_code != 200:
                    fehlerliste.append({
                        "Schlüssel": key,
                        "Typ": "URL nicht erreichbar",
                        "Detail": f"Status {response.status_code}"
                    })
            except Exception as e:
                fehlerliste.append({
                    "Schlüssel": key,
                    "Typ": "URL-Fehler",
                    "Detail": str(e)
                })

        # Typprüfung Datum
        if not isinstance(eintrag.get("aktualisiert_am"), str):
            fehlerliste.append({
                "Schlüssel": key,
                "Typ": "Falscher Typ",
                "Detail": "aktualisiert_am ist kein String"
            })

    return fehlerliste
