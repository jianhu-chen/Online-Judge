#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/jian-sheng-zi-lcof
import math


class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n - 1
        d, m = divmod(n, 3)
        if m == 0:
            ans = math.pow(3, d)
        elif m == 1:
            ans = math.pow(3, d - 1) * 4
        else:
            ans = math.pow(3, d) * 2
        return int(ans)
