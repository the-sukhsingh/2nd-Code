# python dictionaries
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
# Example
# Create and print a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang", 
  "year": 1964
}
print(thisdict)
# Output
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:
# Example
# Get the value of the "model" key:
x = thisdict["model"]
# There is also a method called get() that will give you the same result:
# Example
# Get the value of the "model" key:
x = thisdict.get("model")
# Change Values
# You can change the value of a specific item by referring to its key name:
# Example
# Change the "year" to 2018:
thisdict["year"] = 2018
print(thisdict)
# Output
{'brand': 'Ford', 'model': 'Mustang', 'year': 2018}
# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
# Example
# Print all key names in the dictionary, one by one:
for x in thisdict:
  print(x)
# Example
# Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x])
# You can also use the values() function to return values of a dictionary:
# Example
# Print all values in the dictionary, one by one:
for x in thisdict.values():
  print(x)
# Example
# Loop through both keys and values, by using the items() function:
for x, y in thisdict.items():
  print(x, y)
# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:
# Example
# Check if "model" is present in the dictionary:

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
# Dictionary Length
# To determine how many items (key-value pairs) a dictionary has, use the len() method.
# Example
# Print the number of items in the dictionary:
print(len(thisdict))
# Adding Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
# Example
# Add a color item to the dictionary:
thisdict["color"] = "red"
print(thisdict)
# Output
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
# Removing Items
# There are several methods to remove items from a dictionary:
# Example
# The pop() method removes the item with the specified key name:
thisdict.pop("model")
print(thisdict)
# Output
{'brand': 'Ford', 'year': 1964}
# Example
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict.popitem()
print(thisdict)
# Output
{'brand': 'Ford', 'model': 'Mustang'}
# Example
# The del keyword removes the item with the specified key name:
del thisdict["model"]
print(thisdict)
# Output
{'brand': 'Ford', 'year': 1964}
# Example
# The del keyword can also delete the dictionary completely:
del thisdict
# print(thisdict) #this will cause an error because "thisdict" no longer exists.
# Example
# The clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# thisdict.clear()
# print(thisdict)
# Output
# {}
# Copy a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().
# Example
# Make a copy of a dictionary with the copy() method:

# mydict = thisdict.copy()
# print(mydict)
# Output
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
# Another way to make a copy is to use the built-in function dict().
# Example
# Make a copy of a dictionary with the dict() function:

mydict = dict(thisdict)
print(mydict)
# Output
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
# Nested Dictionaries
# A dictionary can also contain many dictionaries, this is called nested dictionaries.
# Example
# Create a dictionary that contain three dictionaries:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
}
}
# Example
# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
# The dict() Constructor
# It is also possible to use the dict() constructor to make a new dictionary:
# Example
# Create a dictionary with the dict() constructor:
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)
# Output
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
# Dictionary Methods
# Python has a set of built-in methods that you can use on dictionaries.
#-----------------------------------------------------------------------------
# Method	    Description
# clear()	    Removes all the elements from the dictionary
# copy()	    Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	        Returns the value of the specified key
# items()	    Returns a list containing a tuple for each key value pair
# keys()	    Returns a list containing the dictionary's keys
# pop()	        Removes the element with the specified key
# popitem()	    Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	    Updates the dictionary with the specified key-value pairs
# values()	    Returns a list of all the values in the dictionary
#-----------------------------------------------------------------------
# Example
# Get a list of the keys:
x = thisdict.keys()
# Example
# Get a list of the values:
x = thisdict.values()
# Example
# Get a list of the key:value pairs
x = thisdict.items()
# Example
# Check if "model" is present in the dictionary:
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
# Example
# Print the number of items in the dictionary:
print(len(thisdict))
# Example
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict["color"] = "red"
print(thisdict)
# Output
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
# Example
# Removing Items
# There are several methods to remove items from a dictionary:
# Example
# The pop() method removes the item with the specified key name:
thisdict.pop("model")
print(thisdict)
# Output
{'brand': 'Ford', 'year': 1964}
# Example
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
# Output
{'brand': 'Ford', 'model': 'Mustang'}




dict1 = {
  1:3,
  4:'John',
  'tree':12.9
}
dict1.keys()
#Output
#dict_keys([1, 4, 'tree'])
dict1.values()
#Output
#dict_values([3, 'John', 12.9])
dict1
#Output
#{1: 3, 4: 'John', 'tree': 12.9}