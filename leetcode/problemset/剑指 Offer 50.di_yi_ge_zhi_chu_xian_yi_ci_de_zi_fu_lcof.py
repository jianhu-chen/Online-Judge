#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> str:
        cnt = Counter(s)
        for c in s:
            if cnt[c] == 1:
                return c
        return " "
