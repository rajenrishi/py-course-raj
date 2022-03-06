# Define a variable “a = 0b10111011”. Use a bitmask so that all the
# bits are flipped. Use any bitwise operator.
# Print the output in binary format.
a = 0b10111011
bm = 0b11111111
ret = a ^ bm
print(bin(ret))
