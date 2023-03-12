#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/rearrange-array-to-maximize-prefix-score
from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ps, cnt = 0, 0
        for x in nums:
            ps += x
            if ps <= 0:
                break
            cnt += 1
        return cnt
