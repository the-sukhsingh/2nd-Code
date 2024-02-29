#Python Program to demonstrate teh use of Assignment Operators
a = 10
b = 20
c = 2

c = a + b
print("The result of simple assignment is ", c)

c += a
print("The result of addition assignment is ", c)

c -= a
print("The result of subtraction assignment is ", c)

c *= a
print("The result of multiplication assignment is ", c)

c /= a
print("The result of division assignment is ", c)

c %= a
print("The result of modulus assignment is ", c)

c **= a
print("The result of exponentiation assignment is ", c)

c //= a
print("The result of floor division assignment is ", c)

#Output:
#The result of simple assignment is  30
#The result of addition assignment is  40
#The result of subtraction assignment is  30
#The result of multiplication assignment is  300
#The result of division assignment is  30.0
#The result of modulus assignment is  0.0
#The result of exponentiation assignment is  0.0
#The result of floor division assignment is  0.0