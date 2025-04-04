#Baut den vollständigen Prompt aus Kontext und Frage

def erstelle_prompt(kontext: str, frage: str) -> str:
    if kontext.strip():
        return f"""
Hier ist der Kontextauszug:
{kontext}

Frage: {frage}

Wenn du die Frage nicht vollständig beantworten kannst, gib bitte an,
welche weiteren Informationen, Unterlagen oder Daten benötigt würden,
um eine fachlich fundierte Antwort zu geben.
"""
    else:
        return f"""
Frage: {frage}

Wenn du die Frage nicht vollständig beantworten kannst, gib bitte an,
welche weiteren Informationen, Unterlagen oder Daten benötigt würden,
um eine fachlich fundierte Antwort zu geben.
"""