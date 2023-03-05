#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/merge-intervals
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        max_r, ans = -1, []
        for ll, rr in intervals:
            if ll > max_r:  # 新区间
                ans.append([ll, rr])
            max_r = max(max_r, rr)
            if ans:
                ans[-1][1] = max_r
        return ans
