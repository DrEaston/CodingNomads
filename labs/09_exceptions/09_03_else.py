'''
Write a script that demonstrates a try/except/else.

'''

while True:
    try:
        x = int(input("enter a number: "))
        y = int(input("another number: "))
        x/y
    except ValueError:
        print(f"last entered value is not a number")
    
    except ZeroDivisionError:
        print("can't divide by 0")

    else:
        print(x/y)