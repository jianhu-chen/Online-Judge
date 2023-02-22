#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
from functools import lru_cache


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        grid = [[0] * n for _ in range(m)]
        ans = 0

        @lru_cache
        def bs(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        def dfs(i, j):
            if i == m or j == n:
                return
            if grid[i][j] == 1:
                return
            if bs(i) + bs(j) > k:
                return
            nonlocal ans
            ans += 1
            grid[i][j] = 1
            dfs(i + 1, j)
            dfs(i, j + 1)

        dfs(0, 0)
        return ans
