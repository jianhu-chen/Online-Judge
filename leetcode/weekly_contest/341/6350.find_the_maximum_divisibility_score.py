#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/find-the-maximum-divisibility-score
from typing import List


class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        return -sorted([(sum(x % d == 0 for x in nums), -d) for d in divisors])[-1][1]
