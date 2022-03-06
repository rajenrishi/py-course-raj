# Write a program to find the largest number in the given list.
# Define list with only numbers.
in_list = [-1, 1, 441, 2, 3, 4, 44]
ln = None
for ele in in_list:
    if ln == None:
        ln = 0
    if ele > ln:
        ln = ele

print(f"Largest number in the list is {ln}")
