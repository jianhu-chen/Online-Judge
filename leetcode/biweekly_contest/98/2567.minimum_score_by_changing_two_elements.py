#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/minimum-score-by-changing-two-elements
from typing import List


class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        return min(nums[-3] - nums[0], nums[-2] - nums[1], nums[-1] - nums[2])
