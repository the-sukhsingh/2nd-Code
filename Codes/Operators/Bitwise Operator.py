#Python Program to demonstrate the use of bitwise operator
a = 10
b = 20
c = d = e = f = g = h = 0
c = a & b
print("The value of bitwise AND is ",c)
d = a | b
print("The value of bitwise OR is ",d)
e = a ^ b
print("The value of bitwise XOR is ",e)
f = ~a
print("The value of binary ones complement is ",f)
g = a << 2
print("The value of binary left shift by 2 digits is ", g)
h = a >> 2
print("The value of binary right shift by 2 digits is ",h)