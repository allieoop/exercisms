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


if __name__ == '__main__':
    try:
        f = fib(-1)
    except ValueError as e:
        print('whoops')
    f = fib(n=3)
    print(f)
    f2 = fib(n=3)
    print(f2)
    f3 = fib(3)
    print(f3)
    fr = fib_recursive(5)
    print(fr)
    fr2 = fib_recursive(5)
    print(fr2)
