#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/find-longest-awesome-substring

class Solution:
    def longestAwesome(self, s: str) -> int:
        ps, first = 0, {0: -1}
        ans = 1
        for i, ch in enumerate(s):
            bit = 1 << int(ch)
            ps ^= bit
            if ps in first:
                ans = max(ans, i - first[ps])
            else:
                first[ps] = i
            for j in range(10):
                tbit = ps ^ (1 << j)
                if tbit in first:
                    ans = max(ans, i - first[tbit])
        return ans
