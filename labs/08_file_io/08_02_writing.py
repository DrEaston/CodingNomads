'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

with  open('words.txt', 'r') as fin:
    text = (fin.readlines())  # read schoology .csv into python



with open("words_reverse.txt", "w") as fout:
    for item in text:
            fout.write(text[x])
        



with open("words_reverse.txt", "w") as fout:
    for x in reversed(range(len(text))):
            fout.write(text[x])
        
