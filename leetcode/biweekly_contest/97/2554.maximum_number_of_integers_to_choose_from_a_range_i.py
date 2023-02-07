#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/maximum-number-of-integers-to-choose-from-a-range-i
from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        cnt, s = 0, 0
        for x in range(1, n + 1):
            if x not in banned:
                s += x
                if s > maxSum:
                    return cnt
                cnt += 1
        return cnt
