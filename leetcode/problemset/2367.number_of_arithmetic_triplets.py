#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/number-of-arithmetic-triplets
from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        m = set(nums)
        return sum(x - diff in m and x + diff in m for x in nums)
