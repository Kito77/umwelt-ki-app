# app.py – Umweltplanungs-KI mit Modulstruktur
# -------------------------------------------
# Hauptdatei welche Basis dient um alle Services aufzurufen

import streamlit as st

# 🔧 Importiere Services aus dem Projekt
from services.file_loader import lade_textdatei, lade_pdf
from services.frage_service import stelle_ki_frage
from services.datenbedarf_service import datenbedarf_ermitteln
from services.anfrage_service import erstelle_anfragevorschlaege
from services.datenbeschaffung_service import (
    ist_automatisch_abrufbar,
    kann_angeschrieben_werden,
    generiere_emailtext,
    hole_daten_automatisch
)


#Importiere Core Funktionen
from core.analyse import erkenne_fehlende_infos
from core.datenquellen import get_regionale_quellen
from core.datenbedarf import analysiere_datenbedarf
from core.vorschlaege import generiere_vorschlaege
from core.anfrage_manager import lade_anfragequellen, generiere_anfragevorschlaege

#Hilfsfunktion
def sichere_eingabe(text: str) -> bool:
    """
    Prüft, ob eine Eingabe verbotene Zeichen enthält.
    Gibt False zurück, wenn Sonderzeichen enthalten sind.
    """
    verbotene_zeichen = ["<", ">", ";", "{", "}", "&&"]
    return not any(z in text for z in verbotene_zeichen)

# 🔰 TITEL UND BESCHREIBUNG
st.title("🌿 Umweltplanungs-KI")
st.markdown("""
Gib eine Frage ein – optional mit Kontext (z. B. Auszug aus einem Umweltbericht oder 
            einem PDF).
Die KI beantwortet deine Frage und nennt bei Bedarf fehlende Unterlagen oder Datenquellen.
""")
st.markdown("💡 *Beispiele: 'Welche Auswirkungen hat ein Eingriff in LRT 91E0?' oder 'Fehlen Unterlagen?*'")

# 🧾 MANUELLE KONTEXTEINGABE
kontext = st.text_area(
    "Optional: Manuell eingegebener Kontext",
    placeholder="Hier kannst du einen Abschnitt aus einem Gutachten, Lagebeschreibung oder Gesetzestext einfügen."
)

# 📥 DATEI-UPLOAD (PDF ODER TXT)
st.markdown("### 📎 Datei hochladen (optional)")
hochgeladene_datei = st.file_uploader("Datei auswählen", type=["txt", "pdf"])

# 🧾 TEXT AUS DATEI EXTRAHIEREN
dokument_text = ""
if hochgeladene_datei is not None:
    if hochgeladene_datei.name.endswith(".txt"):
        dokument_text = lade_textdatei(hochgeladene_datei)
        if dokument_text:
            st.success("Textdatei erfolgreich geladen ✅")

    elif hochgeladene_datei.name.endswith(".pdf"):
        dokument_text = lade_pdf(hochgeladene_datei)
        if dokument_text:
            st.success("PDF-Datei erfolgreich verarbeitet ✅")

    # 📄 VORSCHAU
    if dokument_text:
        st.markdown("**Auszug aus der Datei:**")
        st.text(dokument_text[:500])

# 🧠 KONTEXT ZUSAMMENSETZEN
kombinierter_kontext = kontext + "\n" + dokument_text

# 🗺️ GEODATEN-UPLOAD (GeoJSON)
st.markdown("### 🗺️ Geodaten anzeigen (optional)")
geojson_datei = st.file_uploader("GeoJSON-Datei auswählen", type=["geojson"], key="geojson")

if geojson_datei is not None:
    from services.map_tools import zeige_karte
    zeige_karte(geojson_datei)

# ❓ FRAGEINGABE
frage = st.text_area(
    "Gib hier deine Frage ein:",
    placeholder="Beispiel: Welche Einschränkungen gelten für diesen Lebensraumtyp?"
)

# 🔘 BUTTON → KI ANTWORT
if st.button("Frage stellen"):
    if frage.strip() == "":
        st.warning("Bitte gib eine Frage ein.")
    elif not sichere_eingabe(frage):
        st.error("❗ Deine Eingabe enthält Zeichen, die nicht erlaubt sind (z. B. <, >, ;). Bitte formuliere deine Frage ohne technische Sonderzeichen.")
    else:
        st.info("KI denkt nach …")

        # ✨ KI über ausgelagerten Service fragen
        antwort = stelle_ki_frage(kombinierter_kontext, frage)

        # Datenbedarf analysieren & Quellen für Bedarfsanfragen
        datenbedarf_liste, vorschlaege_dict = datenbedarf_ermitteln(antwort)
        anfragevorschlaege = erstelle_anfragevorschlaege(datenbedarf_liste)

        # Fehlende Infos analysieren
        fehlende_infos = erkenne_fehlende_infos(antwort)

        # 💬 ANTWORT AUSGEBEN
        st.success("Antwort der KI:")
        st.markdown(antwort)

        #wenn nötig Quellenvorschläge
        if fehlende_infos:
            st.markdown("### 🔍 Erkannte Informationslücken")
            st.info("Die KI hat Hinweise auf fehlende Daten oder Unterlagen erkannt.")
            st.markdown("#### 📎 Empfohlene Datenquellen:")
            for name, link in get_regionale_quellen().items():
                st.markdown(f"- [{name}]({link})")

        # 🔍 Wenn Datenbedarf erkannt wurde
        if datenbedarf_liste:
            st.markdown("### 📎 Mögliche fehlende Informationen / Unterlagen")
            for punkt in datenbedarf_liste:
                st.markdown(f"- {punkt.capitalize()}")
                st.markdown(f"  → {vorschlaege_dict.get(punkt)}")

                  # Automatisierte Datenbeschaffung
                if ist_automatisch_abrufbar(punkt):
                    st.markdown(f"🔄 *Diese Information kann automatisch abgerufen werden.*")
                
                if st.button(f"Jetzt {punkt} laden", key=f"btn_{punkt}"):
                    vorschau = hole_daten_automatisch(punkt)
                    st.code(vorschau, language="text")

                elif kann_angeschrieben_werden(punkt):
                    st.markdown("📨 *Diese Information kann per E-Mail angefragt werden:*")
                    st.code(generiere_emailtext(punkt), language="text")

            #Wenn Anfragen nötig sind
            if anfragevorschlaege:
                st.markdown("### 📨 Vorschläge zur Datenanforderung")
                for text in anfragevorschlaege:
                    st.markdown(text)
