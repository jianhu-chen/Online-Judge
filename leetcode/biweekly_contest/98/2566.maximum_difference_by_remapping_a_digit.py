#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/maximum-difference-by-remapping-a-digit

class Solution:
    def minMaxDifference(self, num: int) -> int:
        # 时间复杂度 O(lognum)
        s = str(num)
        for c in s:
            if c != "9":
                break
        mx, mn = int(s.replace(c, "9")), int(s.replace(s[0], "0"))
        return mx - mn
