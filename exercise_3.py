# Write a decorator that caches the n most recent return values from the function it is applied to, so that the function does not have to be invoked again.

# CURRENT PROBLEM
# implement queue

from functools import reduce

def saveresults(n):
    def decorator(fn):

        # todo: set a length 
        cache = []
        keys = []
        max_items = n

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

            # keep it at n elements
            if len(cache) == max_items + 1:
                del cache[0]
                del keys[0]

                print('after reducing it to 8, check it:')
                print('the current keys are ', keys, ' *********')
                print('the current cache is ', cache, ' *********')

            print('the index of the key is ', keys.index(args[0]))
            index = keys.index(args[0])

            return cache[index]
        return inner    
    return decorator

@saveresults(5)
def powerup(a):
    return a * a

a = [powerup(i) for i in range(5)]
print('the a list is ', a)

# things should be cached here
b = [powerup(i) for i in range(5)]
print('the b list is ', b)

powerup(10)
powerup(10)
