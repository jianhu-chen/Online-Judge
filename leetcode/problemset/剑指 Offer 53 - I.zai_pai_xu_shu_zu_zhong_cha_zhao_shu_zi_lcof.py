#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        LL, RR = -1, -1

        L, R = 0, n - 1
        while L <= R:
            M = L + ((R - L) >> 1)
            if nums[M] >= target:
                if nums[M] == target:
                    LL = M
                R = M - 1
            else:
                L = M + 1

        L, R = 0, n - 1
        while L <= R:
            M = L + ((R - L) >> 1)
            if nums[M] <= target:
                if nums[M] == target:
                    RR = M
                L = M + 1
            else:
                R = M - 1

        return RR - LL + 1 if LL != -1 else 0
