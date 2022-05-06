"""
Assignment: 72
Write a Python program to count the number of lines in a file.
Create a text file with any data and use for writing program.
"""

fh = open("assign_72_line_count.txt", "r")
lines = fh.readlines()
print(f"Number of lines in the given file are: {len(lines)}")
