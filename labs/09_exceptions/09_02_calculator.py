'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''
while True:
    try:
        x = int(input("enter a number: "))
        y = int(input("another number: "))
        print(x/y)
        
    except ValueError:
        print(f"last entered value is not a number")
        
    except ZeroDivisionError:
        print("can't divide by 0")