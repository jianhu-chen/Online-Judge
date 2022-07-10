#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/minimum-lines-to-represent-a-line-chart
from typing import List


class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        cnt = 0
        stockPrices = sorted(stockPrices, key=lambda x: x[0])
        pre_dy, pre_dx = 1, 0
        for i in range(1, len(stockPrices)):
            dy = stockPrices[i][1] - stockPrices[i - 1][1]
            dx = stockPrices[i][0] - stockPrices[i - 1][0]
            if dy * pre_dx != dx * pre_dy:
                cnt += 1
                pre_dy = dy
                pre_dx = dx
        return cnt
