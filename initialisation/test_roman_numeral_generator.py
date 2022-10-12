import pytest
from initialisation.roman_numeral_generator import RomanNumeralGenerator


@pytest.mark.parametrize(
    "arabic_numeral,expected_roman",
    [
        (1, "I"),
        (2, "II"),
        (3, "III"),
        (4, "IV"),
        (5, "V"),
        (6, "VI"),
        (7, "VII"),
        (90, "XC"),
        (100, "C"),
        (1000, "M"),
        (199, "CXCIX"),
        (2399, "MMCCCXCIX"),
    ],
)
def test_eval(arabic_numeral, expected_roman):
    roman_generator = RomanNumeralGenerator()
    assert roman_generator.generator(arabic=arabic_numeral) == expected_roman
