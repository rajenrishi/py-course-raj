# Assignment: 44
# Write a program calculate total marks and percentage of each student from the
# given nested dictionary. Add one more key called Result. If the percentage is
# greater than 75 then value will be First Class, if less than 75 value will be Second Class
# Input Dictionary:
# student_marks = {
#     "Anil": {"Mathematics": 80, "Computers": 90, "English": 66, "Social": 83, "Science": 78},
#     "Siri": {"Mathematics": 4, "Computers": 7, "English": 2, "Social": 7, "Science": 1},
#     "Rajiv": {"Mathematics": 100, "Computers": 100, "English": 99, "Social": 98, "Science": 97},
#     "Harish": {"Mathematics": 80, "Computers": 90, "English": 66, "Social": 83, "Science": 78},
#     "Sahasra": {"Mathematics": 95, "Computers": 92, "English": 78, "Social": 97, "Science": 69}
# }
# Note: Nested for loop
#     Output Dictionary:
#     students_result = {
#         "Anil": {"Total": xx, "Percentage": yy, "Result": "First Class"},
#         "Siri": {"Total": xx, "Percentage": yy, "Result": "First Class"},
#         "Rajiv": {"Total": xx, "Percentage": yy, "Result": "Second Class"},
#         "Harish": {"Total": xx, "Percentage": yy, "Result": "First Class"},
#         "Sahasra": {"Total": xx, "Percentage": yy, "Result": "First Class"}
#     }

student_marks = {
    "Anil": {"Mathematics": 80, "Computers": 90, "English": 66, "Social": 83, "Science": 78},
    "Siri": {"Mathematics": 4, "Computers": 7, "English": 2, "Social": 7, "Science": 1},
    "Rajiv": {"Mathematics": 100, "Computers": 100, "English": 99, "Social": 98, "Science": 97},
    "Harish": {"Mathematics": 80, "Computers": 90, "English": 66, "Social": 83, "Science": 78},
    "Sahasra": {"Mathematics": 95, "Computers": 92, "English": 78, "Social": 97, "Science": 69}
}
students_result = {}

for stu in student_marks:
    # get marks list
    res = {"Total": 0, "Percentage": 0, "Result": ""}
    marks = student_marks[stu]
    for sub in marks:
        res["Total"] = res["Total"] + marks[sub]

    res["Percentage"] = (res["Total"]/(100*len(marks))) * 100
    if res["Percentage"] >= 75:
        res["Result"] = "First Class"
    else:
        res["Result"] = "Second Class"

    students_result[stu] = res

print("Students results: \n", students_result)
