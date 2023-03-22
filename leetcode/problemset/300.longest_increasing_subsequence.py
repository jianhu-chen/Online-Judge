#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/longest-increasing-subsequence
from typing import List
from functools import lru_cache


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.solution2(nums)

    def solution1(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(maxsize=None)
        def dfs(i: int) -> int:
            """返回以nums[i]结尾的最长严格递增子序列."""
            res = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, dfs(j))
            return res + 1

        return max(dfs(x) for x in range(n))

    def solution2(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(n):
            res = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, dp[j])
            dp[i] = res + 1
        return max(dp)
