#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/fei-bo-na-qi-shu-lie-lcof
from functools import lru_cache

MOD = 10 ** 9 + 7


class Solution:
    def fib(self, n: int) -> int:
        return self.solution2(n)

    def solution1(self, n: int) -> int:
        """递归."""

        @lru_cache
        def f(i):
            if i <= 1:
                return i
            return f(i - 1) + f(i - 2)

        return f(n) % MOD

    def solution2(self, n: int) -> int:
        """dp."""
        if n <= 1:
            return n
        a, b = 0, 1
        for i in range(n):
            a, b = a + b, a
        return a % MOD
