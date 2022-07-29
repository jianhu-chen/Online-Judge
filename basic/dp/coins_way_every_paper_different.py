#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import random
import unittest
from typing import List

import numpy as np


class CoinWays:
    """
    arr是货币数组，其中的值都是正数。再给定一个正数aim。
    每个值都认为是一张货币，
    即便是值相同的货币也认为每一张都是不同的，
    返回组成aim的方法数
    例如：arr = {1,1,1}，aim = 2
    第0个和第1个能组成2，第1个和第2个能组成2，第0个和第2个能组成2
    一共就3种方法，所以返回3
    """

    def solution1(self, amount: int, coins: List[int]) -> int:
        def process(amount, coins, idx):
            if amount < 0:
                return 0
            if amount == 0:
                return 1
            if idx == len(coins):
                return 0
            a1 = process(amount - coins[idx], coins, idx + 1)
            a2 = process(amount, coins, idx + 1)
            return a1 + a2
        return process(amount, coins, 0)

    def solution2(self, amount: int, coins: List[int]) -> int:
        dp = np.zeros(shape=[len(coins) + 1, amount + 1])
        dp[:, 0] = 1
        for i in range(len(coins) - 1, -1, -1):
            for a in range(amount + 1):
                p1 = dp[i + 1][a]
                p2 = dp[i + 1][a - coins[i]] if a - coins[i] >= 0 else 0
                dp[i][a] = p1 + p2
        return dp[0, amount]


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = CoinWays()
        s1_cost = 0
        s2_cost = 0
        for _ in range(1000):
            amount = random.randint(1, 100)
            coins = [random.randint(1, 10) for _ in range(random.randint(1, 20))]
            s = time.perf_counter()
            ans1 = obj.solution1(amount, coins)
            s1_cost += time.perf_counter() - s
            s = time.perf_counter()
            ans2 = obj.solution2(amount, coins)
            s2_cost += time.perf_counter() - s
            self.assertEqual(ans1, ans2)
        print("solution1 cost:", s1_cost)
        print("solution2 cost:", s2_cost)


if __name__ == "__main__":
    amount = 2
    coins = [1, 1, 1]
    print(CoinWays().solution2(amount, coins))
    unittest.main()
