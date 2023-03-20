#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/numbers-with-repeated-digits
from functools import lru_cache


class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        s = str(n)

        @lru_cache(maxsize=None)
        def f(i: int, mask: int, is_limit: bool, is_num: bool) -> int:
            if i == len(s):
                return int(is_num)
            res = 0
            if not is_num:
                res = f(i + 1, mask, False, False)
            low = 0 if is_num else 1
            up = int(s[i]) if is_limit else 9
            for d in range(low, up + 1):
                if not mask & (1 << d):
                    res += f(i + 1, mask | (1 << d), is_limit and d == up, True)
            return res
        return n - f(0, 0, True, False)
