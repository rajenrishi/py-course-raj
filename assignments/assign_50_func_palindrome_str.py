# Assignments: 50
# Write a program to check if a string is palindrome or not.
# str = "madam"
# # reverse the string
# rev_string = ""
#
# if str == rev_string:
#     print("palindrome")
# else:
#     print("Not a palindrome")


def is_palindrome_str(name):
    # reverse the string
    rev_str = ""
    for i in range(len(name)-1, -1, -1):
        rev_str = rev_str + name[i]
    print("Reversed string: ", rev_str)
    if name == rev_str:
        return True
    else:
        return False


ret = is_palindrome_str("madam")
if ret:
    print("Given string is palindrome.")
else:
    print("Given string is not palindrome.")
