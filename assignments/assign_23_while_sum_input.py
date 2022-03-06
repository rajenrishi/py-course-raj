# Write a program to find the sum of the numbers accepted
# from the user, until user types ‘stop’.
usr_sum = 0
max_entries_allowed = 5
while max_entries_allowed > 0:
    usr_in = input("Enter number or 'stop' to exit: ")
    if usr_in.lower() == 'stop':
        print("Exiting...")
        break
    usr_sum = usr_sum + int(usr_in)
    max_entries_allowed = max_entries_allowed - 1
else:
    print("Max entries completed.")

print(f"Sum of user input numbers is: {usr_sum}")
# TODO: above code handle in case user never enters stop
