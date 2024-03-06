#Python Program to demonstrate the use of Logical Operators
a = 10
b = 20
c = 30
if ((a>b) and (a>c)):
    print("a is the greatest number")
if ((b>c) and (b>a)):
    print("b is the greatest number")
if ((c>a) and (c>b)):
    print("c is the greatest number")
if ((a>0) and a % 2 == 0):
    print("a is an even integer.")
if ((a>b) or (c>a)):
    print("The statement is being printed as the demonstration of OR operation in Logical Operators")
if (not(a>b)):
    print("b is greater")