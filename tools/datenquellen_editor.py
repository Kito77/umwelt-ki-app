# tools/datenquellen_editor.py
import streamlit as st
import json
import os
import pandas as pd
#Abrufen Pruefer
from pruefer import pruefe_datenquellen

# 🛠️ Neuer Pfad, der vom Projektverzeichnis aus immer korrekt ist:
PFAD = os.path.join(os.path.dirname(__file__), "..", "data", "datenquellen.json")
PFAD = os.path.abspath(PFAD)

def lade_daten():
    if not os.path.exists(PFAD):
        return {}
    with open(PFAD, encoding="utf-8") as f:
        return json.load(f)

def speichere_datenquellen(neuer_eintrag, schlüssel):
    daten = lade_daten()
    daten[schlüssel] = neuer_eintrag
    with open(PFAD, "w", encoding="utf-8") as f:
        json.dump(daten, f, ensure_ascii=False, indent=2)

def editor_ui():
    st.title("📘 Datenquellen-Editor")

    schlüssel = st.text_input("🆔 Interner Schlüssel", help="z. B. 'lärmkarte_brandenburg'")
    beschreibung = st.text_input("📄 Beschreibung")
    abfrage_schlüssel = st.text_input("🔍 Suchbegriffe (kommasepariert)", help="z. B. lärmbelastung,laermkarte")
    region = st.text_input("🌍 Region", value="Deutschland")
    thema = st.text_input("📚 Thema", value="Lärm")
    quelle = st.text_input("🔗 Datenquelle (URL)")
    dateityp = st.selectbox("📁 Dateityp", ["html", "pdf", "json", "csv", "andere"])
    aktualisiert = st.date_input("📆 Letzte Aktualisierung")
    autom = st.checkbox("Automatisierbar?")
    anfragbar = st.checkbox("Anfrage möglich?")
    offen = st.checkbox("Quelle ist offen verfügbar?")
    
    email = ""
    vorlage = ""
    if anfragbar:
        email = st.text_input("📨 Anfrage-E-Mail")
        vorlage = st.text_area("📑 Textvorlage")

    if st.button("✅ Speichern"):
        eintrag = {
            "abfrage_schlüssel": [s.strip() for s in abfrage_schlüssel.split(",")],
            "beschreibung": beschreibung,
            "region": region,
            "thema": thema,
            "quelle": quelle,
            "dateityp": dateityp,
            "aktualisiert_am": str(aktualisiert),
            "automatisierbar": autom,
            "anfrage_möglich": anfragbar,
            "quelle_offen": offen
        }
        if anfragbar:
            eintrag["anfrage_email"] = email
            eintrag["vorlage"] = vorlage
        speichere_datenquellen(eintrag, schlüssel)
        st.success(f"✅ '{schlüssel}' erfolgreich gespeichert!")
    
    st.markdown("---")
    st.markdown("## 🔎 Datenquellen überprüfen")

    if st.button("🧪 Alle Einträge prüfen"):
        fehler = pruefe_datenquellen()
        if fehler:
            st.warning(f"{len(fehler)} Fehler/Warnungen gefunden:")
            df = pd.DataFrame(fehler)
            st.dataframe(df, use_container_width=True)
        else:
            st.success("✅ Alle Datenquellen sind vollständig und gültig!")

if __name__ == "__main__":
    editor_ui()


