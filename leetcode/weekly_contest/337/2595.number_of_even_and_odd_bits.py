#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/number-of-even-and-odd-bits
from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        cnt1, cnt2 = 0, 0
        while n:
            cnt1 += n & 1
            cnt2 += (n & 2) >> 1
            n >>= 2
        return cnt1, cnt2
