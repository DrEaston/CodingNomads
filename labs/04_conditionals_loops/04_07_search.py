'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

#I'm assuming this is just to test a "while" loop and am not writing this code efficiently

num=int(input("Enter a number from 0 to a billion: "))
count=0
while count<=1000000000:
    if count==num:
        print("Your number is: "+str(num))
        break
    count+=1


    
