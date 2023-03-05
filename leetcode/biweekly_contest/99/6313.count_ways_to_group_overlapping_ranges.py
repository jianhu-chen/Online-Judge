#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/count-ways-to-group-overlapping-ranges
from typing import List

MOD = 10 ** 9 + 7


class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        cnt, max_r = 0, -1
        for ll, rr in ranges:
            cnt += ll > max_r
            max_r = max(max_r, rr)
        return pow(2, cnt, MOD)
