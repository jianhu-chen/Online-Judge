#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/shu-zhi-de-zheng-shu-ci-fang-lcof

class Solution:
    def myPow(self, x: float, n: int) -> float:

        def quick_pow1(a, b):
            """回溯版 空间O(logn)."""
            if b == 0:
                return 1
            c = quick_pow1(a, b // 2)
            return c * c * a if b & 1 else c * c

        def quick_pow2(a, b):
            """迭代版 空间O(1)."""
            if b == 0:
                return 1
            ans = 1
            while b:
                if b & 1:
                    ans *= a
                a *= a
                b >>= 1
            return ans

        return quick_pow2(x, n) if n >= 0 else 1 / quick_pow2(x, -n)
