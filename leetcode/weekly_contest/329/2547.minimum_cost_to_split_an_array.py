#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/minimum-cost-to-split-an-array
from typing import List


class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        return self.solution2(nums, k)

    def solution1(self, nums: List[int], k: int) -> int:
        """递归解, 超时."""
        def process(i: int) -> int:
            """计算从0...i的最小代价."""
            if i == -1:
                return 0
            ans = float("inf")
            cnt = [0] * len(nums)
            cost = k
            # 选择分裂点: 前面算process, 后面算cost
            for j in reversed(range(i + 1)):
                x = nums[j]
                cnt[x] += 1
                if cnt[x] == 2:
                    cost += 2
                elif cnt[x] > 2:
                    cost += 1
                ans = min(ans, process(j - 1) + cost)
            return ans
        return process(len(nums) - 1)

    def solution2(self, nums: List[int], k: int) -> int:
        """DP."""
        n = len(nums)
        dp = [float("inf")] * n

        for i in range(n):
            cost = k
            cnt = [0] * n
            for j in reversed(range(i + 1)):
                x = nums[j]
                cnt[x] += 1
                if cnt[x] == 2:
                    cost += 2
                elif cnt[x] > 2:
                    cost += 1
                if j == 0:
                    dp[i] = min(dp[i], cost)
                else:
                    dp[i] = min(dp[i], dp[j - 1] + cost)
        return dp[-1]
