#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof

class Solution:
    def translateNum(self, num: int) -> int:
        if num < 10:
            return 1
        n2, n1 = 2 if 9 < num % 100 < 26 else 1, 1
        num //= 10
        while num:
            if 9 < num % 100 < 26:
                n2, n1 = n1 + n2, n2
            else:
                n2, n1 = n2, n2
            num //= 10
        return n2
