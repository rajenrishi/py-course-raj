# Assignment: 38
# Write a program to create dictionary by taking keys and values from two lists:
# subjects: [“English”, “Science”, “Mathematics”, “Social”, “Computers”]
# marks: [45, 53, 67, 33, 76]
# Output:
# {“English”:45, “Science”:53, “Mathematics”:67, “Social”:33, “Computers”:76}
# Hint: Use loop

subjects = ["English", "Science", "Mathematics", "Social", "Computers"]
marks = [45, 53, 67, 33, 76]
sub_marks_dict = {}
for i in range(len(subjects)):
    sub_marks_dict[subjects[i]] = marks[i]

print("Dict with subjects and marks: ", sub_marks_dict)
