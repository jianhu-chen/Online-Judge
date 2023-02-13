#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/replace-the-substring-for-balanced-string
from collections import Counter


class Solution:
    def balancedString(self, s: str) -> int:
        cnt, qn = Counter(s), len(s) // 4
        rest = {c: max(0, cnt[c] - qn) for c in "QWER"}

        def check():
            for c in "QWER":
                if rest[c] > 0:
                    return False
            return True

        if check():
            return 0

        ans, left = len(s) - 1, 0
        for right, c in enumerate(s):
            rest[c] -= 1
            while check():
                ans = min(ans, right - left + 1)
                rest[s[left]] += 1
                left += 1
        return ans
