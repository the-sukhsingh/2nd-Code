# Membership Operators
# Membership operators are used to test if a sequence is presented in an object:
# Operator	Description	                                            Example
# in 	    Returns True if a sequence with the specified           x in y 
#              value is present in the object  
# not in	Returns True if a sequence with the specified           x not in y
#              value is not present in the object
# Example
# Check if "apple" is present in the fruit object:
# Example
# Check if "apple" is NOT present in the fruit object:
##                      fruit = ["apple", "banana"]
##                      if "apple" in fruit:
##                          print("Yes, apple is a fruit!")
##                      fruit = ["apple", "banana"]
##                      if "apple" not in fruit:
##                          print("No, apple is a fruit!")
##                      else:
##                          print("Yes, apple is a fruit!")
# Output
# Yes, apple is a fruit!
# Yes, apple is a fruit!



# Python Program to demonstrate the use of Membership Operator
a = 10
b = 2
c = 'h'
d = 'l'
str1 = 'Sukhjit'
list1 = [1, 2, 3, 4, 5]
tup1 = (1,10,'Sukhjit',30)

if (c in str1):
    print("c is a member of str1")
if (d not in str1):
    print("d is not in str1")

if (a in list1):
    print("a is a member of list1")
elif(a not in list1):
    print("a is not a member of list1")
else:
    print('We have tested membership operators for lists')

if (b in list1):
    print("b is a member of list1")
else:
    print("b is not a member of list1")
if (str1 in tup1):
    print('string 1 is a member of tup1')
else:
    print('string 1 is not a member of tup1')

# Output:
# c is a member of str1
# d is not in str1
# a is a member of list1
# b is not a member of list1
# string 1 is a member of tup1