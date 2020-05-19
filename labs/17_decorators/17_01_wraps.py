'''
Write a decorator function that wraps text passed to it in a html <p> tag.

'''
def decorate(func):
    def wrapper(item):
        return "<p>"+ func(item) + "</p>"
    return wrapper


@decorate
def shout(msg):
    return msg


a=shout("message")
print(a)