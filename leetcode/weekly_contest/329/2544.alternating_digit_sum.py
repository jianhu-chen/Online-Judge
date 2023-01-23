#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/alternating-digit-sum

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        return self.solution2(n)

    def solution1(self, n: int) -> int:
        ans = 0
        sign = 1 if len(str(n)) % 2 else -1
        while n:
            ans += sign * (n % 10)
            n //= 10
            sign = -sign
        return ans

    def solution2(self, n: int) -> int:
        """赛后优化: 空间复杂度O(1)"""
        ans, sign = 0, 1
        while n:
            ans += sign * (n % 10)
            n //= 10
            sign = -sign
        return ans * -sign
