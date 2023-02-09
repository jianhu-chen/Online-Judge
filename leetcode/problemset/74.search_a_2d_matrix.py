#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/search-a-2d-matrix
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        L, R = 0, m * n - 1
        while L <= R:
            M = L + ((R - L) >> 1)
            i, j = M // n, M % n
            if matrix[i][j] < target:
                L = M + 1
            elif matrix[i][j] > target:
                R = M - 1
            else:
                return True
        return False
