# Write a program to remove duplicate elements from the list.
# Example: [1,1,2,3,4,4] == [1,2,3,4]   => pop or remove
in_list = [1, 1, 2, 3, 4, 4, 4,4,4,4,4,4]
out_list = []
for ele in in_list:
    if ele not in out_list:   # [1, 2]
        out_list.append(ele)

print(out_list)
