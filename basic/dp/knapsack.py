#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import random
import unittest


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print("{:<30} cost: {} ms".format(func.__name__, (end - start) * 1000))
    return wrapper


class Knapsack:
    """
    给定两个长度都为N的数组weights和values, weights[i]和values[i]分别代表 i号物品的重量和价值
    给定一个正数bag, 表示一个载重bag的袋子, 装的物品不能超过这个重量
    返回能装下的最大价值
    """

    def solution_recursion(self, weights, values, bag):
        if len(weights) != len(values) or bag <= 0:
            return 0

        def recursion_process(weights, values, idx, rest, ans):
            if idx == len(weights):
                return ans

            if rest < 0:
                return 0

            return max(
                recursion_process(weights, values, idx + 1, rest - values[idx], ans + values[idx]),
                recursion_process(weights, values, idx + 1, rest, ans)
            )

        return recursion_process(weights, values, 0, bag, 0)

    def solution_memory_search(self, weights, values, bag):
        if len(weights) != len(values) or bag <= 0:
            return 0

        def memory_search_process(weights, values, idx, rest, ans, dp):
            if idx == len(weights):
                pass
            elif rest < 0:
                ans = 0
            else:
                ans = max(
                    memory_search_process(
                        weights, values, idx + 1, rest - values[idx], ans + values[idx], dp),
                    memory_search_process(weights, values, idx + 1, rest, ans, dp)
                )
            dp[idx][rest] = ans
            return ans

        # row (idx) range: [0, N], col(rest) range: [0, rest]
        dp = [[-1 for _ in range(bag + 1)] for _ in range(len(weights))]
        return memory_search_process(weights, values, 0, bag, 0, dp)

    def solution_dp(self, weights, values, bag):
        if len(weights) != len(values) or bag <= 0:
            return 0


class TestKnapsack(unittest.TestCase):

    def test_solution(self):
        TEST_TIMES = 10
        obj = Knapsack()
        for _ in range(TEST_TIMES):
            weights = list(range(1, 20))
            values = list(range(1, 20))
            random.shuffle(weights)
            random.shuffle(values)
            sum_weights = sum(weights)
            bag = random.randint(sum_weights // 3, sum_weights)
            A = obj.solution_recursion(weights, values, bag)
            B = obj.solution_memory_search(weights, values, bag)
            # C = obj.solution_dp(weights, values, bag)
            self.assertEqual(A, B, (weights, values, bag))
            # self.assertEqual(B, C, (weights, values, bag))


if __name__ == "__main__":
    unittest.main()
