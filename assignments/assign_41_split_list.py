# Assignment: 41
# Write a program to split a list into two with numbers lesser than and
# greater than user input number.
# If the value of list is same as given number that number should be discarded.
# Input:
# value = 12
# num_list = [3, 10, 5, 21, 31, 11, 7, 22, 15, 19]
# Output:
# less_list = [3, 10, 5, 7, 11]
# greater_list = [21, 22, 31, 19, 15]

num_list = [3, 10, 5, 21, 31, 11, 7, 22, 15, 19]
value = int(input("Enter number: "))
less_list = []
greater_list = []
for vl in num_list:
    if vl < value:
        less_list.append(vl)
    elif vl > value:
        greater_list.append(vl)
    else:
        pass
print(less_list)
print(greater_list)
