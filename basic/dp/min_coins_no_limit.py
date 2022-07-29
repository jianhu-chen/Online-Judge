#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import random
import unittest
from typing import List


class CoinWays:
    """
    给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

    计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

    你可以认为每种硬币的数量是无限的。

    https://leetcode.cn/problems/coin-change/
    """

    def solution1(self, amount: int, coins: List[int]) -> int:
        def process(rest, coins, idx):
            if rest == 0:
                return 0
            if idx == len(coins):
                return float("inf")
            ans = float("inf")
            for n in range(rest // coins[idx] + 1):
                candidate = process(rest - n * coins[idx], coins, idx + 1)
                if candidate != float("inf"):
                    ans = min(ans, n + candidate)
            return ans
        ans = process(amount, coins, 0)
        return ans if ans != float("inf") else -1

    def solution2(self, amount: int, coins: List[int]) -> int:
        # [len(coins), amount + 1]
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        dp[-1][1:] = [float("inf")] * (amount)
        for i in range(len(coins) - 1, -1, -1):
            for a in range(1, amount + 1):
                dp[i][a] = dp[i + 1][a]
                for n in range(a // coins[i] + 1):
                    candidate = dp[i + 1][a - n * coins[i]]
                    if candidate != float("inf"):
                        dp[i][a] = min(dp[i][a], n + candidate)
        ans = dp[0][amount]
        return ans if ans != float("inf") else -1

    def solution3(self, amount: int, coins: List[int]) -> int:
        # [len(coins), amount + 1]
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        dp[-1][1:] = [float("inf")] * (amount)
        for i in range(len(coins) - 1, -1, -1):
            for a in range(1, amount + 1):
                dp[i][a] = dp[i + 1][a]
                if a - coins[i] >= 0:
                    dp[i][a] = min(dp[i][a], dp[i][a - coins[i]] + 1)
        ans = dp[0][amount]
        return ans if ans != float("inf") else -1


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = CoinWays()
        s1_cost, s2_cost, s3_cost = 0, 0, 0
        for _ in range(100):
            amount = random.randint(1, 55)
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
    coins = [1, 2, 5]
    amount = 11
    print(CoinWays().solution1(amount, coins))
    print(CoinWays().solution2(amount, coins))
    print(CoinWays().solution3(amount, coins))
    unittest.main()
