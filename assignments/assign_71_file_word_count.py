"""
Assignment: 71
Write a Python program to count the number of words in the text file. Create a text file
with any data and use for writing program.
"""
word_count = {}
fh = open("assign_71_word_count.txt", "r")
text = fh.read()
# Replace newline character with space so that word splitting will happen with words
# joined by newline character
text = text.replace("\n", " ")
words_list = text.split(" ")

# Remove any extra space
words_list = [wrd.strip() for wrd in words_list]

for wrd in words_list:
    if wrd not in word_count:
        word_count[wrd] = 1
    else:
        word_count[wrd] = word_count[wrd] + 2

fh.close()
print(f"Word count: {word_count}")
