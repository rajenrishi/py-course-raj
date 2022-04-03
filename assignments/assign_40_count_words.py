# Assignment: 40
# Write a program to count occurrence of each word in a text. Print the same on terminal.
# Hint: Use dictionary
# Text.txt
# Str = “This is python program. This is a ppt.”

text = "This is python program. This is a ppt."
op_word_cnt = {}
words_list = text.split(" ")
print(words_list)
for wrd in words_list:
    # print(wrd)
    if wrd in op_word_cnt:
        op_word_cnt[wrd] = op_word_cnt[wrd] + 1
    else:
        op_word_cnt[wrd] = 1
print(op_word_cnt)
