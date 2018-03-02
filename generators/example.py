def firstn(n):
    num = 0
    nums = []
    while num < n:
        nums.append(num)
        num += 1
    return nums


def firstn_gen(n):
    num = 0
    while num < n:
        yield num
        num += 1


def list_comprehension(numbers):
    print([x * x for x in numbers])


def set_comprehension(numbers):
    print({x * x for x in numbers})


def dict_comprehension(numbers):
    print({x: x * x for x in numbers})


def gen_expression_numbers(numbers):
    # note: this is not a tuple comprehension
    gen = (x * x for x in numbers)
    print(list(gen))


def gen_expression_words(words):
    print(words)
    stuff = [[word.lower(), len(word)] for word in words]
    for i in stuff:
        print(i)


def frange(start, stop, step):
    """Use like range but with floats.
    """
    i = start
    while i < stop:
        yield i
        i += step


def gen_in_for_loop(numbers):
    gen = (x * x for x in numbers)
    for i in gen:
        print('im the next element in the gen {}'.format(i))


def gen():
    for i in range(1, 6):
        yield i


if __name__ == '__main__':
    numbers = gen()
    squares = (x*x for x in numbers)
    sums = (sum(map(int, str(x))) for x in squares)
    for i in sums:
        print(i)

    # list comprehension
    numbers = [1, 2, 3, 4, 5, 6]
    list_comprehension(numbers)
    set_comprehension(numbers)
    dict_comprehension(numbers)
    gen_expression_numbers(numbers)
    words = 'The quick brown fox jumps over the lazy dog'.split()
    gen_expression_words(words)
    gen_in_for_loop(numbers)

    # use our own float range generator
    for i in frange(0.5, 1.5, 0.1):
        print(i)

    sum_of_first_n = sum(firstn(1000000))
    sum_of_first_n = sum(firstn_gen(1000000))
