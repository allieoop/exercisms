from functools import lru_cache
from utils import memoize, validate_input


@validate_input
@memoize
#@lru_cache()
def fib(n):
    prev = 0
    curr = 1
    counter = 1
    while counter < n:
        prev, curr = curr, prev + curr
        counter += 1
    return curr


@validate_input
@memoize
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)


def fib_gen():
    # write fib as a generator
    prev = 0
    curr = 1
    while True:
        yield curr
        prev, curr = curr, prev + curr


@validate_input
def fib_gen_2(n):
    curr = 1
    prev = 0
    counter = 0
    while counter < n:
        yield curr
        # sum = prev + curr
        # prev = curr
        # curr = sum
        prev, curr = curr, prev + curr  # Update state variables at the same time 
                                        # Elimate out-of-order issues
                                        # allows higer-level thinking "chunking"
        counter += 1


if __name__ == '__main__':
    fg_a = fib_gen()
    print(next(fg_a))
    print(next(fg_a))
    print(next(fg_a))
    try:
        fg2_a = fib_gen_2(-5)
    except ValueError as e:
        print(e)
    fg2_a = fib_gen_2(5)
    print(list(fg2_a))
    fg2_b = fib_gen_2(5)
    print(list(fg2_b))
