#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/count-the-digits-that-divide-a-number
from functools import lru_cache


class Solution:
    def countDigits(self, num: int) -> int:
        ans = 0
        n = num

        @lru_cache
        def check(d: int) -> int:
            if n % d == 0:
                return 1
            return 0

        while num != 0:
            digit = num % 10
            ans += check(digit)
            num //= 10
        return ans
