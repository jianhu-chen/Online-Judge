#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/minimum-score-triangulation-of-polygon
from typing import List
from functools import lru_cache


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        return self.solution2(values)

    def solution1(self, values: List[int]) -> int:
        n = len(values)

        @lru_cache(maxsize=None)
        def dfs(i, j):
            if j - i == 1:  # 相邻的两个点
                return 0
            res = float("inf")
            m = values[i] * values[j]
            for k in range(i + 1, j):
                res = min(res, dfs(i, k) + dfs(k, j) + m * values[k])
            return res

        return dfs(0, n - 1)

    def solution2(self, values: List[int]) -> int:
        """动态规划."""
        n = len(values)
        f = [[float("inf")] * n for _ in range(n)]
        for i in range(n - 2, -1, -1):
            f[i][i + 1] = 0
            for j in range(i + 2, n):
                m = values[i] * values[j]
                for k in range(i + 1, j):
                    f[i][j] = min(f[i][j], f[i][k] + f[k][j] + m * values[k])
        return f[0][n - 1]
