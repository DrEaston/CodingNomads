'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

#the quick brown fox jumped over the lazy dog because the dog is lazier than the fox

sentence=input("Gimme a sentence: ") 
splitSent=sentence.split()
occurrances=[]

for item in splitSent:
    occurrances.append(splitSent.count(item))

print()    
print(splitSent[occurrances.index(max(occurrances))])
