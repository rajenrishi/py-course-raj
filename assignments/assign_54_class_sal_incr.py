# Assignment: 54
# Write a Python class named Employee with attributes “age”, “name”, “salary”.
# Add two methods => one method to increase the age of the Employee and another
# to increase the salary of the employee by 30%.


class Employee:
    # Class variable to hold number of books in library
    total_books = 0

    def __init__(self, emp_name, emp_age, emp_salary):
        self.emp_name = emp_name
        self.emp_age = emp_age
        self.emp_salary = emp_salary

    def update_emp_age(self):
        self.emp_age = self.emp_age + 1

    def update_emp_sal(self, sal_percent):
        self.emp_salary = (self.emp_salary*30)/100 + self.emp_salary

    def display_emp_details(self):
        print("Employee Name: ", self.emp_name)
        print("Employee Age: ", self.emp_age)
        print("Employee Salary: ", self.emp_salary)


# Add three books
emp1 = Employee("emp1", 31, 1000)
emp1.update_emp_age()

# Employee details after updating age
emp1.display_emp_details()

# Increment the salary
emp1.update_emp_sal(30)

# Employee details after updating salary
emp1.display_emp_details()
