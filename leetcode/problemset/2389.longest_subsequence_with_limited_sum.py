#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/longest-subsequence-with-limited-sum
import bisect
from typing import List
from itertools import accumulate


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ps = list(accumulate(nums, initial=0))
        return [bisect.bisect_right(ps, q) - 1 for q in queries]
