# Write a program to create list with the characters from a sentence.
# Only alphabets should be included other characters like spaces,
# special characters and numbers should be excluded.
# Also the find the number of alphabets used to make the sentence.
# Input sentence: "Exerci$e @ Progr@m“
# Output:
# Character List: ['E', 'x', 'e', 'r', 'c', 'i', 'e', 'P', 'r', 'o', 'g', 'r', 'm']
# Number of alphabets in sentence: 13
inl = "Exerci$e @ Progr@m"
ol = []
for ch in inl:
    if ch.isalpha():
        ol.append(ch)

print(f"Output list is: {ol}")
