#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/find-the-longest-balanced-substring-of-a-binary-string

class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        cnt0, cnt1 = 0, 0
        res = 0
        for ch in s:
            if ch == "0":
                if cnt1 != 0:
                    cnt0 = 0
                    cnt1 = 0
                cnt0 += 1
            else:
                cnt1 += 1
                res = max(res, min(cnt0, cnt1) * 2)
        return res
