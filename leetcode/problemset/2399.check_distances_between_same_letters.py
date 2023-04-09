#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/check-distances-between-same-letters
from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        m = [-1] * 26
        ord_a = ord('a')
        for i, ch in enumerate(s):
            idx = ord(ch) - ord_a
            if m[idx] == -1:
                m[idx] = i
            elif i - m[idx] - 1 != distance[idx]:
                return False
            m[idx] = i
        return True
