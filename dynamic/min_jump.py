import unittest


def min_jump(arr):
    """Returns minimum number of jumps to reach arr[n-1] from arr[0].

    Maintain a min jumps array that gets updated at every point in the inner 
    loop if we can get farther than before with fewer jumps.

    Time complexity:
    O(n^2)

    Space complexity:
    O(n) to maintain min jumps
    """
    n = len(arr)
    min_jumps = [float('inf')] * n
    min_jumps[0] = 0
    for i in range(1, n):
        for j in range(i):
            if j + arr[j] < i:  # we can't reach i from j
                continue
            if min_jumps[j] + 1 < min_jumps[i]:
                min_jumps[i] = min_jumps[j] + 1
        print(min_jumps)
    return min_jumps[n-1]


def min_jump_fast(arr):
    """Returns minimum number of jumps to reach arr[n-1] from arr[0].
    
    Maintain longest ladder. When we reach the last step of the  current ladder
    we take a jump onto the longest ladder. If we reach the end, jump off 
    ladder.

    Time complexity:
    O(n) time

    Space complexity:
    O(1) to maintain three ints: max_reach, last_step, jumps
    """
    n = len(arr)
    if (n == 0):  # how fast to jump to nothing?
        return -1
    if (n == 1):  # how fast to jump to ourselves?
        return 0
    if (arr[0] == 0):  # no jumping allowed!
        return -1

    max_reach = arr[0]  # max_reach is distance of first ladder
    last_step = arr[0]
    jumps = 0
    for i in range(1, n):
        max_reach = max(max_reach, i + arr[i])
        if (i == last_step):  # we've reached the last step of current ladder
            jumps += 1  # jump onto new ladder
            last_step = max_reach  # store last step of new ladder
    return jumps


def min_jump_recurse(arr, src, dest):
    """Returns minimum number of jumps to reach arr[src] from arr[dest].

    A naive approach is to start from the first element and recursively call for
    all the elements reachable from first element. The minimum number of jumps
    to reach end from first can be calculated using minimum number of jumps
    needed to reach end from the elements reachable from first.
    """

    if (dest == src):
        return 0
    if (arr[src] == 0):
        return float('inf')
    minimum = float('inf')
    for i in range(src + 1, dest + 1):
        if (i < src + arr[src] + 1):
            jumps = min_jump_recurse(arr, i, dest)
            if (jumps + 1 < minimum):
                minimum = jumps + 1
    return minimum


if __name__ == '__main__':
    print(min_jump([2,3,1,1,2,4,2,0,1,1]))
    print(min_jump_fast([2,3,1,1,2,4,2,0,1,1]))
    print(min_jump_recurse([2,3,1,1,2,4,2,0,1,1], 0, 9))
