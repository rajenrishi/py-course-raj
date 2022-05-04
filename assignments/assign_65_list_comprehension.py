"""
Assignment: 65
Write a Python program using List Comprehension to remove words starting with 's' from
the input list.
Input List: [‘salary’, ‘office’, ‘scale’, ‘pencil’, ‘lift’]
"""
str_list = ["salary", "office", "scale", "pencil", "lift"]

filtered_list = [s for s in str_list if not s.startswith('s')]
print(f"Filtered list: {filtered_list}")
