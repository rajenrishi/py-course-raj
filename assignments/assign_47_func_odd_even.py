# Assignment: 47
# Write a program to define a function which takes a number and
# returns if the number is Odd or Even number.

def odd_even(num):
    rem = num%2
    if rem == 0:
        return "even"
    else:
        return "odd"

ret = odd_even(13)
print("The given number is an '{}' number.".format(ret))
