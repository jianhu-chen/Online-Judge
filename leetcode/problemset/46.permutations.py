#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/permutations
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, path = [], []

        def dfs(i, rest):
            if not rest:
                ans.append(path.copy())
                return
            for x in rest:
                path.append(x)
                dfs(i + 1, rest - {x})
                path.pop()

        dfs(0, set(nums))
        return ans
