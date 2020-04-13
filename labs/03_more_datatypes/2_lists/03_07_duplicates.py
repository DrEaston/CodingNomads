'''

Write a script that removes all duplicates from a list.

'''

list_ = [1, 2, 3, 4, 3, 4, 5]

testAll="False"

for x in range(len(list_)-2):
    for y in range(x+1,len(list_)-1):
        if list_[x]==list_[y]:
            del(list_[y])
            
print(list_)

    
    