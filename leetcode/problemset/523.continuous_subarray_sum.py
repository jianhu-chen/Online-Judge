#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/continuous-subarray-sum
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        ps, first = 0, {0: -1}
        for i, x in enumerate(nums):
            ps += x
            mod = ps % k
            if mod in first and first[mod] != i - 1:
                return True
            if mod not in first:
                first[mod] = i
        return False
