"""
Assignment: 68
Write a Python program using List Comprehension to create a matrix with even numbers.
"""
mat_even = [[j for j in range(1, 7) if j % 2 == 0] for i in range(3)]
print(mat_even)
