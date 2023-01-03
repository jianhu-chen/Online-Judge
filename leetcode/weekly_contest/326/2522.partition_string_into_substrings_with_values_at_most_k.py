#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/partition-string-into-substrings-with-values-at-most-k

class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        """贪心"""
        for ch in s:
            if int(ch) > k:
                return -1

        ans = 0
        L, R = 0, 0
        while R < len(s):
            if int(s[L:R + 1]) <= k:
                R += 1
            else:
                ans += 1
                L = R

        return ans + 1
