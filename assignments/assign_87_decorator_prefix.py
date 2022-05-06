"""
Assignment: 87
Write a Python program develop a decorator.
This decorator will prefix todays date and length of the string.
For example, if the string is “DEVICE FAIL”, then output should be
in following format: “YYYY-MM-DD 11 DEVICE FAIL”
"""
from datetime import date


def prefix_date_len(function):
    def wrapper(name):
        func = function(name)
        make_uppercase = str(date.today()) + " " + str(len(func)) + " " + func
        return make_uppercase

    return wrapper


@prefix_date_len
def show_log(str_log):
    return str_log


print(show_log("DEVICE FAIL"))
