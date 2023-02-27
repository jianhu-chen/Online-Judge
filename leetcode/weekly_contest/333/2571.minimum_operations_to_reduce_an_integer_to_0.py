#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/minimum-operations-to-reduce-an-integer-to-0
from functools import lru_cache


class Solution:
    def minOperations(self, n: int) -> int:
        return self.solution1(n)

    def solution1(self, n: int) -> int:
        """比赛时的思路."""
        mi = []
        for i in range(18):
            mi.append(1 << i)

        cnt = 0
        while n:
            mn = mi[-1]
            for x in mi:
                diff = n - x if n > x else x - n
                mn = min(mn, diff)
            n = mn
            cnt += 1

        return cnt

    def solution2(self, n: int) -> int:

        @lru_cache
        def dfs(x):
            if x & (x - 1) == 0:
                return 1
            r1 = x & -x
            return min(dfs(x + r1), dfs(x - r1)) + 1

        return dfs(n)
