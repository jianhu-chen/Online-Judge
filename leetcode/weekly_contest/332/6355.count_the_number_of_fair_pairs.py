#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/count-the-number-of-fair-pairs
from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i, x in enumerate(nums):
            LL, RR = -1, -1
            L, R = i + 1, n - 1
            while L <= R:
                M = L + ((R - L) >> 1)
                if nums[M] >= lower - x:
                    LL = M
                    R = M - 1
                else:
                    L = M + 1
            L, R = i + 1, n - 1
            while L <= R:
                M = L + ((R - L) >> 1)
                if nums[M] <= upper - x:
                    RR = M
                    L = M + 1
                else:
                    R = M - 1
            if LL != -1 and RR != -1:
                ans += RR - LL + 1
        return ans
