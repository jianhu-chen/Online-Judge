#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/maximum-count-of-positive-integer-and-negative-integer
from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # 找小于0的第一个数
        lidx = -1
        L, R = 0, len(nums) - 1
        while L <= R:
            M = L + ((R - L) >> 1)
            if nums[M] < 0:
                L = M + 1
                lidx = M
            else:
                R = M - 1

        # 找大于0的第一个数
        ridx = -1
        L, R = 0, len(nums) - 1
        while L <= R:
            M = L + ((R - L) >> 1)
            if nums[M] > 0:
                R = M - 1
                ridx = M
            else:
                L = M + 1

        return max(lidx + 1, len(nums) - ridx if ridx != -1 else -float("inf"))
