'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''

lenList=int(input("How long is your list?"))
list_=[]
for i in range(lenList):
    list_.append(int(input("Enter list element: ")))

list_.sort()
tupleList=[]

if len(list_)%2==1:
    list_.append(0)
    
count=0

while count<len(list_):
    tempTuple=(list_[count],list_[count+1])
    tupleList.append(tempTuple)
    count+=2
    
print(tupleList)
    
    
        