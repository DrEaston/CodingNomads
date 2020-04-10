'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
import math

amount=float(input("How much you got? "))
apr=float(input("Whats the return? "))
years=float(input("How long invested? "))
10
finalVal=amount*math.pow((1+(apr/100)),years)

print("You'll have: " + str(finalVal))