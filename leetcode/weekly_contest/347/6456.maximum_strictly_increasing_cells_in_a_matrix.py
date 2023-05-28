#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/maximum-strictly-increasing-cells-in-a-matrix
from typing import List
from collections import defaultdict


class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        v2pos = defaultdict(list)
        for i in range(m):
            for j in range(n):
                v2pos[mat[i][j]].append((i, j))

        ans = 0
        row_max, col_max = [0] * m, [0] * n
        for _, pos in sorted(v2pos.items(), key=lambda x: x[0]):
            mx = [max(row_max[i], col_max[j]) + 1 for i, j in pos]
            ans = max(max(mx), ans)
            # 更新
            for (i, j), m in zip(pos, mx):
                row_max[i] = max(row_max[i], m)
                col_max[j] = max(col_max[j], m)
        return ans
