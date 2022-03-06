# Write a program to find area of the circle.
# Diameter of the circle will be read from user input.
import math
dia = int(input("Enter circle diameter: "))
rad = dia / 2
area = math.pi * rad ** 2
print(f"Area of circle with diameter {dia} is : {area}")
