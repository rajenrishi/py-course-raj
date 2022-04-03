# Write a program to read 5 fruits and there price per kg.
# Create a dictionary with fruit names as key & price as values.
# Hint: Use any loop, input function

fruits_count = 5
fruits_dict = {}
for i in range(fruits_count):
    fruit_name = input("Enter fruit name: ")
    fruit_cost_kg = input("Enter price per kg: ")
    fruits_dict[fruit_name] = int(fruit_cost_kg)

print("Fruits with price: ", fruits_dict)
