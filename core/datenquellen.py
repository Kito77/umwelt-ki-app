# Gibt die Liste regionaler Datenquellen für die Anzeige zurück

def get_regionale_quellen() -> dict:
    return {
        "BfN Kartenserver": "https://www.bfn.de/karten",
        "Umweltbundesamt (UBA)": "https://www.umweltbundesamt.de",
        "Geoportal Brandenburg": "https://geoportal.brandenburg.de",
        "LfU Brandenburg Altlasten": "https://lfu.brandenburg.de/lfu/de/",
        "Untere Naturschutzbehörde PM": "https://www.potsdam-mittelmark.de/...",
        "Stadt Potsdam – Umwelt & Natur": "https://www.potsdam.de/de/content/naturschutz",
        "BUND Brandenburg": "https://www.bund-brandenburg.de/",
        "Umweltportal Uni Potsdam": "https://www.uni-potsdam.de/de/umweltportal/index"
    }