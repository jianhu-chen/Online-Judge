#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/minimum-operations-to-make-all-array-elements-equal
from bisect import bisect_left
from typing import List
from itertools import accumulate


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        ps = list(accumulate(nums, initial=0))
        res = []
        for q in queries:
            idx = bisect_left(nums, q)
            left = q * idx - ps[idx]
            right = ps[n] - ps[idx] - q * (n - idx)
            res.append(left + right)
        return res
