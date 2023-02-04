#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/subsets
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = []

        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return
            # 不选
            dfs(i + 1)
            # 选
            path.append(nums[i])
            dfs(i + 1)
            path.pop()

        dfs(0)
        return ans
