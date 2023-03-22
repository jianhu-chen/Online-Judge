#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/number-of-2s-in-range-lcci
from functools import lru_cache


class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        s = str(n)

        @lru_cache(maxsize=None)
        def f(i: int, twos: int, is_limit: bool, is_num: bool) -> int:
            if i == len(s):
                return twos
            res = 0
            if not is_num:
                res = f(i + 1, 0, False, False)
            low = 0 if is_num else 1
            up = int(s[i]) if is_limit else 9
            for d in range(low, up + 1):
                res += f(i + 1, twos + int(d == 2), is_limit and d == up, True)
            return res

        return f(0, 0, True, False)
