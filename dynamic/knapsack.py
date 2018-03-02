import unittest
from ddt import ddt, data, unpack


class Knapsack():
    def __init__(self, weights, values, capacity):
        self.weights = weights
        self.values = values
        self.capacity = 10
        self.memo = [[None for x in range(capacity+1)] for x in range(len(weights))]

    def solve_naive(self):
        return self.ks(len(self.weights)-1, self.capacity)

    def solve_dynamic(self):
        return self.ks_dynamic(len(self.weights)-1, self.capacity)

    def ks(self, item, capacity):
        if item == 0 or capacity == 0:
            return 0

        if self.weights[item] > capacity:
            return self.ks(item-1, capacity)
        
        tmp = self.ks(item-1, capacity)
        sum = self.values[item] + self.ks(item-1, capacity-self.weights[item])
        return max(sum, tmp)

    def ks_dynamic(self, item, capacity):
        if self.memo[item][capacity]: return self.memo[item][capacity]

        if item == 0 or capacity == 0:
            return 0

        if self.weights[item] > capacity:
            return self.ks_dynamic(item-1, capacity)
        
        tmp = self.ks_dynamic(item-1, capacity)
        sum = self.values[item] + self.ks_dynamic(item-1, capacity-self.weights[item])
        result =  max(sum, tmp)
        self.memo[item][capacity] = result
        return result


@ddt
class KnapsackTest(unittest.TestCase):
    def setUp(self):
        weights = [None, 1, 2, 4, 2, 5]
        values = [None, 5, 3, 5, 3, 2]
        capacity = 10
        self.ks = Knapsack(weights, values, capacity)

    def test_solve_naive(self):
        result = self.ks.solve_naive()
        self.assertEqual(result, 16)

    def test_solve_dynamic(self):
        result = self.ks.solve_dynamic()
        self.assertEqual(result, 16)


if __name__ == '__main__':
    unittest.main()
