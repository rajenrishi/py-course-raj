# In the given list rearrange the items so that all numbers and all strings are together.
# Input list: [87, 3, “PY”, 4, “P”, 5, “RR”, “RT”, 44, 31, “RET”]
# Output list: [87, 3, 4, 5, 44, 31, “RR”, “P”, “RT”, “PY”, “RET”]
# Note: Use insert() method. List items order can be anything.
in_list = ["we", 87, 3, "PY", 4, "P", 5, "RR", "RT", 44, 31, "RET"]
out_list = []
for ele in in_list:
    if str(ele).isnumeric():
        out_list.insert(0, ele)   # [3, 87, "we"]
    else:
        out_list.append(ele)    # [3, 87, "we", "PY"]

print(out_list)
