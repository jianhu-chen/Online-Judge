#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/trapping-rain-water
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        return self.solution2(height)

    def solution1(self, height: List[int]) -> int:
        n = len(height)
        pre_max, suf_max = [0] * n, [0] * n
        pre_max[0] = height[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], height[i])
        suf_max[-1] = height[-1]
        for j in reversed(range(n - 1)):
            suf_max[j] = max(suf_max[j + 1], height[j])
        ans = 0
        for h, p, s in zip(height, pre_max, suf_max):
            ans += min(p, s) - h
        return ans

    def solution2(self, height: List[int]) -> int:
        """通过双指针优化空间复杂度."""
        ans = 0
        pre_max, suf_max = 0, 0
        left, right = 0, len(height) - 1
        while left < right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if height[left] < height[right]:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right]
                right -= 1
        return ans
