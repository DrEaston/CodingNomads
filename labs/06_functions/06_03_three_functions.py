'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''


def echo(name):
    name= name + " " + name
    print(name)
    return echo1(name)

def echo1(name):
    name = name + " " + name
    print(name)
    return echo2(name)

def echo2(name):
    name = input("Name?\n")
    while name != "stop already":
        return echo(name)

echo("cats")