#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/russian-doll-envelopes
from bisect import bisect_left
from typing import List
from functools import lru_cache


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        return self.solution2(envelopes)

    def solution1(self, nums: List[List[int]]) -> int:
        nums.sort()

        @lru_cache(maxsize=None)
        def f(i: int) -> int:
            if i == 0:
                return 1
            res = 0
            for j in range(i):
                if nums[j][0] < nums[i][0] and nums[j][1] < nums[i][1]:
                    res = max(res, f(j))
            return res + 1

        return max(f(i) for i in range(len(nums)))

    def solution2(self, nums: List[List[int]]) -> int:
        """贪心+二分."""
        nums.sort(key=lambda x: (x[0], -x[1]))
        # 求第二维的最长上升子序列
        g = []  # 表示长度为i + 1 的 LIS 的末尾元素的最小值
        for _, x in nums:
            i = bisect_left(g, x)
            if i == len(g):
                g.append(x)
            else:
                g[i] = x
        return len(g)
