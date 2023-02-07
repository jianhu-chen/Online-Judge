#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/n-queens
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans, path = [], []

        def dfs(i, ll, cl, rl):
            if i == n:
                ans.append(path.copy())
                return
            for j in range(n):
                s = 1 << j
                if s & ll or s & cl or s & rl:
                    continue
                path.append("." * j + "Q" + "." * (n - j - 1))
                dfs(i + 1, (ll | (1 << j)) >> 1, cl | (1 << j), (rl | (1 << j)) << 1)
                path.pop()

        dfs(0, 0, 0, 0)
        return ans
