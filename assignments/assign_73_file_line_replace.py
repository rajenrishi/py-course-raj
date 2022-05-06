"""
Assignment: 73
Write a Python program to replace a word in text file with new word.
For example replace Java with Python and write to a new file.
Input text file 1:
Java is a popular language.
Java is used in many applications.
"""

fhr = open("assign_73_line_replace.txt", "r")
fhw = open("assign_73_line_after_replace.txt", "w")
data = fhr.read()
new_data = data.replace("Java", "Python")
print(new_data)
fhw.write(new_data)
