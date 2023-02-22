#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/minimum-number-of-taps-to-open-to-water-a-garden
from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        """贪心."""
        # O(n)
        farthest = [0] * (n + 1)
        for i in range(n + 1):
            left, right = max(0, i - ranges[i]), min(n, i + ranges[i])
            farthest[left] = max(farthest[left], right)
        # O(n)
        pre, end, ans = 0, 0, 0
        for i in range(n + 1):
            if i > end:
                return -1
            end = max(end, farthest[i])
            if i == pre and i != n:
                ans += 1
                pre = end
        return ans
