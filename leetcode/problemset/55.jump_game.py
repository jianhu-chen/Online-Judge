#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/jump-game
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """贪心."""
        end = 0
        for i in range(len(nums)):
            if end < i:
                return False
            end = max(end, i + nums[i])
        return True
