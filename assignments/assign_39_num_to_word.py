# Assignment: 39
# Write a program to convert the user entered number into words.
# Input: 123
# Output: One Two Three

num_in_words = {1: "One", 2: "two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 0: "Zero"}
# Read number from the user
num = input("Enter number: ")

for dig in num:
    print(num_in_words[int(dig)], end=" ")
