"""
Assignment: 64
Write two functions in python module. One function to find average for numbers in
list and the other function is to find index of the given value in the list.
Inside python program import the functions from the module using ‘from’ keyword.
"""
from assign_63_64_mod_utils import find_avg

numbers = [34, 22, 45, 67, 19, 90, 39]

avg = find_avg(numbers)
print(f"Average: {avg}")
