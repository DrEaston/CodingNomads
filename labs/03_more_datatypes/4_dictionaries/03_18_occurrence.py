'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''

my_str=input("Pls enter a string: ")
my_dict={}

for item in my_str:
    if item==" ":
        pass
    else:
        my_dict[item]=my_str.count(item)
        
print(my_dict)
            