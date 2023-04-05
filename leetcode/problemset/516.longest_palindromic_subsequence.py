#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/longest-palindromic-subsequence
from functools import lru_cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.solution1(s)

    def solution1(self, s: str) -> int:

        @lru_cache(maxsize=None)
        def dfs(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            if s[i] == s[j]:
                return dfs(i + 1, j - 1) + 2
            return max(dfs(i + 1, j), dfs(i, j - 1))

        return dfs(0, len(s) - 1)

    def solution2(self, s: str) -> int:
        # 动态规划
        n = len(s)
        f = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            f[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    f[i][j] = f[i + 1][j - 1] + 2
                else:
                    f[i][j] = max(f[i + 1][j], f[i][j - 1])
        return f[0][n - 1]
