from core.analyse import erkenne_fehlende_infos

def test_erkennt_fehlendes():
    antwort = "Die Datenlage ist unvollständig und weitere Unterlagen werden benötigt."
    result = erkenne_fehlende_infos(antwort)
    assert "benötigt" in result or "unvollständig" in result
