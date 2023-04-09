#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/make-k-subarray-sums-equal
from math import gcd
from typing import List


class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        k = gcd(k, len(arr))
        ans = 0
        for i in range(k):
            b = sorted(arr[i::k])
            mid = b[len(b) // 2]
            ans += sum(abs(x - mid) for x in b)
        return ans
