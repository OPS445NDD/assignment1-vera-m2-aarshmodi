import pytest
from assignment1 import leap_year, mon_max, after, valid_date, day_count

def test_leap_year():
    assert leap_year(2000) == True
    assert leap_year(1900) == False
    assert leap_year(2024) == True
    assert leap_year(2023) == False

def test_mon_max():
    assert mon_max(1, 2023) == 31
    assert mon_max(2, 2024) == 29
    assert mon_max(2, 2023) == 28
    assert mon_max(4, 2023) == 30

def test_after():
    assert after('2023-01-31') == '2023-02-01'
    assert after('2023-12-31') == '2024-01-01'
    assert after('2024-02-28') == '2024-02-29'
    assert after('2023-02-28') == '2023-03-01'

def test_valid_date():
    assert valid_date('2023-01-01') == True
    assert valid_date('2023-02-28') == True
    assert valid_date('20-03-13') == False
    assert valid_date('2023-13-01') == False
    assert valid_date('2023-02-31') == False

def test_day_count():
    assert day_count('2023-05-01', '2023-05-30') == 8
    assert day_count('2023-05-18', '2023-06-04') == 6
