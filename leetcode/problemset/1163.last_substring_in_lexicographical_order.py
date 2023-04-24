#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/last-substring-in-lexicographical-order
from itertools import accumulate


class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        # 预处理: 后缀最大字符最先出现的位置
        ss = list(accumulate(
            range(n - 1, -1, -1), func=lambda x, y: y if s[y] >= s[x] else x, initial=n - 1
        ))

        def f(i: int) -> str:
            """返回从 s[i] 开始的最后子串."""
            if i == n:
                return ""
            max_idx = ss[n - i]
            sub = f(max_idx + 1)
            return s[max_idx:] if s[max_idx:] > sub else sub

        return f(0)
