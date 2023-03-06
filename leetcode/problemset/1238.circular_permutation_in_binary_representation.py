#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/circular-permutation-in-binary-representation
from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        """参见: https://leetcode.cn/problems/gray-code."""
        return (x ^ start for x in self.solution2(n))

    def solution1(self, n: int) -> List[int]:
        """镜像法."""
        if n == 0:
            return [0]
        left = self.solution1(n - 1)
        right = [(1 << n - 1) + x for x in reversed(left)]
        return [x for x in left + right]

    def solution2(self, n: int) -> List[int]:
        """公式法."""
        return (i ^ (i >> 1) for i in range(1 << n))
