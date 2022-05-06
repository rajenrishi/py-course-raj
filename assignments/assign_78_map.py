"""
Assignment: 78
Write a map function to increase a number in list by 10 if the number is less
than 10 else decrease the number by 5.
Input list: [23, 12, 4, 56, 33, 9, 21, 61, 23, 55, 41, 67]
"""

values = [23, 12, 4, 56, 33, 9, 21, 61, 23, 55, 41, 67]
ret = list(map(lambda x: x - 5 if x > 10 else x + 10, values))
print(ret)
