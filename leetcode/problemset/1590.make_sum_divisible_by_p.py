#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/make-sum-divisible-by-p
from typing import List
from functools import reduce


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        ps, s = 0, reduce(int.__add__, nums)
        last, ans = {ps % p: -1}, len(nums)
        for i, x in enumerate(nums):
            ps += x
            last[ps % p] = i
            j = last.get((ps - s) % p)
            if j is not None:
                ans = i - j if i - j < ans else ans
        return ans if ans != len(nums) else -1
