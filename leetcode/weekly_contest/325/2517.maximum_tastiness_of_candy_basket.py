#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/maximum-tastiness-of-candy-basket
from typing import List


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        # 利用二分查找到结果
        # 1. 确定结果范围: 先排序
        price.sort()
        L, R = 0, (price[-1] - price[0]) // (k - 1)
        # 2. 二分查找
        index = 0  # 记录小于等于某个数字的最左侧的位置
        while L <= R:
            M = L + ((R - L) >> 1)
            cnt = 1
            x = price[0]
            for p in price[1:]:
                if p - x >= M:
                    cnt += 1
                    x = p
            if cnt >= k:
                L = M + 1
                index = M
            else:
                R = M - 1
        return index
