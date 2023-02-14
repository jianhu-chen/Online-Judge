#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        return self.solution2(nums)

    def solution1(self, nums: List[int]) -> int:
        s = set()
        for x in nums:
            if x in s:
                return x
            else:
                s.add(x)

    def solution2(self, nums: List[int]) -> int:
        """原地交换, 空间复杂度 O(1)."""
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]:
                return nums[i]
            nums[nums[i]], nums[i] =  nums[i], nums[nums[i]]
        return -1
