#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/find-the-array-concatenation-value
from typing import List


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans = 0
        i, j = 0, len(nums) - 1
        while i < j:
            x, y = nums[i], nums[j]
            while y:
                x *= 10
                y //= 10
            ans += x + nums[j]
            i, j = i + 1, j - 1
        if i == j:
            ans += nums[i]
        return ans
