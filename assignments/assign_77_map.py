"""
Assignment: 77
Write a map function to calculate square root of the numbers in a given list.
"""

values = [4, 2, 7, 1, 9]
ret = list(map(lambda x: x*x*x, values))
print(ret)
