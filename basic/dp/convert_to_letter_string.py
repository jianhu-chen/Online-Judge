#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random
import string
import unittest


class ConvertToLetterString:
    """
    规定1和A对应、2和B对应、3和C对应...26和Z对应
    那么一个数字字符串比如"111”就可以转化为:
    "AAA"、"KA"和"AK"
    给定一个只有数字字符组成的字符串str,返回有多少种转化结果
    """

    def solution1(self, s: str):
        def process(s, idx, ans):
            if idx == len(s):
                return [ans]
            ret = []
            if s[idx] != "0":
                ret += process(s, idx + 1, ans + chr(ord("A") + int(s[idx]) - 1))
            if idx < len(s) - 1 and s[idx:idx + 2] < "26":
                ret += process(s, idx + 2, ans + chr(ord("A") + int(s[idx:idx + 2]) - 1))
            return ret
        return len(process(s, 0, ""))

    def solution2(self, s: str):
        dp = [0 for _ in range(len(s))]
        dp.append(1)
        for idx in range(len(s) - 1, -1, -1):
            if s[idx] != "0":
                dp[idx] += dp[idx + 1]
            if idx < len(s) - 1 and s[idx:idx + 2] < "26":
                dp[idx] += dp[idx + 2]
        return dp[0]


class Timer(unittest.TestCase):

    def test_solution(self):
        obj = ConvertToLetterString()
        s1_cost, s2_cost = 0, 0
        for _ in range(200):
            s = "".join(random.choice(string.digits) for _ in range(random.randint(1, 100)))
            start = time.perf_counter()
            ans1 = obj.solution1(s)
            s1_cost += time.perf_counter() - start
            start = time.perf_counter()
            ans2 = obj.solution2(s)
            s2_cost += time.perf_counter() - start
            self.assertEqual(ans1, ans2)
        print("solution1 cost: {}".format(s1_cost))
        print("solution2 cost: {}".format(s2_cost))


if __name__ == "__main__":
    s = "1111"
    print(ConvertToLetterString().solution1(s))
    print(ConvertToLetterString().solution2(s))
    unittest.main()
