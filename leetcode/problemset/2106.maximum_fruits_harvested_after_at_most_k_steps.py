#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/maximum-fruits-harvested-after-at-most-k-steps
from typing import List


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        ans = i = s = 0
        for j, (pj, fj) in enumerate(fruits):
            s += fj
            while i <= j and pj - fruits[i][0] + min(abs(startPos - fruits[i][0]), abs(startPos - fruits[j][0])) > k:
                s -= fruits[i][1]
                i += 1
            ans = max(ans, s)
        return ans
