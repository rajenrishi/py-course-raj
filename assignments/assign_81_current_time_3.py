"""
Assignment: 81
Write a Python program to add 3 hours to current time.
"""

from datetime import datetime, timedelta
print(datetime.now() + timedelta(hours=3))
