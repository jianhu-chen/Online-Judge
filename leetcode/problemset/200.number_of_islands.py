#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/number-of-islands
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])

        def infect(x, y):
            if x < 0 or x > M - 1 or y < 0 or y > N - 1 or grid[x][y] != "1":
                return
            grid[x][y] = "2"
            infect(x - 1, y)
            infect(x + 1, y)
            infect(x, y - 1)
            infect(x, y + 1)

        result = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1":
                    result += 1
                    infect(i, j)
        return result
