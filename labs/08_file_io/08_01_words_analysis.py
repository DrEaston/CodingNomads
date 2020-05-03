'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''

with  open('words.txt', 'r') as fin:
    text = (fin.readlines())  # read schoology .csv into python

shortest_word = min(text, key=lambda word: len(word))
longest_word = max(text, key=lambda word: len(word))

short_words = [item for item in text if len(item)==len(shortest_word)]
long_words = [item for item in text if len(item)==len(longest_word)]

for item in short_words:
    print(item)
    
for item in long_words:
    print(item)
    
print(f"The length of the list is: {len(text)}")