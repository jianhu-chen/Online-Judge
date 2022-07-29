#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import random
import unittest
from typing import List

import numpy as np


class CoinWays:
    """
    arr是面值数组，其中的值都是正数且没有重复。再给定一个正数aim。
    每个值都认为是一种面值，且认为张数是无限的。
    返回组成aim的方法数
    例如：arr = {1,2}，aim = 4
    方法如下：1+1+1+1、1+1+2、2+2
    一共就3种方法，所以返回3

    https://leetcode.cn/problems/coin-change-2/
    """

    def solution1(self, amount: int, coins: List[int]) -> int:
        def process(amount, coins, idx):
            if amount < 0:
                return 0
            if amount == 0:
                return 1
            if idx == len(coins):
                return 0
            ans = 0
            for n in range(amount // coins[idx] + 1):
                ans += process(amount - n * coins[idx], coins, idx + 1)
            return ans
        return process(amount, coins, 0)

    def solution2(self, amount: int, coins: List[int]) -> int:
        dp = np.zeros(shape=[len(coins) + 1, amount + 1])
        dp[:, 0] = 1
        for i in range(len(coins) - 1, -1, -1):
            for a in range(amount + 1):
                ans = 0
                for n in range(a // coins[i] + 1):
                    ans += dp[i + 1][a - coins[i] * n]
                dp[i][a] = ans
        return dp[0][amount]

    def solution3(self, amount: int, coins: List[int]) -> int:
        dp = np.zeros(shape=[len(coins) + 1, amount + 1])
        dp[:, 0] = 1
        for i in range(len(coins) - 1, -1, -1):
            for a in range(amount + 1):
                dp[i][a] = dp[i + 1][a]
                if a - coins[i] >= 0:
                    dp[i][a] += dp[i][a - coins[i]]
        return dp[0][amount]


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = CoinWays()
        s1_cost = 0
        s2_cost = 0
        s3_cost = 0
        for _ in range(100):
            amount = random.randint(1, 50)
            # remove duplicate
            coins = list(set([random.randint(1, 20) for _ in range(random.randint(1, 20))]))
            s = time.perf_counter()
            ans1 = obj.solution1(amount, coins)
            s1_cost += time.perf_counter() - s
            s = time.perf_counter()
            ans2 = obj.solution2(amount, coins)
            s2_cost += time.perf_counter() - s
            s = time.perf_counter()
            ans3 = obj.solution3(amount, coins)
            s3_cost += time.perf_counter() - s
            self.assertEqual(ans1, ans2)
            self.assertEqual(ans2, ans3)
        print("solution1 cost:", s1_cost)
        print("solution2 cost:", s2_cost)
        print("solution3 cost:", s2_cost)


if __name__ == "__main__":
    amount = 5
    coins = [1, 2, 5]
    print(CoinWays().solution1(amount, coins))
    unittest.main()
