'''
Write a script with a function that demonstrates the use of *args.

'''
things_i_like=['pizza','piano','butts']

def shout(*likes):
    for pleasure in things_i_like:
        print(pleasure)
        
shout(things_i_like)