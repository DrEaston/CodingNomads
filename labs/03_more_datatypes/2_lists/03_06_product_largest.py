'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''

noInputs=10
count=0
numbahList=[]
product=1
while count<10:
    numbah=input("Gimme a numbah: ")
    numbahList.append(int(numbah))
    count+=1
    product*=int(numbah)
    
print(numbahList)
print("Max number: "+str(max(numbahList)))
print("Product is: "+str(product))

        
