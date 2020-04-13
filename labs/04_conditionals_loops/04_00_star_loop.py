'''

Write a loop that for a number n prints n rows of stars in a triangle shape.

For example if n is 3, you print:

*
**
***

'''


n=int(input('How many rows? '))

stars='*'

for i in range(n):
    print(stars*(i+1))

