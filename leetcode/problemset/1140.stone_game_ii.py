#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/stone-game-ii
from typing import List
from functools import lru_cache
from itertools import accumulate


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        return self.solution2(piles)

    def solution1(self, piles: List[int]) -> int:
        """回溯方法1."""
        n = len(piles)
        ps = list(accumulate(piles, initial=0))

        @lru_cache(maxsize=None)
        def first(i, m):
            """先手能拿到的最高分."""
            if 2 * m > n - i:
                return ps[n] - ps[i]
            mx = 0
            for x in range(1, min(2 * m + 1, n - i + 1)):
                mx = max(mx, second(i + x, max(x, m)) + ps[i + x] - ps[i])
            return mx

        @lru_cache(maxsize=None)
        def second(i, m):
            """后手能拿到的最高分."""
            if i == n:
                return 0
            mn = float("inf")
            for x in range(1, min(2 * m + 1, n - i + 1)):
                mn = min(mn, first(i + x, max(x, m)))
            return mn

        return first(0, 1)

    def solution2(self, piles: List[int]) -> int:
        """回溯方法2."""
        n = len(piles)
        # 后缀和
        ss = list(accumulate(reversed(piles)))[::-1]

        @lru_cache(maxsize=None)
        def dfs(i, m):
            if i + 2 * m >= n:
                return ss[i]
            mn = float("inf")
            for x in range(1, 2 * m + 1):
                mn = min(mn, dfs(i + x, max(x, m)))
            return ss[i] - mn

        return dfs(0, 1)

    def solution3(self, piles: List[int]) -> int:
        """dp."""
        n = len(piles)
        # 后缀和
        ss = list(accumulate(reversed(piles)))[::-1]
        dp = [[0] * n for _ in range(n)]
        for i in reversed(range(n)):
            for j in reversed(range(1, n)):
                if i + 2 * j >= n:
                    dp[i][j] = ss[i]
                    continue
                mn = float("inf")
                for k in range(1, 2 * j + 1):
                    mn = min(mn, dp[i + k][max(j, k)])
                dp[i][j] = ss[i] - mn
        return dp[0][1] if len(piles) > 1 else piles[0]
