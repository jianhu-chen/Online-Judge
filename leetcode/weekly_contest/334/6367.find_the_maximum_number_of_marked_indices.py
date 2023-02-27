#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/find-the-maximum-number-of-marked-indices
from typing import List


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n, ans = len(nums), 0
        i, j = 0, len(nums) // 2
        while i < n // 2 and j < n:
            if nums[i] * 2 <= nums[j]:
                ans += 2
                i += 1
            j += 1
        return ans
