#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/minimize-the-maximum-difference-of-pairs
from bisect import bisect_left
from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        """贪心 + 二分."""
        nums.sort()

        def check(mx: int):
            cnt, i = 0, 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= mx:  # 选
                    cnt += 1
                    i += 2
                else:  # 不选
                    i += 1
            return cnt

        return bisect_left(range(nums[-1] - nums[0]), p, key=check)
