# decorator that prints the values of the parameters passed into it

import functools

def printparams(fn):

    @functools.wraps(fn)
    def inner(*args, **kwargs):

        print('the passed arguments are, ', args)
        print('the passed keyword arguments are, ', kwargs)

        # the dilemma here, return a function or just call it?
        return fn(*args, **kwargs)
    return inner
    

@printparams
def add(a, b):
    return a + b
    

@printparams
def printUser(name, age):
    print('Hey your name is {}, and you are {} years old'.format(name, age))
    

add(4, 5)
printUser('Daniel Chia', 23)
