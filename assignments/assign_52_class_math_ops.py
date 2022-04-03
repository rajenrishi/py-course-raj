# Assignment: 52
# Write a Python class MathOperations. Create “add”, “subtract” methods in the class.
# These methods take two numbers as arguments and returns the sum and difference
# respectively. Call these methods using class object and print the result.


class MathOperations:

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2


mop = MathOperations()
num_sum = mop.add(10, 12)
print("Sum of given numbers is: ", num_sum)

diff = mop.subtract(12, 10)
print("Difference of given numbers is: ", diff)

