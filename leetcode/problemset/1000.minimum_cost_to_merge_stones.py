#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/minimum-cost-to-merge-stones
from typing import List
from functools import lru_cache
from itertools import accumulate


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        return self.solution3(stones, k)

    def solution1(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1):
            return -1

        ps = list(accumulate(stones, initial=0))

        @lru_cache(maxsize=None)
        def dfs(i, j, p):
            """返回把i...j堆石块合并成p堆的最低成本."""
            if i == j and p == 1:
                return 0

            if p == 1:
                return dfs(i, j, k) + ps[j + 1] - ps[i]
            else:
                return min(
                    dfs(i, m, 1) + dfs(m + 1, j, p - 1)
                    for m in range(i, j, k - 1)
                )

        return dfs(0, n - 1, 1)

    def solution2(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1):
            return -1

        ps = list(accumulate(stones, initial=0))

        @lru_cache(maxsize=None)
        def dfs(i, j):
            if i == j:
                return 0
            res = min(
                dfs(i, m) + dfs(m + 1, j)
                for m in range(i, j, k - 1)
            )
            if (j - i) % (k - 1) == 0:
                res += ps[j + 1] - ps[i]
            return res

        return dfs(0, n - 1)

    def solution3(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1):
            return -1

        ps = list(accumulate(stones, initial=0))
        f = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                res = float("inf")
                for m in range(i, j, k - 1):
                    res = min(res, f[i][m] + f[m + 1][j])
                if (j - i) % (k - 1) == 0:
                    res += ps[j + 1] - ps[i]
                f[i][j] = res
        return f[0][n - 1]
