#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/longest-arithmetic-subsequence
from typing import List
from functools import lru_cache


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(maxsize=None)
        def f(i: int):
            max_len = {}
            for j in range(i - 1, -1, -1):
                d = nums[i] - nums[j]  # 公差
                if d not in max_len:
                    max_len[d] = f(j).get(d, 1) + 1
            return max_len

        return max(max(f(i).values()) for i in range(1, n))
