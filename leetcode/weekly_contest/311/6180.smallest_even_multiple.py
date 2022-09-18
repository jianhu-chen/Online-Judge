#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/smallest-even-multiple

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n <= 2:
            return 2
        elif n % 2 == 0:
            return n
        else:
            return 2 * n
