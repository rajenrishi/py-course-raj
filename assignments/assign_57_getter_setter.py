"""
Assignment: 57
Write a program to create a Employee class. Create a private variable to save
salary (__sal) and public variable which takes the grade of employee.
Salary & grade (A, B, C) will be passed during object initialization.
Now write getter & setter method to get and update the salary of the employee.
In setter method; if the employee belongs to grade A, increase the salary by 15%;
if grade B, increase by 10%; if grade C increase by 5%.
In getter method; return the update salary.
"""


class Employee:
    grade_int = {
        "A": 15,
        "B": 10,
        "C": 5
    }

    def __init__(self, salary, grade):
        self.__salary = salary
        self.grade = grade

    def set_sal(self):
        increment = (self.__salary * Employee.grade_int[self.grade])/100
        self.__salary = self.__salary + increment

    def get_sal(self):
        return self.__salary


emp1 = Employee(10000, 'A')
emp1.set_sal()
new_sal = emp1.get_sal()
print(f"Employees new salary: {new_sal}")


emp2 = Employee(10000, 'B')
emp2.set_sal()
new_sal = emp2.get_sal()
print(f"Employees new salary: {new_sal}")


emp3 = Employee(10000, 'C')
emp3.set_sal()
new_sal = emp3.get_sal()
print(f"Employees new salary: {new_sal}")
