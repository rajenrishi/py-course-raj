"""
Assignment: 67
Write a Python program using List Comprehension to create list with length of
the strings in input list.
Input List: [‘salary’, ‘office’, ‘scale’, ‘pencil’, ‘lift’]
Output List: [6, 6, 5, 6, 4]
"""
str_list = ["salary", "office", "scale", "pencil", "lift"]

str_lens = [len(d) for d in str_list]
print(f"Lengths of strings: {str_lens}")
