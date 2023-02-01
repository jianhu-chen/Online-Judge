#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/container-with-most-water
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            distance = right - left
            if height[left] <= height[right]:
                ans = max(ans, distance * height[left])
                left += 1
            else:
                ans = max(ans, distance * height[right])
                right -= 1
        return ans
