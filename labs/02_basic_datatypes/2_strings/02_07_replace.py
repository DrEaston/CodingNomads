'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

good=input("Tell me sumthin good  ")
symbol=input("Whats your sign? ")

first=good[0]

good=good.replace(first,symbol)

print(good)