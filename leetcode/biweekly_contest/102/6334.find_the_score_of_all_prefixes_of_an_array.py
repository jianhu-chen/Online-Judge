#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/find-the-score-of-all-prefixes-of-an-array
from typing import List
from itertools import accumulate


class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        mx = 0
        res = []
        for x in nums:
            mx = max(x, mx)
            res.append(x + mx)
        return list(accumulate(res))
