"""
Assignment: 59
Write a program to handle IndexError. Program will take index value as input from
the user. It will try to print the value at the given index. If the index is not
valid then the program should print “Invalid index” message to the user.
Use 'try-except' block.
Hardcoded Input: my_list = ['The', 'exception', 'handling', 'demo', 'python']
User Input: Any number
"""


my_list = ['The', 'exception', 'handling', 'demo', 'python']
# Read the input from the user
index_value = int(input("Enter index value: "))

try:
    print(f"Value at given index is '{my_list[index_value]}'")

except IndexError:
    print("Invalid index")
