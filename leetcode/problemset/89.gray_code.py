#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/gray-code
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        return self.solution2(n)

    def solution1(self, n: int) -> List[int]:
        """镜像法."""
        if n == 0:
            return [0]
        tmp1 = self.solution1(n - 1)
        tmp2 = [(1 << n - 1) + x for x in reversed(tmp1)]
        return tmp1 + tmp2

    def solution2(self, n: int) -> List[int]:
        """公式法."""
        return [i ^ (i >> 1) for i in range(1 << n)]
