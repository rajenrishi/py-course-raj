# Assignment: 43
# Write a program to remove items with duplicate value from the dictionary.
# Input:
# dict_in = {1: "One", 2: "Two", 3: "Three", 4: "Four", 7: "One", 5: "Five", 8: "Three"}
# Output:
# dict_out = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}
# Hint: for loop, values(), in operator


dict_in = {1: "One", 2: "Two", 3: "Two", 4: "Four", 7: "One", 5: "Five", 8: "Two"}
dict_out = {}

for key in dict_in:
    # get values of output dictionary and check if current value is
    # present or not, if not present add the current key value to out dictionary
    out_values = dict_out.values()
    # getting the value from in dict
    in_value = dict_in[key]
    # check if in_value present in out_values or not
    if in_value not in out_values:
        dict_out[key] = in_value
    else:
        continue

print("Dictionary after removing duplicate values items: ", dict_out)
