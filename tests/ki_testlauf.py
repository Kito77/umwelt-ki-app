#damit die Modulansprache funktioniert egal wo das Skript startet
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from KI_Umweltplanung.models.model import OllamaAssistant

def main():
    assistent = OllamaAssistant()
    frage = "Welche gesetzlichen Anforderungen gelten für Eingriffe in FFH-Gebiete?"
    antwort = assistent.frage_stellen(frage)
    print("Antwort der KI:")
    print(antwort)

if __name__ == "__main__":
    main()
