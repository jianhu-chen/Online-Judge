#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import random
import unittest


class KillMonster:
    """
    给定3个参数，N，M，K
    怪兽有N滴血，等着英雄来砍自己
    英雄每一次打击，都会让怪兽流失[0~M]的血量
    到底流失多少？每一次在[0~M]上等概率的获得一个值
    求K次打击之后，英雄把怪兽砍死的概率
    """

    def solution1(self, n: int, m: int, k: int):
        def process(n, m, k):
            """返回怪兽是否死亡."""
            if n <= 0:
                return 1
            if k == 0:
                return 0
            ans = 0
            for hurt in range(m + 1):
                ans += process(n - hurt, m, k - 1)
            return ans
        return process(n, m, k)

    def solution2(self, n: int, m: int, k: int):
        dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 0
        for j in range(k + 1):
            dp[0][j] = 1
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for hurt in range(m + 1):
                    if i - hurt <= 0:
                        dp[i][j] += 1
                    else:
                        dp[i][j] += dp[i - hurt][j - 1]
        return dp[n][k]


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = KillMonster()
        s1_cost, s2_cost = 0, 0
        for _ in range(100):
            n = random.randint(1, 25)
            m = random.randint(1, 10)
            k = random.randint(1, 8)
            s = time.perf_counter()
            ans1 = obj.solution1(n, m, k)
            s1_cost += time.perf_counter() - s
            s = time.perf_counter()
            ans2 = obj.solution2(n, m, k)
            s2_cost += time.perf_counter() - s
            self.assertEqual(ans1, ans2)
        print("solution1 cost:", s1_cost)
        print("solution2 cost:", s2_cost)


if __name__ == "__main__":
    unittest.main()
