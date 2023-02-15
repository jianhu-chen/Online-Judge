#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof
from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
