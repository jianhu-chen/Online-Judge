#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/find-pivot-index
from typing import List
from functools import reduce


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ps, s = 0, reduce(int.__add__, nums)
        for i, x in enumerate(nums):
            if ps == s - x - ps:
                return i
            ps += x
        return -1
