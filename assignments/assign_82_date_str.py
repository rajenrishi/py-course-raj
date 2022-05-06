"""
Assignment: 82
Write a Python program to convert string to datetime.
Input: 27-10-2020 11:22:00
"""

from datetime import datetime

str_dt = "27-10-2020 11:22:00"
dt = datetime.strptime(str_dt, "%d-%m-%Y %H:%M:%S")
print(type(dt))
print(dt)
