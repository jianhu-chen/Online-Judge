#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/li-wu-de-zui-da-jie-zhi-lcof
from copy import deepcopy
from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = deepcopy(grid)
        for i in range(m):
            for j in range(n):
                p1, p2 = 0, 0
                if i != 0:
                    p1 = dp[i - 1][j]
                if j != 0:
                    p2 = dp[i][j - 1]
                dp[i][j] += p1 if p1 > p2 else p2
        return dp[-1][-1]
