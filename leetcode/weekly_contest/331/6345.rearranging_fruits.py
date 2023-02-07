#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/rearranging-fruits
from typing import List
from collections import Counter


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt = Counter()
        for x, y in zip(basket1, basket2):
            cnt[x] += 1
            cnt[y] -= 1

        mn = min(cnt)
        a, b = [], []
        for x, c in cnt.items():
            if c % 2 != 0:
                return -1
            if c > 0:
                a.extend([x] * (c // 2))
            elif c < 0:
                b.extend([x] * (-c // 2))

        a.sort()
        b.sort(reverse=True)

        ans = 0
        for x, y in zip(a, b):
            ans += min(x, y, 2 * mn)

        return ans
