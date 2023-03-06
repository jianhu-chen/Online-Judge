#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        """动态规划."""
        x = 0
        for i in range(2, n + 1):
            x = (x + m) % i
        return x
