#Bitwise Operators
#Bitwise operators are used to compare (binary) numbers:
#Operator	        Name	        Description
#&	                AND	            Sets each bit to 1 if both bits are 1
#|	                OR	            Sets each bit to 1 if one of two bits is 1
#^	                XOR	            Sets each bit to 1 if only one of two bits is 1
#~	                NOT	            Inverts all the bits
#<<	            Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
#>>	            Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
# Example
# 5 =       0101
# 3 =       0011
# 5 & 3 =   0001
# 5 | 3 =   0111
# 5 ^ 3 =   0110
# ~5 =      1010
# 5 << 1 =  1010
# 5 >> 1 =  0010

#Python Program to demonstrate the use of Bitwise Operator
a = 10
b = 20
c = 0
c = a & b
print("The value of bitwise AND is ", c)
d = a | b
print("The value of bitwise OR is ", d)
e = a ^ b
print("The value of bitwise XOR is ", e)
f = ~a
print("The value of bitwise NOT is ", f)
g = a << 2
print("The value of binary left shift by 2 digits is ", g)
h = a >> 2
print("The value of Binary right shift by 2 digits is ", h)
# Output
# The value of bitwise AND is  0
# The value of bitwise OR is  30
# The value of bitwise XOR is  30
# The value of bitwise NOT is  -11
# The value of binary left shift by 2 digits is  40
# The value of Binary right shift by 2 digits is  2
