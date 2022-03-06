# Read two integers from the user.
# User “pow” math function and print the output.
import math
num = int(input("Enter first value: "))
exp = int(input("Enter second value: "))
pow_res = math.pow(num, exp)
print(f"{num} to the power of {exp} is: {pow_res}")
