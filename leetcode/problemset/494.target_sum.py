#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/target-sum
from typing import List
from functools import cache


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.solution3(nums, target)

    def solution1(self, nums: List[int], target: int) -> int:
        limit = sum(nums) - target
        if limit < 0 or limit % 2 != 0:
            return 0
        neg = limit // 2

        @cache
        def process(idx, t):
            """idx开始到最后, 凑t."""
            if idx == len(nums):
                return 1 if t == 0 else 0
            return process(idx + 1, t) + process(idx + 1, t - nums[idx])
        return process(0, neg)

    def solution2(self, nums: List[int], target: int) -> int:
        """dp"""
        limit = sum(nums) - target
        if limit < 0 or limit % 2 != 0:
            return 0
        neg = limit // 2

        n = len(nums)
        dp = [[0] * (neg + 1) for _ in range(n + 1)]
        dp[n][0] = 1
        for i in reversed(range(n)):
            for j in range(neg + 1):
                dp[i][j] = dp[i + 1][j]
                if j - nums[i] >= 0:
                    dp[i][j] += dp[i + 1][j - nums[i]]
        return dp[0][neg]

    def solution3(self, nums: List[int], target: int) -> int:
        """dp 压缩."""
        limit = sum(nums) - target
        if limit < 0 or limit % 2 != 0:
            return 0
        neg = limit // 2

        n = len(nums)
        dp = [0] * (neg + 1)
        dp[0] = 1
        for i in reversed(range(n)):
            for j in reversed(range(neg + 1)):
                if j - nums[i] >= 0:
                    dp[j] += dp[j - nums[i]]
        return dp[neg]
