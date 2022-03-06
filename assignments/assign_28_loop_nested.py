# Using nested loop (while or for) print the below pattern:
# *
# *  *
# *  *  *
# *  *  *  *
# *  *  *  *  *
# print(">>>>>>>>>>>>>>> IMPLEMENTATION 1 <<<<<<<<<<<<<<<<<")
# n = 5
# for i in range(1, n+1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# Using single loop
# print(">>>>>>>>>>>>>>> IMPLEMENTATION 2 <<<<<<<<<<<<<<<<<")
n = 5
for i in range(1, n+1):
    print(f"{i * '* '}")
