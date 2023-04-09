#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/minimum-number-of-visited-cells-in-a-grid
from bisect import bisect_left
from typing import List


class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        """dp+优化."""
        m, n = len(grid), len(grid[0])
        stacks = [[] for _ in range(n)]  # 列单调栈
        for i in range(m - 1, -1, -1):
            st1 = []  # 行单调栈, 存(到达终点的最小步数, 列下标)
            for j in range(n - 1, -1, -1):
                st2 = stacks[j]
                res = float("inf")
                g = grid[i][j]
                if i == m - 1 and j == n - 1:
                    res = 1
                else:
                    # 向右: 在行单调栈上二分
                    k = bisect_left(st1, -j - g, key=lambda x: x[1])
                    if k < len(st1):
                        res = min(res, st1[k][0] + 1)
                    # 向下: 在列单调栈上二分
                    k = bisect_left(st2, -i - g, key=lambda x: x[1])
                    if k < len(st2):
                        res = min(res, st2[k][0] + 1)
                if res == float("inf"):  # 到不了终点
                    continue
                # 维护行单调栈
                while st1 and res < st1[-1][0]:
                    st1.pop()
                st1.append((res, -j))
                # 维护列单调栈
                while st2 and res < st2[-1][0]:
                    st2.pop()
                st2.append((res, -i))
        return res if res != float("inf") else -1
