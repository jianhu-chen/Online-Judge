#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/find-the-substring-with-maximum-cost
import string
from typing import List


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        expenses = dict(zip(chars, vals))
        for val, ch in enumerate(string.ascii_lowercase, 1):
            if ch not in expenses:
                expenses[ch] = val
        dp = [0] * len(s)
        for i, ch in enumerate(s):
            dp[i] = max(dp[i - 1] + expenses[ch], expenses[ch]) if i != 0 else expenses[ch]
        return max(max(dp), 0)
