#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/largest-local-values-in-a-matrix
from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        return self.solution2(grid)

    def solution1(self, grid: List[List[int]]) -> List[List[int]]:
        """暴力解."""
        n = len(grid)
        ans = [[0] * (n - 2) for _ in range(n - 2)]
        for i in range(n - 2):
            for j in range(n - 2):
                ans[i][j] = max(grid[x][y] for x in range(i, i + 3) for y in range(j, j + 3))
        return ans

    def solution2(self, grid: List[List[int]]) -> List[List[int]]:
        """二维单调队列."""

        def max_pool1d(x, k, axis):
            if axis == 0:
                x = list(zip(*x))  # transpose
            m, n = len(x), len(x[0])
            ans = [[] for _ in range(m)]
            for i in range(m):
                vec = x[i]
                j, q = 0, []
                while j < n:
                    while q and vec[q[-1]] <= vec[j]:
                        q.pop()
                    q.append(j)
                    if q[0] == j - k:
                        q.pop(0)
                    if j >= k - 1:
                        ans[i].append(x[i][q[0]])
                    j += 1
            return ans if axis == 1 else list(zip(*ans))

        grid = max_pool1d(grid, k=3, axis=0)
        grid = max_pool1d(grid, k=3, axis=1)
        return grid
