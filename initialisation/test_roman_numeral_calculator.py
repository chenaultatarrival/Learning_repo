import pytest
from initialisation.roman_numeral_calculator import calculator


@pytest.mark.parametrize(
    "roman_input,expected_output",
    [
        (["I","I"], "II"),
        (["I","II"], "III"),

    ],
)
def test_eval(roman_input, expected_output):
    assert calculator(calculator_input=roman_input) == expected_output