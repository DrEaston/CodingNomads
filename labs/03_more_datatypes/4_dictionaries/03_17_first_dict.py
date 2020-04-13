'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''

result = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6:36, 7: 49, 8: 64, 9: 81, 10:100}

my_dict = {}

for i in range(1,11):
    my_dict[i]=i**2
    
print(my_dict)