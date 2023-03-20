#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/count-special-integers
from functools import lru_cache


class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        """数位dp."""
        s = str(n)

        @lru_cache(maxsize=None)
        def f(i: int, mask: int, is_limit: bool, is_num: bool) -> int:
            """
            mask: 数位, 存放已经有的数字
            is_limit: 是否第i位前的每一位都达到了n对应位的值
            is_num: 是否第i位前都是0(还未构成数字)
            """
            if i == len(s):
                return int(is_num)
            res = 0
            if not is_num:
                res = f(i + 1, mask, False, False)
            low = 0 if is_num else 1
            up = int(s[i]) if is_limit else 9
            for d in range(low, up + 1):
                if (mask & (1 << d)) == 0:
                    res += f(i + 1, mask | (1 << d), is_limit and d == up, True)
            return res
        return f(0, 0, True, False)
