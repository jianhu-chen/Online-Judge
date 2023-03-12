#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/find-the-longest-substring-containing-vowels-in-even-counts

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        ps, first = 0, {0: -1}
        ch2bit = dict(zip("aeiou", range(5)))
        ans = 0
        for i, ch in enumerate(s):
            ps ^= 1 << ch2bit[ch] if ch in ch2bit else 0
            if ps in first:
                ans = i - first[ps] if i - first[ps] > ans else ans
            else:
                first[ps] = i
        return ans
