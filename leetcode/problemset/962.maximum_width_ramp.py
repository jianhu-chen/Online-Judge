#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/maximum-width-ramp
from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        return self.solution2(nums)

    def solution1(self, nums: List[int]) -> int:
        """排序."""
        ans, m = 0, float("inf")
        for i in sorted(range(len(nums)), key=nums.__getitem__):
            ans = max(ans, i - m)
            m = i if i < m else m
        return ans

    def solution2(self, nums: List[int]) -> int:
        """单调栈."""
        st = []
        for i, x in enumerate(nums):
            if not st or nums[st[-1]] > x:
                st.append(i)
        ans = 0
        for j in reversed(range(len(nums))):
            while st and nums[j] >= nums[st[-1]]:
                ans = max(ans, j - st.pop())
        return ans
