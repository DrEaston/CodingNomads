'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''

def my_enumerate(iterable):
    count = 0
    output = []
    for item in iterable:
        count += 1
        output.append((count, item))
    return output
          

    
    
print(my_enumerate(['cats','dogs','spiders','frogs']))
    
