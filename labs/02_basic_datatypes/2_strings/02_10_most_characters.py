'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
strings=[]
strings.append(input("First String:"))
strings.append(input("Second String:"))
strings.append(input("Third String:"))

strLen=[]

print("")
print("Length, String")
for item in strings:
    print (str(len(item))+ ", "+item)
    strLen.append(len(item))

maxLength=max(strLen)
longString=strings[strLen.index(maxLength)]

print("\nLongest length, Longest string: ")
print(str(maxLength)+", "+longString)
