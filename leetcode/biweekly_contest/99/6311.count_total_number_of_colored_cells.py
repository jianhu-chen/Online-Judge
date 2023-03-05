#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/count-total-number-of-colored-cells

class Solution:
    def coloredCells(self, n: int) -> int:
        """找规律."""
        # 1 -> 1  diff = 1
        # 2 -> 5  diff = 4
        # 3 -> 13 diff = 8
        # 4 -> 25 diff = 12
        return 1 if n == 1 else self.coloredCells(n - 1) + 4 * (n - 1)
