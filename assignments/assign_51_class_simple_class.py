# Assignment: 51
# Write a Python class named Student with two attributes student_id, student_name.
# Create a method to display the attribute and their values in Student class.


class Student:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display_stu_details(self):
        print("Student ID: ", self.id)
        print("Student Name: ", self.name)


s = Student(10, "Rajendra")
s.display_stu_details()
