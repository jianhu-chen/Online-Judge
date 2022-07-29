#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import random
import unittest
from typing import List
from collections import Counter


class CoinWays:
    """
    arr是货币数组，其中的值都是正数。再给定一个正数aim。
    每个值都认为是一张货币，
    认为值相同的货币没有任何不同，
    返回组成aim的方法数
    例如：arr = {1,2,1,1,2,1,2}，aim = 4
    方法：1+1+1+1、1+1+2、2+2
    一共就3种方法，所以返回3
    """

    def solution1(self, amount: int, coins: List[int]) -> int:
        def process(amount, coins, idx):
            if amount == 0:
                return 1
            if amount < 0 or idx == len(coins):
                return 0
            ans = 0
            n = 0  # 使用改coin的数量
            while n <= coins[idx][1] and n * coins[idx][0] <= amount:
                ans += process(amount - n * coins[idx][0], coins, idx + 1)
                n += 1
            return ans

        coins = list(Counter(coins).items())
        return process(amount, coins, 0)

    def solution2(self, amount: int, coins: List[int]) -> int:
        coins = list(Counter(coins).items())
        # [len(coins) + 1, amount + 1]
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        for i in range(len(coins) + 1):
            dp[i][0] = 1
        for i in range(len(coins) - 1, -1, -1):
            for a in range(1, amount + 1):
                n = 0
                while n <= coins[i][1] and n * coins[i][0] <= a:
                    dp[i][a] += dp[i + 1][a - n * coins[i][0]]
                    n += 1
        return dp[0][amount]

    def solution3(self, amount: int, coins: List[int]) -> int:
        coins = list(Counter(coins).items())
        # [len(coins) + 1, amount + 1]
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        for i in range(len(coins) + 1):
            dp[i][0] = 1
        for i in range(len(coins) - 1, -1, -1):
            for a in range(1, amount + 1):
                dp[i][a] = dp[i + 1][a]
                # TODO
                if a - coins[i][0] >= 0:
                    dp[i][a] += dp[i][a - coins[i][0]]
        return dp[0][amount]


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = CoinWays()
        s1_cost, s2_cost, s3_cost = 0, 0, 0
        for _ in range(1000):
            amount = random.randint(1, 100)
            coins = [random.randint(1, 10) for _ in range(random.randint(1, 20))]
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
            self.assertEqual(ans1, ans3)
        print("solution1 cost:", s1_cost)
        print("solution2 cost:", s2_cost)
        print("solution3 cost:", s3_cost)


if __name__ == "__main__":
    coins = [1, 2, 1, 1, 2, 1, 2]
    amount = 4
    print(CoinWays().solution1(amount, coins))
    print(CoinWays().solution2(amount, coins))
    print(CoinWays().solution3(amount, coins))
    unittest.main()
