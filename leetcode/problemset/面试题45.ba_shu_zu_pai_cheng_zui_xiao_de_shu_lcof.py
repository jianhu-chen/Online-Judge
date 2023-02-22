#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof
from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        n = len(nums)

        def qs(L, R):
            if L >= R:
                return
            left = L - 1
            idx = L
            while idx < R:
                if nums[idx] + nums[R] < nums[R] + nums[idx]:
                    left += 1
                    nums[left], nums[idx] = nums[idx], nums[left]
                idx += 1
            left += 1
            nums[left], nums[R] = nums[R], nums[left]
            qs(L, left - 1)
            qs(left + 1, R)
        qs(0, n - 1)
        return "".join(nums)
