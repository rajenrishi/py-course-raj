# Define a list with integers [6, 2, 2, 6, 2, 2, 2].
# Using nested loop print the character ‘@’ the number of times given in the list.

print(">>>>>>>>>>>>>>> IMPLEMENTATION 1 <<<<<<<<<<<<<<<<<")
in_list = [1, 2, 3, 4, 5, 2, 2]
for ele in in_list:
    for j in range(ele):
        print("@", end=" ")
    print()

# print(">>>>>>>>>>>>>>> IMPLEMENTATION 2 <<<<<<<<<<<<<<<<<")
# in_list = [6, 2, 2, 6, 2, 2, 2]
# for ele in in_list:
#     print(f"{ele * '@'}")
