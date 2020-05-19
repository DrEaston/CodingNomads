'''
Improve the decorator from the previous exercise by allowing it to take
any specified HTML tag as an input - making it more general.

'''

def decorate(func):
    def wrapper(tag,item):
        return tag+ func(item) + tag[0] + "/" + tag[1:]
    return wrapper


@decorate
def shout(msg):
    return msg


a=shout('<m>',"message")
print(a)