# Read/Define two float numbers from user and perform the below operations:
# Perform “ceil” on first float value and save to a variable.
# Perform “floor” on second float value and save to a variable.
# Multiple both the variables and print the output.
import math

f1 = float(input("Enter first float value: "))
f2 = float(input("Enter second float value: "))
ceil_f1 = math.ceil(f1)
floor_f2 = math.floor(f2)
prod = ceil_f1 * floor_f2
print(f"Product of ceil & floored floats is {prod}")
