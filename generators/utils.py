from functools import wraps


def memoize(func):
    """All arguments passed to a method decorated with memoize must be hashable.
    """
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Return value in cache if key exists
        """
        key = str(args) + str(kwargs)
        if key in cache:
            print('Return value from cache with key: {}'.format(key))
            return cache[key]
        result = func(*args, **kwargs)
        print('Add newly computed value to cache with key: {}'.format(key))
        cache[key] = result
        return result
    return wrapper


def validate_input(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg < 0:
                raise ValueError("'n' must be a positive integer")
        for name, val in kwargs.items():
            if val < 0:
                raise ValueError("'n' must be a positive integer")
        return func(*args, **kwargs)
    return wrapper
