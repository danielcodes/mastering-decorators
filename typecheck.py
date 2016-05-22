
import functools

# an outer wrap is order to process parameters
def accepts(*types, **keywords):

    # the real decorator doing the work
    def decorator(fn):
        @functools.wraps(fn)

        # as typical, we have the function that is going to be returned
        # this part always throws me off, the args and kwargs part
        def inner(*args, **kwargs):
            print("the types to check for are ", types)
            print("the passed args are ", args)

            print('the keys to check for are ', keywords)
            print('the key passed are ', kwargs)

            # before the function is process, check the types of the arguments
            for (t, a) in zip(types, args):
                assert isinstance(a, t)

            # check for kwargs
            # all the arguments keys are in keys
            for key in kwargs.keys():
                assert key in keywords.keys()

            print('all inputs are correct')
            
            # we just pass back the function
            return fn(*args, **kwargs)
        return inner
    return decorator


empty = {'blue': 'azul', 'yellow': 'amarillo'}

@accepts(int, red=0, green=1, blue=4)
def is_even(*args, **kwargs):
    pass


is_even(4, red=4, green=4, blue=1)


