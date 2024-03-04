# Logical Operators
# Logical operators are used to combine conditional statements:
# Operator	Description	                    Example
# not 	    Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
# and 	    Returns True if both statements are true	x < 5 and  x < 10
# or 	    Returns True if one of the statements is true	x < 5 or x < 4


#Condition 1     Condition 2     and     or
#True            True            True    True
#True            False           False   True
#False           True            False   True
#False           False           False   False


# Example
# Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")
# Example
# Test if a is greater than b, OR if a is greater than c:
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")
# Example
# Use the not keyword to reverse the result:
a = 200
b = 33
if not b > a:
    print("b is not greater than a")
else:
    print("b is greater than a")
# Example
# The following example will print "Yes" if a is greater than b, otherwise it will print "No":
a = 200
b = 33
print("Yes") if a > b else print("No")