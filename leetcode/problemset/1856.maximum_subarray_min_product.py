#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/maximum-subarray-min-product
from typing import List


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        # 找出两侧最近的比自己小的值, 单调递增栈
        left = [None] * len(nums)
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            left[i] = stack[-1] if stack else None
            stack.append(i)

        right = [None] * len(nums)
        stack = []
        for i in reversed(range(len(nums))):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            right[i] = stack[-1] if stack else None
            stack.append(i)

        pre_sum = [0]
        for i in range(len(nums)):
            pre_sum.append(nums[i] + pre_sum[-1])

        result = 0
        for i in range(len(nums)):
            L = left[i] + 1 if left[i] is not None else 0
            R = right[i] if right[i] is not None else len(nums)
            result = max(nums[i] * (pre_sum[R] - pre_sum[L]), result)
        return result % (10 ** 9 + 7)
