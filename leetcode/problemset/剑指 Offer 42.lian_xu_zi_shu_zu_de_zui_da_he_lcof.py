#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s, ans = -float("inf"), -float("inf")
        for x in nums:
            s = max(s + x, x)
            ans = max(ans, s)
        return ans
