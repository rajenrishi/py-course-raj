"""
Assignment: 69
Write a Python program to read text from a file. Each line will have a number. The Python program has to add all the numbers and print the sum.
Input:
    Text file content:
        Network cables: 10
        USB Drives: 12
        HDMI Cables: 5
        RAM: 4
        HDD: 15
Output:
    46
"""
fh = open("assign_69_text.txt", "r")
items_count = 0
for line in fh.readlines():
    quantity = line.strip().split(":")[1].strip()
    items_count = items_count + int(quantity)

print(f"Items count: {items_count}")
fh.close()
