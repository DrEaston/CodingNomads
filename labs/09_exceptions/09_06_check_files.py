'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

file_name = 'integers.txt'

try:
    with open(file_name, 'r') as fin:
        data=int(fin.readline())
        print(data*data)
except FileNotFoundError:
        print("check file name and location")
except ValueError:
        print("check data type")