#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/minimum-size-subarray-sum
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """双指针, 时间复杂度 O(n), 空间复杂度 O(1)."""
        ans = float("inf")
        left = 0
        s = 0
        for right, n in enumerate(nums):
            s += n
            while s >= target:
                ans = min(ans, right - left + 1)
                s -= nums[left]
                left += 1
        return ans if ans != float("inf") else 0
