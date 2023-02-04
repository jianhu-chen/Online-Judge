#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/palindrome-partitioning
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        path = []

        def dfs(i, j):
            if j == n:
                ans.append(path.copy())
                return

            # 不选
            if j != n - 1:
                dfs(i, j + 1)

            # 选
            t = s[i:j + 1]
            if t != t[::-1]:
                return

            path.append(t)
            dfs(j + 1, j + 1)
            path.pop()

        dfs(0, 0)
        return ans
