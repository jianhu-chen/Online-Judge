#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/split-with-minimum-sum


class Solution:
    def splitNum(self, num: int) -> int:
        """贪心 + 排序."""
        num = sorted(str(num))
        t = [0, 0]
        for i, x in enumerate(num):
            t[i & 1] = t[i & 1] * 10 + int(x)
        return t[0] + t[1]
