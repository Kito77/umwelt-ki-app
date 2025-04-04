from services.ki_client import frage_an_ki

def test_ki_antwortet():
    antwort = frage_an_ki("Was sind FFH-Gebiete?")
    assert isinstance(antwort, str)
    assert len(antwort.strip()) > 10
