"""
Assignment: 61
Write a program to raise an appropriate exception. Program will take user name as input.
A valid name should be at least 5 characters. If the user enters
invalid name, program will throw exception.
"""


# Read the input from the user
name = input("Enter name: ")

try:
    if len(name) < 5:
        raise ValueError("Name should have more than 5 characters.")

    print(f"Name of employee: {name}")

except ValueError as e:
    print(e)
