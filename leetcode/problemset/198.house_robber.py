#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/house-robber
from typing import List
from functools import lru_cache


class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.solution1(nums)

    def solution1(self, nums: List[int]) -> int:
        """回溯 + 缓存."""
        n = len(nums)

        @lru_cache
        def dfs(i):
            if i >= n:
                return 0
            return max(dfs(i + 1), dfs(i + 2) + nums[i])
        return dfs(0)

    def solution2(self, nums: List[int]) -> int:
        """dp."""
        n = len(nums)
        # dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        dp = [nums[0]] * n
        for i in range(1, n):
            ch1 = dp[i - 1]
            ch2 = dp[i - 2] + nums[i] if i > 1 else nums[1]
            dp[i] = max(ch1, ch2)
        return dp[-1]
