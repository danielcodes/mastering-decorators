# Write a decorator that caches the n most recent return values from the function it is applied to, so that the function does not have to be invoked again.

# create a dictionary, 
# start by creating a queue like structure

# CURRENT PROBLEM
# the actual data structure that is needed is a queue of n length
# if the queue is full, push an element in and drop the first one

# another problem is the cache, since we have a queue (list), we have to store a dictionary for each element
# on lookup, we have to collect the keys and do a check against that

# its already a mess

from functools import reduce

def saveresults(n):
    def decorator(fn):

        # todo: set a length 
        cache = []
        keys = []

        def inner(*args, **kwargs):

            # two checks, the key is not there and list is not full
            if args[0] not in keys:
                print('caching now***********')

                # push a dictionary in
                cache.append(fn(*args, **kwargs))
                keys.append(args[0])

                print('the arg is ', args[0])
                print('the current keys are ', keys, ' *********')
                print('the current cache is ', cache, ' *********')

                # the return is also a pain

            # have to do a look up here as well
            # if the value is in the cache, thennnn
            print('the index of the key is ', keys.index(args[0]))
            index = keys.index(args[0])

            return cache[index]
        return inner    
    return decorator

@saveresults(5)
def powerup(a):
    return a * a

a = [powerup(i) for i in range(6)]

print('the a list is ', a)


b = [powerup(i) for i in range(3)]

print('the b list is ', b)
