# Read an integer from the user and print the factorial of the given number.
num = int(input("Enter number: "))
fact = 1
for n in range(1, num + 1):
    fact = fact * n
print(f"Factorial of number is: {fact}")
