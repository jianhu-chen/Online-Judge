#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip
from typing import List


class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            if x == m - 1 and y == n - 1:
                return True
            grid[x][y] = 0
            return x < m - 1 and grid[x + 1][y] and dfs(x + 1, y) or \
                y < n - 1 and grid[x][y + 1] and dfs(x, y + 1)

        return not dfs(0, 0) or not dfs(0, 0)
