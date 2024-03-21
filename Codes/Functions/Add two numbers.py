# Python program to demonstrate simple function in python

a = int(input('Enter first number '))
b = int(input('Enter second number '))

def fun_add(x,y):
    z = x + y
    return z

c = fun_add(a,b)

print('The sum of a and b is', c)