# memoize factorial function
import functools

def memoize(fn):

    # it makes sense that this doesn't run all the time, cus it would just get reassigned everytime
    # so I'm guessing that this doesn't run
    cache = {}
    # why is this only called once?
    print('Start of the decorator \n')

    @functools.wraps(fn)
    def inner(n):
        # since inner is the function returned, it could be said that it takes the same arguments as the original function
        print('=========================')
        print('inner is being called, before factorial')
        print('current n is, ', n, ' and the current cache is ', cache)

        if n not in cache:
            print('hey i entered the if statement \n')
            # this is the line that changes everything

            # things are stuck in here for a while
            # here is where fact is first called
            cache[n] = fn(n)
            print('i dont know whats going on ', cache)

        return cache[n]
    return inner


@memoize
def factorial(n):
    if n == 0:
        return 1

    # for some strange reason, this runs before inner
    print('from factorial, current n is ', n)

    # starts a new fact call, which is also wrapped by the decorator
    return n * factorial(n-1)

print(factorial(5))

