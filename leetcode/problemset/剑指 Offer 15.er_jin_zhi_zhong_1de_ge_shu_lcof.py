#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/er-jin-zhi-zhong-1de-ge-shu-lcof

class Solution:
    def hammingWeight(self, n: int) -> int:
        return self.solution2(n)

    def solution1(self, n):
        """时间O(k)."""
        cnt = 0
        while n:
            cnt += n & 1
            n >>= 1
        return cnt

    def solution2(self, n):
        """时间O(logk)."""
        cnt = 0
        while n:
            n &= (n - 1)  # 去掉最右侧的1
            cnt += 1
        return cnt
