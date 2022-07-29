#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import random
import string
import unittest

import numpy as np


class LongestPalindromicSubsequence:
    """
    给定一个字符串str，返回这个字符串的最长回文子序列长度
    比如 ： str = “a12b3c43def2ghi1kpm”
    最长回文子序列是“1234321”或者“123c321”，返回长度7

    https://leetcode.cn/problems/longest-palindromic-subsequence/
    """

    def solution1(self, s: str) -> int:
        def process(s):
            if len(s) <= 1:
                return len(s)
            if s[0] == s[-1]:
                return process(s[1:-1]) + 2
            else:
                return max(
                    process(s[1:]),
                    process(s[:-1])
                )
        return process(s)

    def solution2(self, s: str) -> int:
        n = len(s)
        dp = np.zeros(shape=(n, n))
        dp[np.diag_indices_from(dp)] = 1
        for subl in range(2, n + 1):
            for i in range(n - subl + 1):
                j = i + subl - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return int(dp[0][n - 1])


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = LongestPalindromicSubsequence()
        s1_cost, s2_cost = 0, 0
        for _ in range(100):
            text = "".join(
                random.choice(string.ascii_letters + string.digits)
                for _ in range(random.randint(1, 20))
            )
            s = time.perf_counter()
            ans1 = obj.solution1(text)
            s1_cost += time.perf_counter() - s
            s = time.perf_counter()
            ans2 = obj.solution2(text)
            s2_cost += time.perf_counter() - s
            self.assertEqual(ans1, ans2)
        print(f"solution1 cost: {s1_cost}")
        print(f"solution2 cost: {s2_cost}")


if __name__ == "__main__":
    text = "a12b3c43def2ghi1kpm"
    print(LongestPalindromicSubsequence().solution1(text))
    print(LongestPalindromicSubsequence().solution2(text))
    unittest.main()
