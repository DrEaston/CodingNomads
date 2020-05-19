'''
Write a script with a function that demonstrates the use of **kwargs.

'''

things_i_like={'like1':'pizza','like2':'piano','like3':'butts'}

def shout(**likes):
    for index, pleasure in things_i_like.items():
        print(index, pleasure)
        
shout(**things_i_like)