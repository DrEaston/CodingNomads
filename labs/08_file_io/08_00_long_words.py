'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''

with  open('words.txt', 'r') as fin:
    text = (fin.readlines())  # read schoology .csv into python
for item in text:  # iterate through all the quiz scores to be added
    if len(item) >= 20:
        print(item)