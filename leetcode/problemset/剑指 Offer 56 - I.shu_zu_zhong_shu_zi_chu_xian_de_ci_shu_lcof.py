#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof
from typing import List
from functools import reduce


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        eor = reduce(lambda x, y: x ^ y, nums)
        right1 = eor & -eor
        num1 = 0
        for x in nums:
            if x & right1:
                num1 ^= x
        num2 = reduce(lambda x, y: x ^ y, nums, num1)
        return num1, num2
