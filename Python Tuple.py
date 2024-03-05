#Python Tuple
#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
#Example
#Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple) #Output: ('apple', 'banana', 'cherry')
#Access Tuple Items
#You can access tuple items by referring to the index number, inside square brackets:
#Example
#Print the second item in the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) #Output: banana
#Negative Indexing
#Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
#Example
#Print the last item of the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) #Output: cherry
#Range of Indexes
#You can specify a range of indexes by specifying where to start and where to end the range.
#When specifying a range, the return value will be a new tuple with the specified items.
#Example
#Return the third, fourth, and fifth item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) #Output: ('cherry', 'orange', 'kiwi')
#Range of Negative Indexes
#Specify negative indexes if you want to start the search from the end of the tuple:
#Example
#This example returns the items from index -4 (included) to index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1]) #Output: ('orange', 'kiwi', 'melon')
#Change Tuple Values
#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
#Example
#Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x) #Output: ('apple', 'kiwi', 'cherry')
