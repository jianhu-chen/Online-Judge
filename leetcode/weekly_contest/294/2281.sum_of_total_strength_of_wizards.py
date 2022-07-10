#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/sum-of-total-strength-of-wizards
import random
import unittest
from typing import List


class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        return self.solution2(strength)

    def solution1(self, strength: List[int]) -> int:
        """暴力解. O(N^3)"""
        n = len(strength)

        ans = 0
        for w in range(1, n + 1):
            for s in range(n - w + 1):
                min_val = min(strength[s: s + w])
                sum_val = sum(strength[s: s + w])
                ans += min_val * sum_val

        return ans % (10 ** 9 + 7)

    def solution2(self, strength: List[int]) -> int:
        """O(N^2)"""
        n = len(strength)

        # 前缀和
        presum = []
        for num in strength:
            presum.append(presum[-1] + num if presum else num)
        presum.append(0)  # 哨兵

        ans = 0
        min_table = [[-1 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            min_table[i][i] = strength[i]
            ans += strength[i] ** 2

        for w in range(2, n + 1):
            for s in range(n - w + 1):
                min_table[s][s + w - 1] = min(min_table[s][s + w - 2], strength[s + w - 1])
                ans += min_table[s][s + w - 1] * (presum[s + w - 1] - presum[s - 1])

        return ans % (10 ** 9 + 7)

    def solution3(self, strength: List[int]) -> int:
        """单调递增栈. O(N)"""
        n = len(strength)

        # 单调栈
        left, right = [-1] * n, [n] * n
        stack: List[int] = []
        for i in range(n):
            while stack and strength[i] <= strength[stack[-1]]:
                top = stack.pop()
                right[top] = i  # 非严格
            left[i] = stack[-1] if stack else -1  # 严格
            stack.append(i)

        # 前缀和
        s = [0]
        for num in strength:
            s.append(s[-1] + num)
        ss = [0]
        for num in s:
            ss.append(ss[-1] + num)

        ans = 0
        for i, v in enumerate(strength):
            l, r = left[i] + 1, right[i] - 1  # 左闭右闭
            total = (i - l + 1) * (ss[r + 2] - ss[i + 1]) - (r - i + 1) * (ss[i + 1] - ss[l])
            ans += v * total
        return ans % (10 ** 9 + 7)


class Tester(unittest.TestCase):

    def test_solution(self):
        obj = Solution()
        for _ in range(100):
            strength = [
                random.randint(1, 10 ** 9)
                for _ in range(random.randint(1, 500))
            ]
            ans1 = obj.solution1(strength)
            ans2 = obj.solution2(strength)
            ans3 = obj.solution3(strength)
            self.assertEqual(ans1, ans2)
            self.assertEqual(ans1, ans3)
            print(".", end="", flush=True)


if __name__ == "__main__":
    strength = [1, 3, 1, 2]
    obj = Solution()
    ans1 = obj.solution1(strength)
    print(ans1)
    ans2 = obj.solution2(strength)
    print(ans2)
    ans3 = obj.solution3(strength)
    print(ans3)
    unittest.main()
