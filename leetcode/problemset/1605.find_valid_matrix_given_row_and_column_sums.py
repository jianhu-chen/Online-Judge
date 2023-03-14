#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/find-valid-matrix-given-row-and-column-sums
from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        i, j = 0, 0
        m, n = len(rowSum), len(colSum)
        ans = [[0] * n for _ in range(m)]
        while i < m and j < n:
            rs, cs = rowSum[i], colSum[j]
            if rs < cs:
                ans[i][j] = rs
                colSum[j] -= rs
                i += 1
            else:
                ans[i][j] = cs
                rowSum[i] -= cs
                j += 1
        return ans
