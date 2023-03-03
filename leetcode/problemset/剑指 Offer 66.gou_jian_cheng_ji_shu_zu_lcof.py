#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/gou-jian-cheng-ji-shu-zu-lcof
from typing import List


class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        left, right = [1], [1]
        for i, (x, y) in enumerate(zip(a, a[::-1])):
            left.append(left[-1] * x)
            right.append(right[-1] * x)

        ans = []
        for i, x in enumerate(a):
            ans.append(left[i] * right[len(a) - i])
        return ans
