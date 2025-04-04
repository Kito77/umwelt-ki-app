# Analysiert die KI-Antwort nach Hinweisen auf fehlende Informationen

def erkenne_fehlende_infos(antwort: str) -> list:
    suchworte = [
        "fehlt", "benötigt", "nicht vorhanden", "nicht verfügbar",
        "weiterführende Unterlagen", "zusätzliche Informationen",
        "unvollständig", "nicht bekannt"
    ]
    return [wort for wort in suchworte if wort in antwort.lower()]