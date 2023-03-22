#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/check-knight-tour-configuration
from typing import List


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)

        def dfs(i, j, x):
            if i < 0 or i >= n or j < 0 or j >= n:
                return False
            if grid[i][j] != x:
                return False
            if x == n * n - 1:
                return True
            return any([
                dfs(i - 1, j - 2, x + 1),
                dfs(i - 2, j - 1, x + 1),
                dfs(i + 1, j - 2, x + 1),
                dfs(i + 2, j - 1, x + 1),
                dfs(i - 1, j + 2, x + 1),
                dfs(i - 2, j + 1, x + 1),
                dfs(i + 1, j + 2, x + 1),
                dfs(i + 2, j + 1, x + 1)
            ])

        return dfs(0, 0, 0)
