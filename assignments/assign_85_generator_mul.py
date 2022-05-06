"""
Assignment: 85
Write a Python program develop custom iterator which will generate multiples of 4.
It should be able to generate 10 values.
"""


def gen_num():
    for i in range(10):
        yield i * 4


for el in gen_num():
    print(el)
