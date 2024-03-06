# Python Program to demonstrate the use of Identity Operator
a = 20
b = 20
c = 10
if (a is b):
    print("a and b have same identity")
else:
    print("a and b do not have same identity")

if (id(a) == id(b)):
    print("a and b have same identity")
else:
    print("a and b do not have same identity")

if (a is c):
    print("a and c have same identity")
else:
    print("a and c do not have same identity")

if (a is not c):
    print('a and c do not have same identity')
else:
    print('a and c have same identity')