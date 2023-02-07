#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/house-robber-iv
from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        """
        二分.
        198.打家劫舍: https://leetcode.cn/problems/house-robber/.
        定义 dp[i] 表示 偷前 i 个房子, 在窃取能力不超过max的情况下, 最多可以偷多少个房子
        dp[i] = max(dp[i - 1], dp[i - 2] + 1) => dp[i + 2] = max(dp[i + 1], dp[i] + 1)
        """
        def check(m):
            dp = [0] * (len(nums) + 2)
            for i in range(len(nums)):
                dp[i + 2] = dp[i + 1]
                if nums[i] <= m:
                    dp[i + 2] = max(dp[i + 2], dp[i] + 1)
            return dp[-1]

        def check2(m):
            """空间优化版."""
            dp0, dp1 = 0, 0
            for i in range(len(nums)):
                tmp = dp1
                if nums[i] <= m:
                    tmp = max(tmp, dp0 + 1)
                dp0, dp1 = dp1, tmp
            return dp1

        # 二分
        ans = 0
        L, R = 0, max(nums)
        while L <= R:
            M = L + ((R - L) >> 1)
            if check2(M) < k:
                L = M + 1
            else:
                ans = M
                R = M - 1
        return ans
