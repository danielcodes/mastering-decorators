# Write a decorator that caches the n most recent return values from the function it is applied to, so that the function does not have to be invoked again.
# so an outer wrap, to pass the n parameter
# what it sounds like to me, create decorator that caches n values
# but how to make a dictionary of certain length?

# this is for later, but the actual problem actually involves creating a queue like data structure, to save the n most recent

# ok so the n values cache is doable, start there

# create a dictionary, 
# start by creating a queue like structure

# its already a mess
def saveresults(n):
    def decorator(fn):

        # todo: set a length 

        cache = {}

        def inner(*args, **kwargs):
            if args[0] not in cache:
                print('caching now')
                cache[args[0]] = fn(*args, **kwargs)

            print('the arg is ', args[0])
            print('the current cache is ', cache)
            return cache[args[0]]
        return inner    
    return decorator

@saveresults(5)
def powerup(a):
    return a * a

print('the real result is ', powerup(5))
print('the real result is ', powerup(10))
print('the real result is ', powerup(5))



