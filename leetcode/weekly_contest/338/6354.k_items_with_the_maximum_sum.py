#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/k-items-with-the-maximum-sum

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        diff = k - numOnes
        return k if diff <= 0 else numOnes - max(0, diff - numZeros)
