'''
Demonstrate the use of the .enumerate() function.

'''
list_ = ['cats','dogs','mice','birds','starfish']

obj1= enumerate(list_)

[print(index, animal) for index, animal in obj1]