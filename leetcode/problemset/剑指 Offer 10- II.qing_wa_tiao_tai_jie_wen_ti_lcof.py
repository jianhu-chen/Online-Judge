#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/qing-wa-tiao-tai-jie-wen-ti-lcof
MOD = 10 ** 9 + 7


class Solution:
    def numWays(self, n: int) -> int:
        if n <= 1:
            return 1
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = a + b, a
        return a % MOD
