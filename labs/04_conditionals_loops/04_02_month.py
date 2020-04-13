'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''

month=int(input("What month? "))

monthList=["January","February","March","April","May","June","July","August","Septemeber","October","November","December"]

if month in range(1,12):
    print(monthList[month-1])
    #or do a bunch of elif here for each month
else:
    print("other")