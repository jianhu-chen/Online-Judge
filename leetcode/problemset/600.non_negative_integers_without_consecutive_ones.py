#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/non-negative-integers-without-consecutive-ones
from functools import lru_cache


class Solution:
    def findIntegers(self, n: int) -> int:
        s = str(bin(n))[2:]

        @lru_cache(maxsize=None)
        def f(i: int, p1: int, is_limit: bool) -> int:
            if i == len(s):
                return 1
            up = int(s[i]) if is_limit else 1
            # 填0
            res = f(i + 1, False, is_limit and up == 0)
            # 填1
            if up == 1 and not p1:
                res += f(i + 1, True, is_limit)
            return res

        return f(0, False, True)
