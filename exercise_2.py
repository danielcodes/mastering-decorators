# decorator that causes an assertion error if the function returns None

def notnone(fn):
    def inner(*args, **kwargs):
        # if return is None, assert error
        assert fn(*args, **kwargs) is not None

        print('hooray, no error')
        return fn(*args, **kwargs)
    return inner


@notnone
def add():
    return 1
    
@notnone
def subtract():
    # pass gives a return type of None, cool
    pass


add()
subtract()
