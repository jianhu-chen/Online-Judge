#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/gu-piao-de-zui-da-li-run-lcof
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.solution2(prices)

    def solution1(self, prices: List[int]) -> int:
        """一次遍历."""
        mn, ans = float("inf"), 0
        for p in prices:
            if p < mn:
                mn = p
            ans = max(ans, p - mn)
        return ans

    def solution2(self, prices: List[int]) -> int:
        """dp."""
        n = len(prices)
        if n < 2:
            return 0
        ans, cost = 0, prices[0]
        for p in prices[1:]:
            ans = max(ans, p - cost)
            cost = min(cost, p)
        return ans
