#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import random
import string
import unittest

import numpy as np


class LongestCommonSubsequence:
    """
    给定两个字符串str1和str2,
    返回这两个字符串的最长公共子序列长度
    比如: str1 = “a12b3c456d”,str2 = “1ef23ghi4j56k”
    最长公共子序列是“123456”, 所以返回长度6

    ref: https://leetcode.cn/problems/longest-common-subsequence/
    """

    def solution1(self, text1: str, text2: str) -> int:

        def process(text1, text2, idx1, idx2, same_lenght):
            if idx1 == len(text1) or idx2 == len(text2):
                return same_lenght

            if text1[idx1] == text2[idx2]:
                return process(text1, text2, idx1 + 1, idx2 + 1, same_lenght + 1)
            else:
                return max(
                    process(text1, text2, idx1 + 1, idx2, same_lenght),
                    process(text1, text2, idx1, idx2 + 1, same_lenght)
                )
        return process(text1, text2, 0, 0, 0)

    def solution2(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        dp = np.zeros(shape=(n1 + 1, n2 + 1), dtype=np.int32)
        for idx1 in range(n1 - 1, -1, -1):
            for idx2 in range(n2 - 1, -1, -1):
                if text1[idx1] == text2[idx2]:
                    dp[idx1][idx2] = dp[idx1 + 1][idx2 + 1] + 1
                else:
                    dp[idx1][idx2] = max(dp[idx1 + 1][idx2], dp[idx1][idx2 + 1])
        return int(dp[0][0])


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = LongestCommonSubsequence()
        s1_cost, s2_cost = 0, 0
        for _ in range(100):
            l1, l2 = random.randint(1, 13), random.randint(1, 13)
            text1 = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(l1))
            text2 = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(l2))
            s = time.perf_counter()
            ans1 = obj.solution1(text1, text2)
            s1_cost += time.perf_counter() - s
            s = time.perf_counter()
            ans2 = obj.solution2(text1, text2)
            s2_cost += time.perf_counter() - s
            self.assertEqual(ans1, ans2)
        print(f"solution1 cost: {s1_cost}")
        print(f"solution2 cost: {s2_cost}")


if __name__ == "__main__":
    str1 = "a12b3c456d"
    str2 = "1ef23ghi4j56k"
    print(LongestCommonSubsequence().solution1(str1, str2))
    print(LongestCommonSubsequence().solution2(str1, str2))
    unittest.main()
