#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/form-smallest-number-from-two-digit-arrays
from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        tmp = set(nums1) & set(nums2)
        if tmp:
            return min(tmp)
        mn1, mn2 = min(nums1), min(nums2)
        return min(mn1 * 10 + mn2, mn2 * 10 + mn1)
