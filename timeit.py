# Implementation of timeit as a class decorator
# will keep a dictionary with avg of times of functions

# TODO

import time
import functools

def timeit(fn):
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        start_time = time.time()
        retval = fn(*args, **kwargs)
        duration = time.time() - start_time
        print("%s : %2.2f sec" % (fn.__name__,
            duration))
        return retval
    return inner

# first iteration, everytime a function is called, it keeps only the latest time

class timefunc(object):
    __instances = {}

    def __init__(self, f):
        self.__f = f
        self.__num_calls = 0
        countcalls.__instances[f] = self

    def __call__(self, *args, **kwargs):
        self.__num_calls += 1
        return self.__f(*args, **kwargs)

    def count(self):
        return self.__num_calls

    @staticmethod
    def counts():
        return dict([(f.__name__,
            countcalls.__instances[f].__num_calls) for f in
            countcalls.__instances])



