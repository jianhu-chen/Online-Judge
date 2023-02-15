#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        L, R = 0, len(numbers) - 1
        while L <= R:
            M = L + ((R - L) >> 1)
            if numbers[M] < numbers[R]:
                R = M
            elif numbers[M] > numbers[R]:
                L = M + 1
            else:
                R -= 1
        return numbers[L]
