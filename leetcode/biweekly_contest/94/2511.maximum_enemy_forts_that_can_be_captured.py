#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/maximum-enemy-forts-that-can-be-captured
from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        n = len(forts)
        i, L = 0, None
        ans = 0
        while i < n:
            if forts[i] == 1 or forts[i] == -1:
                if L is not None and forts[i] == -forts[L]:
                    ans = max(ans, i - L - 1)
                L = i
            i += 1
        return ans
