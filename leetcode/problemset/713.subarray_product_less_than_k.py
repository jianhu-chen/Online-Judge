#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/subarray-product-less-than-k
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        ans = 0
        m = 1
        left = 0
        for right, x in enumerate(nums):
            m *= x
            while m >= k:
                m /= nums[left]
                left += 1
            ans += right - left + 1
        return ans
