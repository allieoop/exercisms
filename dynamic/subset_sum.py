def three_sum_brute_force(arr):
    """Most naive approach to three sum.

    Loop over the numbers three times to check all the subsets for the sum.

    Time complexity: O(n^3)
    Space complexity: O(1) - for one result, O(m) for m results
    """
    result = []
    n = len(arr)

    for i in range(0, n-2): 
        for j in range(i+1, n-1):
            for k in range (j+1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    result.append([arr[i], arr[j], arr[k]])
    return result


def three_sum_binary_sort(arr):
    """
    First sort the array with Merge sort or Quick sort. Then iterate over the
    array twice and instead of using a third loop, look for the third value
    using a binary search over the already sorted array.

    Time complexity: O(n^2logn) TODO: Double check
    Space complexity: O(1) - for one result, O(m) for m results
    """
    pass


def three_sum_hash_table(arr, target):
    """Use a set to look up the third number we need to complete our sum.

    Time complexity: O(n^2) [AVERAGE TIME]
    Space complexity: O(n) - size of the hash table
    """
    n = len(arr)
    result = []
    lookup = set()
    for i in range(n-1):
        for j in range(i+1, n):
            s = arr[i] + arr[j]
            complement = target - s
            if complement in lookup:
                result.append([arr[i], arr[j], complement])
        lookup.add(arr[i])
    return result


print(three_sum_hash_table([1,2,3,4,5], 6))


def three_sum_quadratic(arr):
    """Solve three sum in quadratic time worst case.

    Time complexity: O(n^2) [AVERAGE AND WORST TIME]
    """
    pass


def count_sets(arr, target):
    return two_sum(arr, target, len(arr)-1)


def two_sum(arr, target, pos):
    """Recursive naive approach.

    Use a second loop to find the compliment of the value chosen in the first
    loop.

    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    if target == 0:
        return 1
    elif target < 0:
        return 0
    elif pos < 0:
        return 0
    elif target < arr[pos]: # Check next position
        return two_sum(arr, target, pos-1)
    else:
        return two_sum(arr, target-arr[pos], pos-1) + two_sum(arr, target, pos-1)



print(count_sets([1,2,3,4,5], 7))
