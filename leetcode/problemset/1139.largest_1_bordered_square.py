#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/largest-1-bordered-square
from copy import deepcopy
from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        # 1 1 1 1      4 3 2 1     4 1 3 4
        # 1 0 1 1  ->  1 0 2 1  |  3 0 2 3
        # 1 1 1 1 右边  4 3 2 1 下边 2 1 1 2
        # 1 0 0 1      1 0 0 1     1 0 0 1
        m, n = len(grid), len(grid[0])
        rs, bs = deepcopy(grid), deepcopy(grid)

        for i in range(m):
            for j in reversed(range(n - 1)):
                if grid[i][j] == 1:
                    rs[i][j] += rs[i][j + 1]

        for j in range(n):
            for i in reversed(range(m - 1)):
                if grid[i][j] == 1:
                    bs[i][j] += bs[i + 1][j]

        # O(n^3)
        mx = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                mk = rs[i][j] if rs[i][j] < bs[i][j] else bs[i][j]
                for k in reversed(range(mk)):
                    if rs[i + k][j] >= k + 1 and bs[i][j + k] >= k + 1:
                        mx = k + 1 if k + 1 > mx else mx
        return mx ** 2
