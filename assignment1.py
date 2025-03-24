#!/usr/bin/env python3
 
 
'''
OPS445 Assignment 1 - Winter 2025
Program: assignment1.py 
Author: "Fuad Ahmed"
The python code in this file (a1_182853218.py) is original work written by
"Fuad Ahmed". No code in this file is copied from any other source
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
 
 
 
 
def mon_max(month: int, year: int) -> int:
    "Returns the maximum day for a given month. Includes leap year check"
    mon_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    
    if month == 2 and leap_year(year):
        return 29
    elif 1 <= month <= 12:
        return mon_dict[month]
    else:
        return None

 
def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format
 
 
    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This fucntion has been tested to work for year after 1582
    '''
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)
    tmp_day = day + 1  # next day
 
 
    if tmp_day > mon_max(month, year):
        to_day = tmp_day % mon_max(month, year)  # if tmp_day > this month's max, reset to 1 
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month + 0
 
 
    if tmp_month > 12:
        to_month = 1
        year = year + 1
    else:
        to_month = tmp_month + 0
 
 
    next_date = f"{year}-{to_month:02}-{to_day:02}"
 
 
    return next_date
 
 
 
 
def usage():
    "Print a usage message to the user"
    print("Usage: Type ./assignment1.py start-date end-date. Make sure it is in YYYY-MM-DD format")
 
 
 
 
def leap_year(year: int) -> bool:
    "return True if the year is a leap year"
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
 

def valid_date(date: str) ->y bool:
    "check validity of date and return True if valid"
    try:
        year= int(date[:4])
        month= int(date[5:7])
        day=int(date[8:10])

        if not (1<= month <= 12):
            return False

        if not (1<=day<=mon_max(month,year)):
            return False

        return True
    except (ValueError):
        return False
 
def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"
    if not (valid_date(start_date) and valid_date(stop_date)):
        print("Invalid date format")
        sys.exit(1)
    
    count = 0
    year, month, day = int(start_date[:4]), int(start_date[5:7]), int(start_date[8:])
    stop_year, stop_month, stop_day = int(stop_date[:4]), int(stop_date[5:7]), int(stop_date[8:])
    
    while (year, month, day) <= (stop_year, stop_month, stop_day):
        if day_of_week(year, month, day) in ['sat', 'sun']:
            count += 1
        day += 1
        if day > mon_max(month, year):
            day = 1
            month += 1
        if month > 12:
            month = 1
            year += 1
    
    return count
 
 
if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()

    start_date = sys.argv[1]
    if not valid_date(start_date):
        print(f"Invalid Start Date: {start_date}")
        usage()

    try:
        num = int(sys.argv[2])
    except ValueError:
        print(f"Invalid number of days: {sys.argv[2]}")
        usage()
    end_date = day_iter(start_date, num)
    day = day_of_week(end_date)

    print(f"The end date is: {end_date} ({day})")

