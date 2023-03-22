#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/smallest-missing-non-negative-integer-after-operations
from typing import List
from collections import Counter


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mod = Counter(x % value for x in nums)
        i = 0
        while 1:
            mod[i % value] -= 1
            if mod[i % value] < 0:
                return i
            i += 1
