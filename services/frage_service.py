#services/frage_services.py
"""
Dieses Modul verwaltet die Kommunikation mit der KI:
- Erstellung des Prompts
- Senden der Frage
- Rückgabe der KI-Antwort
"""

from core.prompt_builder import erstelle_prompt
from KI_Umweltplanung.models.model import OllamaAssistant

def stelle_ki_frage(kontext: str, frage: str) -> str:
    """
    Baut einen Prompt mit Kontext und Frage, sendet ihn an die KI,
    gibt die Antwort zurück.
    """
    prompt = erstelle_prompt(kontext, frage)
    assistent = OllamaAssistant()
    antwort = assistent.frage_stellen(prompt)
    return antwort