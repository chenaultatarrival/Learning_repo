from initialisation.module import *

def test_total_empty() -> None:
    assert total([]) == 0.0

def test_numeral():
    assert numeral(1) == "I"