# Read one string, and two numbers from user.
# String can take following values: add, subtract, multiply, division.
# If user input is add, print the sum of two numbers
# If user input is subtract, print the subtraction of two numbers.
# Similarly for multiply and division
# If user inputs any other string then print “Incorrect operation.”
def implementation_1():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    action = input("Enter mathematical operation: ")
    if action.lower() == "add":
        print(num1 + num2)
    elif action.lower() == "subtract":
        print(num1 - num2)
    else:
        print("Incorrect operation.")


def implementation_2():
    valid_op_list = ["add", "multiply", "subtract", "division"]
    action = input("Enter mathematical operation: ")
    print(f"User entered action: {action}")
    if action.lower() in valid_op_list:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        # add, subtract, multiply, division
        if action.lower() == "add":
            print(num1 + num2)
        elif action.lower() == "subtract":
            print(num1 - num2)
    else:
        print("Incorrect operation.")


print(">>>>>>>>>>> IMPLEMENTATION 1 <<<<<<<<<<<<")
# implementation_1()
print(">>>>>>>>>>> IMPLEMENTATION 2 <<<<<<<<<<<<")
implementation_2()
