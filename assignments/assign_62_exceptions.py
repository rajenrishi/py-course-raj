"""
Assignment: 62
Write a program to define a function which will take two numbers and performs division.
If any number is Zero, the function will throw exception.
"""


def div(a1, b1):
    try:
        if b1 == 0:
            raise ValueError("Divisor cannot be zero.")

        return a1/b1

    except ValueError as e:
        print(e)
        return None


a = 10
b = 0
ret = div(a, b)
print(f"Division result: {ret}")
