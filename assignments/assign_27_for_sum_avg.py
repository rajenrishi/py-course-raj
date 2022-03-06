# Accept 10 numbers from the user and display their average.
usr_sum = 0
MAX_ENTRIES = 10
for n in range(MAX_ENTRIES):
    usr_in = input("Enter number: ")
    usr_sum = usr_sum + int(usr_in)

print(f"Average of user input numbers is: {usr_sum/MAX_ENTRIES}")
