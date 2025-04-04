# CLI-Schnittstelle zum Fragenstellen
# my_environment_ai/rag/ask_bot.py

from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
import os

# 1️⃣ Pfad zu den Quelldaten (könnte später auch dynamisch sein)
DATA_PATH = "data/processed/sample_text.txt"

def lade_dokumente():
    """Lädt eine Textdatei und teilt sie in kleine Chunks."""
    loader = TextLoader(DATA_PATH, encoding="utf-8")
    documents = loader.load()
    
    # Splitten in kleinere Abschnitte (für bessere Suche)
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(documents)

def baue_vektor_speicher(dokumente):
    """Erstellt eine Chroma-Vektordatenbank aus den Textabschnitten."""
    embedding_model = OllamaEmbeddings(model="mistral")
    vectordb = Chroma.from_documents(dokumente, embedding_model)
    return vectordb

def baue_chain(vectordb):
    """Verbindet lokalen LLM mit der Vektorsuche (Retrieval-Augmented Generation)."""
    mistral_llm = Ollama(model="mistral")
    qa_chain = RetrievalQA.from_chain_type(
        llm=mistral_llm,
        retriever=vectordb.as_retriever()
    )
    return qa_chain

def main():
    print("🌿 Umwelt-KI Mistral RAG – Stell deine Frage (oder tippe 'exit')")
    
    # Lade & verarbeite Daten
    dokumente = lade_dokumente()
    vectordb = baue_vektor_speicher(dokumente)
    chain = baue_chain(vectordb)
    
    # CLI-Schleife
    while True:
        frage = input("❓ Frage: ")
        if frage.lower() in ["exit", "quit"]:
            break
        antwort = chain.run(frage)
        print("🤖 Antwort:", antwort)
        print("-" * 60)

if __name__ == "__main__":
    main()
