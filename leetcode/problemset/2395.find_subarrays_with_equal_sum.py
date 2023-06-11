#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/find-subarrays-with-equal-sum
from typing import List


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        visited = set()
        for i in range(len(nums) - 1):
            s = nums[i] + nums[i + 1]
            if s in visited:
                return True 
            visited.add(s)
        return False
