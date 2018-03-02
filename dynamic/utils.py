# import pickle
from functools import wraps


def memoize(key_parameters=[]):
    """Outer memoize function allows us to pass in additional parameters to our decorator.
    """
    def the_real_memoize(func):
        """All arguments passed to a method decorated with memoize must be hashable.
        """
        cache = {}
        @wraps(func)
        def wrapper(*args, **kwargs):
            """Return value in cache if key exists, otherwise add to cache and execute func.
            """
            key = ''
            if not key_parameters: # then use all parameters of the original function for the key
                key = str(args) + str(kwargs)
            else: # use specified parameters in key_parameters for the key
                for kwarg in kwargs:
                    if kwarg in key_parameters:
                        key = ''.join([key, kwarg, ':', str(kwargs[kwarg]), ', '])
            if key in cache:
                print('Return value from cache with key: {}'.format(key))
                return cache[key]
            result = func(*args, **kwargs)
            print('Add newly computed value to cache with key: {}'.format(key))
            cache[key] = result
            return result
        return wrapper
    return the_real_memoize


def validate_input(parameters=[]):
    def the_real_validate_input(func):
        def wrapper(*args, **kwargs):
            if parameters: # only validate given parameteres
                for name, val in kwargs.items():
                    if name in parameters:
                        if val < 0:
                            raise ValueError("'n' must be a positive integer") 
            return func(*args, **kwargs)
        return wrapper
    return the_real_validate_input