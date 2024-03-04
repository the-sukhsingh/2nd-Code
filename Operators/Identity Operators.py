# Identity Operators
# Identity operators are used to compare the objects, not if they are equal, 
#   but if they are actually the same object, with the same memory location:
# Operator	        Description	                        Example
# is 	            Returns True if both variables       x is y
#                    are the same object	           
# is not	        Returns True if both variables       x is not y
#                    are not the same object
# Example
# Check if two objects are the same object:
# Example
# Check if two objects are not the same object:
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
# Output
# a and b have same identity
# a and b have same identity
# a and c do not have same identity
# a and c do not have same identity