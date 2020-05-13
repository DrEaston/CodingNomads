'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''
list_ = [0, 1111, 2222, 4, 69, 9999, 19998]

gen = (x for x in list_ if x%1111==0)

print([item for item in gen])