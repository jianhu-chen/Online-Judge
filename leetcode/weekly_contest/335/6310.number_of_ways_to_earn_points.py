#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/number-of-ways-to-earn-points
from typing import List
from functools import lru_cache

MOD = 10 ** 9 + 7


class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        # return self.solution1(target, types)
        # return self.solution2(target, types)
        return self.solution3(target, types)

    def solution1(self, target: int, types: List[List[int]]) -> int:
        """回溯 + 记忆化搜索."""

        @lru_cache(maxsize=None)
        def dfs(i, j):
            if j == 0:
                return 1
            if i < 0:
                return 0

            s, (cnt, marks) = 0, types[i]
            for k in range(min(cnt, j // marks) + 1):
                s += dfs(i - 1, j - k * marks)
            return s % MOD

        return dfs(len(types) - 1, target)

    def solution2(self, target: int, types: List[List[int]]) -> int:
        """动态规划."""
        n = len(types)
        # dp[i][j]: 前i种题型, 取得j分的方法数量
        dp = [[1] + [0] * target for _ in range(n + 1)]
        for i, (cnt, marks) in enumerate(types, 1):
            for j in range(1, target + 1):
                for k in range(min(cnt, j // marks) + 1):
                    dp[i][j] += dp[i - 1][j - k * marks]
        return dp[-1][-1] % MOD

    def solution3(self, target: int, types: List[List[int]]) -> int:
        """动态规划 + 状态压缩."""
        dp = [1] + [0] * target
        for cnt, marks in types:
            for j in reversed(range(1, target + 1)):
                for k in range(1, min(cnt, j // marks) + 1):
                    dp[j] += dp[j - k * marks]
                dp[j] %= MOD
        return dp[-1]
