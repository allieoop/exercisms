import timeit


def reverse(string):
    reverse = ''
    index = len(string)
    while index > 0:
        reverse += string[index-1]
        index = index - 1
    return reverse


def reverse2(string):
    return string[::-1]


def reverse3(string):
    reverse = ''
    for c in string:
        reverse = c + reverse
    return reverse


def reverse4(string):
    if len(string) == 0:
        return string
    else:
        return reverse4(string[1:]) + string[0]


def time_it():
    str = '`1234567890-=qwertyuiop[]]\asdfghjkl;zxcvbnm,./1234567890'
    t = timeit.Timer(lambda: reverse(str))
    print("reverse: {}".format(t.timeit()))
    t = timeit.Timer(lambda: reverse2(str))
    print("reverse2: {}".format(t.timeit()))
    t = timeit.Timer(lambda: reverse3(str))
    print("reverse3: {}".format(t.timeit()))
    t = timeit.Timer(lambda: reverse4(str))
    print("reverse4: {}".format(t.timeit()))


if __name__ == '__main__':
    time_it()
    """Results:
            reverse: 12.0324048996
            reverse2: 0.60010099411
            reverse3: 5.80424308777
            reverse4: 23.485131979
    """
