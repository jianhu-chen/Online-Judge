#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/count-distinct-numbers-on-board

class Solution:
    def distinctIntegers(self, n: int) -> int:
        # n在桌面, 下一轮n-1就在桌面了, 不断循环后 [2, n] 都在桌面上
        # 特例: n == 1
        return 1 if n == 1 else n - 1
