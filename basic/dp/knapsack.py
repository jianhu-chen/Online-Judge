#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import random
import unittest

import numpy as np


class Knapsack:
    """
    给定两个长度都为N的数组weights和values, weights[i]和values[i]分别代表 i号物品的重量和价值
    给定一个正数bag, 表示一个载重bag的袋子, 装的物品不能超过这个重量
    返回能装下的最大价值
    """

    def solution_recursion(self, weights, values, bag):
        if len(weights) != len(values) or bag <= 0:
            return 0

        def process(weights, values, idx, rest, ans):
            if rest < 0:
                return 0

            if idx == len(weights):
                return ans

            return max(
                process(weights, values, idx + 1, rest - weights[idx], ans + values[idx]),
                process(weights, values, idx + 1, rest, ans)
            )

        return process(weights, values, 0, bag, 0)

    def solution_dp(self, weights, values, bag):
        if len(weights) != len(values) or bag <= 0:
            return 0

        # row (idx) range: [0, N], col(rest) range: [0, rest]
        dp = np.zeros(shape=[len(weights) + 1, bag + 1], dtype=np.int32)
        for idx in range(len(weights) - 1, -1, -1):
            for rest in range(bag + 1):
                p1 = dp[idx + 1][rest]
                p2 = 0
                if rest - weights[idx] >= 0:
                    p2 = dp[idx + 1][rest - weights[idx]] + values[idx]
                dp[idx][rest] = max(p1, p2)
        return dp[0][bag]


class TestKnapsack(unittest.TestCase):

    def test_solution(self):
        TEST_TIMES = 20
        obj = Knapsack()
        s1_cost, s2_cost = 0, 0
        for _ in range(TEST_TIMES):
            weights = list(range(1, 20))
            values = list(range(1, 20))
            random.shuffle(weights)
            random.shuffle(values)
            sum_weights = sum(weights)
            bag = random.randint(sum_weights // 3, sum_weights)
            s = time.perf_counter()
            ans1 = obj.solution_recursion(weights, values, bag)
            s1_cost += time.perf_counter() - s
            s = time.perf_counter()
            ans2 = obj.solution_dp(weights, values, bag)
            s2_cost += time.perf_counter() - s
            self.assertEqual(ans1, ans2)
        print("solution1 cost: {}".format(s1_cost))
        print("solution2 cost: {}".format(s2_cost))


if __name__ == "__main__":
    unittest.main()
