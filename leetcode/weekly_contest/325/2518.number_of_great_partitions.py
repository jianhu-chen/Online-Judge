#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/number-of-great-partitions
from typing import List


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        # 正难则反
        # 坏分区: 两个分区中至少有一个分区的元素和小于k
        # 分区1: [], [1], [2], [3], [1, 2]
        # 分区2: [], [1], [2], [3], [1, 2]
        # 一共有 2^4 = 16 种分区方法, 减去坏分区, 就能得到好分区

        # 特殊判例
        if sum(nums) < 2 * k:
            return 0

        # 先算坏分区的数量, 相当于求目标和
        n = len(nums)
        dp = [0] * k
        dp[0] = 1
        for i in reversed(range(n)):
            for j in reversed(range(k)):
                if j - nums[i] >= 0:
                    dp[j] += dp[j - nums[i]]
        return (2 ** n - sum(dp) * 2) % (10 ** 9 + 7)
