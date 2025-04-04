#Test Text kombinieren mit Frage

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#print("Lade Datei von:", os.path.abspath(pfad))

from KI_Umweltplanung.models.model import OllamaAssistant
import os

def lade_kontext(pfad):
    with open(pfad, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    pfad = os.path.join("..", "data", "raw", "umwelttext.txt")
    kontext = lade_kontext(pfad)

    frage = "Welche Anforderungen ergeben sich daraus für eine Bauplanung in diesem Gebiet?"
    prompt = f"Hier ist ein Auszug aus einem Umweltbericht:\n{kontext}\n\n{frage}"

    assistent = OllamaAssistant()
    antwort = assistent.frage_stellen(prompt)
    
    print("Antwort der KI:")
    print(antwort)

if __name__ == "__main__":
    main()
