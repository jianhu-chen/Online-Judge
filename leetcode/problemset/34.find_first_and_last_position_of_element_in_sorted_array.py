#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        L, R = 0, len(nums) - 1
        while L <= R:
            M = L + ((R - L) >> 1)
            if nums[M] >= target:
                if nums[M] == target:
                    ans[0] = M
                R = M - 1
            else:
                L = M + 1

        L, R = 0, len(nums) - 1
        while L <= R:
            M = L + ((R - L) >> 1)
            if nums[M] <= target:
                if nums[M] == target:
                    ans[1] = M
                L = M + 1
            else:
                R = M - 1
        return ans
