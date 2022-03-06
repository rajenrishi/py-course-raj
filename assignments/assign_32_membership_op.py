# Write a program to check if entered character is vowel or not.
# Input should be read from user continuously until ‘quit’ string is entered.
vowel_l = ['a', 'e', 'i', 'o', 'u']
while True:
    user_in = input("Enter value: ")
    if user_in.lower() in vowel_l:
        print(f"Entered alphabet '{user_in}' is a vowel.")
    elif user_in.lower() == 'quit':
        print("Exiting the loop.")
        break
    else:
        print(f"Entered alphabet '{user_in}' is not a vowel.")
