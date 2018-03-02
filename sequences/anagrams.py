import string
import unittest
from ddt import ddt, data, unpack


ALPHABET_SIZE = 26
ASCII_ALPHABET_START_POSITION = ord('a')


def get_alphabet_counts(word):
    alphabet_counts = [0] * ALPHABET_SIZE
    for c in word:
        alphabet_counts[ord(c.lower())-ASCII_ALPHABET_START_POSITION] += 1
    return alphabet_counts


def get_diff(word_a, word_b):\
    return sum([abs(x-y) for x,y in zip(get_alphabet_counts(word_a), get_alphabet_counts(word_b))])


def is_anagram(word_a, word_b):
    return (get_alphabet_counts(word_a) == get_alphabet_counts(word_b))


@ddt
class SolutionTest(unittest.TestCase):
    def setUp(self):
        pass

    @data (
        ('dog', 'cat', 6), 
        ('adrian', 'allie', 7),
        ('', '', 0),
        ('fox', 'fox', 0),
        ('nona', 'none', 2),
        ('none', 'non', 1),
        ('alex', 'lexa', 0),
    )
    @unpack
    def test_get_diff(self, input_word_a, input_word_b, expected_output):
        sum = get_diff(input_word_a, input_word_b)
        self.assertEqual(sum, expected_output)

    @data (
        ('dog', 'cat', False), 
        ('adrian', 'allie', False),
        ('', '', True),
        ('fox', 'fox', True),
        ('nona', 'none', False),
        ('none', 'non', False),
        ('alex', 'lexa', True),
    )
    @unpack
    def test_is_anagram(self, input_word_a, input_word_b, expected_output):
        result = is_anagram(input_word_a, input_word_b)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
