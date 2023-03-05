#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/kth-largest-element-in-an-array
from random import randint
from typing import List


def quick_select(nums, L, R, k):
    """快速选择, 返回 nums 中第 k 大的数 (k 从 0 开始)."""
    t = randint(L, R)
    nums[t], nums[R] = nums[R], nums[t]
    left, idx = L - 1, L
    while idx < R:
        if nums[idx] > nums[R]:
            left += 1
            nums[left], nums[idx] = nums[idx], nums[left]
        idx += 1
    left += 1
    nums[left], nums[R] = nums[R], nums[left]
    if left == k:
        return nums[left]
    elif left > k:
        return quick_select(nums, L, left - 1, k)
    elif left < k:
        return quick_select(nums, left + 1, R, k)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return quick_select(nums, 0, len(nums) - 1, k - 1)
