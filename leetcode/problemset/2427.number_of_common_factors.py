#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/number-of-common-factors

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        a, b = (b, a) if b < a else (a, b)
        return sum(a % x == b % x == 0 for x in range(1, a + 1))
