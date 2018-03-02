from sys import maxsize


class Solution:
    def max_subarray(arr):
        """ Return consecutive subarray with largest sum.

        Kadane's Algorithm. Loop once while maintaining a maximum subarray. For each 
        position in the array, choose the subarray with the maximum value between:
        arr[i], current_max + arr[i], current_max.

        Time complexity:
        O(n)

        Space complexity:
        O(1) for max values, start positions, and end postion
        """
        if len(arr) == 0:
            return arr

        global_maxval = arr[0]
        global_start = 0
        global_end = 0
        maxval = arr[0]
        start = 0

        for i in range(1, len(arr)):
            # Get new local maximum subarray
            if arr[i] > arr[i] + maxval:
                maxval = arr[i]
                start = i
            else:
                maxval += arr[i]

            # Check if local maximum is greater than global maximum
            if maxval > global_maxval:
                global_maxval = maxval
                global_start = start
                global_end = i
        return arr[global_start:global_end + 1]

    def max_sum(arr):
        """Return the maximum sum of consecutive values.
        """
        if not arr:
            return arr
        maximum = current_max = arr[0]
        for x in arr[1:]:
            current_max = max(x, x + current_max)
            maximum = max(current_max, maximum)
        return maximum

    def max_sum_recursive(arr):
        """Return the maximum sum of consecutive values.

        This is the naive approach that uses divide and conquer technique.

            1. Break array into two halves
            2. Choose maximum from following three results:
                1) max from subarray left
                2) max from subarray right
                3) max from cross-section of subarrays
        """
        print(arr)
        n = len(arr)
        if not arr:
            return []
        if n == 1:
            return arr[0]
        mid_point = n // 2
        return max(
            Solution.max_sum_recursive(arr[0:mid_point]),
            Solution.max_sum_recursive(arr[mid_point:n + 1]),
            Solution.max_cross_subarr(arr, mid_point))

    def max_cross_subarr(arr, mid_point):
        """Find the maxium subarray that contains the mid_point.
        """
        left_sum = arr[0]
        right_sum = arr[-1]
        for x in arr[1:mid_point]:
            if left_sum + x > left_sum:
                left_sum = left_sum + x
        for x in arr[mid_point:-1]:  # include midpoint
            if right_sum + x > right_sum:
                right_sum = right_sum + x

        print('sum for array {}: {}'.format(arr, left_sum + right_sum))
        return left_sum + right_sum


import unittest
from ddt import ddt, data, unpack

@ddt
class SolutionTest(unittest.TestCase):
    def setUp(self):
        pass

    @data(
        ([], []),
        ([1 , 2, -8, 9], 9),        # last element
        ([1, -3 , 2, 1, -1], 3),    # middle subset
        ([-1, 1, 2], 3),            # beginning with negative
        ([-2, -1, -3, -1], -1),     # all negatives
        ([1 , 2, 3, 4], 10),        # all positives
        ([8, -1, 4, 4], 15)         # includes positives and negatives
    )
    @unpack
    def test_max_sum(self, input_array, expected_output):
        max_sum = Solution.max_sum(input_array)
        self.assertEqual(expected_output, max_sum)

    @data(
        ([], []),
        ([1 , 2, -8, 9], [9]),          # last element
        ([1, -3 , 2, 1, -1], [2, 1]),   # middle subset
        ([-1, 1, 2], [1, 2]),           # beginning with negative
        ([-2, -1, -3, -1], [-1]),       # all negatives
        ([1 , 2, 3, 4], [1, 2, 3, 4]),  # all positives
        ([8, -1, 4, 4], [8, -1, 4, 4])  # includes positives and negatives
    )
    @unpack
    def test_max_subarray(self, input_array, expected_output):
        max_subarray = Solution.max_subarray(input_array)
        self.assertEqual(expected_output, max_subarray)

    # @data(
    #     ([], []),
    #     ([1 , 2, -8, 9], 9),        # last element
    #     # ([1, -3 , 2, 1, -1], 3),    # middle subset
    #     # ([-1, 1, 2], 3),            # beginning with negative
    #     # ([-2, -1, -3, -1], -1),     # all negatives
    #     # ([1 , 2, 3, 4], 10),        # all positives
    #     # ([8, -1, 4, 4], 15)         # includes positives and negatives
    # )
    # @unpack
    # def test_max_sum_recursive(self, input_array, expected_output):
    #     max_sum = Solution.max_sum_recursive(input_array)
    #     self.assertEqual(expected_output, max_sum)


if __name__ == '__main__':
    unittest.main()
