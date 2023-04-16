#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/find-the-width-of-columns-of-a-grid
from typing import List


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        res = [0] * len(grid[0])
        for row in grid:
            for i, x in enumerate(row):
                res[i] = max(res[i], len(str(x)))
        return res
