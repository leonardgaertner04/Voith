import pytest
from converter import number_to_words

@pytest.mark.parametrize("zahl, wort", [
    (0, "null"),
    (1, "eins"),
    (7, "sieben"),
    (10, "zehn"),
    (11, "elf"),
    (19, "neunzehn"),
    (20, "zwanzig"),
    (21, "einundzwanzig"),
    (45, "fünfundvierzig"),
    (99, "neunundneunzig"),
    (100, "einhundert"),
])
def test_number_to_words(zahl, wort):
    assert number_to_words(zahl) == wort

def test_out_of_range():
    with pytest.raises(ValueError):
        number_to_words(-1)
    with pytest.raises(ValueError):
        number_to_words(101)
    with pytest.raises(ValueError):
        number_to_words(1.5)    
