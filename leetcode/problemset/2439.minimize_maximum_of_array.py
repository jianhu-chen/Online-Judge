#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/minimize-maximum-of-array
from typing import List


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)

        def check(mx):
            diff = 0
            for i in reversed(range(1, n)):
                diff = max(nums[i] + diff - mx, 0)
            return nums[0] + diff <= mx

        L, R = 0, max(nums)
        ans = R
        while L <= R:
            M = L + ((R - L) >> 1)
            if check(M):
                ans = M
                R = M - 1
            else:
                L = M + 1
        return ans
