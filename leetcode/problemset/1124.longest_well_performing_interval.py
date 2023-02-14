#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/longest-well-performing-interval
from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        return self.solution1(hours)

    def solution1(self, hours: List[int]) -> int:
        """前缀和 + 单调栈."""
        ps = [0]  # 前缀和
        stack = [0]  # 前缀和的单调递减栈(栈中存idx)
        for i, h in enumerate(hours):
            ps.append(ps[-1] + (1 if h > 8 else -1))
            if ps[-1] < ps[stack[-1]]:
                stack.append(i + 1)

        ans = 0
        for i in reversed(range(1, len(ps))):
            while stack and ps[i] > ps[stack[-1]]:
                ans = max(ans, i - stack.pop())
        return ans

    def solution2(self, hours: List[int]) -> int:
        """前缀和 + 哈希表."""
        ps = [0]  # 前缀和
        m = {}
        ans = 0
        for i, h in enumerate(hours):
            ps.append(ps[-1] + (1 if h > 8 else -1))
            if ps[-1] > 0:
                ans = max(ans, i + 1)
            elif ps[-1] - 1 in m:
                ans = max(ans, i - m[ps[-1] - 1])
            if ps[-1] not in m:
                m[ps[-1]] = i
        return ans
