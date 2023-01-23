#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/difference-between-element-sum-and-digit-sum-of-an-array
from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            ans += n
            while n:
                ans -= n % 10
                n //= 10
        return abs(ans)
