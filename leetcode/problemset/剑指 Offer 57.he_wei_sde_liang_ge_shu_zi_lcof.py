#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/he-wei-sde-liang-ge-shu-zi-lcof
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left <= right:
            s = nums[left] + nums[right]
            if s > target:
                right -= 1
            elif s < target:
                left += 1
            else:
                return nums[left], nums[right]
