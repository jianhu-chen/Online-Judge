#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/minimum-recolors-to-get-k-consecutive-black-blocks
from itertools import accumulate


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ps = list(accumulate(blocks, lambda x, y: x + (y == 'W'), initial=0))
        return min(ps[i] - ps[i - k] for i in range(k, len(ps)))
