#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/combination-sum-iii
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans, path = [], []

        def dfs(i, s):
            if len(path) == k:
                if s == n:
                    ans.append(path.copy())
                return
            if i > 9 or s >= n:
                return
            dfs(i + 1, s)  # 不选
            path.append(i)
            dfs(i + 1, s + i)  # 选
            path.pop()

        dfs(1, 0)
        return ans
