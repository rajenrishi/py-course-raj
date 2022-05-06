"""
Assignment: 86
Write a Python program develop custom generator. This generator will generate lengths of
the strings passed. Use string list as input.
"""


str_list = ["the", "python", "tutorial", "course"]


def gen_str_len(l):
    for s in l:
        yield len(s)


for str_l in gen_str_len(str_list):
    print(str_l)
