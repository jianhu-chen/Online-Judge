#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/number-of-digit-one
from functools import lru_cache


class Solution:
    def countDigitOne(self, n: int) -> int:
        s = str(n)

        @lru_cache(maxsize=None)
        def f(i: int, ones: int, is_limit: bool) -> int:
            if i == len(s):
                return ones
            res = 0
            up = int(s[i]) if is_limit else 9
            for d in range(up + 1):
                res += f(i + 1, ones + (d == 1), is_limit and d == up)
            return res

        return f(0, 0, True)
