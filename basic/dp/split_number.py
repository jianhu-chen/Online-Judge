#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import unittest


class SplitNumber:
    """
    给定一个正数n，求n的裂开方法数，
    规定：后面的数不能比前面的数小
    比如4的裂开方法有：
    1+1+1+1、1+1+2、1+3、2+2、4
    5种，所以返回5
    """

    def solution1(self, n: int):
        def process(rest, pre):
            if rest == 0:
                return 1
            if pre > rest:
                return 0
            ans = 0
            for x in range(pre, rest + 1):
                ans += process(rest - x, x)
            return ans
        return process(n, 1)

    def solution2(self, n: int):
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for pre in range(1, n + 1):
            dp[0][pre] = 1
            dp[pre][pre] = 1
        for pre in range(n - 1, 0, -1):
            for rest in range(pre + 1, n + 1):
                for x in range(pre, rest + 1):
                    dp[rest][pre] += dp[rest - x][x]
        return dp[n][1]

    def solution3(self, n: int):
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for pre in range(1, n + 1):
            dp[0][pre] = 1
            dp[pre][pre] = 1
        for pre in range(n - 1, 0, -1):
            for rest in range(pre + 1, n + 1):
                dp[rest][pre] = dp[rest][pre + 1]
                dp[rest][pre] += dp[rest - pre][pre]
        return dp[n][1]


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = SplitNumber()
        s1_cost, s2_cost, s3_cost = 0, 0, 0
        for n in range(1, 55):
            s = time.perf_counter()
            ans1 = obj.solution1(n)
            s1_cost += time.perf_counter() - s
            s = time.perf_counter()
            ans2 = obj.solution2(n)
            s2_cost += time.perf_counter() - s
            s = time.perf_counter()
            ans3 = obj.solution3(n)
            s3_cost += time.perf_counter() - s
            self.assertEqual(ans1, ans2)
            self.assertEqual(ans2, ans3)
        print("solution1 cost: {}".format(s1_cost))
        print("solution2 cost: {}".format(s2_cost))
        print("solution3 cost: {}".format(s3_cost))


if __name__ == "__main__":
    unittest.main()
