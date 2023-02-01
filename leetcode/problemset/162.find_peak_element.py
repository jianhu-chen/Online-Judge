#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/find-peak-element
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return n - 1

        L, R = 0, n - 1
        while L <= R:
            M = L + ((R - L) >> 1)
            if nums[M] < nums[M + 1]:
                L = M + 1
            elif nums[M] < nums[M - 1]:
                R = M - 1
            else:
                return M
