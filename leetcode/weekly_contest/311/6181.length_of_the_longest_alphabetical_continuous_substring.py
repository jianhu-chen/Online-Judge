#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/length-of-the-longest-alphabetical-continuous-substring

class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        max_len = 1
        i, j = 0, 1
        while j < len(s):
            while j < len(s) and ord(s[j]) - ord(s[j - 1]) == 1:
                j += 1
            max_len = max(max_len, j - i)
            i, j = j, j + 1
        return max_len
