#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        """双指针."""
        left, s, ans = 1, 1, []
        for right in range(2, target):
            while s > target:
                s -= left
                left += 1
            if s == target:
                ans.append(list(range(left, right)))
            s += right
        return ans
