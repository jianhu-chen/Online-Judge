#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 参考第 162 题: https://leetcode.cn/problems/find-peak-element
        n = len(nums)
        if n == 1:
            return nums[0]

        if nums[0] < nums[1] and nums[0] < nums[-1]:
            return nums[0]
        if nums[-1] < nums[-2] and nums[-1] < nums[0]:
            return nums[-1]

        L, R = 0, n - 1
        while L <= R:
            M = L + ((R - L) >> 1)
            if nums[M] < nums[M - 1] and nums[M] < nums[M + 1]:
                return nums[M]
            elif nums[M] >= nums[0]:
                L = M + 1
            elif nums[M] <= nums[-1]:
                R = M - 1

# [0,1,2,3,4]
# [5,1,2,3,4]
