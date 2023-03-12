#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/find-longest-subarray-lcci
from typing import List


class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        max_len, s, e = 0, 0, 0
        ps, first = 0, {0: -1}
        for i, ch in enumerate(array):
            ps += 1 if ch >= 'A' else -1
            if ps in first:
                if i - first[ps] > max_len:
                    max_len = i - first[ps]
                    s, e = first[ps], i
            else:
                first[ps] = i
        return array[s + 1:e + 1]
