#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/arithmetic-subarrays
from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        return self.solution2(nums, l, r)

    def solution1(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        """暴力解, 能过."""
        res = []
        for i, j in zip(l, r):
            sub = nums[i:j + 1]
            sub.sort()
            res.append(len(set([sub[k] - sub[k + 1] for k in range(j - i)])) == 1)
        return res

    def solution2(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i, j in zip(l, r):
            s = set(nums[i:j + 1])
            mx, mn = max(s), min(s)
            d, m = divmod(mx - mn, j - i)
            res.append(m == 0 and all([mn + k * d in s for k in range(j - i)]))
        return res
