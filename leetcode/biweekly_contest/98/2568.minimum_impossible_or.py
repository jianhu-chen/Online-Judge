#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/minimum-impossible-or
from typing import List


class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        """只需检查 2 ^ k 是否在 nums 中即可."""
        return self.solution2(nums)

    def solution1(self, nums: List[int]) -> int:
        """O(n + logmax(num)) + O(n)"""
        nums = set(nums)
        for i in range(31):
            if 1 << i not in nums:
                return 1 << i

    def solution2(self, nums: List[int]) -> int:
        mask = 0
        for x in nums:
            if x & (x - 1) == 0:  # 2的幂
                mask |= x
        # 取出mask最右侧的0
        mask = ~mask
        return mask & -mask
