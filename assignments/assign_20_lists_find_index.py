# Write a program to find the occurrences of a given list item.
# [1,1,2,1,4,1,5] ==> 2 is occurring one time in the list.
in_list = [1, 2, 2, 3, 4, 44]
val = 4
index = -1
for ele in in_list:
    index = index + 1
    if ele == val:
        break
print(f"Element '{val}' is located at index: {index}")
