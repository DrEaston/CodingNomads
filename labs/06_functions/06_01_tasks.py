'''

Write a script that completes the following tasks.

'''


def div_4or7(n):
    if n % 4 == 0 or n % 7 == 0:
        return True
    else:
        return False


def div_4and7(n):
    if n % 4 == 0 and n % 7 == 0:
        return True
    else:
        return False


def num_under_1billion(n):
    if 1 < n < 1000000000:
        num = n
        return (n)
    else:
        print("number not between 1 and a billion")


a = div_4or7(4)
print(a)

b = div_4or7(14)
print(b)

c = div_4and7(5)
print(c)

d = div_4and7(28)
print(d)

e = num_under_1billion(20004)
print(e)


# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

# take in a number from the user between 1 and 1,000,000,000

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 

# print your new variables to display the results
