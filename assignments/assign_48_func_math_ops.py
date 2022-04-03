# Assignment: 48
# Write a program to define a function which takes two numbers and one string as parameters.
# The string will be one of the mathematical operations like “add”, “subtract”,
# “multiply”, “division”.
# The function should perform the given mathematical operation and return the result.
# Default mathematical operation should be “add”.

def math_operations(num1, num2, action="add"):
    if action.lower() == "add":
        return num1 + num2
    elif action.lower() == "subtract":
        return num1 - num2
    elif action.lower() == "multiply":
        return num1 * num2
    elif action.lower() == "division":
        return num1 / num2
    else:
        print("Invalid math operation.")


# Default operation
sumnum = math_operations(10, 12)
print(f"Sum of given numbers is: {sumnum}")

sumnum = math_operations(10, 12, action="add")
print(f"Sum of given numbers is: {sumnum}")

diff = math_operations(10, 12, action="subtract")
print(f"Difference of given numbers is: {diff}")
