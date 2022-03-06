# Write a program to check if two lists have any common values in them.
# L1 = [1, 2, 3, 5],                 l2=[3, 4, 5]    => Output: 3 and 5
in_list1 = [1, 2, 3, 5]
in_list2 = [3, 4, 5]
for ele in in_list1:
    if ele in in_list2:
        print(ele)
