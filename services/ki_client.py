# services/ki_client.py
from KI_Umweltplanung.models.model import OllamaAssistant

def frage_an_ki(prompt: str) -> str:
    """Frage die KI mit dem gegebenen Prompt und gib die Antwort zurück."""
    assistent = OllamaAssistant()
    return assistent.frage_stellen(prompt)
