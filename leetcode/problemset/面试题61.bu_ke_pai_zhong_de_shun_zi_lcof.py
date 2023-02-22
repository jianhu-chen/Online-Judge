#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/bu-ke-pai-zhong-de-shun-zi-lcof
from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        k = 0
        for i, x in enumerate(nums):
            if x == 0:
                k += 1
            elif i != 0 and x == nums[i - 1]:
                return False
        return nums[4] - nums[k] < 5
