#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/triples-with-bitwise-and-equal-to-zero
from typing import List
from collections import Counter


class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        """三层循环改两层."""
        # O(n^2)
        cnt = Counter(x & y for x in nums for y in nums)
        return sum(c for x, c in cnt.items() for y in nums if x & y == 0)
