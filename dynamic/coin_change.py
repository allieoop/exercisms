from utils import memoize, validate_input


def make_change(coins, target):
    """
    Given a set of coin denominations, e.g. 1, 2, 5, 10 and a target sum, how
    many different combinations of those coins can make up the target sum. Coins
    can be reused as many times as you need.

    Time complexity:
    O(mn) - m is target sum, n is set size

    e.g.
    coin_types: 1,2,5,10
    target sum: 5
    answer: 4
    1+1+1+1+1
    1+1+1+2
    1+2+2
    5
        (coins X totals)
       |0  |1  |2  |3  |4  |5
    0  |1  |0  |0  |0  |0  |0
    1  |1  |1  |1  |1  |1  |1
    2  |1  |1  |2  |2  |3  |3
    5  |1  |1  |2  |2  |3  |4
    10 |1  |1  |2  |2  |3  |4
    """
    n = target + 1
    m = len(coins) + 1
    table = [[0] * n] * m
    # Base case: n=0, 1 way for each coin to make that
    for i in range(n):
        table[0][i] = 0
    for i in range(m):
        table[i][0] = 1
    for i in range(1, m):
        for j in range(1, n):
            table[i][j] = table[i-1][j] + table[i][max(j-coins[i-1], 0)]
        print(table[i])


if __name__ == '__main__':
    make_change([1,2,3], 5)
