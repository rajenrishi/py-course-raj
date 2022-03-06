# Write a program to find the sum of the numbers accepted from the user.
usr_sum = 0
MAX_ENTRIES = 100
for n in range(MAX_ENTRIES):
    usr_in = input("Enter number or 'stop' to exit: ")
    if usr_in.lower() == 'stop':
        print("Exiting...")
        break
    usr_sum = usr_sum + int(usr_in)

print(f"Sum of user input numbers is: {usr_sum}")

