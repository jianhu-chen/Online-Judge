#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/combinations
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans, path = [], []

        def dfs(i):
            if len(path) == k:
                ans.append(path.copy())
                return
            if i > n:
                return
            dfs(i + 1)  # 不选
            path.append(i)  # 选
            dfs(i + 1)
            path.pop()

        dfs(1)
        return ans
