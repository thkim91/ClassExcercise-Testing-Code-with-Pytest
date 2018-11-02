import pytest
def test_year_to_sec():
    assert calc_number_of_seconds(5, "year") == 157680000

def test_month_to_sec():
    assert calc_number_of_seconds(6, "month") == 15552000

def test_week_to_sec():
    assert calc_number_of_seconds(7, "week") == 4233600

def test_day_to_sec():
    assert calc_number_of_seconds(8, "day") == 691200

def test_hour_to_sec():
    assert calc_number_of_seconds(9, "hour") == 32400

def test_minute_to_sec():
    assert calc_number_of_seconds(10, "mintue") == 600

def test_second_to_sec():
    assert calc_number_of_seconds(11, "second") == 11

def test_negative_input():
    calc_number_of_seconds(-11, "second")
    with pytest.raises(Expection):
        1 / 0
