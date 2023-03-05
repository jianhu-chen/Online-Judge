#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/maximum-profit-of-operating-a-centennial-wheel
from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        """阅读理解题..."""
        ans = -1
        wait = 0
        max_profit, profit = 0, 0
        i = 0
        for x in customers:
            wait += x
            up = wait if wait <= 4 else 4
            wait = wait - up
            i += 1
            profit += boardingCost * up - runningCost
            if profit > max_profit:
                ans, max_profit = i, profit

        while wait:
            up = wait if wait <= 4 else 4
            wait = wait - up
            i += 1
            profit += boardingCost * up - runningCost
            if profit > max_profit:
                ans, max_profit = i, profit

        return ans
