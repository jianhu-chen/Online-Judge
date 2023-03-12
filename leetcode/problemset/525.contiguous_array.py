#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/contiguous-array
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ps, first = 0, {0: -1}
        ans = 0
        for i, x in enumerate(nums):
            ps += x if x else -1
            if ps in first:
                ans = i - first[ps] if i - first[ps] > ans else ans
            else:
                first[ps] = i
        return ans
