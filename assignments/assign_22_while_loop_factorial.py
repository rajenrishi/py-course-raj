# Read an integer from the user and print the factorial of the given number.
# For Example: 5! = 5 * 4 * 3 * 2 * 1
num = int(input("Enter number: "))
fact = 1
while num > 0:
    fact = fact * num
    num = num - 1
print(f"Factorial of number is: {fact}")
