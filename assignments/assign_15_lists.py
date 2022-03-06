# Split the below input list into two lists; one list with only
# numbers and other with only strings.
# Input list = [3, 4, “P”, 5, “RR”, “RT”, 44, 31, “RET”]
# Tip: user for loop, append, if else, string methods eg: isalnum()
# Output: Two lists should be created
in_list = [3, 4, "P", 5, "RR", "RT", 44, 31, "RET"]
num_list = []
str_list = []
for ele in in_list:
    if str(ele).isalpha():
        str_list.append(ele)
    else:
        num_list.append(ele)

print(num_list)
print(str_list)
