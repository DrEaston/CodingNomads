'''
Print out every prime number between 1 and 100.

'''
for i in range(2,101):
    divisors=0
    for j in range(2,i):
        if i%j==0:
            divisors += 1
    if divisors==0:
        print(i)

        