#Python Lists
#List
#List is a collection which is ordered and changeable. Allows duplicate members.
#In Python lists are written with square brackets.
#Example
#Create a List:
list1 = [1,2,3,4,5,3+2j,3.14,"apple","banana","cherry"]
thislist = ["apple", "banana", "cherry"]
print(thislist) #['apple', 'banana', 'cherry']
print(thislist*2) #['apple', 'banana', 'cherry', 'apple', 'banana', 'cherry']
#Access Items
#You access the list items by referring to the index number:
#Example
#Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1]) #banana
#Change Item Value
#To change the value of a specific item, refer to the index number:
#Example
#Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) #['apple', 'blackcurrant', 'cherry']
#List Length
#To determine how many items a list has, use the len() method:
#Example
#Print the number of items in the list:
thislist = ["apple", "banana", "cherry"]
print(len(thislist)) #3
#Add Items
#To add an item to the end of the list, use the append() method:
#Example
#Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) #['apple', 'banana', 'cherry', 'orange']
#To add an item at the specified index, use the insert() method:
#Example
#Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) #['apple', 'orange', 'banana', 'cherry']
#Remove Item
#There are several methods to remove items from a list:
#Example
#The remove() method removes the specified item:
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) #['apple', 'cherry']
#The pop() method removes the specified index, (or the last item if index is not specified):
#Example
#The pop() method removes the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) #['apple', 'banana']
#The del keyword removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) #['banana', 'cherry']
#The del keyword can also delete the list completely:
thislist = ["apple", "banana", "cherry"]
del thislist
#print(thislist) #this will cause an error because "thislist" no longer exists.
#The clear() method empties the list:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) #[]
#Copy a List
#You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
#There are ways to make a copy, one way is to use the built-in List method copy().
#Example
#Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist) #['apple', 'banana', 'cherry']
#Another way to make a copy is to use the built-in method list().
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist) #['apple', 'banana', 'cherry']
#Join Two Lists
#There are several ways to join, or concatenate, two or more lists in Python.
#One of the easiest ways are by using the + operator.
#Example
#Join two list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3) #['a', 'b', 'c', 1, 2, 3]
#Another way to join two lists are by appending all the items from list2 into list1, one by one:
#Example
#Append list2 into list1:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1) #['a', 'b', 'c', 1, 2, 3]
#Or you can use the extend() method, which purpose is to add elements from one list to another list:
#Example
#Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1) #['a', 'b', 'c', 1, 2, 3]
