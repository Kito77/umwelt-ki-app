from core.prompt_builder import erstelle_prompt

def test_prompt_mit_kontext():
    frage = "Was gilt im FFH-Gebiet?"
    kontext = "Dies ist ein Umweltbericht über das FFH-Gebiet X."
    prompt = erstelle_prompt(kontext, frage)
    assert "FFH" in prompt
    assert "Kontextauszug" in prompt or "Frage" in prompt
