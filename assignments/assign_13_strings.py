# Define a string with value “string methods demo” and perform the below operations:
# 1. Convert string to upper case and print the output on the terminal.
# 2. Replace the word “demo” with new string “class” and print the output.
# 3. Count the number of occurrences of “s”.
# 4. Using string slicing method print “method” as output.
str_in = "string methods demo"

out_1 = str_in.upper()
print(out_1)

out_2 = str_in.replace("demo", "class")
print(out_2)

out_3 = str_in.count("s")
print(out_3)

out_4 = str_in[7:13]
print(out_4)
