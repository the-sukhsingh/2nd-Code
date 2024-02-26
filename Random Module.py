from random import *
print(random()) # returns a random float between 0.0 and 1.0
print(randint(1, 10)) # returns a random integer between 1 and 10
print(randrange(1, 10, 2)) # returns a random odd integer between 1 and 10
seed(1) # sets the seed for the random number generator
print(uniform(1, 10)) # returns a random float between 1.0 and 10.0
print(shuffle([1, 2, 3, 4, 5])) # shuffles the list and returns None
print(choice([1, 2, 3, 4, 5])) # returns a random element from the list
print(sample([1, 2, 3, 4, 5], 2)) # returns a random 3-element list from the list
