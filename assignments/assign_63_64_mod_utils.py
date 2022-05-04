"""
Assignment: 63
Write a function in a module to find maximum number in a list.
Import the module in python program and use the module.
"""


def find_max(obj):
    """
    :param obj: List with numbers
    :return: int: max number from the list
    """
    max_num = 0
    for e in obj:
        if e > max_num:
            max_num = e
    return max_num


def find_avg(obj):
    """
    :param obj: List with numbers
    :return: int: average of given numbers in list
    """
    sum = 0
    avg = 0
    for e in obj:
        sum = sum + e

    avg = sum/len(obj)
    return avg
