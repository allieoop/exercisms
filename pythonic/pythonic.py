def test(*args, **kwargs):
    print(type(args))
    print(args)
    print(type(kwargs))
    print(kwargs)


def test_list(list):
    try:
        print(list[5])
    except IndexError as e:
        print('Error: {}'.format(e))


def eafp(person):
    # Pythonic: Easier to ask forgiveness
    try:
        print('{name} was a {occupation} born in {birth_city}'.format(**person))
    except KeyError as e:
        print('Missing info: {}'.format(e))


def lbyl(person):
    # Non-pythonic: Look before you leap
    if ('name' in person and 'occupation' in person and 'birth_city' in person):
        print('{name} was a {occupation} born in {birth_city}'.format(**person))
    else:
        print('Missing info')


def open_file_lbyl(file):
    # Race condition
    import os
    if os.access(file, os.R_OK):
        with open(file) as f:  # file could now be inaccessible and we get an exception
            print(f.read())
    else:
        print('Cannot read file')


def open_file_eafp(file):
    # No race condition
    try:
        f = open(file)
    except IOError as e:
        print('Error: Cannot open ' + file)
    else:
        with f:
            print(f.read())


def fib():
    # write fib as a generator
    prev = 0
    curr = 1
    while True:
        yield curr
        prev, curr = curr, prev + curr


def fib2(n):
    curr = 1
    prev = 0
    counter = 0
    while counter < n:
        yield curr
        prev, curr = curr, prev + curr
        counter += 1


if __name__ == '__main__':
    test('a', 'b', 'c', name='name', value='value')
    person = {'name': 'Octavia', 'occupation': 'writer', 'birth_city': 'Pasadena'}
    eafp(person)
    lbyl(person)
    person_missing_info = {'name': 'Octavia', 'occupation': 'writer'}
    eafp(person_missing_info)
    lbyl(person_missing_info)
    test_list([1,2,3,4,5,6])
    test_list([1,2,3,4,5])
    file_path = '/Users/allie/does_not_exist.py'
    open_file_eafp(file_path)
    open_file_lbyl(file_path)

    from itertools import islice
    f = fib()
    print(list(islice(f, 0, 10)))
    print(next(f))

    my_string = 'balloon'
    joined_string = ', '.join(my_string)
    print(joined_string)
    print(''.join(reversed(my_string)))

    my_list = ['b', 'a', 'l', 'l', 'o', 'o', 'n']
    print(''.join(my_list))
    print(my_string.split('l'))
    print(my_string.replace('oo', '00'))

    a = 'allie'
    b = 'crevier'
    print(a + b)
    print(''.join([a, b]))

    """
    a + b is easier to read than ''.join([a,b])
    a + b + c + ... is an O(n^2) operation, because each concatenation produces a new string
    join is an O(n) operation
    """
