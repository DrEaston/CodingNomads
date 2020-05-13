'''
Write a simple aggregate function, sum(), that takes a list a returns the sum.

'''
list_=[1,2,3,4,5]

def sum(x):
    sum=0
    for item in x:
        sum += item
    return sum

print(sum(list_))