#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/find-positive-integer-solution-for-a-given-equation
from typing import List

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
"""


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        f = customfunction.f
        ans = []
        # O(nlogn)
        for x in range(1, 1001):
            L, R = 1, 1001
            while L <= R:
                y = L + ((R - L) >> 1)
                fxy = f(x, y)
                if fxy < z:
                    L = y + 1
                elif fxy > z:
                    R = y - 1
                else:
                    ans.append([x, y])
                    break
        return ans
