"""
Assignment: 70
Write a Python program to write 9 multiplication table to a text file.
Output file content:
    9 x 1 = 9
    9 x 2 = 18
    ...
"""

fh = open("assign_70_mul_table.txt", "w")
num = 9
for ind in range(1, 11):
    fh.write(f"9 x {ind} = {num * ind}")
    fh.write("\n")

fh.close()
