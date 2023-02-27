#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/left-and-right-sum-differences
from typing import List
from itertools import accumulate


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ps, ss = list(accumulate(nums, initial=0)), list(accumulate(nums[::-1], initial=0))
        return [abs(ps[i] - ss[n - i - 1]) for i in range(n)]
