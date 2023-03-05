#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/k-closest-points-to-origin
from random import randint
from typing import List


def quick_select(nums, L, R, k, key=lambda x: x):
    """快速选择, 返回 nums 中前 k 小的数."""
    t = randint(L, R)
    nums[t], nums[R] = nums[R], nums[t]
    left, idx = L - 1, L
    while idx < R:
        if key(nums[idx]) < key(nums[R]):
            left += 1
            nums[left], nums[idx] = nums[idx], nums[left]
        idx += 1
    left += 1
    nums[left], nums[R] = nums[R], nums[left]
    if left == k:
        return nums[:left]
    elif left > k:
        return quick_select(nums, L, left - 1, k)
    elif left < k:
        return quick_select(nums, left + 1, R, k)


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """快速选择."""
        n = len(points)
        if k == n:
            return points
        distance = [(x * x + y * y, (x, y)) for x, y in points]
        topk = quick_select(distance, 0, len(distance) - 1, k, key=lambda x: x[0])
        return [r for _, r in topk]
