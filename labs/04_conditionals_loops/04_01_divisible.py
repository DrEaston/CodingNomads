'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''

num=int(input("Number between 1 and 1 billion: "))

if num%3==0:
    print(f"{num} is divisible by 3")
else:
    print(f"{num} is not divisible by 3")