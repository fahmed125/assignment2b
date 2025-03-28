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
from datetime import datetime, timedelta

def after(date: str) -> str:
    """
    Given a date in YYYY-MM-DD format, returns the next day's date.
    """
    input_date = datetime.strptime(date, "%Y-%m-%d")
    next_day = input_date + timedelta(days=1)
    return next_day.strftime("%Y-%m-%d")

def before(date: str) -> str:
    """
    Given a date in YYYY-MM-DD format, returns the previous day's date.
    """
    input_date = datetime.strptime(date, "%Y-%m-%d")
    prev_day = input_date - timedelta(days=1)
    return prev_day.strftime("%Y-%m-%d")

def leap_year(year: int) -> bool:
    """
    Returns True if the given year is a leap year, False otherwise.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def mon_max(month: int, year: int) -> int:
    """
    Returns the number of days in the given month of the given year.
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year(year):
        month_days[1] = 29
    return month_days[month - 1]

def dbda(start_date: str, days: int) -> str:
    """
    Given a start date and number of days, calculates the resulting date.
    A positive number of days moves the date forward, and a negative number moves it back.
    """
    input_date = datetime.strptime(start_date, "%Y-%m-%d")
    result_date = input_date + timedelta(days=days)
    return result_date.strftime("%Y-%m-%d")

def valid_date(date: str) -> bool:
    """
    Checks if the date is in the correct YYYY-MM-DD format and is a valid date.
    """
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def usage():
    """
    Displays the correct usage of the script.
    """
    print("Usage: ./assignment1.py <start_date> <divisor>")
    print("Example: ./assignment1.py 2023-01-25 2")
    sys.exit(1)

def main():
    # Check if the number of arguments is correct
    if len(sys.argv) != 3:
        usage()
    
    start_date = sys.argv[1]
    divisor = sys.argv[2]

    # Validate the start date
    if not valid_date(start_date):
        print(f"Invalid date: {start_date}")
        usage()
    
    # Validate the divisor
    try:
        divisor = int(divisor)
        if divisor == 0:
            print("Error: Divisor cannot be zero.")
            usage()
    except ValueError:
        print(f"Invalid divisor: {divisor}")
        usage()
    
    # Calculate the number of days
    days = round(365 / divisor)
    print(f"A year divided by {divisor} gives {days} days.")
    
    # Calculate the past and future dates
    past_date = dbda(start_date, -days)
    future_date = dbda(start_date, days)
    
    # Print the results
    print(f"The date {days} days ago was {past_date}.")
    print(f"The date {days} days from now will be {future_date}.")

if __name__ == "__main__":
    main()
