#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/difference-of-number-of-distinct-values-on-diagonals
from typing import List
from copy import deepcopy


class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        ans = deepcopy(grid)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                tl = set()
                p, q = i - 1, j - 1
                while p >= 0 and q >= 0:
                    tl.add(grid[p][q])
                    p -= 1
                    q -= 1
                br = set()
                p, q = i + 1, j + 1
                while p < m and q < n:
                    br.add(grid[p][q])
                    p += 1
                    q += 1
                ans[i][j] = abs(len(tl) - len(br))
        return ans
