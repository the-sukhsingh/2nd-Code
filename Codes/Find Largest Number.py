# Python Program to find Largest of three numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if (num1 > num2) and (num1 > num3):
    largest = num1
elif (num2 > num3) and (num2 > num1):
    largest = num2
else:
    largest = num3
print("The largest number among ",num1,",",num2," and ", num3," is ", largest)