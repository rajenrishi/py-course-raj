"""
Assignment: 80
Write a Python program to print the date and time of day which is 5 days
from current date & time.
"""

from datetime import date, timedelta
print(date.today() + timedelta(5))
