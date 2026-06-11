#!/usr/bin/env python3
'''
OPS445 Assignment 1
Program: assignment1.py 
Author: "Aarsh Modi"
Semester: "Summer 2026"
The python code in this file (assignment1.py) is original work written by
"Aarsh Modi". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''
import sys

def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]

def leap_year(year: int) -> bool:
    "Return True if the year is a leap year, False otherwise"
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def mon_max(month: int, year: int) -> int:
    "Return the maximum number of days in a given month, accounting for leap years"
    feb = 29 if leap_year(year) else 28
    mm = {1:31, 2:feb, 3:31, 4:30, 5:31, 6:30,
          7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    return mm[month]

def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This function has been tested to work for year after 1582
    '''
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    tmp_day = day + 1

    if tmp_day > mon_max(month, year):
        to_day = 1
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month

    if tmp_month > 12:
        to_month = 1
        year = year + 1
    else:
        to_month = tmp_month

    next_date = f"{year}-{to_month:02}-{to_day:02}"
    return next_date

def valid_date(date: str) -> bool:
    "Check validity of date string in YYYY-MM-DD format, return True if valid"
    parts = date.split('-')
    if len(parts) != 3:
        return False
    if len(parts[0]) != 4 or len(parts[1]) != 2 or len(parts[2]) != 2:
        return False
    try:
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
    except ValueError:
        return False
    if month < 1 or month > 12:
        return False
    if day < 1 or day > mon_max(month, year):
        return False
    return True

def day_count(start_date: str, stop_date: str) -> int:
    "Loop through range of dates and return number of weekend days"
    count = 0
    current = start_date
    while current <= stop_date:
        str_year, str_month, str_day = current.split('-')
        dow = day_of_week(int(str_year), int(str_month), int(str_day))
        if dow in ('sat', 'sun'):
            count += 1
        current = after(current)
    return count

def usage():
    "Print a usage message to the user and exit"
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()

    date1 = sys.argv[1]
    date2 = sys.argv[2]

    if not valid_date(date1) or not valid_date(date2):
        usage()

    start_date = min(date1, date2)
    end_date = max(date1, date2)

    count = day_count(start_date, end_date)
    print(f"The period between {start_date} and {end_date} includes {count} weekend days.")

