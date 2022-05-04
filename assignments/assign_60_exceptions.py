"""
Assignment: 60
Write a program to take Employee Age and Salary as inputs from the user.
If the user enters the age less than 18, program should throw ValueError.
Once the valid Age and Salary, are entered program should print the same.
"""


# Read the input from the user
salary = int(input("Enter salary: "))
age = int(input("Enter age: "))

try:
    if age < 18:
        raise ValueError("Enter age greater than 18.")

    print(f"Salary of employee: {salary}")
    print(f"Age of employee: {age}")

except ValueError as e:
    print(e)
