#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/minimum-cost-to-make-all-characters-equal

class Solution:
    def minimumCost(self, s: str) -> int:
        ans = 0
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                ans += min(i, len(s) - i)
        return ans
