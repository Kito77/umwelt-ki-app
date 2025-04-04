#Laden von PDF/TXT

# services/file_loader.py
"""
Dieses Modul enthält Funktionen zum Laden und Verarbeiten von Text- und PDF-Dateien.
Wird verwendet für die Kontextbereitstellung in der Umwelt-KI-App.
"""

from typing import Optional
from PyPDF2 import PdfReader
import streamlit as st

def lade_textdatei(datei) -> Optional[str]:
    """Liest eine Textdatei (.txt) und gibt den Inhalt als String zurück."""
    try:
        return datei.read().decode("utf-8")
    except Exception as e:
        st.error(f"Fehler beim Laden der Textdatei: {e}")
        return None

def lade_pdf(datei) -> Optional[str]:
    """Extrahiert Text aus einer PDF-Datei."""
    try:
        reader = PdfReader(datei)
        text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
        return text
    except Exception as e:
        st.error(f"Fehler beim Verarbeiten der PDF-Datei: {e}")
        return None
