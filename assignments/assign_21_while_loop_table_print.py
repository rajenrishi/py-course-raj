# Read the number from user, print the table of number entered by user
# using while loop. Print table till 10.
num = int(input("Enter number: "))
max_cnt = 1
while max_cnt <= 10:
    print(f"{num:4} X {max_cnt:2} = {num * max_cnt:5}")
    max_cnt = max_cnt + 1
