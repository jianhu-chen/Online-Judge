#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/n-queens
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        return self.process(0, n, 0, 0, 0, [])

    def process(self, i, n, L, C, R, lines):
        if i == n:
            return [lines]
        result = []
        for j in range(n):
            shift = (1 << j)
            if (shift & L) or (shift & C) or (shift & R):
                continue
            jL = (L | shift) << 1
            jC = C | shift
            jR = (R | shift) >> 1
            new_line = ["."] * n
            new_line[j] = "Q"
            result += self.process(i + 1, n, jL, jC, jR, lines + ["".join(new_line)])
        return result
