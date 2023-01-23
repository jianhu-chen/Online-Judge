#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/increment-submatrices-by-one
from typing import List


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        return self.solution2(n, queries)

    def solution1(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        """一维差分."""
        ans = [[0] * n for _ in range(n)]
        for r1, c1, r2, c2 in queries:
            for r in range(r1, r2 + 1):
                ans[r][c1] += 1
                if c2 < n - 1:
                    ans[r][c2 + 1] -= 1
        # 求前缀和
        for row in ans:
            for j in range(1, n):
                row[j] += row[j - 1]
        return ans

    def solution2(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        """二维差分."""
        ans = [[0] * n for _ in range(n)]
        for r1, c1, r2, c2 in queries:
            ans[r1][c1] += 1
            if c2 < n - 1:
                ans[r1][c2 + 1] -= 1
            if r2 < n - 1 and c2 < n - 1:
                ans[r2 + 1][c2 + 1] += 1
            if r2 < n - 1:
                ans[r2 + 1][c1] -= 1

        # 二维差分求二维前缀和得到原始矩阵
        for j in range(1, n):
            ans[0][j] += ans[0][j - 1]

        for j in range(1, n):
            ans[j][0] += ans[j - 1][0]

        for i in range(1, n):
            for j in range(1, n):
                ans[i][j] = ans[i][j - 1] + ans[i - 1][j] - ans[i - 1][j - 1] + ans[i][j]

        return ans
