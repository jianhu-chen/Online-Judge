#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/que-shi-de-shu-zi-lcof
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        L, R = 0, n - 1
        while L <= R:
            M = L + ((R - L) >> 1)
            if nums[M] == M:
                L = M + 1
            elif nums[M] > M:
                R = M - 1
        return L
