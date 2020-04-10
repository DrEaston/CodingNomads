'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

x=5
print(type(x))
x=float(x)
print(type(x))
y=4
print(type(y))
print(str(x//y))

x=input("Enter first value to multiply: ")
y=input("Enter first value to multiply: ")

print("The product is: "+str(float(x)*float(y)))
