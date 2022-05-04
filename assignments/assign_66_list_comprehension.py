"""
Assignment: 66
Write a Python program using List Comprehension to find cube of numbers in given list.
Input List: [2, 4, 1, 5, 8, 9]
"""
nums = [2, 4, 1, 5, 8, 9]

cubes_list = [d*d*d for d in nums]
print(f"Cubes list: {cubes_list}")
