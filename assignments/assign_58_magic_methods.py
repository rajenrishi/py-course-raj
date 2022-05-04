"""
Assignment: 58
Write a program to create a ManDays class. This class will take number of days an employee
worked. Number of days is passed during object initialization.
Write one more class named Employee. This class will take salary per day for the employee.
This value is passed during object initialization.
Now using multiplication magic method (__mul__) and calculate the salary of the employee.
Salary is number of days multiplied by salary per day.
"""


class ManDays:
    def __init__(self, num_days):
        self.num_days = num_days


class Employee:
    def __init__(self, sal_day):
        self.sal_day = sal_day

    # Override multiplication magic method
    # other argument will have ManDays object
    def __mul__(self, other):
        return self.sal_day * other.num_days


man_days = ManDays(4)
emp = Employee(1000)

sal_to_pay = emp * man_days
print(f"Total salary to be paid to employee: {sal_to_pay}")
