# Write a program to find the occurrences of a given list item.
# [1,1,2,1,4,1,5] ==> 2 is occurring one time in the list.
in_list = [1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 44]
val = 2
cnt = 0
for ele in in_list:
    if ele == val:
        cnt = cnt + 1

print(f"Number of times '{val}' occurring in list is: {cnt}")
