import timeit
import unittest
from ddt import data, ddt, unpack


def get_first_recurring_char(char):
    seen = []
    for c in char:
        if (c not in seen):
            seen.append(c)
        else:
            return c


def get_first_recurring_char_2(char):
    seen = set()
    for c in char:
        if c in seen:
            return c
        seen.add(c)


def get_longest_recurring_char(word):
    prev_char = ''
    max_count = 0
    max_char = ''
    count = 0
    for c in word:
        if (prev_char == c):
            count += 1
        else:
            count = 1
        if count > max_count:
            max_count = count
            max_char = c
        prev_char = c
    return {max_char: max_count}


def time_it():
    str = '`1234567890-=qwertyuiop[]]\asdfghjkl;zxcvbnm,./1234567890'
    t = timeit.Timer(lambda: get_first_recurring_char(str))
    print("get_first_recurring_char: {}".format(t.timeit()))
    t = timeit.Timer(lambda: get_first_recurring_char_2(str))
    print("get_first_recurring_char_2: {}".format(t.timeit()))


@ddt
class SolutionTest(unittest.TestCase):
    def setUp(self):
        pass

    @data (
        ('aabcddbbbea', 'a')
    )
    @unpack
    def test_get_first_recurring_char(self, input_string, expected_result):
        result = get_first_recurring_char(input_string)
        self.assertEqual(expected_result, result)

    @data (
        ('aabcddbbbea', {'b': 3})
    )
    @unpack
    def test_get_longest_recurring_char(self, input_string, expected_result):
        result = get_longest_recurring_char(input_string)
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
