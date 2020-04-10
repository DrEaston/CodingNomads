'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''

myString=input("Whats your string? ")

a=myString.count("a")
e=myString.count("e")
i=myString.count("i")
o=myString.count("o")
u=myString.count("u")

total=a+e+i+o+u


print("There are " + str(total) + " vowels. Breakdown by letter:")

print("a: "+str(a))
print("e: "+str(e))
print("i: "+str(i))
print("o: "+str(o))
print("u: "+str(u))

