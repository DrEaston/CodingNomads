'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

'''
list_ = [0, 1111, 2222, 4, 69, 9999, 19998]

gen = (x for x in list_ if x%1111==0)

print([item//1111 for item in gen])


# I get the number of times 1111 goes into each number in gen