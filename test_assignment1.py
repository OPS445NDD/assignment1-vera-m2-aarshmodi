import pytest
from assignment1 import leap_year, mon_max, after, valid_date, day_count, day_of_week

def test_after_next_date():
    assert after('2023-01-25') == '2023-01-26'

def test_after_end_of_month():
    assert after('2023-01-31') == '2023-02-01'

def test_after_end_of_year():
    assert after('2023-12-31') == '2024-01-01'

def test_after_leap_year():
    assert after('2024-02-28') == '2024-02-29'

def test_after_non_leap_year():
    assert after('2023-02-28') == '2023-03-01'

def test_after_returns_string():
    assert isinstance(after('2023-05-01'), str)

def test_leap_year_400():
    assert leap_year(2000) == True

def test_leap_year_100():
    assert leap_year(1900) == False

def test_leap_year_4():
    assert leap_year(2024) == True

def test_leap_year_false():
    assert leap_year(2023) == False

def test_mon_max_january():
    assert mon_max(1, 2023) == 31

def test_mon_max_april():
    assert mon_max(4, 2023) == 30

def test_mon_max_feb_leap():
    assert mon_max(2, 2024) == 29

def test_mon_max_feb_non_leap():
    assert mon_max(2, 2023) == 28

def test_valid_date_true():
    assert valid_date('2023-01-01') == True

def test_valid_date_false_short_year():
    assert valid_date('20-03-13') == False

def test_valid_date_false_bad_month():
    assert valid_date('2023-13-01') == False

def test_valid_date_false_bad_day():
    assert valid_date('2023-02-31') == False

def test_valid_date_false_format():
    assert valid_date('2023-99-99') == False

def test_day_count_may():
    assert day_count('2023-05-01', '2023-05-30') == 8

def test_day_count_range():
    assert day_count('2023-05-18', '2023-06-04') == 6

def test_day_of_week_monday():
    assert day_of_week(2023, 5, 1) == 'mon'

def test_day_of_week_saturday():
    assert day_of_week(2023, 5, 6) == 'sat'

def test_day_of_week_sunday():
    assert day_of_week(2023, 5, 7) == 'sun'
