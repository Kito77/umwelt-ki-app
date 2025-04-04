# Umwelt-KI-App

🧠 Eine modulare, lokal laufende KI-Anwendung zur Unterstützung von Umweltplanungsprozessen.  
Ziel: Fehlende Daten erkennen, strukturierte Vorschläge erzeugen, externe Anfragen vorbereiten.  
Erweiterbar mit RAG-System, JSON-Datenbank und Geodatenanalyse.

## 🔧 Hauptkomponenten
- `core/` – Zentrale Funktionen (Analyse, Prompt, Vorschläge)
- `services/` – Datenanfrage, KI-Service, Editor-Tools
- `data/` – Strukturierte Quelldaten (z. B. datenquellen.json)
- `models/` – Trainingsfunktionen für späteres Fine-Tuning
- `tools/` – Prüfer, Dateneditoren
- `app.py` – Einstiegspunkt (Streamlit oder CLI)

## 📦 Installieren
```bash
pip install -r requirements.txt
