#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/jump-game-ii
from typing import List
from collections import defaultdict


class Solution:
    def jump(self, nums: List[int]) -> int:
        return self.solution3(nums)

    def solution1(self, nums: List[int]) -> int:
        """dp."""
        n = len(nums)
        m = defaultdict(list)
        # O(1000n): m记录 某位置 到 能到达这个位置的前方的idx集合 的映射
        for i, x in enumerate(nums):
            for j in range(1, min(x + 1, n - i)):
                m[i + j].append(i)

        # O(1000n)
        dp = [n] * n
        dp[0] = 0
        for i in range(1, n):
            for p in m[i]:
                dp[i] = min(dp[i], dp[p] + 1)
        return dp[-1]

    def solution2(self, nums: List[int]) -> int:
        """贪心1."""
        n, step = len(nums), 0
        target = n - 1
        while target > 0:
            for i in range(target):
                if i + nums[i] >= target:
                    target = i
                    step += 1
                    break
        return step

    def solution3(self, nums: List[int]) -> int:
        """贪心2.

        最优解O(n)
        """
        n, end = len(nums), 0
        step, mx = 0, 0
        for i in range(n - 1):
            mx = max(mx, i + nums[i])
            if i == end:
                end = mx
                step += 1
        return step

    def solution4(self, nums: List[int]) -> int:
        """递归(超时)."""
        mn = len(nums)

        def dfs(i, s):
            if i >= len(nums) - 1:
                nonlocal mn
                mn = min(mn, s)
                return
            for j in range(1, nums[i] + 1):
                dfs(i + j, s + 1)
        dfs(0, 0)
        return mn
