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