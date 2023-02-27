#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/qiu-12n-lcof

class Solution:
    def sumNums(self, n: int) -> int:

        def dfs(x):
            return 0 if x == 0 else x + dfs(x - 1)

        return dfs(n)
