import pytest


@pytest.mark.parametrize("amount_input, current_unit_input, converted_unit_input, expected_output",
                         [(4, "pound", "kilogram" , 2.16),
                          (2, "kilometer", "mile", 1.24),
                          (2, "gallon", "liter", 7.57),
                          (75, "fahrenheit", "celsius", 23.89),
                          (2, "miles", "kilometer", 3.22)
                          ])
def test_convert_units(amount_input, current_unit_input, converted_unit_input, expected_output):
    units = convert_units(amount_input, current_unit_input, converted_unit_input)
    assert round(units, 2) == expected_output


def test_pound_kilo():
    units = convert_units(4, "pound", "kilogram")
    assert round(units, 2) == 2.16


def test_kilo_miles():
    units = convert_units(4, "kilo", "miles")
    assert round(units, 2) == 1.24


def test_gallon_liter():
    units = convert_units(2, "gallon", "liter")
    assert round(units, 2) == 7.57


def test_fahrenheit_celsius():
    units = convert_units(75, "fahrenheit", "celsius")
    assert round(units, 2) == 23.89


def test_miles_kilo():
    units = convert_units(2, "miles", "kilometer")
    assert round(units, 2) == 3.22
