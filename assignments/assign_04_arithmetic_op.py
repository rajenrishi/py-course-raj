# Read radius from the user and calculate the area of a circle.
# Print the output with the decimal value rounded
# of to 2 digits. Use ‘math’ module.
import math
radius = int(input("Enter circle radius: "))
area = math.pi * radius * radius
print(f"Area of circle with radius {radius} is: {area:.2f}")
