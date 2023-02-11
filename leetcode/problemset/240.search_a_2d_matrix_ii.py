#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/search-a-2d-matrix-ii
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # return any(target in row for row in matrix)
        return self.solution1(matrix, target)

    def solution1(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            L, R = 0, n - 1
            while L <= R:
                M = L + ((R - L) >> 1)
                if matrix[i][M] > target:
                    R = M - 1
                elif matrix[i][M] < target:
                    L = M + 1
                else:
                    return True
        return False

    def solution2(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else:
                return True
        return False
