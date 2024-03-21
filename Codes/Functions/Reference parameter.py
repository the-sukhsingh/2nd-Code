# Python program to demonstrate call by reference in a fuction

def changeme(mylist):
    mylist.append([1,2,3,4])
    print('Values inside the function is ',mylist)

list1 = [10,20,30]
list2 = [40,50,60]

changeme(list1)
print('The value outside the function is ',list1)

changeme([40,50,60])
print('The value outside the function is ',list2)