#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/minimum-deletions-to-make-string-balanced
from itertools import accumulate


class Solution:
    def minimumDeletions(self, s: str) -> int:
        left = list(accumulate(s, lambda x, y: x + (1 if y == 'b' else 0), initial=0))
        right = list(accumulate(s[::-1], lambda x, y: x + (1 if y == 'a' else 0), initial=0))[::-1]
        return min(ll + rr for ll, rr in zip(left, right))
